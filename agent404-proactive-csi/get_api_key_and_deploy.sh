#!/bin/bash

# ProActive CSI - Get API Key and Deploy Automatically
# Opens API key page, then deploys once you have the key

cd "$(dirname "$0")"

GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║  🔑 Get API Key & Auto Deploy 🚀                            ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""

# Open API key creation page
echo -e "${BLUE}📋 Step 1: Opening API key creation page...${NC}"
open "https://cloud.ibm.com/iam/apikeys" 2>/dev/null || \
xdg-open "https://cloud.ibm.com/iam/apikeys" 2>/dev/null || \
echo "Please open: https://cloud.ibm.com/iam/apikeys"

echo -e "${GREEN}✅ Browser opened${NC}\n"

echo -e "${BLUE}📋 Step 2: Create API Key${NC}"
echo -e "${YELLOW}1. Click 'Create an IBM Cloud API key'${NC}"
echo -e "${YELLOW}2. Name it: proactive-csi-deployment${NC}"
echo -e "${YELLOW}3. Click 'Create'${NC}"
echo -e "${YELLOW}4. Copy the API key${NC}\n"

# Wait for user to get API key
echo -e "${BLUE}Press Enter after you've copied your API key...${NC}"
read -p ""

# Get API key from user
echo -e "${BLUE}📋 Step 3: Enter your NEW API key${NC}"
read -p "Paste your API key here: " NEW_API_KEY

if [ -z "$NEW_API_KEY" ]; then
    echo -e "${RED}❌ No API key provided${NC}"
    exit 1
fi

echo -e "${GREEN}✅ API key received${NC}\n"

# Deploy with new key
echo -e "${BLUE}🚀 Step 4: Deploying with new API key...${NC}\n"

# Activate environment
echo "$NEW_API_KEY" | orchestrate env activate production-au

if [ $? -ne 0 ]; then
    echo -e "${RED}❌ Failed to activate environment${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Environment activated${NC}\n"

# Deploy agent
echo -e "${BLUE}Deploying agent...${NC}"
orchestrate agents import --file proactive-csi-agent-orchestrate.yaml

if [ $? -eq 0 ]; then
    echo -e "\n${GREEN}═══════════════════════════════════════════════════════════════${NC}"
    echo -e "${GREEN}✅ DEPLOYMENT SUCCESSFUL!${NC}"
    echo -e "${GREEN}═══════════════════════════════════════════════════════════════${NC}\n"
    
    echo -e "${BLUE}Verifying...${NC}"
    orchestrate agents list | grep -i "proactive\|name" | head -5
    
    echo -e "\n${GREEN}🎉 Done! Agent is deployed!${NC}\n"
else
    echo -e "\n${RED}❌ Deployment failed${NC}"
    exit 1
fi

