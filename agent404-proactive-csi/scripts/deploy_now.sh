#!/bin/bash

# Complete Automated Deployment Script
# Deploys ProActive CSI Agent to IBM watsonx Orchestrate

set -e

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

cd /Users/ishwaryasridharan/Desktop/Hackathon_2025/Agentic_AI/agent404-proactive-csi

clear

echo -e "${CYAN}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${CYAN}🚀 ProActive CSI - Complete Automated Deployment${NC}"
echo -e "${CYAN}   Version 1.2.0 (STT & TTS Integration)${NC}"
echo -e "${CYAN}═══════════════════════════════════════════════════════════════${NC}"
echo ""

# Configuration
SERVICE_URL="https://api.au-syd.watson-orchestrate.cloud.ibm.com/instances/f16c2181-a811-4d84-8e15-33cfebe50928"
API_KEY="OhBxVuewV9Mz0HYlQVl3ZqeHHprOJ5xONqn77CbDF8xK"
CONFIG_FILE="proactive-csi-agent-orchestrate.yaml"
ENV_NAME="production-au"

# Step 1: Verify Configuration File
echo -e "${YELLOW}[1/8] Verifying configuration file...${NC}"
if [ ! -f "$CONFIG_FILE" ]; then
    echo -e "${RED}❌ Configuration file not found: $CONFIG_FILE${NC}"
    exit 1
fi

FILE_SIZE=$(ls -lh "$CONFIG_FILE" | awk '{print $5}')
echo -e "${GREEN}✅ Configuration file found: $CONFIG_FILE ($FILE_SIZE)${NC}"

# Step 2: Update Credentials File
echo -e "\n${YELLOW}[2/8] Updating credentials file...${NC}"
cat > ../ibm-credentials_Orchestrate_data_Updated.json <<EOF
{
  "watsonx_orchestrate": {
    "api_key": "$API_KEY",
    "service_url": "$SERVICE_URL"
  }
}
EOF
echo -e "${GREEN}✅ Credentials file updated${NC}"

# Step 3: Check Orchestrate CLI
echo -e "\n${YELLOW}[3/8] Checking Orchestrate CLI...${NC}"
if ! command -v orchestrate &> /dev/null; then
    echo -e "${RED}❌ Orchestrate CLI not found${NC}"
    echo -e "${YELLOW}Installing...${NC}"
    pip3 install ibm-watsonx-orchestrate 2>/dev/null || pip install ibm-watsonx-orchestrate 2>/dev/null
fi

if command -v orchestrate &> /dev/null; then
    CLI_VERSION=$(orchestrate --version 2>&1 | grep -i "version" | head -1 || echo "found")
    echo -e "${GREEN}✅ Orchestrate CLI found${NC}"
else
    echo -e "${RED}❌ Could not install Orchestrate CLI${NC}"
    exit 1
fi

# Step 4: Remove Old Environment
echo -e "\n${YELLOW}[4/8] Removing old environment...${NC}"
echo "y" | orchestrate env remove --name "$ENV_NAME" 2>/dev/null || true
echo -e "${GREEN}✅ Old environment removed${NC}"

# Step 5: Add New Environment
echo -e "\n${YELLOW}[5/8] Adding environment...${NC}"
echo -e "${BLUE}Trying different authentication types...${NC}"

# Try ibm_iam first
if orchestrate env add -n "$ENV_NAME" -u "$SERVICE_URL" --type ibm_iam 2>&1; then
    echo -e "${GREEN}✅ Environment added with ibm_iam type${NC}"
elif orchestrate env add -n "$ENV_NAME" -u "$SERVICE_URL" --type mcsp 2>&1; then
    echo -e "${GREEN}✅ Environment added with mcsp type${NC}"
elif orchestrate env add -n "$ENV_NAME" -u "$SERVICE_URL" --type mcsp_v2 2>&1; then
    echo -e "${GREEN}✅ Environment added with mcsp_v2 type${NC}"
else
    echo -e "${RED}❌ Failed to add environment${NC}"
    echo -e "${YELLOW}Falling back to Web UI deployment...${NC}"
    open "https://cloud.ibm.com/watsonx/orchestrate" 2>/dev/null || true
    echo ""
    echo -e "${CYAN}Please deploy via Web UI:${NC}"
    echo -e "${BLUE}1. Click 'All agents' or 'Skills'${NC}"
    echo -e "${BLUE}2. Click 'Edit' or 'Import from file'${NC}"
    echo -e "${BLUE}3. Upload: $CONFIG_FILE${NC}"
    echo -e "${BLUE}4. Save → Activate${NC}"
    exit 1
fi

# Step 6: Activate Environment
echo -e "\n${YELLOW}[6/8] Activating environment...${NC}"
echo -e "${BLUE}Using API key: ${API_KEY:0:20}...${NC}"

