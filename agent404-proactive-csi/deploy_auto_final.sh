#!/bin/bash

# ProActive CSI - Fully Automated Deployment
# Uses all available methods to deploy automatically

set -e

cd "$(dirname "$0")"

GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║  🚀 ProActive CSI - Fully Automated Deployment 🚀          ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""

# Credentials
ORCHESTRATE_API_KEY="azE6dXNyXzBhYzkzMjI4LTE5YWMtMzhmNi1hY2VmLWRhYTEzYmU1NzYzYjpNUzNVUnVycVB6NWpBcTd5dUc5VEhreGduVWRLNndkY0I5TFhRMWpDRXdnPTpwczVM"
ORCHESTRATE_URL="https://api.au-syd.watson-orchestrate.cloud.ibm.com/instances/f16c2181-a811-4d84-8e15-33cfebe50928"
YAML_FILE="proactive-csi-agent-orchestrate.yaml"

echo -e "${BLUE}📋 Step 1: Setting up environment...${NC}"

# Export credentials
export ORCHESTRATE_API_KEY
export ORCHESTRATE_URL
export ORCHESTRATE_INSTANCE_ID="f16c2181-a811-4d84-8e15-33cfebe50928"

echo -e "${GREEN}✅ Environment variables set${NC}\n"

# Check CLI
if ! command -v orchestrate &> /dev/null; then
    echo -e "${YELLOW}Installing orchestrate CLI...${NC}"
    pip3 install -q ibm-watsonx-orchestrate
fi

echo -e "${GREEN}✅ Orchestrate CLI ready${NC}\n"

# Check YAML
if [ ! -f "$YAML_FILE" ]; then
    echo -e "${RED}❌ $YAML_FILE not found${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Configuration file found${NC}\n"

# Try to add/update environment
echo -e "${BLUE}📋 Step 2: Configuring environment...${NC}"

# Remove old environment if exists
orchestrate env remove --name production-au 2>/dev/null || true

# Add environment
echo "$ORCHESTRATE_API_KEY" | orchestrate env add -n production-au \
    -u "$ORCHESTRATE_URL" \
    --type ibm_iam 2>&1 || {
    echo -e "${YELLOW}⚠️  Environment add failed, trying activate...${NC}"
}

# Activate environment
echo -e "${BLUE}🔑 Activating environment...${NC}"
echo "$ORCHESTRATE_API_KEY" | orchestrate env activate production-au 2>&1 || {
    echo -e "${YELLOW}⚠️  Auto-activation failed${NC}"
    echo -e "${BLUE}Trying with environment variables...${NC}"
    
    # Try with env vars
    ORCHESTRATE_API_KEY="$ORCHESTRATE_API_KEY" \
    ORCHESTRATE_URL="$ORCHESTRATE_URL" \
    orchestrate env activate production-au <<< "$ORCHESTRATE_API_KEY" 2>&1 || {
        echo -e "${RED}❌ Could not activate environment${NC}"
        echo -e "${YELLOW}The API key may be invalid or expired${NC}"
        echo -e "${BLUE}Please get a new API key from: https://cloud.ibm.com/iam/apikeys${NC}"
        exit 1
    }
}

echo -e "${GREEN}✅ Environment activated${NC}\n"

# Deploy
echo -e "${BLUE}🚀 Step 3: Deploying agent...${NC}"
orchestrate agents import --file "$YAML_FILE"

if [ $? -eq 0 ]; then
    echo -e "\n${GREEN}═══════════════════════════════════════════════════════════════${NC}"
    echo -e "${GREEN}✅ DEPLOYMENT SUCCESSFUL!${NC}"
    echo -e "${GREEN}═══════════════════════════════════════════════════════════════${NC}\n"
    
    echo -e "${BLUE}Verifying deployment...${NC}"
    orchestrate agents list | grep -i "proactive\|name" | head -5
    
    echo -e "\n${GREEN}🎉 Agent deployed successfully!${NC}\n"
    echo -e "${BLUE}Next steps:${NC}"
    echo "1. Open: https://cloud.ibm.com/watsonx/orchestrate"
    echo "2. Find: ProActive_CSI_Agent_404"
    echo "3. Test: 'Good morning, what's my priority today?'"
    echo ""
else
    echo -e "\n${RED}❌ Deployment failed${NC}"
    exit 1
fi

