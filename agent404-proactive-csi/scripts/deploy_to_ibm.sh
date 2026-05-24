#!/bin/bash

# ProActive CSI - IBM watsonx Orchestrate Deployment Script

echo "🚀 ProActive CSI - IBM watsonx Orchestrate Deployment"
echo "========================================================="
echo ""

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}This script will deploy ProActive CSI to IBM watsonx Orchestrate${NC}"
echo ""

# Check if configuration file exists
if [ ! -f "proactive-csi-agent.yaml" ]; then
    echo -e "${RED}❌ Configuration file not found: proactive-csi-agent.yaml${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Configuration file found${NC}"
echo ""

# Deployment steps
echo "📋 Deployment Steps:"
echo "1. Login to IBM Cloud"
echo "2. Configure watsonx Orchestrate"
echo "3. Upload agent configuration"
echo "4. Deploy services"
echo "5. Test deployment"
echo ""

read -p "Do you want to continue? (y/n) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Deployment cancelled."
    exit 1
fi

# Step 1: IBM Cloud Login
echo ""
echo "Step 1: IBM Cloud Login"
echo "========================"
echo ""
echo "Please ensure you're logged in to IBM Cloud:"
echo "  ibmcloud login --sso"
echo ""
read -p "Are you logged in to IBM Cloud? (y/n) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Please login to IBM Cloud first and run this script again."
    exit 1
fi

# Step 2: Configure watsonx Orchestrate
echo ""
echo "Step 2: Configure watsonx Orchestrate"
echo "======================================"
echo ""
echo "Manual steps required:"
echo "1. Go to: https://dl.watson-orchestrate.ibm.com/"
echo "2. Navigate to 'Skills' → 'Import Skill'"
echo "3. Upload: proactive-csi-agent.yaml"
echo "4. Configure IBM service connections:"
echo "   - watsonx.ai"
echo "   - NLU"
echo "   - Speech-to-Text"
echo "   - Text-to-Speech"
echo "   - Cloudant"
echo ""
read -p "Have you completed these steps? (y/n) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Please complete the configuration and run this script again."
    exit 1
fi

# Step 3: Test deployment
echo ""
echo "Step 3: Test Deployment"
echo "======================="
echo ""
echo "Testing agent connections..."
python3 -c "
from agents.customer_success_agent import CustomerSuccessAgent
from agents.procurement_agent import ProcurementAgent
from agents.revenue_agent import RevenueAgent

print('Testing Customer Success Agent...')
cs_agent = CustomerSuccessAgent()
print('✅ Customer Success Agent loaded')

print('Testing Procurement Agent...')
proc_agent = ProcurementAgent()
print('✅ Procurement Agent loaded')

print('Testing Revenue Agent...')
rev_agent = RevenueAgent()
print('✅ Revenue Agent loaded')

print('')
print('🎉 All agents loaded successfully!')
"

if [ $? -eq 0 ]; then
    echo ""
    echo -e "${GREEN}========================================${NC}"
    echo -e "${GREEN}✅ Deployment Completed Successfully!${NC}"
    echo -e "${GREEN}========================================${NC}"
    echo ""
    echo "Next steps:"
    echo "1. Open watsonx Orchestrate: https://dl.watson-orchestrate.ibm.com/"
    echo "2. Test the agent skills"
    echo "3. Run demo workflows"
    echo ""
    echo "For testing locally:"
    echo "  ./scripts/run_demo.sh"
    echo ""
else
    echo ""
    echo -e "${RED}❌ Deployment failed. Please check the errors above.${NC}"
    exit 1
fi

