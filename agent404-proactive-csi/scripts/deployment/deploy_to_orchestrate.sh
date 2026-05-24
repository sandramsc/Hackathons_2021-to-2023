#!/bin/bash

# ProActive CSI - Deployment Script for IBM watsonx Orchestrate
# Same method as Onboarding-Coordinator project

set -e

echo "╔═══════════════════════════════════════════════════════════════════════════╗"
echo "║                                                                           ║"
echo "║           🚀 Deploying ProActive CSI Agent to IBM watsonx Orchestrate    ║"
echo "║                                                                           ║"
echo "╚═══════════════════════════════════════════════════════════════════════════╝"
echo ""

# Navigate to project directory
cd "$(dirname "$0")"
PROJECT_DIR=$(pwd)

echo "📍 Project Directory: $PROJECT_DIR"
echo ""

# Check if agent YAML exists
if [ ! -f "proactive-csi-agent-orchestrate.yaml" ]; then
    echo "❌ Error: Agent YAML file not found: proactive-csi-agent-orchestrate.yaml"
    exit 1
fi

echo "✅ Agent YAML file found: proactive-csi-agent-orchestrate.yaml"
echo ""

# Check Orchestrate CLI
if ! command -v orchestrate &> /dev/null; then
    echo "❌ Error: Orchestrate CLI not found. Please install it first:"
    echo "   pip install ibm-watsonx-orchestrate"
    exit 1
fi

echo "✅ Orchestrate CLI found: $(orchestrate --version | head -n 1)"
echo ""

# Show current environments
echo "📋 Current Orchestrate Environments:"
orchestrate env list
echo ""

# Activate production environment (Australia Sydney)
echo "🔑 Activating environment..."
echo "   Please enter your IBM Cloud API key when prompted"
echo "   (Get it from: https://cloud.ibm.com/iam/apikeys)"
echo ""
echo "   Service URL: https://api.au-syd.watson-orchestrate.cloud.ibm.com/instances/f16c2181-a811-4d84-8e15-33cfebe50928"
echo ""

# Force activation of production-au (Australia Sydney)
echo "🔧 Targeting Australia Sydney environment (production-au)"
echo "   This matches your web UI: https://au-syd.watson-orchestrate.cloud.ibm.com"
echo ""

# Check if production-au exists
if orchestrate env list | grep -q "production-au"; then
    echo "✅ Found production-au environment"
    echo "   Activating now (you'll need to enter API key)..."
    orchestrate env activate production-au
    ENV_NAME="production-au"
else
    echo "⚠️  production-au environment not found. Creating it..."
    echo "   Run this command first:"
    echo ""
    echo "   orchestrate env add -n production-au \\"
    echo "     -u 'https://api.au-syd.watson-orchestrate.cloud.ibm.com/instances/f16c2181-a811-4d84-8e15-33cfebe50928' \\"
    echo "     --type mcsp --activate"
    echo ""
    echo "   Then re-run this script."
    exit 1
fi

echo ""
echo "📤 Importing agent..."
echo ""

# Import agent
if orchestrate agents import -f proactive-csi-agent-orchestrate.yaml; then
    echo ""
    echo "╔═══════════════════════════════════════════════════════════════════════════╗"
    echo "║                                                                           ║"
    echo "║                    ✅ DEPLOYMENT SUCCESSFUL! ✅                          ║"
    echo "║                                                                           ║"
    echo "╚═══════════════════════════════════════════════════════════════════════════╝"
    echo ""
    echo "🎉 Your agent 'ProActive_CSI_Agent_404' has been deployed!"
    echo ""
    echo "📋 Verify deployment:"
    echo "   orchestrate agents list"
    echo ""
    echo "🌐 Access in Web UI:"
    echo "   https://au-syd.watson-orchestrate.cloud.ibm.com/build/manage"
    echo ""
    echo "🧪 Test your agent:"
    echo "   1. Go to the web UI above"
    echo "   2. Click on your agent 'ProActive_CSI_Agent_404'"
    echo "   3. Try these queries:"
    echo "      • 'What's my priority today?'"
    echo "      • 'Show me critical customers at risk'"
    echo "      • 'Generate daily executive brief'"
    echo ""
else
    echo ""
    echo "❌ Deployment failed. Please check the error above."
    exit 1
fi

