#!/bin/bash

# ProActive CSI - CLI Deployment with Credentials from ibm_services.py
# Uses all credentials from integrations/ibm_services.py

echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║  🚀 ProActive CSI - CLI Deployment (Using ibm_services.py) 🚀║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

cd "$(dirname "$0")"

# Extract credentials from ibm_services.py
echo -e "${BLUE}📋 Extracting credentials from ibm_services.py...${NC}"

# Extract NLU credentials
NLU_APIKEY=$(grep -oP "NATURAL_LANGUAGE_UNDERSTANDING_APIKEY.*?'\K[^']+" integrations/ibm_services.py | head -1)
NLU_URL=$(grep -oP "NATURAL_LANGUAGE_UNDERSTANDING_URL.*?'\K[^']+" integrations/ibm_services.py | head -1)

# Extract STT credentials
STT_APIKEY=$(grep -oP "SPEECH_TO_TEXT_APIKEY.*?'\K[^']+" integrations/ibm_services.py | head -1)
STT_URL=$(grep -oP "SPEECH_TO_TEXT_URL.*?'\K[^']+" integrations/ibm_services.py | head -1)

# Extract TTS credentials
TTS_APIKEY=$(grep -oP "TEXT_TO_SPEECH_APIKEY.*?'\K[^']+" integrations/ibm_services.py | head -1)
TTS_URL=$(grep -oP "TEXT_TO_SPEECH_URL.*?'\K[^']+" integrations/ibm_services.py | head -1)

# Extract Cloudant credentials
CLOUDANT_APIKEY=$(grep -oP '"apikey":\s*"\K[^"]+' integrations/ibm_services.py | head -1)
CLOUDANT_URL=$(grep -oP '"url":\s*"\K[^"]+' integrations/ibm_services.py | head -1)

# Orchestrate credentials (from deployment status)
ORCHESTRATE_URL="https://api.au-syd.watson-orchestrate.cloud.ibm.com/instances/f16c2181-a811-4d84-8e15-33cfebe50928"
ORCHESTRATE_APIKEY="OhBxVuewV9Mz0HYlQVl3ZqeHHprOJ5xONqn77CbDF8xK"

echo -e "${GREEN}✅ Credentials extracted${NC}"
echo ""

# Display credentials (masked)
echo -e "${BLUE}📋 Service Credentials:${NC}"
echo -e "  NLU API Key: ${GREEN}${NLU_APIKEY:0:10}...${NC}"
echo -e "  STT API Key: ${GREEN}${STT_APIKEY:0:10}...${NC}"
echo -e "  TTS API Key: ${GREEN}${TTS_APIKEY:0:10}...${NC}"
echo -e "  Cloudant API Key: ${GREEN}${CLOUDANT_APIKEY:0:10}...${NC}"
echo -e "  Orchestrate URL: ${GREEN}${ORCHESTRATE_URL}${NC}"
echo ""

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

# Check if production-au environment exists
if orchestrate env list | grep -q "production-au"; then
    echo -e "${BLUE}🔑 Activating production-au environment...${NC}"
    echo -e "${YELLOW}Using Orchestrate API key from credentials...${NC}"
    echo ""
    
    # Try to activate with the API key
    echo "$ORCHESTRATE_APIKEY" | orchestrate env activate production-au 2>&1
    
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✅ Environment activated${NC}"
    else
        echo -e "${YELLOW}⚠️  Auto-activation failed, trying manual activation...${NC}"
        echo ""
        echo -e "${BLUE}Please enter your IBM Cloud API key when prompted:${NC}"
        echo -e "${YELLOW}API Key: ${ORCHESTRATE_APIKEY:0:20}...${NC}"
        echo ""
        orchestrate env activate production-au
    fi
else
    echo -e "${YELLOW}⚠️  production-au environment not found${NC}"
    echo -e "${BLUE}Creating new environment...${NC}"
    echo ""
    
    orchestrate env add -n production-au \
        -u "$ORCHESTRATE_URL" \
        --type ibm_iam
    
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✅ Environment created${NC}"
        echo -e "${BLUE}Activating environment...${NC}"
        echo "$ORCHESTRATE_APIKEY" | orchestrate env activate production-au
    else
        echo -e "${RED}❌ Failed to create environment${NC}"
        exit 1
    fi
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
    echo -e "${BLUE}📋 Service Credentials Summary:${NC}"
    echo -e "  ✅ NLU: ${NLU_URL}"
    echo -e "  ✅ STT: ${STT_URL}"
    echo -e "  ✅ TTS: ${TTS_URL}"
    echo -e "  ✅ Cloudant: ${CLOUDANT_URL}"
    echo -e "  ✅ Orchestrate: ${ORCHESTRATE_URL}"
    echo ""
    echo -e "${BLUE}Next steps:${NC}"
    echo "1. Open IBM Portal: https://cloud.ibm.com/watsonx/orchestrate"
    echo "2. Find your agent: ProActive_CSI_Agent_404"
    echo "3. Connect services in Connections tab:"
    echo "   - NLU: ${NLU_URL}"
    echo "   - STT: ${STT_URL}"
    echo "   - TTS: ${TTS_URL}"
    echo "   - Cloudant: ${CLOUDANT_URL}"
    echo "4. Test with: 'Good morning, what's my priority today?'"
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

