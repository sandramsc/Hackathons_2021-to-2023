#!/bin/bash

cd "$(dirname "$0")"

GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║  🔧 Fix Instance & Deploy ProActive CSI                      ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""

echo -e "${YELLOW}⚠️  The instance ID 'f16c2181-a811-4d84-8e15-33cfebe50928' was not found.${NC}"
echo -e "${YELLOW}    This means either:${NC}"
echo -e "${YELLOW}    1. The instance was deleted/moved${NC}"
echo -e "${YELLOW}    2. The API key doesn't have access${NC}"
echo -e "${YELLOW}    3. You need to create a new instance${NC}"
echo ""
echo -e "${BLUE}📋 To fix this, you need the correct instance URL:${NC}"
echo ""
echo "1. Go to: https://cloud.ibm.com/watsonx/orchestrate"
echo "2. If you see an instance, click on it"
echo "3. Go to: Settings → API details"
echo "4. Copy the 'Service instance URL'"
echo ""
echo "OR if you don't have an instance:"
echo "1. Go to: https://cloud.ibm.com/catalog/services/watsonx-orchestrate"
echo "2. Create a new instance"
echo "3. Then get the Service instance URL from Settings"
echo ""
read -p "Paste the correct Service instance URL here: " INSTANCE_URL

if [ -z "$INSTANCE_URL" ]; then
    echo -e "${RED}❌ No URL provided${NC}"
    exit 1
fi

echo ""
echo -e "${BLUE}📋 Getting API key...${NC}"
echo "Go to: https://cloud.ibm.com/watsonx/orchestrate"
echo "Click: Profile icon → Settings → API details"
echo "Click: Generate API key"
echo ""
read -p "Paste your watsonx Orchestrate API key here: " API_KEY

if [ -z "$API_KEY" ]; then
    echo -e "${RED}❌ No API key provided${NC}"
    exit 1
fi

echo ""
echo -e "${BLUE}📋 Step 1: Removing old environment...${NC}"
echo "y" | orchestrate env remove --name production-au 2>/dev/null || true

echo ""
echo -e "${BLUE}📋 Step 2: Creating new environment...${NC}"
orchestrate env add -n production-au -u "$INSTANCE_URL" --type mcsp 2>&1 | grep -v "Warning" || {
    echo -e "${YELLOW}⚠️  Environment may already exist${NC}"
}

echo ""
echo -e "${BLUE}📋 Step 3: Activating environment...${NC}"
echo "$API_KEY" | orchestrate env activate production-au 2>&1 | grep -v "Warning\|getpass" || {
    echo -e "${RED}❌ Failed to activate. Check your API key and instance URL.${NC}"
    exit 1
}

echo ""
echo -e "${GREEN}✅ Environment activated${NC}"

echo ""
echo -e "${BLUE}📋 Step 4: Deploying agent...${NC}"
orchestrate agents import -f proactive-csi-agent-orchestrate.yaml 2>&1

if [ $? -eq 0 ]; then
    echo ""
    echo -e "${GREEN}═══════════════════════════════════════════════════════════════${NC}"
    echo -e "${GREEN}✅ DEPLOYMENT SUCCESSFUL!${NC}"
    echo -e "${GREEN}═══════════════════════════════════════════════════════════════${NC}"
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
    echo -e "${YELLOW}Check the error above and verify:${NC}"
    echo "  - Instance URL is correct"
    echo "  - API key is from watsonx Orchestrate Settings (not IBM Cloud)"
    echo "  - Instance exists and is accessible"
fi

