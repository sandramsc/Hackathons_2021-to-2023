"""
Revenue Protection Agent
Calculates ARR/MRR at risk, monitors contract value impact, creates finance insights
"""

import pandas as pd
import json
from datetime import datetime, timedelta
from typing import Dict, List, Tuple

class RevenueAgent:
    """
    AI-powered Revenue Protection Agent
    Monitors revenue at risk and provides financial impact analysis
    """
    
    def __init__(self, data_path: str = "data/"):
        self.data_path = data_path
        self.revenue_df = None
        self.customers_df = None
        self.load_data()
    
    def load_data(self):
        """Load revenue and customer data"""
        try:
            self.revenue_df = pd.read_csv(f"{self.data_path}/revenue_exposure_data.csv")
            self.customers_df = pd.read_csv(f"{self.data_path}/customer_success_data.csv")
            print("✅ Revenue Agent: Data loaded successfully")
        except Exception as e:
            print(f"❌ Error loading revenue data: {e}")
    
    def calculate_revenue_at_risk(self, customer_id: str, churn_probability: float) -> Dict:
        """
        Calculate revenue at risk for a specific customer
        """
        revenue = self.revenue_df[self.revenue_df['customer_id'] == customer_id]
        
        if revenue.empty:
            return {"error": "Customer revenue data not found"}
        
        revenue = revenue.iloc[0]
        customer = self.customers_df[self.customers_df['customer_id'] == customer_id]
        
        if customer.empty:
            return {"error": "Customer data not found"}
        
        customer = customer.iloc[0]
        
        # Calculate revenue at risk
        arr_at_risk = revenue['arr'] * churn_probability
        mrr_at_risk = revenue['mrr'] * churn_probability
        
        # Calculate days until renewal
        renewal_date = pd.to_datetime(customer['renewal_date'])
        days_to_renewal = (renewal_date - datetime.now()).days
        
        # Determine urgency
        if days_to_renewal <= 30 and churn_probability >= 0.7:
            urgency = "CRITICAL"
            urgency_color = "🔴"
        elif days_to_renewal <= 60 and churn_probability >= 0.5:
            urgency = "HIGH"
            urgency_color = "🟠"
        elif churn_probability >= 0.3:
            urgency = "MEDIUM"
            urgency_color = "🟡"
        else:
            urgency = "LOW"
            urgency_color = "🟢"
        
        return {
            "customer_id": customer_id,
            "customer_name": customer['name'],
            "churn_probability": churn_probability,
            "arr": revenue['arr'],
            "mrr": revenue['mrr'],
            "arr_at_risk": round(arr_at_risk, 2),
            "mrr_at_risk": round(mrr_at_risk, 2),
            "renewal_stage": revenue['renewal_stage'],
            "days_to_renewal": days_to_renewal,
            "urgency": urgency,
            "urgency_color": urgency_color,
            "retention_value": self._calculate_lifetime_value(revenue['arr'], churn_probability),
            "recommended_investment": self._calculate_recommended_investment(arr_at_risk)
        }
    
    def _calculate_lifetime_value(self, arr: float, churn_prob: float) -> Dict:
        """
        Calculate customer lifetime value
        Assuming average customer lifespan and retention scenarios
        """
        # If we retain them (success scenario)
        avg_lifespan_years = 3
        retention_probability = 1 - churn_prob
        expected_ltv = arr * avg_lifespan_years * retention_probability
        
        # If we lose them (failure scenario)
        lost_value = arr * avg_lifespan_years
        
        return {
            "expected_ltv": round(expected_ltv, 2),
            "potential_loss": round(lost_value, 2),
            "value_at_stake": round(lost_value - expected_ltv, 2)
        }
    
    def _calculate_recommended_investment(self, arr_at_risk: float) -> Dict:
        """
        Calculate recommended intervention investment
        Rule: Invest up to 20% of ARR at risk for intervention
        """
        max_investment = arr_at_risk * 0.20
        
        return {
            "max_investment": round(max_investment, 2),
            "rationale": f"Up to 20% of ARR at risk (${round(max_investment, 2):,})",
            "roi_breakeven": "Break-even if intervention success rate > 20%"
        }
    
    def get_total_revenue_exposure(self, churn_predictions: Dict[str, float]) -> Dict:
        """
        Calculate total revenue exposure across all at-risk customers
        churn_predictions: {customer_id: churn_probability}
        """
        total_arr_at_risk = 0
        total_mrr_at_risk = 0
        total_arr = 0
        customer_risks = []
        
        for customer_id, churn_prob in churn_predictions.items():
            if churn_prob >= 0.3:  # Only count customers with meaningful risk
                risk = self.calculate_revenue_at_risk(customer_id, churn_prob)
                
                if "error" not in risk:
                    total_arr_at_risk += risk['arr_at_risk']
                    total_mrr_at_risk += risk['mrr_at_risk']
                    total_arr += risk['arr']
                    customer_risks.append(risk)
        
        # Sort by ARR at risk (highest first)
        customer_risks.sort(key=lambda x: x['arr_at_risk'], reverse=True)
        
        # Calculate percentage of portfolio at risk
        portfolio_risk_pct = (total_arr_at_risk / total_arr * 100) if total_arr > 0 else 0
        
        return {
            "total_arr": round(total_arr, 2),
            "total_arr_at_risk": round(total_arr_at_risk, 2),
            "total_mrr_at_risk": round(total_mrr_at_risk, 2),
            "portfolio_risk_percentage": round(portfolio_risk_pct, 2),
            "num_at_risk_customers": len(customer_risks),
            "top_risks": customer_risks[:10],
            "risk_breakdown": self._calculate_risk_breakdown(customer_risks),
            "recommended_actions": self._generate_revenue_actions(customer_risks)
        }
    
    def _calculate_risk_breakdown(self, customer_risks: List[Dict]) -> Dict:
        """Break down revenue risk by urgency level"""
        critical = sum(r['arr_at_risk'] for r in customer_risks if r['urgency'] == 'CRITICAL')
        high = sum(r['arr_at_risk'] for r in customer_risks if r['urgency'] == 'HIGH')
        medium = sum(r['arr_at_risk'] for r in customer_risks if r['urgency'] == 'MEDIUM')
        
        return {
            "critical": round(critical, 2),
            "high": round(high, 2),
            "medium": round(medium, 2)
        }
    
    def _generate_revenue_actions(self, customer_risks: List[Dict]) -> List[str]:
        """Generate financial action items"""
        actions = []
        
        # Top 3 risks
        for risk in customer_risks[:3]:
            actions.append(
                f"🚨 Protect ${risk['arr_at_risk']:,.0f} ARR from {risk['customer_name']} - "
                f"{risk['days_to_renewal']} days to renewal"
            )
        
        # High-level recommendations
        total_at_risk = sum(r['arr_at_risk'] for r in customer_risks)
        if total_at_risk > 500000:
            actions.append("💰 Consider executive-level customer retention program")
        
        if len([r for r in customer_risks if r['urgency'] == 'CRITICAL']) > 3:
            actions.append("📊 Request emergency revenue protection budget allocation")
        
        return actions
    
    def generate_cfo_briefing(self, churn_predictions: Dict[str, float]) -> Dict:
        """
        Generate executive briefing for CFO/Finance team
        """
        exposure = self.get_total_revenue_exposure(churn_predictions)
        
        # Calculate financial impact scenarios
        best_case = exposure['total_arr_at_risk'] * 0.2  # Save 80%
        expected_case = exposure['total_arr_at_risk'] * 0.5  # Save 50%
        worst_case = exposure['total_arr_at_risk'] * 0.8  # Save 20%
        
        # Calculate ROI of intervention program
        intervention_cost = exposure['total_arr_at_risk'] * 0.15  # 15% investment
        expected_return = expected_case
        roi = ((expected_return - intervention_cost) / intervention_cost * 100) if intervention_cost > 0 else 0
        
        return {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "executive_summary": {
                "total_annual_revenue": exposure['total_arr'],
                "revenue_at_risk": exposure['total_arr_at_risk'],
                "portfolio_risk_percentage": exposure['portfolio_risk_percentage'],
                "customers_at_risk": exposure['num_at_risk_customers']
            },
            "risk_breakdown": exposure['risk_breakdown'],
            "financial_scenarios": {
                "best_case_loss": round(best_case, 2),
                "expected_case_loss": round(expected_case, 2),
                "worst_case_loss": round(worst_case, 2)
            },
            "intervention_economics": {
                "recommended_investment": round(intervention_cost, 2),
                "expected_revenue_saved": round(expected_return, 2),
                "estimated_roi": round(roi, 1),
                "payback_period_months": 3
            },
            "top_revenue_risks": exposure['top_risks'][:5],
            "strategic_recommendations": self._generate_cfo_recommendations(exposure)
        }
    
    def _generate_cfo_recommendations(self, exposure: Dict) -> List[str]:
        """Generate strategic recommendations for CFO"""
        recommendations = []
        
        risk_pct = exposure['portfolio_risk_percentage']
        
        if risk_pct > 15:
            recommendations.append("🚨 Portfolio risk exceeds 15% threshold - implement emergency retention program")
        elif risk_pct > 10:
            recommendations.append("⚠️ Portfolio risk elevated - increase customer success investment")
        
        if exposure['risk_breakdown']['critical'] > 200000:
            recommendations.append("💰 Approve executive escalation budget for critical accounts")
        
        recommendations.extend([
            "📊 Implement predictive churn analytics across all segments",
            "🎯 Increase customer success team headcount by 20%",
            "💼 Develop retention bonus structure for account managers",
            "📈 Invest in customer health monitoring infrastructure"
        ])
        
        return recommendations
    
    def analyze_renewal_pipeline(self) -> Dict:
        """
        Analyze upcoming renewal pipeline and risks
        """
        # Merge customer and revenue data
        pipeline = pd.merge(
            self.customers_df,
            self.revenue_df,
            on='customer_id',
            how='inner'
        )
        
        # Calculate days to renewal
        pipeline['renewal_date'] = pd.to_datetime(pipeline['renewal_date'])
        today = pd.Timestamp(datetime.now())
        pipeline['days_to_renewal'] = (pipeline['renewal_date'] - today).dt.days
        
        # Segment by time horizon
        next_30_days = pipeline[pipeline['days_to_renewal'] <= 30]
        next_60_days = pipeline[(pipeline['days_to_renewal'] > 30) & (pipeline['days_to_renewal'] <= 60)]
        next_90_days = pipeline[(pipeline['days_to_renewal'] > 60) & (pipeline['days_to_renewal'] <= 90)]
        
        return {
            "pipeline_summary": {
                "next_30_days": {
                    "count": len(next_30_days),
                    "total_arr": round(next_30_days['arr'].sum(), 2),
                    "avg_contract_value": round(next_30_days['arr'].mean(), 2) if len(next_30_days) > 0 else 0
                },
                "next_60_days": {
                    "count": len(next_60_days),
                    "total_arr": round(next_60_days['arr'].sum(), 2),
                    "avg_contract_value": round(next_60_days['arr'].mean(), 2) if len(next_60_days) > 0 else 0
                },
                "next_90_days": {
                    "count": len(next_90_days),
                    "total_arr": round(next_90_days['arr'].sum(), 2),
                    "avg_contract_value": round(next_90_days['arr'].mean(), 2) if len(next_90_days) > 0 else 0
                }
            },
            "immediate_attention_required": next_30_days[['customer_id', 'name', 'arr', 'days_to_renewal']].to_dict('records')
        }


