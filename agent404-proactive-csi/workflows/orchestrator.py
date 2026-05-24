"""
Workflow Orchestrator - Coordinates all 6 workflows
Simulates IBM watsonx Orchestrate functionality
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.customer_success_agent import CustomerSuccessAgent
from agents.procurement_agent import ProcurementAgent
from agents.revenue_agent import RevenueAgent
from integrations.ibm_services import get_ibm_services
from datetime import datetime
from typing import Dict, List
import json

class WorkflowOrchestrator:
    """
    Master orchestrator that coordinates all three agents and executes workflows
    This simulates IBM watsonx Orchestrate's agent coordination capabilities
    """
    
    def __init__(self, data_path: str = "data/"):
        self.cs_agent = CustomerSuccessAgent(data_path)
        self.procurement_agent = ProcurementAgent(data_path)
        self.revenue_agent = RevenueAgent(data_path)
        self.ibm_services = get_ibm_services()
        print("🚀 Workflow Orchestrator initialized with 3 agents")
    
    # ===== WORKFLOW 1: Churn Prediction =====
    
    def workflow_churn_prediction(self, customer_id: str) -> Dict:
        """
        Workflow 1: Churn Prediction
        1. Pull customer data
        2. Analyze ticket sentiment
        3. Predict churn probability
        4. Push risk score to Orchestrate
        5. Trigger CS Agent
        """
        print(f"\n🔄 WORKFLOW 1: Churn Prediction for {customer_id}")
        print("="*60)
        
        results = {
            "workflow": "Churn Prediction",
            "customer_id": customer_id,
            "timestamp": datetime.now().isoformat(),
            "steps": []
        }
        
        # Step 1: Pull customer data
        print("📊 Step 1: Pulling customer data...")
        health = self.cs_agent.analyze_customer_health(customer_id)
        results["steps"].append({"step": 1, "action": "Pull customer data", "status": "complete"})
        
        # Step 2: Analyze ticket sentiment using NLU
        print("🧠 Step 2: Analyzing sentiment with IBM NLU...")
        if health.get('recent_communications'):
            latest_comm = health['recent_communications'][0]
            sentiment_analysis = self.ibm_services.analyze_customer_communication(latest_comm['message'])
            results["sentiment_analysis"] = sentiment_analysis
        results["steps"].append({"step": 2, "action": "Analyze sentiment", "status": "complete"})
        
        # Step 3: Predict churn probability
        print("🔮 Step 3: Predicting churn probability...")
        churn_prob = self.cs_agent.predict_churn_probability(customer_id)
        results["churn_probability"] = churn_prob
        results["steps"].append({"step": 3, "action": "Predict churn", "status": "complete"})
        
        # Step 4: Push risk score (to Cloudant)
        print("💾 Step 4: Storing risk score in Cloudant...")
        self.ibm_services.store_customer_health_record(customer_id, {
            "churn_probability": churn_prob,
            "health_metrics": health['health_metrics']
        })
        results["steps"].append({"step": 4, "action": "Store risk score", "status": "complete"})
        
        # Step 5: Trigger CS Agent for intervention
        print("🎯 Step 5: Triggering CS Agent intervention...")
        intervention = self.cs_agent.recommend_intervention(customer_id)
        results["intervention"] = intervention
        results["steps"].append({"step": 5, "action": "Trigger intervention", "status": "complete"})
        
        print(f"✅ Workflow 1 Complete: {health['name']} - {churn_prob*100:.1f}% churn risk")
        
        return results
    
    # ===== WORKFLOW 2: Procurement Early-Warning =====
    
    def workflow_procurement_early_warning(self, vendor_id: str) -> Dict:
        """
        Workflow 2: Procurement Early-Warning
        1. Scan vendor delivery logs
        2. Detect delays
        3. Correlate with affected customers
        4. Create procurement alert
        5. Trigger Revenue Agent
        """
        print(f"\n🔄 WORKFLOW 2: Procurement Early-Warning for {vendor_id}")
        print("="*60)
        
        results = {
            "workflow": "Procurement Early-Warning",
            "vendor_id": vendor_id,
            "timestamp": datetime.now().isoformat(),
            "steps": []
        }
        
        # Step 1: Scan vendor delivery logs
        print("📦 Step 1: Scanning vendor delivery logs...")
        vendor_info = self.procurement_agent.correlate_vendor_to_customer_risk(vendor_id)
        results["vendor_info"] = vendor_info
        results["steps"].append({"step": 1, "action": "Scan vendor logs", "status": "complete"})
        
        # Step 2: Detect delays
        print("⚠️ Step 2: Detecting delays...")
        delay_days = vendor_info['delay_info']['delay_days']
        results["delay_days"] = delay_days
        results["steps"].append({"step": 2, "action": "Detect delays", "status": "complete"})
        
        # Step 3: Correlate with affected customers
        print("🔗 Step 3: Correlating affected customers...")
        affected_customers = vendor_info['affected_customers']
        results["affected_customers"] = affected_customers
        results["steps"].append({"step": 3, "action": "Correlate customers", "status": "complete"})
        
        # Step 4: Create procurement alert
        print("🚨 Step 4: Creating procurement alert...")
        alert = {
            "vendor": vendor_info['vendor_name'],
            "severity": vendor_info['risk_level'],
            "customers_impacted": len(affected_customers),
            "recommended_actions": vendor_info['customer_impact_prediction']['recommended_actions']
        }
        results["alert"] = alert
        results["steps"].append({"step": 4, "action": "Create alert", "status": "complete"})
        
        # Step 5: Trigger Revenue Agent
        print("💰 Step 5: Triggering Revenue Agent...")
        churn_predictions = {}
        for cust_id in affected_customers:
            churn_prob = self.cs_agent.predict_churn_probability(cust_id)
            churn_predictions[cust_id] = churn_prob
        
        revenue_exposure = self.revenue_agent.get_total_revenue_exposure(churn_predictions)
        results["revenue_exposure"] = revenue_exposure
        results["steps"].append({"step": 5, "action": "Calculate revenue impact", "status": "complete"})
        
        print(f"✅ Workflow 2 Complete: ${revenue_exposure['total_arr_at_risk']:,.0f} ARR at risk")
        
        return results
    
    # ===== WORKFLOW 3: Customer Escalation Auto-Resolution =====
    
    def workflow_customer_escalation(self, customer_id: str) -> Dict:
        """
        Workflow 3: Customer Escalation Auto-Resolution
        1. Detect high-risk sentiment
        2. Summarize ticket
        3. Generate action plan
        4. Notify CSM
        5. Update CRM
        """
        print(f"\n🔄 WORKFLOW 3: Customer Escalation for {customer_id}")
        print("="*60)
        
        results = {
            "workflow": "Customer Escalation Auto-Resolution",
            "customer_id": customer_id,
            "timestamp": datetime.now().isoformat(),
            "steps": []
        }
        
        # Step 1: Detect high-risk sentiment
        print("🔍 Step 1: Detecting high-risk sentiment...")
        health = self.cs_agent.analyze_customer_health(customer_id)
        sentiment_score = health['health_metrics']['sentiment_score']
        results["sentiment_score"] = sentiment_score
        results["steps"].append({"step": 1, "action": "Detect sentiment", "status": "complete"})
        
        # Step 2: Summarize ticket history
        print("📋 Step 2: Summarizing ticket history...")
        ticket_summary = {
            "total_tickets": health['health_metrics']['ticket_volume'],
            "recent_tickets": health['recent_tickets'][:3],
            "dominant_sentiment": health['health_metrics']['last_ticket_sentiment']
        }
        results["ticket_summary"] = ticket_summary
        results["steps"].append({"step": 2, "action": "Summarize tickets", "status": "complete"})
        
        # Step 3: Generate action plan
        print("📝 Step 3: Generating AI-powered action plan...")
        action_plan = self.cs_agent.recommend_intervention(customer_id)
        results["action_plan"] = action_plan
        results["steps"].append({"step": 3, "action": "Generate action plan", "status": "complete"})
        
        # Step 4: Notify CSM
        print("📧 Step 4: Notifying Customer Success Manager...")
        notification = {
            "recipient": "CSM Team",
            "subject": f"URGENT: {health['name']} requires immediate attention",
            "priority": action_plan['priority'],
            "message": f"Customer {health['name']} has {health['churn_probability']*100:.0f}% churn risk. Immediate action required."
        }
        results["notification"] = notification
        results["steps"].append({"step": 4, "action": "Notify CSM", "status": "complete"})
        
        # Step 5: Update CRM (simulated)
        print("💼 Step 5: Updating CRM records...")
        crm_update = {
            "customer_id": customer_id,
            "health_score": f"{(1-health['churn_probability'])*100:.0f}",
            "risk_level": health['risk_level'],
            "last_updated": datetime.now().isoformat(),
            "next_action": action_plan['recommended_interventions'][0] if action_plan['recommended_interventions'] else "Contact customer"
        }
        results["crm_update"] = crm_update
        results["steps"].append({"step": 5, "action": "Update CRM", "status": "complete"})
        
        print(f"✅ Workflow 3 Complete: Escalation created for {health['name']}")
        
        return results
    
    # ===== WORKFLOW 4: Contract Renewal Prep =====
    
    def workflow_contract_renewal_prep(self, customer_id: str) -> Dict:
        """
        Workflow 4: Contract Renewal Prep
        1. Analyze customer history
        2. Generate renewal brief
        3. Auto-draft email
        4. Notify CSM
        """
        print(f"\n🔄 WORKFLOW 4: Contract Renewal Prep for {customer_id}")
        print("="*60)
        
        results = {
            "workflow": "Contract Renewal Prep",
            "customer_id": customer_id,
            "timestamp": datetime.now().isoformat(),
            "steps": []
        }
        
        # Step 1: Analyze customer history
        print("📊 Step 1: Analyzing customer history...")
        health = self.cs_agent.analyze_customer_health(customer_id)
        churn_prob = health['churn_probability']
        results["customer_analysis"] = health
        results["steps"].append({"step": 1, "action": "Analyze history", "status": "complete"})
        
        # Step 2: Generate renewal brief
        print("📄 Step 2: Generating renewal brief...")
        renewal_brief = {
            "customer_name": health['name'],
            "contract_value": health['contract_info']['value'],
            "renewal_date": health['contract_info']['renewal_date'],
            "health_score": f"{(1-churn_prob)*100:.0f}%",
            "key_metrics": health['health_metrics'],
            "risk_factors": self._identify_risk_factors(health),
            "opportunities": self._identify_opportunities(health),
            "recommendation": "Renew" if churn_prob < 0.3 else "At Risk - Intervention Needed"
        }
        results["renewal_brief"] = renewal_brief
        results["steps"].append({"step": 2, "action": "Generate brief", "status": "complete"})
        
        # Step 3: Auto-draft email
        print("✉️ Step 3: Auto-drafting renewal email...")
        email_draft = self._generate_renewal_email(health, renewal_brief)
        results["email_draft"] = email_draft
        results["steps"].append({"step": 3, "action": "Draft email", "status": "complete"})
        
        # Step 4: Notify CSM
        print("📬 Step 4: Notifying CSM with renewal package...")
        notification = {
            "recipient": "CSM Team",
            "subject": f"Renewal Prep: {health['name']}",
            "attachments": ["renewal_brief.pdf", "email_draft.txt"],
            "action_required": "Review and send renewal email"
        }
        results["notification"] = notification
        results["steps"].append({"step": 4, "action": "Notify CSM", "status": "complete"})
        
        print(f"✅ Workflow 4 Complete: Renewal package ready for {health['name']}")
        
        return results
    
    # ===== WORKFLOW 5: Daily Executive Brief =====
    
    def workflow_daily_executive_brief(self) -> Dict:
        """
        Workflow 5: Daily Executive Brief
        1. Fetch data from all agents
        2. Summarize risks
        3. Generate revenue-at-risk insight
        4. Deliver to Slack + email
        """
        print(f"\n🔄 WORKFLOW 5: Daily Executive Brief")
        print("="*60)
        
        results = {
            "workflow": "Daily Executive Brief",
            "timestamp": datetime.now().isoformat(),
            "steps": []
        }
        
        # Step 1: Fetch data from all agents
        print("📊 Step 1: Fetching data from all agents...")
        cs_briefing = self.cs_agent.generate_daily_briefing()
        procurement_briefing = self.procurement_agent.generate_procurement_brief()
        
        # Get churn predictions for revenue analysis
        critical_customers = self.cs_agent.get_critical_customers()
        churn_predictions = {c['customer_id']: c['churn_probability'] for c in critical_customers}
        cfo_briefing = self.revenue_agent.generate_cfo_briefing(churn_predictions)
        
        results["steps"].append({"step": 1, "action": "Fetch agent data", "status": "complete"})
        
        # Step 2: Summarize risks
        print("⚠️ Step 2: Summarizing risks...")
        risk_summary = {
            "customer_success": {
                "critical_customers": cs_briefing['summary']['critical_risk_customers'],
                "high_risk_customers": cs_briefing['summary']['high_risk_customers'],
                "priority_tickets": cs_briefing['summary']['high_priority_tickets']
            },
            "procurement": {
                "delayed_vendors": procurement_briefing['summary']['total_vendors_delayed'],
                "critical_delays": procurement_briefing['summary']['critical_delays'],
                "customers_affected": procurement_briefing['summary']['customers_affected']
            },
            "revenue": {
                "total_arr_at_risk": cfo_briefing['executive_summary']['revenue_at_risk'],
                "portfolio_risk_pct": cfo_briefing['executive_summary']['portfolio_risk_percentage']
            }
        }
        results["risk_summary"] = risk_summary
        results["steps"].append({"step": 2, "action": "Summarize risks", "status": "complete"})
        
        # Step 3: Generate revenue-at-risk insight
        print("💰 Step 3: Generating revenue insights...")
        revenue_insight = {
            "total_arr_at_risk": cfo_briefing['executive_summary']['revenue_at_risk'],
            "expected_loss": cfo_briefing['financial_scenarios']['expected_case_loss'],
            "recommended_investment": cfo_briefing['intervention_economics']['recommended_investment'],
            "estimated_roi": cfo_briefing['intervention_economics']['estimated_roi']
        }
        results["revenue_insight"] = revenue_insight
        results["steps"].append({"step": 3, "action": "Generate revenue insights", "status": "complete"})
        
        # Step 4: Deliver to Slack + Email
        print("📤 Step 4: Delivering executive brief...")
        executive_brief = self._format_executive_brief(cs_briefing, procurement_briefing, cfo_briefing)
        results["executive_brief"] = executive_brief
        results["delivery"] = {
            "slack": {"channel": "#executive-updates", "status": "sent"},
            "email": {"recipients": ["ceo@company.com", "cfo@company.com", "vp-cs@company.com"], "status": "sent"}
        }
        results["steps"].append({"step": 4, "action": "Deliver brief", "status": "complete"})
        
        print(f"✅ Workflow 5 Complete: Executive brief delivered")
        
        return results
    
    # ===== WORKFLOW 6: Procurement → Customer Impact Bridge =====
    
    def workflow_procurement_customer_bridge(self, vendor_id: str) -> Dict:
        """
        Workflow 6: Procurement → Customer Impact Bridge
        1. Vendor issue detected
        2. Detect at-risk customers
        3. Trigger cross-team task
        4. Update dashboards
        """
        print(f"\n🔄 WORKFLOW 6: Procurement-Customer Bridge for {vendor_id}")
        print("="*60)
        
        results = {
            "workflow": "Procurement-Customer Impact Bridge",
            "vendor_id": vendor_id,
            "timestamp": datetime.now().isoformat(),
            "steps": []
        }
        
        # Step 1: Vendor issue detected
        print("🚨 Step 1: Vendor issue detected...")
        vendor_info = self.procurement_agent.correlate_vendor_to_customer_risk(vendor_id)
        results["vendor_issue"] = {
            "vendor_name": vendor_info['vendor_name'],
            "risk_level": vendor_info['risk_level'],
            "delay_days": vendor_info['delay_info']['delay_days']
        }
        results["steps"].append({"step": 1, "action": "Detect vendor issue", "status": "complete"})
        
        # Step 2: Detect at-risk customers
        print("🔍 Step 2: Identifying at-risk customers...")
        affected_customers = vendor_info['affected_customers']
        at_risk_analysis = []
        
        for customer_id in affected_customers:
            health = self.cs_agent.analyze_customer_health(customer_id)
            churn_prob = health['churn_probability']
            revenue_risk = self.revenue_agent.calculate_revenue_at_risk(customer_id, churn_prob)
            
            at_risk_analysis.append({
                "customer_id": customer_id,
                "customer_name": health['name'],
                "churn_probability": churn_prob,
                "arr_at_risk": revenue_risk['arr_at_risk'],
                "urgency": revenue_risk['urgency']
            })
        
        results["at_risk_customers"] = at_risk_analysis
        results["steps"].append({"step": 2, "action": "Identify at-risk customers", "status": "complete"})
        
        # Step 3: Trigger cross-team tasks
        print("📋 Step 3: Creating cross-team tasks...")
        tasks = []
        
        # Procurement team tasks
        tasks.append({
            "team": "Procurement",
            "task": f"Escalate {vendor_info['vendor_name']} delay to vendor management",
            "priority": "HIGH",
            "due": "Immediate"
        })
        
        # CS team tasks for each affected customer
        for customer in at_risk_analysis:
            if customer['churn_probability'] >= 0.5:
                tasks.append({
                    "team": "Customer Success",
                    "task": f"Contact {customer['customer_name']} - vendor delay impact",
                    "priority": "CRITICAL" if customer['urgency'] == "CRITICAL" else "HIGH",
                    "due": "24 hours"
                })
        
        # Finance team task
        total_arr_at_risk = sum(c['arr_at_risk'] for c in at_risk_analysis)
        tasks.append({
            "team": "Finance",
            "task": f"Review ${total_arr_at_risk:,.0f} ARR exposure from vendor delays",
            "priority": "HIGH",
            "due": "48 hours"
        })
        
        results["tasks_created"] = tasks
        results["steps"].append({"step": 3, "action": "Create cross-team tasks", "status": "complete"})
        
        # Step 4: Update dashboards
        print("📊 Step 4: Updating dashboards...")
        dashboard_updates = {
            "procurement_dashboard": {
                "vendor_risk_score": vendor_info['risk_level'],
                "customers_impacted": len(affected_customers)
            },
            "cs_dashboard": {
                "at_risk_from_vendor": len([c for c in at_risk_analysis if c['churn_probability'] >= 0.5])
            },
            "revenue_dashboard": {
                "arr_at_risk_vendor_related": total_arr_at_risk
            }
        }
        results["dashboard_updates"] = dashboard_updates
        results["steps"].append({"step": 4, "action": "Update dashboards", "status": "complete"})
        
        print(f"✅ Workflow 6 Complete: {len(tasks)} tasks created, ${total_arr_at_risk:,.0f} ARR protected")
        
        return results
    
    # ===== Helper Methods =====
    
    def _identify_risk_factors(self, health: Dict) -> List[str]:
        """Identify key risk factors"""
        risks = []
        metrics = health['health_metrics']
        
        if metrics['usage_drop_pct'] > 30:
            risks.append(f"Usage dropped {metrics['usage_drop_pct']}%")
        if metrics['sentiment_score'] < -0.4:
            risks.append("Negative sentiment in communications")
        if metrics['ticket_volume'] > 10:
            risks.append(f"{metrics['ticket_volume']} support tickets in 30 days")
        if metrics['nps_score'] < 30:
            risks.append(f"Low NPS score: {metrics['nps_score']}")
        
        return risks if risks else ["No major risk factors identified"]
    
    def _identify_opportunities(self, health: Dict) -> List[str]:
        """Identify renewal opportunities"""
        opportunities = []
        
        if health['churn_probability'] < 0.3:
            opportunities.append("Strong candidate for upsell")
            opportunities.append("Consider multi-year renewal discount")
        
        opportunities.append("Present new product features")
        opportunities.append("Discuss expanded use cases")
        
        return opportunities
    
    def _generate_renewal_email(self, health: Dict, brief: Dict) -> Dict:
        """Generate personalized renewal email"""
        return {
            "to": f"decision-maker@{health['name'].lower().replace(' ', '')}.com",
            "subject": f"Your {health['name']} Partnership Renewal",
            "body": f"""Dear Valued Partner,

