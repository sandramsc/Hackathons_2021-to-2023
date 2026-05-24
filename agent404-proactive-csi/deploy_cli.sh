#!/bin/bash

# ProActive CSI - CLI Deployment Script
# Deploys agent to IBM watsonx Orchestrate using CLI

echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║  🚀 ProActive CSI - CLI Deployment to IBM Orchestrate 🚀    ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

cd "$(dirname "$0")"

# Check if orchestrate CLI is installed
if ! command -v orchestrate &> /dev/null; then
    echo -e "${RED}❌ Orchestrate CLI not found${NC}"
    echo -e "${YELLOW}Installing...${NC}"
    pip3 install ibm-watsonx-orchestrate
    if ! command -v orchestrate &> /dev/null; then
        echo -e "${RED}❌ Failed to install CLI${NC}"
        exit 1
    fi
fi

echo -e "${GREEN}✅ Orchestrate CLI found${NC}"
echo ""

# Check if YAML file exists
YAML_FILE="proactive-csi-agent-orchestrate.yaml"
if [ ! -f "$YAML_FILE" ]; then
    echo -e "${RED}❌ Configuration file not found: $YAML_FILE${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Configuration file found: $YAML_FILE${NC}"
echo ""

# Show current environments
echo -e "${BLUE}📋 Current environments:${NC}"
orchestrate env list
echo ""

# Check if production-au environment exists
if orchestrate env list | grep -q "production-au"; then
    echo -e "${BLUE}🔑 Activating production-au environment...${NC}"
    echo -e "${YELLOW}You'll need to enter your IBM Cloud API key${NC}"
    echo ""
    echo -e "${BLUE}To get your API key:${NC}"
    echo "1. Go to: https://cloud.ibm.com/iam/apikeys"
    echo "2. Create a new API key or use existing one"
    echo "3. Copy the API key"
    echo ""
    read -p "Press Enter when ready to activate environment..."
    
    orchestrate env activate production-au
    
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✅ Environment activated${NC}"
    else
        echo -e "${RED}❌ Failed to activate environment${NC}"
        echo -e "${YELLOW}Please check your API key and try again${NC}"
        exit 1
    fi
else
    echo -e "${YELLOW}⚠️  production-au environment not found${NC}"
    echo -e "${BLUE}Creating new environment...${NC}"
    echo ""
    echo -e "${BLUE}Service URL:${NC}"
    echo "https://api.au-syd.watson-orchestrate.cloud.ibm.com/instances/f16c2181-a811-4d84-8e15-33cfebe50928"
    echo ""
    echo -e "${YELLOW}You'll need to:${NC}"
    echo "1. Get your IBM Cloud API key from: https://cloud.ibm.com/iam/apikeys"
    echo "2. Run: orchestrate env add -n production-au -u \"<SERVICE_URL>\""
    echo ""
    read -p "Press Enter to continue with manual setup..."
    exit 1
fi

echo ""
echo -e "${BLUE}🚀 Deploying agent...${NC}"
echo ""

# Deploy the agent
orchestrate agents import --file "$YAML_FILE"

if [ $? -eq 0 ]; then
    echo ""
    echo -e "${GREEN}═══════════════════════════════════════════════════════════════${NC}"
    echo -e "${GREEN}✅ DEPLOYMENT SUCCESSFUL!${NC}"
    echo -e "${GREEN}═══════════════════════════════════════════════════════════════${NC}"
    echo ""
    echo -e "${BLUE}Verifying deployment...${NC}"
    orchestrate agents list | grep -i "proactive\|name" | head -10
    echo ""
    echo -e "${GREEN}🎉 Agent deployed successfully!${NC}"
    echo ""
    echo -e "${BLUE}Next steps:${NC}"
    echo "1. Open IBM Portal: https://cloud.ibm.com/watsonx/orchestrate"
    echo "2. Find your agent: ProActive_CSI_Agent_404"
    echo "3. Test with: 'Good morning, what's my priority today?'"
    echo ""
else
    echo ""
    echo -e "${RED}❌ Deployment failed${NC}"
    echo ""
    echo -e "${YELLOW}Troubleshooting:${NC}"
    echo "1. Check your API key is valid"
    echo "2. Verify instance URL is correct"
    echo "3. Try: orchestrate env activate production-au"
    echo "4. Or use Web UI deployment (more reliable)"
    echo ""
    exit 1
fi


