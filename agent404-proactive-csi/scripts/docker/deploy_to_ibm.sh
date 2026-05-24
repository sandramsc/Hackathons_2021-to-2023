#!/bin/bash

# Deploy ProActive CSI Agent 404 to IBM watsonx Orchestrate via Docker
# This script runs inside the Docker container

set -e

echo "╔═══════════════════════════════════════════════════════════════════════════╗"
echo "║     🐳 Deploying to IBM watsonx Orchestrate from Docker 🐳                 ║"
echo "╚═══════════════════════════════════════════════════════════════════════════╝"
echo ""

cd /app

# Check if agent configuration exists
if [ ! -f "proactive-csi-agent-orchestrate.yaml" ]; then
    echo "❌ Error: proactive-csi-agent-orchestrate.yaml not found!"
    exit 1
fi

# Get credentials from environment variables or mounted files
if [ -f "/app/ibm-credentials_Orchestrate_data_Updated.json" ]; then
    ORCHESTRATE_API_KEY=$(cat /app/ibm-credentials_Orchestrate_data_Updated.json | grep -o '"api_key"[^,]*' | cut -d'"' -f4)
    echo "✅ Found Orchestrate credentials in mounted file"
else
    ORCHESTRATE_API_KEY=${WATSONX_ORCHESTRATE_APIKEY:-"9-atsNvf8mx0ymZLaGgZwe28rhyZvLcX_QUQlyDb12rg"}
    echo "✅ Using Orchestrate API key from environment variable"
fi

if [ -z "$ORCHESTRATE_API_KEY" ]; then
    echo "❌ Error: Orchestrate API key not found!"
    echo "   Set WATSONX_ORCHESTRATE_APIKEY environment variable or mount credentials file"
    exit 1
fi

# Step 1: Add environment if it doesn't exist, then activate
echo ""
echo "📍 Step 1: Setting up production-au environment..."

# Check if environment exists
if ! orchestrate env list 2>/dev/null | grep -q "production-au"; then
    echo "   Environment 'production-au' not found. Adding it..."
    orchestrate env add -n production-au -u "https://api.au-syd.watson-orchestrate.cloud.ibm.com/instances/f16c2181-a811-4d84-8e15-33cfebe50928"
    echo ""
fi

# Activate environment
echo "   Activating production-au environment..."
echo "$ORCHESTRATE_API_KEY" | orchestrate env activate production-au

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Environment activated!"
    echo ""
    
    # Step 2: Deploy agent
    echo "📍 Step 2: Deploying agent..."
    orchestrate agents import -f proactive-csi-agent-orchestrate.yaml
    
    if [ $? -eq 0 ]; then
        echo ""
        echo "✅ Agent deployed successfully!"
        echo ""
        
        # Step 3: Verify deployment
        echo "📍 Step 3: Verifying deployment..."
        echo ""
        orchestrate agents list | grep -i "proactive" | head -5
        
        echo ""
        echo "╔═══════════════════════════════════════════════════════════════════════════╗"
        echo "║              ✅ DEPLOYMENT TO IBM COMPLETE! ✅                              ║"
        echo "╚═══════════════════════════════════════════════════════════════════════════╝"
        echo ""
        echo "🎉 Your agent is now live on IBM watsonx Orchestrate!"
        echo ""
        echo "🌐 Access your agent at:"
        echo "   https://au-syd.watson-orchestrate.cloud.ibm.com/build/manage"
        echo ""
    else
        echo ""
        echo "❌ Agent deployment failed"
        exit 1
    fi
else
    echo ""
    echo "❌ Environment activation failed"
    exit 1
fi

