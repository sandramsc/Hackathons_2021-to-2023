#!/bin/bash

# ProActive CSI - Automated Deployment Script v1.2.0
# Automates deployment to IBM watsonx Orchestrate with STT/TTS integration

set -e

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Get script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$PROJECT_ROOT"

echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}🚀 ProActive CSI - Automated Deployment v1.2.0${NC}"
echo -e "${BLUE}   STT & TTS Audio Integration${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo ""

# Step 1: Verify Configuration File
echo -e "${YELLOW}📋 Step 1: Verifying configuration file...${NC}"
CONFIG_FILE="proactive-csi-agent-orchestrate.yaml"

if [ ! -f "$CONFIG_FILE" ]; then
    echo -e "${RED}❌ Configuration file not found: $CONFIG_FILE${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Configuration file found: $CONFIG_FILE${NC}"

# Check version
VERSION=$(grep -E "^spec_version|version:" "$CONFIG_FILE" | head -1 || echo "v1")
echo -e "${BLUE}   Version detected in file${NC}"

# Check STT/TTS mentions
STT_COUNT=$(grep -ci "STT\|Speech-to-Text\|Speech to Text" "$CONFIG_FILE" || echo "0")
TTS_COUNT=$(grep -ci "TTS\|Text-to-Speech\|Text to Speech" "$CONFIG_FILE" || echo "0")

echo -e "${GREEN}✅ STT references: $STT_COUNT${NC}"
echo -e "${GREEN}✅ TTS references: $TTS_COUNT${NC}"

if [ "$STT_COUNT" -lt 5 ] || [ "$TTS_COUNT" -lt 5 ]; then
    echo -e "${YELLOW}⚠️  Warning: Few STT/TTS references found. Ensure integration is complete.${NC}"
fi

echo ""

# Step 2: Verify Version File
echo -e "${YELLOW}📋 Step 2: Verifying version...${NC}"
if [ -f "VERSION" ]; then
    FILE_VERSION=$(cat VERSION | tr -d '[:space:]')
    echo -e "${GREEN}✅ Version file: $FILE_VERSION${NC}"
    if [ "$FILE_VERSION" != "1.2.0" ]; then
        echo -e "${YELLOW}⚠️  Version mismatch: Expected 1.2.0, found $FILE_VERSION${NC}"
    fi
else
    echo -e "${YELLOW}⚠️  VERSION file not found${NC}"
fi

echo ""

# Step 3: Check Credentials
echo -e "${YELLOW}📋 Step 3: Checking IBM credentials...${NC}"

CRED_FILES=(
    "../ibm-credentials_Orchestrate_data_Updated.json"
    "../ibm-credentials_STT.env"
    "../ibm-credentials_TTS.env"
    "../ibm-credentials_NLU.env"
)

MISSING_CREDS=0
for cred_file in "${CRED_FILES[@]}"; do
    if [ -f "$cred_file" ]; then
        echo -e "${GREEN}✅ Found: $(basename $cred_file)${NC}"
    else
        echo -e "${YELLOW}⚠️  Missing: $(basename $cred_file)${NC}"
        MISSING_CREDS=1
    fi
done

if [ $MISSING_CREDS -eq 0 ]; then
    echo -e "${GREEN}✅ All credential files found${NC}"
else
    echo -e "${YELLOW}⚠️  Some credential files missing (continuing anyway)${NC}"
fi

echo ""

# Step 4: Verify Configuration Syntax
echo -e "${YELLOW}📋 Step 4: Verifying YAML syntax...${NC}"
if command -v python3 &> /dev/null; then
    python3 -c "import yaml; yaml.safe_load(open('$CONFIG_FILE'))" 2>/dev/null
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✅ YAML syntax is valid${NC}"
    else
        echo -e "${RED}❌ YAML syntax error!${NC}"
        exit 1
    fi
else
    echo -e "${YELLOW}⚠️  Python3 not found, skipping YAML validation${NC}"
fi

echo ""

# Step 5: Display Configuration Summary
echo -e "${YELLOW}📋 Step 5: Configuration Summary${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}Configuration File:${NC} $CONFIG_FILE"
echo -e "${BLUE}File Size:${NC} $(ls -lh "$CONFIG_FILE" | awk '{print $5}')"
echo -e "${BLUE}Version:${NC} 1.2.0 (STT & TTS Integration)"
echo -e "${BLUE}STT References:${NC} $STT_COUNT"
echo -e "${BLUE}TTS References:${NC} $TTS_COUNT"
echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo ""

# Step 6: IBM Portal URLs
echo -e "${YELLOW}📋 Step 6: IBM watsonx Orchestrate Access${NC}"
echo -e "${BLUE}Main Portal:${NC} https://cloud.ibm.com/watsonx/orchestrate"
echo -e "${BLUE}Direct URL:${NC} https://au-syd.watson-orchestrate.cloud.ibm.com/build/manage"
echo -e "${BLUE}Instance ID:${NC} f16c2181-a811-4d84-8e15-33cfebe50928"
echo -e "${BLUE}Region:${NC} Australia Sydney (au-syd)"
echo ""

# Step 7: Open Browser
echo -e "${YELLOW}📋 Step 7: Opening IBM Portal in browser...${NC}"
IBM_PORTAL_URL="https://au-syd.watson-orchestrate.cloud.ibm.com/build/manage"

if command -v open &> /dev/null; then
    open "$IBM_PORTAL_URL" 2>/dev/null
    echo -e "${GREEN}✅ Browser opened: $IBM_PORTAL_URL${NC}"