if __name__ == "__main__":
    # Test the agent
    agent = RevenueAgent()
    
    print("\n🔍 Testing Revenue Agent\n")
    
    # Test revenue calculation
    test_customer = "C-001"
    test_churn_prob = 0.75
    
    risk = agent.calculate_revenue_at_risk(test_customer, test_churn_prob)
    print(f"Customer: {risk['customer_name']}")
    print(f"ARR at Risk: ${risk['arr_at_risk']:,.2f}")
    print(f"Urgency: {risk['urgency_color']} {risk['urgency']}")
    print(f"Recommended Investment: ${risk['recommended_investment']['max_investment']:,.2f}")
    
    # Test total exposure
    churn_predictions = {
        "C-001": 0.75,
        "C-003": 0.58,
        "C-005": 0.62,
        "C-008": 0.71
    }
    
    exposure = agent.get_total_revenue_exposure(churn_predictions)
    print(f"\n💰 Total Revenue Exposure:")
    print(f"Total ARR at Risk: ${exposure['total_arr_at_risk']:,.2f}")
    print(f"Portfolio Risk: {exposure['portfolio_risk_percentage']:.1f}%")
    print(f"Customers at Risk: {exposure['num_at_risk_customers']}")
    
    # Test CFO briefing
    briefing = agent.generate_cfo_briefing(churn_predictions)
    print(f"\n📊 CFO Briefing Summary:")
    print(f"Expected Case Loss: ${briefing['financial_scenarios']['expected_case_loss']:,.2f}")
    print(f"Recommended Investment: ${briefing['intervention_economics']['recommended_investment']:,.2f}")
    print(f"Estimated ROI: {briefing['intervention_economics']['estimated_roi']:.1f}%")

