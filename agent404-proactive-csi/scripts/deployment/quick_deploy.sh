#!/bin/bash

# Quick deployment script for ProActive CSI Agent 404
# Deploys to IBM watsonx Orchestrate (Australia Sydney)

set -e  # Exit on error

echo "╔═══════════════════════════════════════════════════════════════════════════╗"
echo "║  Deploying ProActive CSI Agent to Australia Sydney Environment           ║"
echo "╚═══════════════════════════════════════════════════════════════════════════╝"
echo ""

# Navigate to project directory
cd /Users/ishwaryasridharan/Desktop/Hackathon_2025/Agentic_AI/agent404-proactive-csi

# Step 1: Verify configuration file exists
if [ ! -f "proactive-csi-agent-orchestrate.yaml" ]; then
    echo "❌ Error: proactive-csi-agent-orchestrate.yaml not found!"
    exit 1
fi

echo "✅ Configuration file found"
echo ""

# Step 2: Activate environment
echo "📍 Step 1: Activating production-au environment..."
echo "   ⚠️  You'll be prompted for API key"
echo "   📋 API Key: 9-atsNvf8mx0ymZLaGgZwe28rhyZvLcX_QUQlyDb12rg"
echo ""
echo "   (Paste the API key above when prompted)"
echo ""

orchestrate env activate production-au

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Environment activated!"
    echo ""
    
    # Step 3: Deploy agent
    echo "📍 Step 2: Importing agent..."
    orchestrate agents import -f proactive-csi-agent-orchestrate.yaml
    
    if [ $? -eq 0 ]; then
        echo ""
        echo "✅ Agent deployed successfully!"
        echo ""
        echo "📍 Step 3: Verifying deployment..."
        echo ""
        orchestrate agents list | grep -i "proactive" | head -5
        echo ""
        echo "╔═══════════════════════════════════════════════════════════════════════════╗"
        echo "║                    ✅ DEPLOYMENT COMPLETE! ✅                              ║"
        echo "╚═══════════════════════════════════════════════════════════════════════════╝"
        echo ""
        echo "🎉 Your agent is now live!"
        echo ""
        echo "🌐 Access your agent at:"
        echo "   https://au-syd.watson-orchestrate.cloud.ibm.com/build/manage"
        echo ""
        echo "🧪 Test your agent with:"
        echo "   • 'What's my priority today?'"
        echo "   • 'Show me critical customers at risk'"
        echo "   • 'Generate daily executive brief'"
        echo ""
    else
        echo ""
        echo "❌ Agent import failed"
        echo "   Check the error message above"
        exit 1
    fi
else
    echo ""
    echo "❌ Environment activation failed"
    echo "   Check your API key and service URL"
    exit 1
fi

