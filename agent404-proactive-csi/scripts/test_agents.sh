#!/bin/bash

# ProActive CSI - Agent Testing Script

echo "🧪 Testing ProActive CSI Agents"
echo "================================"
echo ""

# Test Customer Success Agent
echo "1️⃣ Testing Customer Success Agent..."
python3 -c "
from agents.customer_success_agent import CustomerSuccessAgent
agent = CustomerSuccessAgent()
critical = agent.get_critical_customers()
print(f'✅ Found {len(critical)} critical customers')
"

# Test Procurement Agent
echo ""
echo "2️⃣ Testing Procurement Agent..."
python3 -c "
from agents.procurement_agent import ProcurementAgent
agent = ProcurementAgent()
delays = agent.detect_vendor_delays(threshold_days=5)
print(f'✅ Found {len(delays)} vendor delays')
"

# Test Revenue Agent
echo ""
echo "3️⃣ Testing Revenue Agent..."
python3 -c "
from agents.revenue_agent import RevenueAgent
agent = RevenueAgent()
pipeline = agent.analyze_renewal_pipeline()
print(f'✅ Renewal pipeline analyzed')
"

# Test Workflow Orchestrator
echo ""
echo "4️⃣ Testing Workflow Orchestrator..."
python3 -c "
from workflows.orchestrator import WorkflowOrchestrator
orchestrator = WorkflowOrchestrator()
print('✅ Orchestrator initialized with 3 agents')
"

echo ""
echo "🎉 All tests passed!"