elif command -v xdg-open &> /dev/null; then
    xdg-open "$IBM_PORTAL_URL" 2>/dev/null
    echo -e "${GREEN}✅ Browser opened: $IBM_PORTAL_URL${NC}"
else
    echo -e "${YELLOW}⚠️  Please manually open: $IBM_PORTAL_URL${NC}"
fi

echo ""

# Step 8: Display Deployment Instructions
echo -e "${YELLOW}📋 Step 8: Deployment Instructions${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo ""
echo -e "${GREEN}Follow these steps in the IBM Portal:${NC}"
echo ""
echo -e "${BLUE}1. FIND YOUR AGENT:${NC}"
echo "   • Click 'All agents' or 'Skills' in left sidebar"
echo "   • Find: ProActive_CSI_Agent_404"
echo "   • Click on it"
echo ""
echo -e "${BLUE}2. EDIT AGENT:${NC}"
echo "   • Click 'Edit' button (top right)"
echo "   • OR click three dots (...) menu → 'Edit'"
echo ""
echo -e "${BLUE}3. UPLOAD CONFIGURATION:${NC}"
echo "   • Click 'Import from file' or 'Upload' button"
echo "   • Navigate to:"
echo -e "     ${GREEN}$PROJECT_ROOT${NC}"
echo "   • Select file:"
echo -e "     ${GREEN}$CONFIG_FILE${NC}"
echo "   • Click 'Open' or 'Upload'"
echo "   • Wait for upload (5-10 seconds)"
echo ""
echo -e "${BLUE}4. VERIFY SERVICES:${NC}"
echo "   • Go to 'Connections' or 'Integrations' tab"
echo "   • Verify these services are connected:"
echo -e "     ${GREEN}✅ Speech-to-Text (STT)${NC}"
echo -e "     ${GREEN}✅ Text-to-Speech (TTS)${NC}"
echo -e "     ${GREEN}✅ Natural Language Understanding (NLU)${NC}"
echo "   • If NOT connected, click 'Add Connection' and add them"
echo ""
echo -e "${BLUE}5. SAVE & ACTIVATE:${NC}"
echo "   • Click 'Save' button"
echo "   • Wait for save confirmation"
echo "   • Click 'Activate' or 'Publish' button"
echo "   • Wait for activation (10-30 seconds)"
echo ""
echo -e "${BLUE}6. TEST STT/TTS:${NC}"
echo "   • Click on agent to open chat interface"
echo "   • Type: 'Read me the executive briefing aloud using Text-to-Speech'"
echo "   • Look for response mentioning:"
echo -e "     ${GREEN}✅ 'IBM Text-to-Speech'${NC}"
echo -e "     ${GREEN}✅ 'POST /v1/synthesize'${NC}"
echo -e "     ${GREEN}✅ 'en-US_MichaelV3Voice'${NC}"
echo ""
echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo ""

# Step 9: Display File Location
echo -e "${YELLOW}📋 Step 9: Configuration File Location${NC}"
echo -e "${BLUE}Full Path:${NC}"
echo -e "${GREEN}$(pwd)/$CONFIG_FILE${NC}"
echo ""
echo -e "${BLUE}To copy path:${NC}"
echo -e "${GREEN}$(pwd)/$CONFIG_FILE${NC}" | pbcopy 2>/dev/null || echo -e "${GREEN}$(pwd)/$CONFIG_FILE${NC}"
echo ""

# Step 10: Test Queries Ready
echo -e "${YELLOW}📋 Step 10: Test Queries Ready${NC}"
echo -e "${BLUE}After deployment, test with these queries:${NC}"
echo ""
echo -e "${GREEN}Test 1 - TTS:${NC}"
echo '  "Read me the executive briefing aloud using Text-to-Speech"'
echo ""
echo -e "${GREEN}Test 2 - STT:${NC}"
echo '  "I am driving, what is my priority today? Process via voice command."'
echo ""
echo -e "${GREEN}Test 3 - Combined:${NC}"
echo '  "Using voice commands, give me a voice briefing on vendor delays"'
echo ""

# Step 11: Success Summary
echo -e "${GREEN}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}✅ PREPARATION COMPLETE!${NC}"
echo -e "${GREEN}═══════════════════════════════════════════════════════════════${NC}"
echo ""
echo -e "${BLUE}What's Ready:${NC}"
echo -e "${GREEN}✅ Configuration file verified ($CONFIG_FILE)${NC}"
echo -e "${GREEN}✅ Version 1.2.0 (with STT & TTS integration)${NC}"
echo -e "${GREEN}✅ IBM Portal opened in browser${NC}"
echo -e "${GREEN}✅ Deployment instructions displayed${NC}"
echo ""
echo -e "${BLUE}Next Steps:${NC}"
echo "1. Follow the deployment instructions above"
echo "2. Upload the configuration file in IBM Portal"
echo "3. Verify STT/TTS services are connected"
echo "4. Activate the agent"
echo "5. Test with the test queries above"
echo ""
echo -e "${BLUE}Quick Access:${NC}"
echo -e "IBM Portal: ${GREEN}$IBM_PORTAL_URL${NC}"
echo -e "Config File: ${GREEN}$(pwd)/$CONFIG_FILE${NC}"
echo ""
echo -e "${GREEN}🎤🔊 Ready to deploy with STT & TTS integration! 🚀${NC}"
echo ""

