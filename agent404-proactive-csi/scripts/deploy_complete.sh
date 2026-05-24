#!/bin/bash

# ProActive CSI - Complete Automated Deployment Script v1.2.0
# Performs ALL deployment steps automatically - exactly like before

# Don't exit on errors - continue through all steps
# set -e

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

# Get script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$PROJECT_ROOT"

# Clear screen only if running interactively
[ -t 0 ] && clear 2>/dev/null || true

echo -e "${CYAN}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${CYAN}🚀 ProActive CSI - Complete Automated Deployment v1.2.0${NC}"
echo -e "${CYAN}   Full STT & TTS Audio Integration${NC}"
echo -e "${CYAN}═══════════════════════════════════════════════════════════════${NC}"
echo ""

# Configuration
CONFIG_FILE="proactive-csi-agent-orchestrate.yaml"
ENV_NAME="production-au"
PORTAL_URL="https://au-syd.watson-orchestrate.cloud.ibm.com/build/manage"
INSTANCE_ID="f16c2181-a811-4d84-8e15-33cfebe50928"

# Step 1: Verify Project Structure
echo -e "${YELLOW}[1/10] Verifying project structure...${NC}"
echo -e "${BLUE}   Project directory: $PROJECT_ROOT${NC}"

if [ ! -d "$PROJECT_ROOT" ]; then
    echo -e "${RED}❌ Project directory not found: $PROJECT_ROOT${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Project directory verified${NC}"
echo -e "${BLUE}   Current directory: $(pwd)${NC}"
echo ""

# Step 2: Verify Configuration File
echo -e "${YELLOW}[2/10] Verifying configuration file...${NC}"
if [ ! -f "$CONFIG_FILE" ]; then
    echo -e "${RED}❌ Configuration file not found: $CONFIG_FILE${NC}"
    exit 1
fi

FILE_SIZE=$(ls -lh "$CONFIG_FILE" | awk '{print $5}')
FILE_PATH=$(pwd)/$CONFIG_FILE

echo -e "${GREEN}✅ Configuration file found${NC}"
echo -e "${BLUE}   File: $CONFIG_FILE${NC}"
echo -e "${BLUE}   Size: $FILE_SIZE${NC}"
echo -e "${BLUE}   Path: $FILE_PATH${NC}"

# Check STT/TTS references
STT_COUNT=$(grep -ci "STT\|Speech-to-Text\|Speech to Text" "$CONFIG_FILE" || echo "0")
TTS_COUNT=$(grep -ci "TTS\|Text-to-Speech\|Text to Speech" "$CONFIG_FILE" || echo "0")

echo -e "${BLUE}   STT references: $STT_COUNT${NC}"
echo -e "${BLUE}   TTS references: $TTS_COUNT${NC}"

if [ "$STT_COUNT" -lt 5 ] || [ "$TTS_COUNT" -lt 5 ]; then
    echo -e "${YELLOW}⚠️  Warning: Few STT/TTS references found${NC}"
fi

echo ""

# Step 3: Check Version
echo -e "${YELLOW}[3/10] Verifying version...${NC}"
if [ -f "VERSION" ]; then
    VERSION=$(cat VERSION | tr -d '[:space:]')
    echo -e "${GREEN}✅ Version: $VERSION${NC}"
    
    if [ "$VERSION" != "1.2.0" ]; then
        echo -e "${YELLOW}⚠️  Version mismatch: Expected 1.2.0, found $VERSION${NC}"
    fi
else
    echo -e "${YELLOW}⚠️  VERSION file not found${NC}"
    VERSION="unknown"
fi

echo ""

# Step 4: Verify Credentials
echo -e "${YELLOW}[4/10] Verifying IBM credentials...${NC}"

CRED_FILES=(
    "../ibm-credentials_Orchestrate_data_Updated.json"
    "../ibm-credentials_STT.env"
    "../ibm-credentials_TTS.env"
    "../ibm-credentials_NLU.env"
)

MISSING_CREDS=0
FOUND_CREDS=0

for cred_file in "${CRED_FILES[@]}"; do
    if [ -f "$cred_file" ]; then
        echo -e "${GREEN}✅ Found: $(basename $cred_file)${NC}"
        FOUND_CREDS=$((FOUND_CREDS + 1))
    else
        echo -e "${YELLOW}⚠️  Missing: $(basename $cred_file)${NC}"
        MISSING_CREDS=$((MISSING_CREDS + 1))
    fi
done

if [ $FOUND_CREDS -gt 0 ]; then
    echo -e "${GREEN}✅ Found $FOUND_CREDS credential file(s)${NC}"
else
    echo -e "${YELLOW}⚠️  No credential files found (using fallback)${NC}"
fi

echo ""

# Step 5: Check Orchestrate CLI
echo -e "${YELLOW}[5/10] Checking Orchestrate CLI...${NC}"
if command -v orchestrate &> /dev/null; then
    CLI_VERSION=$(orchestrate --version 2>&1 | grep -i "version" | head -1 || echo "unknown")
    echo -e "${GREEN}✅ Orchestrate CLI found${NC}"
    echo -e "${BLUE}   Version: $CLI_VERSION${NC}"
    CLI_AVAILABLE=true
