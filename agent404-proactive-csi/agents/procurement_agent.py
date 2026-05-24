"""
Procurement Intelligence Agent
Monitors vendor performance, detects supply chain risks, correlates to customer impact
"""

import pandas as pd
import json
from datetime import datetime, timedelta
from typing import Dict, List, Tuple
import ast

class ProcurementAgent:
    """
    AI-powered Procurement Intelligence Agent
    Detects vendor risks and correlates impact to customers
    """
    
    def __init__(self, data_path: str = "data/"):
        self.data_path = data_path
        self.vendors_df = None
        self.contracts_df = None
        self.load_data()
    
    def load_data(self):
        """Load procurement and vendor data"""
        try:
            self.vendors_df = pd.read_csv(f"{self.data_path}/procurement_vendor_data.csv")
            self.contracts_df = pd.read_csv(f"{self.data_path}/contracts.csv")
            print("✅ Procurement Agent: Data loaded successfully")
        except Exception as e:
            print(f"❌ Error loading procurement data: {e}")
    
    def detect_vendor_delays(self, threshold_days: int = 5) -> List[Dict]:
        """
        Detect vendors with significant delivery delays
        """
        delayed_vendors = self.vendors_df[self.vendors_df['delay_days'] >= threshold_days]
        
        results = []
        for _, vendor in delayed_vendors.iterrows():
            # Parse affected customers
            affected = self._parse_customer_list(vendor['affected_customers'])
            
            # Calculate severity
            severity = self._calculate_delay_severity(
                vendor['delay_days'], 
                vendor['defect_rate'],
                len(affected)
            )
            
            results.append({
                "vendor_id": vendor['vendor_id'],
                "vendor_name": vendor['vendor_name'],
                "delay_days": vendor['delay_days'],
                "defect_rate": vendor['defect_rate'],
                "expected_date": vendor['expected_delivery_date'],
                "actual_date": vendor['actual_delivery_date'],
                "contract_value": vendor['contract_value'],
                "affected_customers": affected,
                "num_affected": len(affected),
                "severity": severity
            })
        
        # Sort by severity (highest first)
        results.sort(key=lambda x: x['severity'], reverse=True)
        
        return results
    
    def _parse_customer_list(self, customer_str: str) -> List[str]:
        """Parse customer list from string representation"""
        try:
            return ast.literal_eval(customer_str)
        except:
            return []
    
    def _calculate_delay_severity(self, delay_days: int, defect_rate: float, num_affected: int) -> float:
        """
        Calculate vendor delay severity score
        Range: 0.0 to 1.0
        """
        # Weighted factors
        delay_score = min(delay_days / 30, 1.0) * 0.5  # 30+ days = max delay impact
        defect_score = min(defect_rate * 10, 1.0) * 0.3  # 10%+ defect = max defect impact
        customer_score = min(num_affected / 5, 1.0) * 0.2  # 5+ customers = max customer impact
        
        return delay_score + defect_score + customer_score
    
    def correlate_vendor_to_customer_risk(self, vendor_id: str) -> Dict:
        """
        Correlate vendor delays to customer churn risk
        """
        vendor = self.vendors_df[self.vendors_df['vendor_id'] == vendor_id]
        
        if vendor.empty:
            return {"error": "Vendor not found"}
        
        vendor = vendor.iloc[0]
        affected_customers = self._parse_customer_list(vendor['affected_customers'])
        
        # Calculate risk level
        delay_days = vendor['delay_days']
        if delay_days >= 14:
            risk_level = "CRITICAL"
            risk_color = "🔴"
        elif delay_days >= 7:
            risk_level = "HIGH"
            risk_color = "🟠"
        elif delay_days >= 3:
            risk_level = "MEDIUM"
            risk_color = "🟡"
        else:
            risk_level = "LOW"
            risk_color = "🟢"
        
        # Check for contract penalties
        contracts = self.contracts_df[self.contracts_df['vendor_id'] == vendor_id]
        penalties_triggered = []
        
        for _, contract in contracts.iterrows():
            sla_days = contract['service_level_days']
            if delay_days > sla_days:
                penalties_triggered.append({
                    "contract_id": contract['contract_id'],
                    "customer_id": contract['customer_id'],
                    "penalty": contract['penalty_clause'],
                    "days_exceeded": delay_days - sla_days
                })
        
        return {
            "vendor_id": vendor_id,
            "vendor_name": vendor['vendor_name'],
            "risk_level": risk_level,
            "risk_color": risk_color,
            "delay_info": {
                "delay_days": delay_days,
                "expected_date": vendor['expected_delivery_date'],
                "actual_date": vendor['actual_delivery_date'],
                "defect_rate": vendor['defect_rate']
            },
            "affected_customers": affected_customers,
            "num_affected": len(affected_customers),
            "contract_value": vendor['contract_value'],
            "penalties_triggered": penalties_triggered,
            "customer_impact_prediction": self._predict_customer_impact(delay_days, affected_customers)
        }
    
    def _predict_customer_impact(self, delay_days: int, affected_customers: List[str]) -> Dict:
        """
        Predict impact on customer satisfaction and churn risk
        """
        # Impact increases with delay duration
        satisfaction_drop = min(delay_days * 2, 40)  # Up to 40% satisfaction drop
        churn_risk_increase = min(delay_days * 0.03, 0.35)  # Up to 35% churn risk increase
        
        return {
            "estimated_satisfaction_drop": f"{satisfaction_drop}%",
            "estimated_churn_risk_increase": f"{int(churn_risk_increase * 100)}%",
            "recommended_actions": self._generate_remediation_actions(delay_days),
            "urgency": "IMMEDIATE" if delay_days >= 14 else "HIGH" if delay_days >= 7 else "MEDIUM"
        }
    
    def _generate_remediation_actions(self, delay_days: int) -> List[str]:
        """Generate recommended remediation actions"""
        actions = []
        
        if delay_days >= 14:
            actions.extend([
                "🚨 Escalate to vendor executive leadership immediately",
                "📞 Schedule emergency call with all affected customers",
                "🎁 Prepare compensation package for impacted customers",
                "🔄 Identify alternative vendors for future orders",
                "📋 Document all delays for contract renegotiation"
            ])
        elif delay_days >= 7:
            actions.extend([
                "📞 Contact vendor account manager for status update",
                "📧 Proactively notify affected customers of delay",
                "🔍 Assess impact on customer deliverables",
                "📊 Update internal stakeholders on timeline",
                "⚠️ Prepare contingency plans"
            ])
        else:
            actions.extend([
                "📧 Request vendor status update",
                "📊 Monitor situation closely",
                "📋 Document delay for vendor scorecard"
            ])
        
        return actions
    
    def generate_procurement_brief(self) -> Dict:
        """
        Generate procurement risk briefing
        """
        delayed_vendors = self.detect_vendor_delays(threshold_days=1)
        
        critical_delays = [v for v in delayed_vendors if v['delay_days'] >= 10]
        total_customers_affected = sum(v['num_affected'] for v in delayed_vendors)
        total_contract_value = sum(v['contract_value'] for v in delayed_vendors)
        
        # Calculate penalties
        total_penalties = 0
        for vendor in delayed_vendors:
            vendor_contracts = self.contracts_df[
                self.contracts_df['vendor_id'] == vendor['vendor_id']
            ]
            for _, contract in vendor_contracts.iterrows():
                if vendor['delay_days'] > contract['service_level_days']:
                    # Extract penalty percentage from clause
                    penalty_clause = contract['penalty_clause']
                    try:
                        penalty_pct = float(penalty_clause.split('%')[0].split()[-1]) / 100
                        total_penalties += vendor['contract_value'] * penalty_pct
                    except:
                        pass
        
        return {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "summary": {
                "total_vendors_delayed": len(delayed_vendors),
                "critical_delays": len(critical_delays),
                "customers_affected": total_customers_affected,
                "total_contract_value_at_risk": total_contract_value,
                "estimated_penalties": total_penalties
            },
            "critical_vendors": critical_delays,
            "top_risks": delayed_vendors[:5],
            "action_items": self._generate_procurement_actions(delayed_vendors)
        }
    
    def _generate_procurement_actions(self, delayed_vendors: List[Dict]) -> List[str]:
        """Generate prioritized procurement action items"""
        actions = []
        
        for vendor in delayed_vendors[:3]:
            actions.append(
                f"🚨 {vendor['vendor_name']} - {vendor['delay_days']} days late, "
                f"{vendor['num_affected']} customers affected"
            )
        
        return actions
    
    def get_vendor_performance_scorecard(self, vendor_id: str) -> Dict:
        """
        Generate vendor performance scorecard
        """
        vendor = self.vendors_df[self.vendors_df['vendor_id'] == vendor_id]
        
        if vendor.empty:
            return {"error": "Vendor not found"}
        
        vendor = vendor.iloc[0]
        
        # Calculate performance scores
        on_time_score = max(0, 100 - (vendor['delay_days'] * 5))
        quality_score = max(0, 100 - (vendor['defect_rate'] * 1000))
        overall_score = (on_time_score * 0.6 + quality_score * 0.4)
        
        # Determine rating
        if overall_score >= 90:
            rating = "⭐⭐⭐⭐⭐ EXCELLENT"
        elif overall_score >= 75:
            rating = "⭐⭐⭐⭐ GOOD"
        elif overall_score >= 60:
            rating = "⭐⭐⭐ SATISFACTORY"
        elif overall_score >= 40:
            rating = "⭐⭐ NEEDS IMPROVEMENT"
        else:
            rating = "⭐ POOR"
        
        return {
            "vendor_id": vendor_id,
            "vendor_name": vendor['vendor_name'],
            "overall_score": round(overall_score, 1),
            "rating": rating,
            "performance_metrics": {
                "on_time_delivery_score": round(on_time_score, 1),
                "quality_score": round(quality_score, 1),
                "delay_days": vendor['delay_days'],
                "defect_rate": vendor['defect_rate']
            },
            "contract_value": vendor['contract_value'],
            "affected_customers": self._parse_customer_list(vendor['affected_customers']),
            "recommendation": self._get_vendor_recommendation(overall_score)
        }
    
    def _get_vendor_recommendation(self, score: float) -> str:
        """Get vendor relationship recommendation"""
        if score >= 90:
            return "✅ Maintain and expand partnership"
        elif score >= 75:
            return "✅ Continue partnership with monitoring"
        elif score >= 60:
            return "⚠️ Place on probation - require improvement plan"
        elif score >= 40:
            return "⚠️ Consider alternative vendors"
        else:
            return "🚫 Recommend contract termination"


if __name__ == "__main__":
    # Test the agent
    agent = ProcurementAgent()
    
    print("\n🔍 Testing Procurement Agent\n")
    
    # Test vendor delays
    delays = agent.detect_vendor_delays(threshold_days=5)
    print(f"Vendors with Delays: {len(delays)}")
    
    if len(delays) > 0:
        vendor = delays[0]
        print(f"\n{vendor['vendor_name']}: {vendor['delay_days']} days late")
        print(f"Affected Customers: {vendor['num_affected']}")
        
        # Test vendor correlation
        correlation = agent.correlate_vendor_to_customer_risk(vendor['vendor_id'])
        print(f"\nRisk Level: {correlation['risk_color']} {correlation['risk_level']}")
        print(f"Customer Impact Actions:")
        for action in correlation['customer_impact_prediction']['recommended_actions'][:3]:
            print(f"  • {action}")
    
    # Generate briefing
    briefing = agent.generate_procurement_brief()
    print(f"\n📊 Procurement Briefing:")
    print(f"Critical Delays: {briefing['summary']['critical_delays']}")
    print(f"Customers Affected: {briefing['summary']['customers_affected']}")
    print(f"Estimated Penalties: ${briefing['summary']['estimated_penalties']:,.2f}")

