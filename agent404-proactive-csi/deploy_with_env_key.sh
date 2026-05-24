#!/bin/bash

# ProActive CSI - Deploy using API key from .env file
# Uses ORCHESTRATE_API_KEY from ../.env

cd "$(dirname "$0")"

GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║  🚀 Auto Deploy with .env API Key 🚀                        ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""

# Load API key from .env
ENV_FILE="../.env"
if [ ! -f "$ENV_FILE" ]; then
    ENV_FILE=".env"
fi

if [ -f "$ENV_FILE" ]; then
    echo -e "${BLUE}📋 Loading API key from $ENV_FILE...${NC}"
    ORCHESTRATE_API_KEY=$(grep "^ORCHESTRATE_API_KEY=" "$ENV_FILE" | cut -d'=' -f2 | tr -d '"' | tr -d "'")
    IBM_CLOUD_API_KEY=$(grep "^IBM_CLOUD_API_KEY=" "$ENV_FILE" | cut -d'=' -f2 | tr -d '"' | tr -d "'")
    
    if [ -n "$ORCHESTRATE_API_KEY" ]; then
        echo -e "${GREEN}✅ Found ORCHESTRATE_API_KEY${NC}"
        API_KEY="$ORCHESTRATE_API_KEY"
    elif [ -n "$IBM_CLOUD_API_KEY" ]; then
        echo -e "${GREEN}✅ Found IBM_CLOUD_API_KEY${NC}"
        API_KEY="$IBM_CLOUD_API_KEY"
    else
        echo -e "${RED}❌ No API key found in .env${NC}"
        exit 1
    fi
else
    echo -e "${RED}❌ .env file not found${NC}"
    exit 1
fi

ORCHESTRATE_URL="https://api.au-syd.watson-orchestrate.cloud.ibm.com/instances/f16c2181-a811-4d84-8e15-33cfebe50928"
YAML_FILE="proactive-csi-agent-orchestrate.yaml"

echo -e "${BLUE}API Key (first 20 chars): ${API_KEY:0:20}...${NC}\n"

# Check CLI
if ! command -v orchestrate &> /dev/null; then
    echo -e "${YELLOW}Installing orchestrate CLI...${NC}"
    pip3 install -q ibm-watsonx-orchestrate
fi

# Check YAML
if [ ! -f "$YAML_FILE" ]; then
    echo -e "${RED}❌ $YAML_FILE not found${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Configuration file found${NC}\n"

# Activate environment
echo -e "${BLUE}🔑 Activating environment...${NC}"
echo "$API_KEY" | orchestrate env activate production-au 2>&1

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Environment activated${NC}\n"
    
    # Deploy
    echo -e "${BLUE}🚀 Deploying agent...${NC}"
    orchestrate agents import --file "$YAML_FILE"
    
    if [ $? -eq 0 ]; then
        echo -e "\n${GREEN}═══════════════════════════════════════════════════════════════${NC}"
        echo -e "${GREEN}✅ DEPLOYMENT SUCCESSFUL!${NC}"
        echo -e "${GREEN}═══════════════════════════════════════════════════════════════${NC}\n"
        
        echo -e "${BLUE}Verifying...${NC}"
        orchestrate agents list | grep -i "proactive\|name" | head -5
        
        echo -e "\n${GREEN}🎉 Agent deployed!${NC}\n"
        exit 0
    else
        echo -e "\n${RED}❌ Deployment failed${NC}"
        exit 1
    fi
else
    echo -e "${RED}❌ Failed to activate environment${NC}"
    echo -e "${YELLOW}The API key may be invalid. Trying IBM Cloud API key...${NC}\n"
    
    # Try IBM Cloud API key
    if [ -n "$IBM_CLOUD_API_KEY" ] && [ "$IBM_CLOUD_API_KEY" != "$API_KEY" ]; then
        echo -e "${BLUE}Trying IBM Cloud API key...${NC}"
        echo "$IBM_CLOUD_API_KEY" | orchestrate env activate production-au 2>&1
        
        if [ $? -eq 0 ]; then
            echo -e "${GREEN}✅ Environment activated with IBM Cloud key${NC}\n"
            orchestrate agents import --file "$YAML_FILE"
            exit $?
        fi
    fi
    
    echo -e "${YELLOW}⚠️  Both API keys failed${NC}"
    echo -e "${BLUE}Please use Web UI deployment:${NC}"
    echo "https://cloud.ibm.com/watsonx/orchestrate"
    exit 1
fi