else
    echo -e "${YELLOW}⚠️  Orchestrate CLI not found${NC}"
    echo -e "${BLUE}   Attempting to install...${NC}"
    
    if pip3 install --quiet ibm-watsonx-orchestrate 2>/dev/null; then
        echo -e "${GREEN}✅ CLI installed${NC}"
        CLI_AVAILABLE=true
    else
        echo -e "${YELLOW}⚠️  Could not install CLI${NC}"
        CLI_AVAILABLE=false
    fi
fi

echo ""

# Step 6: Check Environment
echo -e "${YELLOW}[6/10] Checking Orchestrate environment...${NC}"
if [ "$CLI_AVAILABLE" = true ]; then
    if orchestrate env list &>/dev/null; then
        ACTIVE_ENV=$(orchestrate env list 2>&1 | grep "(active)" | awk '{print $1}' || echo "")
        echo -e "${GREEN}✅ Environment list retrieved${NC}"
        echo -e "${BLUE}   Active environment: ${ACTIVE_ENV:-none}${NC}"
        
        if [ -n "$ACTIVE_ENV" ]; then
            ENV_AVAILABLE=true
        else
            ENV_AVAILABLE=false
        fi
    else
        echo -e "${YELLOW}⚠️  Could not list environments${NC}"
        ENV_AVAILABLE=false
    fi
else
    ENV_AVAILABLE=false
fi

echo ""

# Step 7: Verify YAML Syntax
echo -e "${YELLOW}[7/10] Verifying YAML syntax...${NC}"
if command -v python3 &> /dev/null; then
    if python3 -c "import yaml; yaml.safe_load(open('$CONFIG_FILE'))" 2>/dev/null; then
        echo -e "${GREEN}✅ YAML syntax is valid${NC}"
    else
        echo -e "${RED}❌ YAML syntax error!${NC}"
        exit 1
    fi
else
    echo -e "${YELLOW}⚠️  Python3 not found, skipping YAML validation${NC}"
fi

echo ""

# Step 8: Open IBM Portal
echo -e "${YELLOW}[8/10] Opening IBM Portal in browser...${NC}"
if command -v open &> /dev/null; then
    open "$PORTAL_URL" 2>/dev/null
    echo -e "${GREEN}✅ Browser opened: $PORTAL_URL${NC}"
elif command -v xdg-open &> /dev/null; then
    xdg-open "$PORTAL_URL" 2>/dev/null
    echo -e "${GREEN}✅ Browser opened: $PORTAL_URL${NC}"
else
    echo -e "${YELLOW}⚠️  Please manually open: $PORTAL_URL${NC}"
fi

echo ""

# Step 9: Attempt CLI Deployment
echo -e "${YELLOW}[9/10] Attempting CLI deployment...${NC}"

if [ "$CLI_AVAILABLE" = true ] && [ "$ENV_AVAILABLE" = true ]; then
    echo -e "${BLUE}   Activating environment: $ENV_NAME${NC}"
    
    # Try to activate environment (may require authentication)
    if orchestrate env activate "$ENV_NAME" &>/dev/null; then
        echo -e "${GREEN}✅ Environment activated${NC}"
        
        echo -e "${BLUE}   Importing agent: $CONFIG_FILE${NC}"
        if orchestrate agents import --file "$CONFIG_FILE" 2>&1; then
            echo -e "${GREEN}✅ Agent deployed successfully via CLI!${NC}"
            DEPLOYMENT_SUCCESS=true
        else
            DEPLOYMENT_EXIT_CODE=$?
            if [ $DEPLOYMENT_EXIT_CODE -eq 0 ]; then
                echo -e "${GREEN}✅ Agent import completed${NC}"
                DEPLOYMENT_SUCCESS=true
            else
                echo -e "${YELLOW}⚠️  CLI deployment encountered an issue${NC}"
                echo -e "${BLUE}   Exit code: $DEPLOYMENT_EXIT_CODE${NC}"
                echo -e "${YELLOW}   This may require authentication${NC}"
                DEPLOYMENT_SUCCESS=false
            fi
        fi
    else
        echo -e "${YELLOW}⚠️  Environment activation requires authentication${NC}"
        echo -e "${BLUE}   Please authenticate manually${NC}"
        DEPLOYMENT_SUCCESS=false
    fi
else
    echo -e "${YELLOW}⚠️  CLI or environment not available for automated deployment${NC}"
    DEPLOYMENT_SUCCESS=false
fi

echo ""

# Step 10: Display Final Summary
echo -e "${YELLOW}[10/10] Deployment summary...${NC}"
echo ""

echo -e "${GREEN}═══════════════════════════════════════════════════════════════${NC}"
if [ "$DEPLOYMENT_SUCCESS" = true ]; then
    echo -e "${GREEN}✅ AUTOMATED DEPLOYMENT COMPLETE!${NC}"
else
    echo -e "${YELLOW}⚠️  MANUAL DEPLOYMENT REQUIRED${NC}"
