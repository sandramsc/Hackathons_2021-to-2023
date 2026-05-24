"""
Test Suite for ProActive CSI Agents
Tests all three agents and workflow orchestration
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from agents.customer_success_agent import CustomerSuccessAgent
from agents.procurement_agent import ProcurementAgent
from agents.revenue_agent import RevenueAgent
from workflows.orchestrator import WorkflowOrchestrator


class TestCustomerSuccessAgent:
    """Test Customer Success Intelligence Agent"""
    
    def setup_method(self):
        """Setup test fixtures"""
        self.agent = CustomerSuccessAgent()
    
    def test_agent_initialization(self):
        """Test agent loads successfully"""
        assert self.agent is not None
        assert self.agent.customers_df is not None
        assert len(self.agent.customers_df) > 0
    
    def test_predict_churn_probability(self):
        """Test churn probability prediction"""
        churn_prob = self.agent.predict_churn_probability("C-001")
        assert 0 <= churn_prob <= 1
        assert churn_prob > 0.5  # C-001 should be high risk
    
    def test_analyze_customer_health(self):
        """Test customer health analysis"""
        health = self.agent.analyze_customer_health("C-001")
        assert "churn_probability" in health
        assert "risk_level" in health
        assert health["risk_level"] in ["LOW", "MEDIUM", "HIGH", "CRITICAL"]
    
    def test_get_critical_customers(self):
        """Test critical customer identification"""
        critical = self.agent.get_critical_customers(threshold=0.5)
        assert isinstance(critical, list)
        assert len(critical) >= 0
        if len(critical) > 0:
            assert "churn_probability" in critical[0]
            assert critical[0]["churn_probability"] >= 0.5
    
    def test_recommend_intervention(self):
        """Test intervention recommendation"""
        intervention = self.agent.recommend_intervention("C-001")
        assert "priority" in intervention
        assert "recommended_interventions" in intervention
        assert len(intervention["recommended_interventions"]) > 0
    
    def test_generate_daily_briefing(self):
        """Test daily briefing generation"""
        briefing = self.agent.generate_daily_briefing()
        assert "summary" in briefing
        assert "total_customers" in briefing["summary"]
        assert "total_arr_at_risk" in briefing["summary"]


class TestProcurementAgent:
    """Test Procurement Intelligence Agent"""
    
    def setup_method(self):
        """Setup test fixtures"""
        self.agent = ProcurementAgent()
    
    def test_agent_initialization(self):
        """Test agent loads successfully"""
        assert self.agent is not None
        assert self.agent.vendors_df is not None
        assert len(self.agent.vendors_df) > 0
    
    def test_detect_vendor_delays(self):
        """Test vendor delay detection"""
        delays = self.agent.detect_vendor_delays(threshold_days=5)
        assert isinstance(delays, list)
        for delay in delays:
            assert delay["delay_days"] >= 5
            assert "vendor_name" in delay
            assert "affected_customers" in delay
    
    def test_correlate_vendor_to_customer_risk(self):
        """Test vendor-customer risk correlation"""
        correlation = self.agent.correlate_vendor_to_customer_risk("V-101")
        assert "risk_level" in correlation
        assert "affected_customers" in correlation
        assert "customer_impact_prediction" in correlation
    
    def test_vendor_performance_scorecard(self):
        """Test vendor performance scorecard"""
        scorecard = self.agent.get_vendor_performance_scorecard("V-101")
        assert "overall_score" in scorecard
        assert "rating" in scorecard
        assert 0 <= scorecard["overall_score"] <= 100
    
    def test_generate_procurement_brief(self):
        """Test procurement briefing generation"""
        briefing = self.agent.generate_procurement_brief()
        assert "summary" in briefing
        assert "total_vendors_delayed" in briefing["summary"]


class TestRevenueAgent:
    """Test Revenue Protection Agent"""
    
    def setup_method(self):
        """Setup test fixtures"""
        self.agent = RevenueAgent()
    
    def test_agent_initialization(self):
        """Test agent loads successfully"""
        assert self.agent is not None
        assert self.agent.revenue_df is not None
        assert len(self.agent.revenue_df) > 0
    
    def test_calculate_revenue_at_risk(self):
        """Test revenue at risk calculation"""
        risk = self.agent.calculate_revenue_at_risk("C-001", 0.75)
        assert "arr_at_risk" in risk
        assert "mrr_at_risk" in risk
        assert "urgency" in risk
        assert risk["arr_at_risk"] > 0
    
    def test_get_total_revenue_exposure(self):
        """Test total revenue exposure calculation"""
        churn_predictions = {
            "C-001": 0.75,
            "C-003": 0.58,
            "C-005": 0.62
        }
        exposure = self.agent.get_total_revenue_exposure(churn_predictions)
        assert "total_arr_at_risk" in exposure
        assert "portfolio_risk_percentage" in exposure
        assert exposure["total_arr_at_risk"] > 0
    
    def test_generate_cfo_briefing(self):
        """Test CFO briefing generation"""
        churn_predictions = {"C-001": 0.75}
        briefing = self.agent.generate_cfo_briefing(churn_predictions)
        assert "executive_summary" in briefing
        assert "financial_scenarios" in briefing
        assert "intervention_economics" in briefing
    
    def test_analyze_renewal_pipeline(self):
        """Test renewal pipeline analysis"""
        pipeline = self.agent.analyze_renewal_pipeline()
        assert "pipeline_summary" in pipeline
        assert "next_30_days" in pipeline["pipeline_summary"]


class TestWorkflowOrchestrator:
    """Test Workflow Orchestrator"""
    
    def setup_method(self):
        """Setup test fixtures"""
        self.orchestrator = WorkflowOrchestrator()
    
    def test_orchestrator_initialization(self):
        """Test orchestrator loads all agents"""
        assert self.orchestrator.cs_agent is not None
        assert self.orchestrator.procurement_agent is not None
        assert self.orchestrator.revenue_agent is not None
    
    def test_workflow_churn_prediction(self):
        """Test Workflow 1: Churn Prediction"""
        result = self.orchestrator.workflow_churn_prediction("C-001")
        assert "workflow" in result
        assert result["workflow"] == "Churn Prediction"
        assert "steps" in result
        assert len(result["steps"]) == 5
        assert "churn_probability" in result
    
    def test_workflow_procurement_early_warning(self):
        """Test Workflow 2: Procurement Early-Warning"""
        result = self.orchestrator.workflow_procurement_early_warning("V-101")
        assert "workflow" in result
        assert result["workflow"] == "Procurement Early-Warning"
        assert "steps" in result
        assert "revenue_exposure" in result
    
    def test_workflow_customer_escalation(self):
        """Test Workflow 3: Customer Escalation"""
        result = self.orchestrator.workflow_customer_escalation("C-001")
        assert "workflow" in result
        assert result["workflow"] == "Customer Escalation Auto-Resolution"
        assert "action_plan" in result
        assert "notification" in result
    
    def test_workflow_contract_renewal(self):
        """Test Workflow 4: Contract Renewal Prep"""
        result = self.orchestrator.workflow_contract_renewal_prep("C-001")
        assert "workflow" in result
        assert result["workflow"] == "Contract Renewal Prep"
        assert "renewal_brief" in result
        assert "email_draft" in result
    
    def test_workflow_executive_brief(self):
        """Test Workflow 5: Daily Executive Brief"""
        result = self.orchestrator.workflow_daily_executive_brief()
        assert "workflow" in result
        assert result["workflow"] == "Daily Executive Brief"
        assert "executive_brief" in result
        assert "risk_summary" in result
    
    def test_workflow_procurement_customer_bridge(self):
        """Test Workflow 6: Procurement-Customer Bridge"""
        result = self.orchestrator.workflow_procurement_customer_bridge("V-101")
        assert "workflow" in result
        assert result["workflow"] == "Procurement-Customer Impact Bridge"
        assert "at_risk_customers" in result
        assert "tasks_created" in result


def run_all_tests():
    """Run all tests and print results"""
    print("\n🧪 Running ProActive CSI Test Suite")
    print("=" * 60)
    
    test_count = 0
    passed = 0
    failed = 0
    
    # Test Customer Success Agent
    print("\n1️⃣ Testing Customer Success Agent...")
    cs_tests = TestCustomerSuccessAgent()
    cs_tests.setup_method()
    
    tests = [
        ("Agent Initialization", cs_tests.test_agent_initialization),
        ("Churn Prediction", cs_tests.test_predict_churn_probability),
        ("Customer Health Analysis", cs_tests.test_analyze_customer_health),
        ("Critical Customer Identification", cs_tests.test_get_critical_customers),
        ("Intervention Recommendation", cs_tests.test_recommend_intervention),
        ("Daily Briefing", cs_tests.test_generate_daily_briefing)
    ]
    
    for test_name, test_func in tests:
        test_count += 1
        try:
            test_func()
            print(f"  ✅ {test_name}")
            passed += 1
        except Exception as e:
            print(f"  ❌ {test_name}: {str(e)}")
            failed += 1
    
    # Test Procurement Agent
    print("\n2️⃣ Testing Procurement Agent...")
    proc_tests = TestProcurementAgent()
    proc_tests.setup_method()
    
    tests = [
        ("Agent Initialization", proc_tests.test_agent_initialization),
        ("Vendor Delay Detection", proc_tests.test_detect_vendor_delays),
        ("Vendor-Customer Correlation", proc_tests.test_correlate_vendor_to_customer_risk),
        ("Vendor Scorecard", proc_tests.test_vendor_performance_scorecard),
        ("Procurement Briefing", proc_tests.test_generate_procurement_brief)
    ]
    
    for test_name, test_func in tests:
        test_count += 1
        try:
            test_func()
            print(f"  ✅ {test_name}")
            passed += 1
        except Exception as e:
            print(f"  ❌ {test_name}: {str(e)}")
            failed += 1
    
    # Test Revenue Agent
    print("\n3️⃣ Testing Revenue Agent...")
    rev_tests = TestRevenueAgent()
    rev_tests.setup_method()
    
    tests = [
        ("Agent Initialization", rev_tests.test_agent_initialization),
        ("Revenue at Risk Calculation", rev_tests.test_calculate_revenue_at_risk),
        ("Total Revenue Exposure", rev_tests.test_get_total_revenue_exposure),
        ("CFO Briefing", rev_tests.test_generate_cfo_briefing),
        ("Renewal Pipeline Analysis", rev_tests.test_analyze_renewal_pipeline)
    ]
    
    for test_name, test_func in tests:
        test_count += 1
        try:
            test_func()
            print(f"  ✅ {test_name}")
            passed += 1
        except Exception as e:
            print(f"  ❌ {test_name}: {str(e)}")
            failed += 1
    
    # Test Workflow Orchestrator
    print("\n4️⃣ Testing Workflow Orchestrator...")
    orch_tests = TestWorkflowOrchestrator()
    orch_tests.setup_method()
    
    tests = [
        ("Orchestrator Initialization", orch_tests.test_orchestrator_initialization),
        ("Workflow 1: Churn Prediction", orch_tests.test_workflow_churn_prediction),
        ("Workflow 2: Procurement Warning", orch_tests.test_workflow_procurement_early_warning),
        ("Workflow 3: Customer Escalation", orch_tests.test_workflow_customer_escalation),
        ("Workflow 4: Renewal Prep", orch_tests.test_workflow_contract_renewal),
        ("Workflow 5: Executive Brief", orch_tests.test_workflow_executive_brief),
        ("Workflow 6: Procurement Bridge", orch_tests.test_workflow_procurement_customer_bridge)
    ]
    
    for test_name, test_func in tests:
        test_count += 1
        try:
            test_func()
            print(f"  ✅ {test_name}")
            passed += 1
        except Exception as e:
            print(f"  ❌ {test_name}: {str(e)}")
            failed += 1
    
    # Summary
    print("\n" + "=" * 60)
    print(f"🎯 Test Results: {passed}/{test_count} passed")
    if failed == 0:
        print("🎉 All tests passed!")
    else:
        print(f"⚠️ {failed} tests failed")
    print("=" * 60)
    
    return passed == test_count


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)