# Try to activate with API key
if echo "$API_KEY" | orchestrate env activate "$ENV_NAME" 2>&1 | grep -v "Warning: Password input" | grep -v "Please enter" | grep -v "GetPassWarning" | head -5; then
    # Check if activated successfully
    if orchestrate env list 2>&1 | grep -q "$ENV_NAME.*active"; then
        echo -e "${GREEN}✅ Environment activated successfully!${NC}"
        ACTIVATED=true
    else
        echo -e "${YELLOW}⚠️  Activation may have failed. Checking...${NC}"
        ACTIVATED=false
    fi
else
    echo -e "${YELLOW}⚠️  Automatic activation failed${NC}"
    echo -e "${BLUE}Try manual activation:${NC}"
    echo -e "${YELLOW}   orchestrate env activate $ENV_NAME${NC}"
    echo -e "${BLUE}   Then paste API key when prompted: ${YELLOW}$API_KEY${NC}"
    ACTIVATED=false
fi

# Step 7: Check Environment Status
echo -e "\n${YELLOW}[7/8] Checking environment status...${NC}"
orchestrate env list 2>&1 | head -10

if [ "$ACTIVATED" != true ]; then
    echo ""
    echo -e "${YELLOW}⚠️  Environment not activated. Deploying via Web UI instead...${NC}"
    echo ""
    open "https://cloud.ibm.com/watsonx/orchestrate" 2>/dev/null || true
    echo -e "${CYAN}═══════════════════════════════════════════════════════════════${NC}"
    echo -e "${CYAN}📋 Web UI Deployment Instructions${NC}"
    echo -e "${CYAN}═══════════════════════════════════════════════════════════════${NC}"
    echo ""
    echo -e "${GREEN}1. Find your agent in IBM Portal${NC}"
    echo -e "   • Click 'All agents' or 'Skills' in left sidebar"
    echo -e "   • Find: ProActive_CSI_Agent_404"
    echo ""
    echo -e "${GREEN}2. Edit agent${NC}"
    echo -e "   • Click 'Edit' button"
    echo ""
    echo -e "${GREEN}3. Upload configuration${NC}"
    echo -e "   • Click 'Import from file' or 'Upload'"
    echo -e "   • Select file: ${YELLOW}$(pwd)/$CONFIG_FILE${NC}"
    echo ""
    echo -e "${GREEN}4. Verify services${NC}"
    echo -e "   • Go to 'Connections' tab"
    echo -e "   • Verify: STT, TTS, NLU are connected"
    echo ""
    echo -e "${GREEN}5. Save & Activate${NC}"
    echo -e "   • Click 'Save' → 'Activate'"
    echo ""
    exit 0
fi

# Step 8: Deploy Agent
echo -e "\n${YELLOW}[8/8] Deploying agent...${NC}"
echo -e "${BLUE}Importing agent configuration...${NC}"

if orchestrate agents import --file "$CONFIG_FILE" 2>&1; then
    echo ""
    echo -e "${GREEN}═══════════════════════════════════════════════════════════════${NC}"
    echo -e "${GREEN}✅ DEPLOYMENT SUCCESSFUL!${NC}"
    echo -e "${GREEN}═══════════════════════════════════════════════════════════════${NC}"
    echo ""
    echo -e "${BLUE}List of agents:${NC}"
    orchestrate agents list 2>&1 | head -10
    echo ""
    echo -e "${BLUE}🌐 Access your agent at:${NC}"
    echo -e "${YELLOW}https://cloud.ibm.com/watsonx/orchestrate${NC}"
    echo ""
    echo -e "${BLUE}🧪 Test STT/TTS:${NC}"
    echo -e "${GREEN}'Read me the executive briefing aloud using Text-to-Speech'${NC}"
    echo ""
    echo -e "${GREEN}🎤🔊 Deployment complete! 🚀${NC}"
    exit 0
else
    DEPLOYMENT_EXIT_CODE=$?
    echo ""
    echo -e "${YELLOW}⚠️  CLI deployment encountered an issue${NC}"
    echo -e "${BLUE}Deploying via Web UI instead...${NC}"
    echo ""
    open "https://cloud.ibm.com/watsonx/orchestrate" 2>/dev/null || true
    echo -e "${CYAN}═══════════════════════════════════════════════════════════════${NC}"
    echo -e "${CYAN}📋 Web UI Deployment Instructions${NC}"
    echo -e "${CYAN}═══════════════════════════════════════════════════════════════${NC}"
    echo ""
    echo -e "${GREEN}Configuration file ready:${NC}"
    echo -e "${YELLOW}$(pwd)/$CONFIG_FILE${NC}"
    echo ""
    echo -e "${BLUE}Follow the steps above to deploy via Web UI${NC}"
    exit 0
fi