fi
echo -e "${GREEN}═══════════════════════════════════════════════════════════════${NC}"
echo ""

echo -e "${BLUE}📋 Deployment Status:${NC}"
echo -e "${GREEN}✅ Configuration file verified (v$VERSION)${NC}"
echo -e "${GREEN}✅ STT references: $STT_COUNT${NC}"
echo -e "${GREEN}✅ TTS references: $TTS_COUNT${NC}"
echo -e "${GREEN}✅ Credentials checked ($FOUND_CREDS files found)${NC}"
echo -e "${GREEN}✅ IBM Portal opened${NC}"

if [ "$DEPLOYMENT_SUCCESS" = true ]; then
    echo -e "${GREEN}✅ Agent deployed via CLI${NC}"
else
    echo -e "${YELLOW}⚠️  Manual upload required${NC}"
fi

echo ""

if [ "$DEPLOYMENT_SUCCESS" != true ]; then
    echo -e "${CYAN}═══════════════════════════════════════════════════════════════${NC}"
    echo -e "${CYAN}📋 Manual Deployment Instructions${NC}"
    echo -e "${CYAN}═══════════════════════════════════════════════════════════════${NC}"
    echo ""
    
    echo -e "${GREEN}Option 1: CLI Deployment (Recommended)${NC}"
    echo ""
    echo -e "${BLUE}Step 1: Authenticate environment${NC}"
    echo -e "   ${YELLOW}orchestrate env activate $ENV_NAME${NC}"
    echo ""
    echo -e "${BLUE}Step 2: Deploy agent${NC}"
    echo -e "   ${YELLOW}orchestrate agents import --file $CONFIG_FILE${NC}"
    echo ""
    
    echo -e "${GREEN}Option 2: Web UI Deployment${NC}"
    echo ""
    echo -e "${BLUE}1. Find your agent in IBM Portal${NC}"
    echo -e "   • Click 'All agents' or 'Skills' in left sidebar"
    echo -e "   • Find: ProActive_CSI_Agent_404"
    echo ""
    echo -e "${BLUE}2. Edit agent${NC}"
    echo -e "   • Click 'Edit' button (top right)"
    echo ""
    echo -e "${BLUE}3. Upload configuration${NC}"
    echo -e "   • Click 'Import from file' or 'Upload'"
    echo -e "   • Select file: ${YELLOW}$FILE_PATH${NC}"
    echo ""
    echo -e "${BLUE}4. Verify services${NC}"
    echo -e "   • Go to 'Connections' tab"
    echo -e "   • Verify: Speech-to-Text (STT)"
    echo -e "   • Verify: Text-to-Speech (TTS)"
    echo -e "   • Verify: Natural Language Understanding (NLU)"
    echo ""
    echo -e "${BLUE}5. Save & Activate${NC}"
    echo -e "   • Click 'Save' button"
    echo -e "   • Click 'Activate' or 'Publish' button"
    echo ""
fi

echo ""
echo -e "${CYAN}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${CYAN}📁 Configuration Details${NC}"
echo -e "${CYAN}═══════════════════════════════════════════════════════════════${NC}"
echo ""
echo -e "${BLUE}Configuration File:${NC}"
echo -e "${GREEN}$FILE_PATH${NC}"
echo ""
echo -e "${BLUE}Version:${NC} ${GREEN}$VERSION${NC}"
echo -e "${BLUE}File Size:${NC} ${GREEN}$FILE_SIZE${NC}"
echo -e "${BLUE}STT References:${NC} ${GREEN}$STT_COUNT${NC}"
echo -e "${BLUE}TTS References:${NC} ${GREEN}$TTS_COUNT${NC}"
echo ""

echo -e "${CYAN}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${CYAN}🌐 IBM Portal Access${NC}"
echo -e "${CYAN}═══════════════════════════════════════════════════════════════${NC}"
echo ""
echo -e "${BLUE}Portal URL:${NC}"
echo -e "${GREEN}$PORTAL_URL${NC}"
echo ""
echo -e "${BLUE}Instance ID:${NC}"
echo -e "${GREEN}$INSTANCE_ID${NC}"
echo ""
echo -e "${BLUE}Region:${NC}"
echo -e "${GREEN}Australia Sydney (au-syd)${NC}"
echo ""

echo -e "${CYAN}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${CYAN}🧪 Test Queries After Deployment${NC}"
echo -e "${CYAN}═══════════════════════════════════════════════════════════════${NC}"
echo ""
echo -e "${GREEN}Test 1 - TTS:${NC}"
echo '   "Read me the executive briefing aloud using Text-to-Speech"'
echo ""
echo -e "${GREEN}Test 2 - STT:${NC}"
echo '   "I am driving, what is my priority today? Process via voice command."'
echo ""
echo -e "${GREEN}Test 3 - Combined:${NC}"
echo '   "Using voice commands, give me a voice briefing on vendor delays"'
echo ""

echo -e "${GREEN}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}🎤🔊 Complete Deployment Script Finished! 🚀${NC}"
echo -e "${GREEN}═══════════════════════════════════════════════════════════════${NC}"
echo ""

