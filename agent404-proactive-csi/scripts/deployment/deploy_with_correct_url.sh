#!/bin/bash

# Deploy to AU following IBM documentation exactly

echo "╔═══════════════════════════════════════════════════════════════════════════╗"
echo "║     Deploy to Australia Sydney (Following IBM Documentation)             ║"
echo "╚═══════════════════════════════════════════════════════════════════════════╝"
echo ""

cd /Users/ishwaryasridharan/Desktop/Hackathon_2025/Agentic_AI/agent404-proactive-csi

API_KEY="8c593427-3768-4ae1-a695-b9bcbe84b21e"

echo "📋 According to IBM documentation:"
echo "   1. Go to Settings > API details tab"
echo "   2. Copy the 'Service instance URL'"
echo "   3. Use that URL below"
echo ""
echo "   Current URL we're trying:"
echo "   https://api.au-syd.watson-orchestrate.cloud.ibm.com/instances/f16c2181-a811-4d84-8e15-33cfebe50928"
echo ""
read -p "Enter the Service instance URL from Settings (or press Enter to try current): " SERVICE_URL

if [ -z "$SERVICE_URL" ]; then
    SERVICE_URL="https://api.au-syd.watson-orchestrate.cloud.ibm.com/instances/f16c2181-a811-4d84-8e15-33cfebe50928"
fi

echo ""
echo "📍 Step 1: Removing old environment..."
orchestrate env remove --name production-au 2>/dev/null || true

echo ""
echo "📍 Step 2: Adding environment (following IBM docs format)..."
echo "   URL: $SERVICE_URL"
echo ""
orchestrate env add -n production-au -u "$SERVICE_URL" --type mcsp --activate

if [ $? -eq 0 ]; then
    echo ""
    echo "📍 Step 3: Environment created! Now activating with API key..."
    echo ""
    echo "$API_KEY" | orchestrate env activate production-au 2>&1 | grep -v "Warning: Password input" || {
        echo ""
        echo "⚠️  Activation might need manual input. Please run:"
        echo "   orchestrate env activate production-au"
        echo "   (Enter API key: $API_KEY)"
        echo ""
        read -p "Press Enter after you've activated the environment..."
    }
    
    echo ""
    echo "📍 Step 4: Deploying agent..."
    orchestrate agents import -f proactive-csi-agent-orchestrate.yaml
    
    if [ $? -eq 0 ]; then
        echo ""
        echo "╔═══════════════════════════════════════════════════════════════════════════╗"
        echo "║                    ✅ DEPLOYMENT SUCCESSFUL! ✅                          ║"
        echo "╚═══════════════════════════════════════════════════════════════════════════╝"
        echo ""
        echo "📍 Step 5: Verifying..."
        orchestrate agents list | head -15
        echo ""
        echo "🌐 Access your agent at:"
        echo "   https://au-syd.watson-orchestrate.cloud.ibm.com/build/manage"
        echo ""
        echo "🗑️  To delete 'delete' agent:"
        echo "   orchestrate agents remove --name delete --kind native"
    else
        echo "❌ Agent deployment failed"
    fi
else
    echo ""
    echo "❌ Failed to add environment"
    echo "   Please check the Service instance URL from Settings > API details"
fi

