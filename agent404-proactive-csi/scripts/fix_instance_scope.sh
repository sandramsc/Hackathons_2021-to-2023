#!/bin/bash

# Fix Instance Scope Issue - IBM watsonx Orchestrate
# The error "Scope not found" means the instance ID doesn't exist or API key can't access it

set -e

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

cd /Users/ishwaryasridharan/Desktop/Hackathon_2025/Agentic_AI/agent404-proactive-csi

echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}🔧 Fix Instance Scope Issue${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
echo ""

echo -e "${YELLOW}The issue: 'Scope not found' means the instance ID is wrong${NC}"
echo ""
echo -e "${BLUE}The instance ID needs to be obtained from IBM Portal${NC}"
echo ""

echo -e "${GREEN}Step 1: Get the correct instance ID from IBM Portal${NC}"
echo ""
echo -e "${BLUE}1. Open: ${YELLOW}https://cloud.ibm.com/watsonx/orchestrate${NC}"
echo -e "${BLUE}2. Login with your IBM Cloud credentials${NC}"
echo -e "${BLUE}3. Go to Settings → API details${NC}"
echo -e "${BLUE}4. Copy the 'Service instance URL'${NC}"
echo -e "${BLUE}   It should look like:${NC}"
echo -e "${YELLOW}   https://api.au-syd.watson-orchestrate.cloud.ibm.com/instances/XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX${NC}"
echo ""

read -p "Do you have the correct Service instance URL from IBM Portal? (y/n) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo -e "${YELLOW}Please get the Service instance URL from IBM Portal first${NC}"
    echo ""
    echo -e "${BLUE}Opening IBM Portal...${NC}"
    open "https://cloud.ibm.com/watsonx/orchestrate" 2>/dev/null || true
    exit 1
fi

echo ""
echo -e "${GREEN}Step 2: Enter the correct Service instance URL${NC}"
echo -e "${BLUE}Paste the Service instance URL from IBM Portal:${NC}"
read -p "Service instance URL: " SERVICE_URL

if [ -z "$SERVICE_URL" ]; then
    echo -e "${RED}❌ Service URL is empty. Exiting.${NC}"
    exit 1
fi

# Extract instance ID from URL
INSTANCE_ID=$(echo "$SERVICE_URL" | grep -o '[0-9a-f]\{8\}-[0-9a-f]\{4\}-[0-9a-f]\{4\}-[0-9a-f]\{4\}-[0-9a-f]\{12\}' | head -1)

if [ -z "$INSTANCE_ID" ]; then
    echo -e "${YELLOW}⚠️  Could not extract instance ID from URL. Using full URL.${NC}"
    INSTANCE_ID=""
else
    echo -e "${GREEN}✅ Extracted instance ID: $INSTANCE_ID${NC}"
fi

echo ""
echo -e "${GREEN}Step 3: Enter your IBM Cloud API key${NC}"
echo -e "${BLUE}Get it from: ${YELLOW}https://cloud.ibm.com/iam/apikeys${NC}"
read -sp "IBM Cloud API key: " API_KEY
echo ""

if [ -z "$API_KEY" ]; then
    echo -e "${RED}❌ API key is empty. Exiting.${NC}"
    exit 1
fi

echo ""
echo -e "${GREEN}Step 4: Removing old environment...${NC}"

# Remove old environment
echo "y" | orchestrate env remove --name production-au 2>/dev/null || true

echo ""
echo -e "${GREEN}Step 5: Adding environment with correct instance URL...${NC}"

# Try different authentication types
echo -e "${BLUE}Trying mcsp_v2 type...${NC}"
if orchestrate env add -n production-au -u "$SERVICE_URL" --type mcsp_v2 2>&1; then
    echo -e "${GREEN}✅ Environment added with mcsp_v2${NC}"
elif orchestrate env add -n production-au -u "$SERVICE_URL" --type mcsp 2>&1; then
    echo -e "${GREEN}✅ Environment added with mcsp${NC}"
else
    echo -e "${RED}❌ Failed to add environment. Check the URL.${NC}"
    exit 1
fi

echo ""
echo -e "${GREEN}Step 6: Activating environment...${NC}"
echo -e "${BLUE}Paste your API key when prompted: ${YELLOW}$API_KEY${NC}"
echo ""

# Activate environment
echo "$API_KEY" | orchestrate env activate production-au 2>&1 | grep -v "Warning: Password input" || {
    echo ""
    echo -e "${YELLOW}⚠️  Automatic activation failed. Please activate manually:${NC}"
    echo -e "${BLUE}   orchestrate env activate production-au${NC}"
    echo -e "${BLUE}   Then paste your API key when prompted${NC}"
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
echo -e "${GREEN}Step 7: Updating credentials file...${NC}"

# Update credentials file
cat > ../ibm-credentials_Orchestrate_data_Updated.json <<EOF
{
  "watsonx_orchestrate": {
    "api_key": "$API_KEY",
    "service_url": "$SERVICE_URL"
  }
}
EOF

echo -e "${GREEN}✅ Credentials file updated${NC}"

echo ""
echo -e "${GREEN}Step 8: Testing deployment...${NC}"

if orchestrate agents list 2>&1 | head -5; then
    echo -e "${GREEN}✅ Connection successful!${NC}"
    echo ""
    echo -e "${GREEN}Step 9: Deploying agent...${NC}"
    
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
        echo -e "${YELLOW}$SERVICE_URL" | sed 's|/instances/.*|/build/manage|' || echo -e "${YELLOW}https://cloud.ibm.com/watsonx/orchestrate${NC}"
        echo ""
    else
        echo ""
        echo -e "${YELLOW}⚠️  Agent deployment encountered an issue.${NC}"
        echo -e "${BLUE}Try manually:${NC}"
        echo -e "${BLUE}   orchestrate agents import --file proactive-csi-agent-orchestrate.yaml${NC}"
        echo ""
    fi
else
    echo -e "${YELLOW}⚠️  Connection test failed. Check your API key and instance URL.${NC}"
    exit 1
fi

echo -e "${GREEN}🎤🔊 Instance scope fixed and deployment complete! 🚀${NC}"
echo ""

