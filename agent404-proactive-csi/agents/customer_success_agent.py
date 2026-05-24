"""
Customer Success Intelligence Agent
Predicts churn, analyzes sentiment, triggers interventions
"""

import pandas as pd
import json
from datetime import datetime, timedelta
from typing import Dict, List, Tuple
import os

class CustomerSuccessAgent:
    """
    AI-powered Customer Success Intelligence Agent
    Predicts customer churn and triggers proactive interventions
    """
    
    def __init__(self, data_path: str = "data/"):
        self.data_path = data_path
        self.customers_df = None
        self.tickets_df = None
        self.comms_df = None
        self.load_data()
    
    def load_data(self):
        """Load customer success data"""
        try:
            self.customers_df = pd.read_csv(f"{self.data_path}/customer_success_data.csv")
            self.tickets_df = pd.read_csv(f"{self.data_path}/support_tickets.csv")
            self.comms_df = pd.read_csv(f"{self.data_path}/customer_comms.csv")
            print("✅ Customer Success Agent: Data loaded successfully")
        except Exception as e:
            print(f"❌ Error loading data: {e}")
    
    def predict_churn_probability(self, customer_id: str) -> float:
        """
        Predict churn probability using multiple signals
        Returns: probability between 0 and 1
        """
        customer = self.customers_df[self.customers_df['customer_id'] == customer_id]
        
        if customer.empty:
            return 0.0
        
        customer = customer.iloc[0]
        
        # Churn prediction model using weighted factors
        usage_drop_weight = 0.25
        sentiment_weight = 0.30
        ticket_volume_weight = 0.20
        nps_weight = 0.25
        
        # Normalize and calculate risk scores
        usage_risk = min(customer['usage_drop_pct'] / 50, 1.0)  # 50% drop = max risk
        sentiment_risk = max((customer['sentiment_score'] * -1), 0)  # Negative sentiment = risk
        ticket_risk = min(customer['ticket_volume_last_30d'] / 15, 1.0)  # 15+ tickets = max risk
        nps_risk = 1 - (customer['nps_score'] / 100)  # Low NPS = high risk
        
        churn_probability = (
            usage_risk * usage_drop_weight +
            sentiment_risk * sentiment_weight +
            ticket_risk * ticket_volume_weight +
            nps_risk * nps_weight
        )
        
        return round(churn_probability, 3)
    
    def analyze_customer_health(self, customer_id: str) -> Dict:
        """
        Comprehensive customer health analysis
        """
        customer = self.customers_df[self.customers_df['customer_id'] == customer_id]
        
        if customer.empty:
            return {"error": "Customer not found"}
        
        customer = customer.iloc[0]
        churn_prob = self.predict_churn_probability(customer_id)
        
        # Calculate risk level
        if churn_prob >= 0.7:
            risk_level = "CRITICAL"
            risk_color = "🔴"
        elif churn_prob >= 0.5:
            risk_level = "HIGH"
            risk_color = "🟠"
        elif churn_prob >= 0.3:
            risk_level = "MEDIUM"
            risk_color = "🟡"
        else:
            risk_level = "LOW"
            risk_color = "🟢"
        
        # Get recent tickets
        recent_tickets = self.tickets_df[
            self.tickets_df['customer_id'] == customer_id
        ].sort_values('created_at', ascending=False).head(5)
        
        # Get recent communications
        recent_comms = self.comms_df[
            self.comms_df['customer_id'] == customer_id
        ].sort_values('date', ascending=False).head(5)
        
        return {
            "customer_id": customer_id,
            "name": customer['name'],
            "churn_probability": churn_prob,
            "risk_level": risk_level,
            "risk_color": risk_color,
            "health_metrics": {
                "usage_drop_pct": customer['usage_drop_pct'],
                "sentiment_score": customer['sentiment_score'],
                "ticket_volume": customer['ticket_volume_last_30d'],
                "nps_score": customer['nps_score'],
                "last_ticket_sentiment": customer['last_ticket_sentiment']
            },
            "contract_info": {
                "value": customer['contract_value'],
                "renewal_date": customer['renewal_date']
            },
            "recent_tickets": recent_tickets.to_dict('records') if not recent_tickets.empty else [],
            "recent_communications": recent_comms.to_dict('records') if not recent_comms.empty else []
        }
    
    def get_critical_customers(self, threshold: float = 0.5) -> List[Dict]:
        """
        Identify all customers above churn risk threshold
        """
        critical_customers = []
        
        for _, customer in self.customers_df.iterrows():
            churn_prob = self.predict_churn_probability(customer['customer_id'])
            
            if churn_prob >= threshold:
                critical_customers.append({
                    "customer_id": customer['customer_id'],
                    "name": customer['name'],
                    "churn_probability": churn_prob,
                    "contract_value": customer['contract_value'],
                    "renewal_date": customer['renewal_date'],
                    "sentiment": customer['last_ticket_sentiment']
                })
        
        # Sort by churn probability (highest first)
        critical_customers.sort(key=lambda x: x['churn_probability'], reverse=True)
        
        return critical_customers
    
    def recommend_intervention(self, customer_id: str) -> Dict:
        """
        Recommend specific intervention actions based on customer health
        """
        health = self.analyze_customer_health(customer_id)
        
        if "error" in health:
            return health
        
        interventions = []
        priority = "LOW"
        
        # Determine interventions based on risk factors
        churn_prob = health['churn_probability']
        metrics = health['health_metrics']
        
        if churn_prob >= 0.7:
            priority = "CRITICAL"
            interventions.extend([
                "🚨 Immediate executive escalation call required",
                "📞 Schedule emergency review with VP of Customer Success",
                "🎁 Offer service credits or extended trial period",
                "🔧 Assign dedicated technical support engineer",
                "📊 Create custom success plan with weekly check-ins"
            ])
        elif churn_prob >= 0.5:
            priority = "HIGH"
            interventions.extend([
                "📞 Schedule urgent call with Customer Success Manager",
                "🔍 Conduct technical health check and optimization review",
                "📈 Share success stories and best practices",
                "🎓 Offer personalized training session",
                "💬 Increase touchpoint frequency to weekly"
            ])
        elif churn_prob >= 0.3:
            priority = "MEDIUM"
            interventions.extend([
                "📧 Send personalized check-in email",
                "📊 Share relevant product updates and roadmap",
                "🤝 Schedule quarterly business review",
                "📚 Provide relevant documentation and resources"
            ])
        
        # Add specific interventions based on signals
        if metrics['usage_drop_pct'] > 30:
            interventions.append("📉 Investigate usage drop - check for adoption barriers")
        
        if metrics['ticket_volume'] > 10:
            interventions.append("🎫 Review and prioritize all open support tickets")
        
        if metrics['sentiment_score'] < -0.5:
            interventions.append("💬 Address negative sentiment immediately")
        
        if metrics['nps_score'] < 20:
            interventions.append("📊 Conduct NPS follow-up interview")
        
        return {
            "customer_id": customer_id,
            "priority": priority,
            "churn_probability": churn_prob,
            "recommended_interventions": interventions,
            "estimated_timeline": "Immediate action required" if priority == "CRITICAL" else "Within 48 hours",
            "success_probability": self._estimate_success_probability(churn_prob)
        }
    
    def _estimate_success_probability(self, churn_prob: float) -> float:
        """Estimate probability of successful intervention"""
        # Early intervention has higher success rate
        if churn_prob < 0.5:
            return 0.85
        elif churn_prob < 0.7:
            return 0.65
        else:
            return 0.45
    
    def generate_daily_briefing(self) -> Dict:
        """
        Generate daily executive briefing for Customer Success team
        """
        critical_customers = self.get_critical_customers(threshold=0.5)
        
        total_arr_at_risk = sum(c['contract_value'] for c in critical_customers)
        
        # Calculate sentiment distribution
        sentiment_counts = self.customers_df['last_ticket_sentiment'].value_counts().to_dict()
        
        # Recent ticket trends
        high_priority_tickets = self.tickets_df[
            self.tickets_df['sentiment'].isin(['very_negative', 'negative'])
        ].shape[0]
        
        return {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "summary": {
                "total_customers": len(self.customers_df),
                "critical_risk_customers": len([c for c in critical_customers if c['churn_probability'] >= 0.7]),
                "high_risk_customers": len([c for c in critical_customers if 0.5 <= c['churn_probability'] < 0.7]),
                "total_arr_at_risk": total_arr_at_risk,
                "high_priority_tickets": high_priority_tickets
            },
            "top_at_risk": critical_customers[:5],
            "sentiment_distribution": sentiment_counts,
            "action_items": self._generate_action_items(critical_customers)
        }
    
    def _generate_action_items(self, critical_customers: List[Dict]) -> List[str]:
        """Generate prioritized action items"""
        actions = []
        
        for customer in critical_customers[:3]:
            actions.append(
                f"🚨 Contact {customer['name']} immediately - "
                f"{int(customer['churn_probability']*100)}% churn risk, "
                f"${customer['contract_value']:,} at risk"
            )
        
        return actions


if __name__ == "__main__":
    # Test the agent
    agent = CustomerSuccessAgent()
    
    print("\n🔍 Testing Customer Success Agent\n")
    
    # Test critical customers
    critical = agent.get_critical_customers()
    print(f"Critical Customers: {len(critical)}")
    
    # Test specific customer analysis
    if len(critical) > 0:
        customer_id = critical[0]['customer_id']
        health = agent.analyze_customer_health(customer_id)
        print(f"\n{health['risk_color']} {health['name']} - Risk: {health['risk_level']}")
        print(f"Churn Probability: {health['churn_probability']*100:.1f}%")
        
        # Get intervention recommendations
        intervention = agent.recommend_intervention(customer_id)
        print(f"\nRecommended Interventions:")
        for i, action in enumerate(intervention['recommended_interventions'][:3], 1):
            print(f"{i}. {action}")
    
    # Generate daily briefing
    briefing = agent.generate_daily_briefing()
    print(f"\n📊 Daily Briefing Summary:")
    print(f"Total ARR at Risk: ${briefing['summary']['total_arr_at_risk']:,}")
    print(f"Critical Customers: {briefing['summary']['critical_risk_customers']}")

