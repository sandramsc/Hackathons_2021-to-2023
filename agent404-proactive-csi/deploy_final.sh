#!/bin/bash

# Final deployment script - handles activation and deployment together
# Based on IBM watsonx Orchestrate CLI cheat sheet

cd "$(dirname "$0")"

GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║  🚀 Final Deployment - ProActive CSI                         ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""

export API_KEY="f4493b99-f0b5-47ff-b80c-51b437c02f30"

echo -e "${BLUE}📋 Step 1: Get Correct Instance URL${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "Current instance IDs return 404. We need the correct one."
echo ""
echo "To get it:"
echo "1. Go to: https://cloud.ibm.com/watsonx/orchestrate"
echo "2. Click on your instance (or create one)"
echo "3. Settings → API details"
echo "4. Copy 'Service instance URL'"
echo ""
read -p "Paste Service instance URL: " INSTANCE_URL

if [ -z "$INSTANCE_URL" ]; then
    echo -e "${RED}❌ No URL provided${NC}"
    exit 1
fi

echo ""
echo -e "${BLUE}📋 Step 2: Setup Environment${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Remove old
echo -e "${BLUE}Removing old environment...${NC}"
echo "y" | orchestrate env remove --name production-au 2>/dev/null || true

# Add new
echo -e "${BLUE}Adding environment with correct URL...${NC}"
orchestrate env add -n production-au -u "$INSTANCE_URL" --type mcsp 2>&1 | grep -v "Warning" || {
    echo -e "${YELLOW}⚠️  Environment may already exist${NC}"
}

echo ""
echo -e "${BLUE}📋 Step 3: Activate Environment${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Activate using --api-key flag (from cheat sheet)
orchestrate env activate --api-key "$API_KEY" production-au 2>&1 | grep -v "Warning\|getpass" || {
    echo -e "${YELLOW}⚠️  Activation had warnings, but continuing...${NC}"
}

# Verify activation
echo ""
echo -e "${BLUE}Verifying activation...${NC}"
ACTIVE_ENV=$(orchestrate env list 2>&1 | grep "(active)" | awk '{print $1}')

if [ -z "$ACTIVE_ENV" ]; then
    echo -e "${RED}❌ No active environment found${NC}"
    echo -e "${YELLOW}Trying to activate again...${NC}"
    orchestrate env activate --api-key "$API_KEY" production-au 2>&1 | grep -v "Warning\|getpass"
    
    # Check again
    ACTIVE_ENV=$(orchestrate env list 2>&1 | grep "(active)" | awk '{print $1}')
    if [ -z "$ACTIVE_ENV" ]; then
        echo -e "${RED}❌ Still no active environment${NC}"
        echo -e "${YELLOW}The instance URL or API key may be incorrect${NC}"
        echo -e "${YELLOW}Please verify both in IBM Portal${NC}"
        exit 1
    fi
fi

echo -e "${GREEN}✅ Environment activated: $ACTIVE_ENV${NC}"

echo ""
echo -e "${BLUE}📋 Step 4: Deploy Agent${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

if [ ! -f "proactive-csi-agent-orchestrate.yaml" ]; then
    echo -e "${RED}❌ Agent file not found${NC}"
    exit 1
fi

echo -e "${BLUE}Importing agent...${NC}"
orchestrate agents import -f proactive-csi-agent-orchestrate.yaml 2>&1

DEPLOY_STATUS=$?

if [ $DEPLOY_STATUS -eq 0 ]; then
    echo ""
    echo -e "${GREEN}═══════════════════════════════════════════════════════════════${NC}"
    echo -e "${GREEN}✅ DEPLOYMENT SUCCESSFUL!${NC}"
    echo -e "${GREEN}═══════════════════════════════════════════════════════════════${NC}"
    echo ""
    
    # List agents to verify
    echo -e "${BLUE}Verifying deployment...${NC}"
    orchestrate agents list 2>&1 | grep -i "proactive\|CSI\|name" | head -5
    
    echo ""
    echo -e "${GREEN}🎉 Agent deployed successfully!${NC}"
    echo ""
    echo -e "${BLUE}Next Steps:${NC}"
    echo "1. Go to: https://cloud.ibm.com/watsonx/orchestrate"
    echo "2. Click: Build → Agent Builder"
    echo "3. Find: ProActive_CSI_Agent_404"
    echo "4. Click to open and test"
    echo ""
    echo -e "${BLUE}Test Query:${NC}"
    echo '  "Good morning, what'\''s my priority today?"'
    echo ""
else
    echo ""
    echo -e "${RED}❌ Deployment failed${NC}"
    echo ""
    echo -e "${YELLOW}Troubleshooting:${NC}"
    echo "1. Verify instance URL is correct"
    echo "2. Verify API key is from watsonx Orchestrate Settings"
    echo "3. Check instance exists in IBM Portal"
    echo "4. Try: orchestrate env list (check if environment is active)"
    echo ""
    exit 1
fi
