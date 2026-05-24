#!/bin/bash

# ProActive CSI - Deploy using IBM watsonx Orchestrate ADK
# Following official IBM documentation

cd "$(dirname "$0")"

GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║  🚀 Deploy ProActive CSI using watsonx Orchestrate ADK      ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""

# Step 1: Check ADK
echo -e "${BLUE}📋 Step 1: Checking ADK installation...${NC}"
if ! command -v orchestrate &> /dev/null; then
    echo -e "${RED}❌ ADK not installed. Install with: pip install ibm-watsonx-orchestrate${NC}"
    exit 1
fi

orchestrate --version | head -1
echo -e "${GREEN}✅ ADK installed${NC}"
echo ""

# Step 2: Get API Key from user
echo -e "${BLUE}📋 Step 2: Get API Key from watsonx Orchestrate${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "To get your API key:"
echo "1. Sign in to watsonx Orchestrate: https://cloud.ibm.com/watsonx/orchestrate"
echo "2. Click Profile icon (top-right) → Settings"
echo "3. Go to 'API details' tab"
echo "4. Click 'Generate API key' button"
echo "5. Copy the API key (you'll only see it once!)"
echo ""
read -p "Paste your watsonx Orchestrate API key here: " WXO_API_KEY

if [ -z "$WXO_API_KEY" ]; then
    echo -e "${RED}❌ No API key provided${NC}"
    exit 1
fi

echo -e "${GREEN}✅ API key received${NC}"
echo ""

# Step 3: Setup environment
echo -e "${BLUE}📋 Step 3: Setting up environment...${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

SERVICE_URL="https://api.au-syd.watson-orchestrate.cloud.ibm.com/instances/f16c2181-a811-4d84-8e15-33cfebe50928"

# Remove old environment if exists
echo -e "${BLUE}Removing old environment if exists...${NC}"
echo "y" | orchestrate env remove --name production-au 2>/dev/null || true

# Add environment with mcsp type
echo -e "${BLUE}Creating environment with mcsp type...${NC}"
orchestrate env add -n production-au -u "$SERVICE_URL" --type mcsp 2>&1 | grep -v "Warning\|getpass" || {
    echo -e "${YELLOW}⚠️  Environment may already exist${NC}"
}

# Activate environment
echo -e "${BLUE}Activating environment...${NC}"
echo "$WXO_API_KEY" | orchestrate env activate production-au 2>&1 | grep -v "Warning\|getpass" || {
    echo -e "${RED}❌ Failed to activate environment${NC}"
    echo -e "${YELLOW}Please check your API key and try again${NC}"
    exit 1
}

echo -e "${GREEN}✅ Environment activated${NC}"
echo ""

# Step 4: Deploy agent
echo -e "${BLUE}📋 Step 4: Deploying agent...${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

if [ ! -f "proactive-csi-agent-orchestrate.yaml" ]; then
    echo -e "${RED}❌ Agent file not found: proactive-csi-agent-orchestrate.yaml${NC}"
    exit 1
fi

echo -e "${BLUE}Importing agent...${NC}"
orchestrate agents import -f proactive-csi-agent-orchestrate.yaml 2>&1

if [ $? -eq 0 ]; then
    echo ""
    echo -e "${GREEN}═══════════════════════════════════════════════════════════════${NC}"
    echo -e "${GREEN}✅ DEPLOYMENT SUCCESSFUL!${NC}"
    echo -e "${GREEN}═══════════════════════════════════════════════════════════════${NC}"
    echo ""
    
    # Verify deployment
    echo -e "${BLUE}Verifying deployment...${NC}"
    orchestrate agents list 2>&1 | grep -i "proactive\|CSI\|name" | head -5
    
    echo ""
    echo -e "${GREEN}🎉 Agent deployed successfully!${NC}"
    echo ""
    echo -e "${BLUE}Next Steps:${NC}"
    echo "1. Go to: https://cloud.ibm.com/watsonx/orchestrate"
    echo "2. Click Build → Agent Builder"
    echo "3. Find: ProActive_CSI_Agent_404"
    echo "4. Click to open and test"
    echo ""
    echo -e "${BLUE}Test Query:${NC}"
    echo '  "Good morning, what'\''s my priority today?"'
    echo ""
else
    echo -e "${RED}❌ Deployment failed${NC}"
    exit 1
fi