I hope this message finds you well. As we approach your renewal date on {brief['renewal_date']}, I wanted to personally reach out to discuss your continued partnership with us.

Based on our analysis, your account health score is {brief['health_score']}, and we've identified several opportunities to enhance your experience:

{chr(10).join('• ' + opp for opp in brief['opportunities'])}

I'd love to schedule a brief call to discuss your renewal and how we can continue delivering value to your organization.

Best regards,
Customer Success Team""",
            "priority": "High" if health['churn_probability'] >= 0.5 else "Normal"
        }
    
    def _format_executive_brief(self, cs_brief: Dict, proc_brief: Dict, cfo_brief: Dict) -> str:
        """Format executive brief for delivery"""
        return f"""
🎯 DAILY EXECUTIVE BRIEF - {datetime.now().strftime('%Y-%m-%d')}
{'='*60}

💰 REVENUE IMPACT
• Total ARR at Risk: ${cfo_brief['executive_summary']['revenue_at_risk']:,.0f}
• Portfolio Risk: {cfo_brief['executive_summary']['portfolio_risk_percentage']:.1f}%
• Expected Loss (if no action): ${cfo_brief['financial_scenarios']['expected_case_loss']:,.0f}

🚨 CUSTOMER HEALTH
• Critical Risk: {cs_brief['summary']['critical_risk_customers']} customers
• High Risk: {cs_brief['summary']['high_risk_customers']} customers
• High Priority Tickets: {cs_brief['summary']['high_priority_tickets']}

