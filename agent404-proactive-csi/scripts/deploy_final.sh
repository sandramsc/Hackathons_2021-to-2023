#!/bin/bash

# ProActive CSI - Final Automated CLI Deployment Script v1.2.0
# Uses IBM watsonx Orchestrate CLI for automated deployment

set -e

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

# Get script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$PROJECT_ROOT"

echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}🚀 ProActive CSI - Automated CLI Deployment v1.2.0${NC}"
echo -e "${BLUE}   Complete STT & TTS Integration${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo ""

# Configuration
CONFIG_FILE="proactive-csi-agent-orchestrate.yaml"
ENV_NAME="production-au"

# Step 1: Verify Configuration File
echo -e "${YELLOW}[1/6] Verifying configuration file...${NC}"
if [ ! -f "$CONFIG_FILE" ]; then
    echo -e "${RED}❌ Configuration file not found: $CONFIG_FILE${NC}"
    exit 1
fi
echo -e "${GREEN}✅ Configuration file found: $CONFIG_FILE${NC}"
echo -e "${BLUE}   File size: $(ls -lh "$CONFIG_FILE" | awk '{print $5}')${NC}"

# Step 2: Check Orchestrate CLI
echo -e "\n${YELLOW}[2/6] Checking Orchestrate CLI...${NC}"
if ! command -v orchestrate &> /dev/null; then
    echo -e "${RED}❌ Orchestrate CLI not found${NC}"
    echo -e "${YELLOW}   Please install: pip install ibm-watsonx-orchestrate${NC}"
    exit 1
fi
CLI_VERSION=$(orchestrate --version 2>&1 | grep -i "version" | head -1 || echo "unknown")
echo -e "${GREEN}✅ Orchestrate CLI found: $CLI_VERSION${NC}"

# Step 3: Check Active Environment
echo -e "\n${YELLOW}[3/6] Checking active environment...${NC}"
ACTIVE_ENV=$(orchestrate env list 2>&1 | grep "(active)" | awk '{print $1}' || echo "")
echo -e "${BLUE}   Active environment: ${ACTIVE_ENV:-none}${NC}"

if [ "$ACTIVE_ENV" != "$ENV_NAME" ]; then
    echo -e "${YELLOW}   Activating environment: $ENV_NAME${NC}"
    orchestrate env activate "$ENV_NAME" 2>&1 || {
        echo -e "${YELLOW}⚠️  Environment activation may require authentication${NC}"
        echo -e "${BLUE}   Please run: orchestrate env activate $ENV_NAME${NC}"
    }
fi

# Step 4: Verify Environment
echo -e "\n${YELLOW}[4/6] Verifying environment connection...${NC}"
orchestrate agents list &>/dev/null && {
    echo -e "${GREEN}✅ Environment connection verified${NC}"
} || {
    echo -e "${YELLOW}⚠️  Environment authentication may be required${NC}"
    echo -e "${BLUE}   Please authenticate using: orchestrate env activate $ENV_NAME${NC}"
}

# Step 5: Deploy Agent
echo -e "\n${YELLOW}[5/6] Deploying agent via CLI...${NC}"
echo -e "${BLUE}   Command: orchestrate agents import --file $CONFIG_FILE${NC}"

if orchestrate agents import --file "$CONFIG_FILE" 2>&1; then
    echo -e "${GREEN}✅ Agent deployed successfully!${NC}"
    DEPLOYMENT_SUCCESS=true
else
    DEPLOYMENT_EXIT_CODE=$?
    if [ $DEPLOYMENT_EXIT_CODE -eq 0 ]; then
        echo -e "${GREEN}✅ Agent import completed${NC}"
        DEPLOYMENT_SUCCESS=true
    else
        echo -e "${YELLOW}⚠️  CLI deployment encountered an issue${NC}"
        echo -e "${BLUE}   Exit code: $DEPLOYMENT_EXIT_CODE${NC}"
        DEPLOYMENT_SUCCESS=false
        
        # Check if it's an authentication issue
        if orchestrate agents list &>/dev/null; then
            echo -e "${YELLOW}   Authentication is working. Trying alternative method...${NC}"
        else
            echo -e "${YELLOW}   Authentication may be required.${NC}"
            echo -e "${BLUE}   Please run: orchestrate env activate $ENV_NAME${NC}"
        fi
    fi
fi

# Step 6: List Deployed Agents
echo -e "\n${YELLOW}[6/6] Listing deployed agents...${NC}"
if orchestrate agents list 2>&1; then
    echo -e "${GREEN}✅ Agent list retrieved${NC}"
else
    echo -e "${YELLOW}⚠️  Could not list agents (may require authentication)${NC}"
fi

# Final Summary
echo ""
echo -e "${GREEN}═══════════════════════════════════════════════════════════════${NC}"
if [ "$DEPLOYMENT_SUCCESS" = true ]; then
    echo -e "${GREEN}✅ AUTOMATED DEPLOYMENT COMPLETE!${NC}"
else
    echo -e "${YELLOW}⚠️  DEPLOYMENT REQUIRES MANUAL STEPS${NC}"
fi
echo -e "${GREEN}═══════════════════════════════════════════════════════════════${NC}"
echo ""

if [ "$DEPLOYMENT_SUCCESS" != true ]; then
    echo -e "${BLUE}📋 Manual Deployment Option:${NC}"
    echo ""
    echo -e "${GREEN}1. Authenticate environment:${NC}"
    echo -e "   ${BLUE}orchestrate env activate $ENV_NAME${NC}"
    echo ""
    echo -e "${GREEN}2. Deploy agent:${NC}"
    echo -e "   ${BLUE}orchestrate agents import --file $CONFIG_FILE${NC}"
    echo ""
    echo -e "${GREEN}3. OR use Web UI:${NC}"
    PORTAL_URL="https://au-syd.watson-orchestrate.cloud.ibm.com/build/manage"
    echo -e "   ${BLUE}Open: $PORTAL_URL${NC}"
    
    if command -v open &> /dev/null; then
        open "$PORTAL_URL" 2>/dev/null
        echo -e "${GREEN}   ✅ Browser opened${NC}"
    fi
    echo ""
fi

echo -e "${BLUE}📁 Configuration File:${NC}"
echo -e "${GREEN}$(pwd)/$CONFIG_FILE${NC}"
echo ""
echo -e "${BLUE}🌐 IBM Portal:${NC}"
echo -e "${GREEN}https://au-syd.watson-orchestrate.cloud.ibm.com/build/manage${NC}"
echo ""
echo -e "${BLUE}🧪 Test STT/TTS after deployment:${NC}"
echo '   "Read me the executive briefing aloud using Text-to-Speech"'
echo ""
echo -e "${GREEN}🎤🔊 Deployment script complete! 🚀${NC}"
echo ""

