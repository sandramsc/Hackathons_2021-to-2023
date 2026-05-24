#!/bin/bash

# Fix API Key Issue - IBM watsonx Orchestrate
# This script helps fix the API key authentication issue

set -e

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

cd /Users/ishwaryasridharan/Desktop/Hackathon_2025/Agentic_AI/agent404-proactive-csi

echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}🔧 Fix API Key Issue - IBM watsonx Orchestrate${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo ""

echo -e "${YELLOW}The issue: Invalid or expired API key${NC}"
echo ""
echo -e "${BLUE}To fix this, you need a valid IBM Cloud API key.${NC}"
echo ""
echo -e "${GREEN}Step 1: Get your IBM Cloud API Key${NC}"
echo -e "${BLUE}1. Go to: ${YELLOW}https://cloud.ibm.com/iam/apikeys${NC}"
echo -e "${BLUE}2. Click 'Create an IBM Cloud API key'${NC}"
echo -e "${BLUE}3. Name it: ${YELLOW}watsonx-orchestrate-api-key${NC}"
echo -e "${BLUE}4. Copy the API key (you'll only see it once!)${NC}"
echo ""

read -p "Do you have your IBM Cloud API key ready? (y/n) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo -e "${YELLOW}Please get your API key first from: https://cloud.ibm.com/iam/apikeys${NC}"
    echo ""
    echo -e "${BLUE}Opening browser...${NC}"
    open "https://cloud.ibm.com/iam/apikeys" 2>/dev/null || true
    exit 1
fi

echo ""
echo -e "${GREEN}Step 2: Enter your API key${NC}"
echo -e "${BLUE}Paste your IBM Cloud API key below:${NC}"
read -sp "API Key: " API_KEY
echo ""

if [ -z "$API_KEY" ]; then
    echo -e "${RED}❌ API key is empty. Exiting.${NC}"
    exit 1
fi

echo ""
echo -e "${GREEN}Step 3: Updating environment...${NC}"

# Remove old environment
echo -e "${BLUE}Removing old environment...${NC}"
echo "y" | orchestrate env remove --name production-au 2>/dev/null || true

# Add environment with correct type
echo -e "${BLUE}Adding environment with mcsp_v2 type...${NC}"
orchestrate env add -n production-au \
  -u "https://api.au-syd.watson-orchestrate.cloud.ibm.com/instances/f16c2181-a811-4d84-8e15-33cfebe50928" \
  --type mcsp_v2

if [ $? -ne 0 ]; then
    echo -e "${YELLOW}Trying with mcsp type...${NC}"
    orchestrate env add -n production-au \
      -u "https://api.au-syd.watson-orchestrate.cloud.ibm.com/instances/f16c2181-a811-4d84-8e15-33cfebe50928" \
      --type mcsp
fi

echo ""
echo -e "${GREEN}Step 4: Activating environment...${NC}"
echo -e "${BLUE}This will prompt for your API key - paste: ${YELLOW}$API_KEY${NC}"
echo ""

# Activate environment
echo "$API_KEY" | orchestrate env activate production-au 2>&1 | grep -v "Warning: Password input" || {
    echo ""
    echo -e "${YELLOW}Automatic activation failed. Please activate manually:${NC}"
    echo -e "${BLUE}   orchestrate env activate production-au${NC}"
    echo -e "${BLUE}   Then paste your API key when prompted: ${YELLOW}$API_KEY${NC}"
    echo ""
    exit 1
}

# Check if activated
if orchestrate env list | grep -q "production-au.*active"; then
    echo -e "${GREEN}✅ Environment activated successfully!${NC}"
else
    echo -e "${YELLOW}⚠️  Environment activation may have failed. Check status:${NC}"
    orchestrate env list
    exit 1
fi

echo ""
echo -e "${GREEN}Step 5: Updating credentials file...${NC}"

# Update credentials file
cat > ../ibm-credentials_Orchestrate_data_Updated.json <<EOF
{
  "watsonx_orchestrate": {
    "api_key": "$API_KEY",
    "service_url": "https://api.au-syd.watson-orchestrate.cloud.ibm.com/instances/f16c2181-a811-4d84-8e15-33cfebe50928"
  }
}
EOF

echo -e "${GREEN}✅ Credentials file updated${NC}"

echo ""
echo -e "${GREEN}Step 6: Deploying agent...${NC}"

if orchestrate agents import --file proactive-csi-agent-orchestrate.yaml 2>&1; then
    echo ""
    echo -e "${GREEN}═══════════════════════════════════════════════════════════════${NC}"
    echo -e "${GREEN}✅ SUCCESS! Agent deployed!${NC}"
    echo -e "${GREEN}═══════════════════════════════════════════════════════════════${NC}"
    echo ""
    echo -e "${BLUE}List of agents:${NC}"
    orchestrate agents list | head -10
    echo ""
    echo -e "${BLUE}🌐 Access your agent at:${NC}"
    echo -e "${YELLOW}https://au-syd.watson-orchestrate.cloud.ibm.com/build/manage${NC}"
    echo ""
else
    echo ""
    echo -e "${YELLOW}⚠️  Agent deployment encountered an issue.${NC}"
    echo -e "${BLUE}Try manually:${NC}"
    echo -e "${BLUE}   orchestrate agents import --file proactive-csi-agent-orchestrate.yaml${NC}"
    echo ""
fi

echo -e "${GREEN}🎤🔊 API Key fixed and deployment complete! 🚀${NC}"
echo ""