📦 PROCUREMENT ALERTS
• Vendors Delayed: {proc_brief['summary']['total_vendors_delayed']}
• Critical Delays: {proc_brief['summary']['critical_delays']}
• Customers Affected: {proc_brief['summary']['customers_affected']}

💡 RECOMMENDED ACTIONS
{chr(10).join('• ' + action for action in cs_brief['action_items'][:3])}

📊 ROI PROJECTION
• Recommended Investment: ${cfo_brief['intervention_economics']['recommended_investment']:,.0f}
• Expected ROI: {cfo_brief['intervention_economics']['estimated_roi']:.0f}%
• Payback Period: {cfo_brief['intervention_economics']['payback_period_months']} months
"""


if __name__ == "__main__":
    # Test orchestrator
    print("\n🧪 Testing Workflow Orchestrator\n")
    
    orchestrator = WorkflowOrchestrator()
    
    # Test Workflow 1
    result1 = orchestrator.workflow_churn_prediction("C-001")
    print(f"\nWorkflow 1 Result: {len(result1['steps'])} steps completed")
    
    # Test Workflow 5
    result5 = orchestrator.workflow_daily_executive_brief()
    print(f"\nWorkflow 5 Result: Executive brief generated")
    print(result5['executive_brief'][:200] + "...")

