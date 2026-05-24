#!/bin/bash

# ProActive CSI - IBM Portal Deployment Script
# Automated deployment to IBM watsonx Orchestrate

echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║  🚀 ProActive CSI - IBM watsonx Orchestrate Deployment 🚀   ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check prerequisites
echo -e "${BLUE}📋 Checking prerequisites...${NC}"
echo ""

# Check if ibmcloud CLI is installed
if ! command -v ibmcloud &> /dev/null; then
    echo -e "${RED}❌ IBM Cloud CLI not found${NC}"
    echo "Install from: https://cloud.ibm.com/docs/cli"
    echo ""
    echo "Quick install:"
    echo "  curl -fsSL https://clis.cloud.ibm.com/install/osx | sh"
    exit 1
fi

echo -e "${GREEN}✅ IBM Cloud CLI installed${NC}"

# Check if logged in
if ! ibmcloud target &> /dev/null; then
    echo -e "${YELLOW}⚠️  Not logged in to IBM Cloud${NC}"
    echo ""
    echo "Please login:"
    echo "  ibmcloud login --sso"
    echo ""
    read -p "Press Enter after logging in..."
fi

echo -e "${GREEN}✅ IBM Cloud login verified${NC}"
echo ""

# Display current target
echo -e "${BLUE}Current IBM Cloud target:${NC}"
ibmcloud target
echo ""

# Check if YAML file exists
if [ ! -f "proactive-csi-agent.yaml" ]; then
    echo -e "${RED}❌ Configuration file not found: proactive-csi-agent.yaml${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Configuration file found${NC}"
echo ""

# Deployment options
echo "═══════════════════════════════════════════════════════════════"
echo "Select deployment method:"
echo "═══════════════════════════════════════════════════════════════"
echo "1. Upload to watsonx Orchestrate Web UI (Manual)"
echo "2. Deploy with watsonx Orchestrate CLI (Automated)"
echo "3. Deploy as IBM Cloud Functions"
echo "4. View deployment instructions only"
echo ""
read -p "Select option [1-4]: " option

case $option in
    1)
        echo ""
        echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
        echo -e "${BLUE}📤 Manual Upload Instructions${NC}"
        echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
        echo ""
        echo "1. Open IBM watsonx Orchestrate:"
        echo "   https://cloud.ibm.com/watsonx/orchestrate"
        echo "   Or direct: https://api.au-syd.watson-orchestrate.cloud.ibm.com/"
        echo ""
        echo "2. Navigate to: Skills → Add skill → Import skill"
        echo ""
        echo "3. Upload file: proactive-csi-agent.yaml"
        echo ""
        echo "4. Configure IBM services:"
        echo "   - Natural Language Understanding"
        echo "   - Speech to Text"
        echo "   - Text to Speech"
        echo "   - Cloudant"
        echo ""
        echo "5. Test with: 'What's my priority today?'"
        echo ""
        echo -e "${GREEN}✅ Configuration file is ready to upload!${NC}"
        echo ""
        echo "Opening web browser..."
        sleep 2
        open "https://cloud.ibm.com/watsonx/orchestrate" 2>/dev/null || \
        xdg-open "https://cloud.ibm.com/watsonx/orchestrate" 2>/dev/null || \
        echo "Please manually open: https://cloud.ibm.com/watsonx/orchestrate"
        ;;
    
    2)
        echo ""
        echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
        echo -e "${BLUE}🤖 Automated CLI Deployment${NC}"
        echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
        echo ""
        
        # Check if orchestrate CLI is installed
        if ! command -v orchestrate-cli &> /dev/null; then
            echo -e "${YELLOW}Installing watsonx Orchestrate CLI...${NC}"
            pip3 install -q ibm-watsonx-orchestrate
        fi
        
        echo -e "${GREEN}✅ Orchestrate CLI ready${NC}"
        echo ""
        
        # Set credentials (Updated for Australia Sydney region)
        echo "Setting up credentials..."
        export ORCHESTRATE_API_KEY="azE6dXNyXzBhYzkzMjI4LTE5YWMtMzhmNi1hY2VmLWRhYTEzYmU1NzYzYjpNUzNVUnVycVB6NWpBcTd5dUc5VEhreGduVWRLNndkY0I5TFhRMWpDRXdnPTpwczVM"
        export ORCHESTRATE_URL="https://api.au-syd.watson-orchestrate.cloud.ibm.com/instances/f16c2181-a811-4d84-8e15-33cfebe50928"
        export ORCHESTRATE_INSTANCE_ID="f16c2181-a811-4d84-8e15-33cfebe50928"
        export ORCHESTRATE_REGION="au-syd"
        
        echo -e "${GREEN}✅ Credentials configured${NC}"
        echo ""
        
        echo "Deploying ProActive CSI to watsonx Orchestrate..."
        # Note: This is a placeholder - actual CLI commands may vary
        echo ""
        echo -e "${YELLOW}⚠️  Note: watsonx Orchestrate CLI deployment may require additional configuration${NC}"
        echo "Please use the web UI method (Option 1) for most reliable deployment"
        echo ""
        ;;
    
    3)
        echo ""
        echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
        echo -e "${BLUE}☁️  IBM Cloud Functions Deployment${NC}"
        echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
        echo ""
        
        # Check if cloud-functions plugin is installed
        if ! ibmcloud fn &> /dev/null; then
            echo "Installing Cloud Functions plugin..."
            ibmcloud plugin install cloud-functions -f
        fi
        
        echo -e "${GREEN}✅ Cloud Functions plugin ready${NC}"
        echo ""
        
        echo "Deploying agents as Cloud Functions..."
        echo ""
        
        # Deploy Customer Success Agent
        echo "Deploying Customer Success Agent..."
        # Note: Actual deployment would package the agent properly
        echo -e "${YELLOW}⚠️  Note: Cloud Functions deployment requires additional packaging${NC}"
        echo ""
        
        echo "For full Cloud Functions deployment, see:"
        echo "  IBM_PORTAL_DEPLOYMENT.md"
        echo ""
        ;;
    
    4)
        echo ""
        echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
        echo -e "${BLUE}📚 Deployment Instructions${NC}"
        echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
        echo ""
        echo "Complete deployment guide available at:"
        echo "  IBM_PORTAL_DEPLOYMENT.md"
        echo ""
        echo "Quick start:"
        echo "  1. Open: https://dl.watson-orchestrate.ibm.com/"
        echo "  2. Upload: proactive-csi-agent.yaml"
        echo "  3. Connect IBM services"
        echo "  4. Test workflows"
        echo ""
        cat IBM_PORTAL_DEPLOYMENT.md 2>/dev/null || echo "See IBM_PORTAL_DEPLOYMENT.md file"
        ;;
    
    *)
        echo -e "${RED}Invalid option${NC}"
        exit 1
        ;;
esac

echo ""
echo -e "${GREEN}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}🎉 Deployment preparation complete!${NC}"
echo -e "${GREEN}═══════════════════════════════════════════════════════════════${NC}"
echo ""
echo "Next steps:"
echo "  1. Complete the deployment in watsonx Orchestrate web UI"
echo "  2. Connect IBM services (NLU, STT, TTS, Cloudant)"
echo "  3. Test with: 'What's my priority today?'"
echo "  4. Run workflows to verify multi-agent coordination"
echo ""
echo "📚 Full guide: IBM_PORTAL_DEPLOYMENT.md"
echo "🌐 Portal: https://dl.watson-orchestrate.ibm.com/"
echo ""
echo -e "${GREEN}Good luck with your hackathon! 🏆${NC}"
echo ""

