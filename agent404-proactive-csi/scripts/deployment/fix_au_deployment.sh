#!/bin/bash

# Fix AU deployment with correct instance ID

echo "╔═══════════════════════════════════════════════════════════════════════════╗"
echo "║         Fix Australia Sydney Deployment                                   ║"
echo "╚═══════════════════════════════════════════════════════════════════════════╝"
echo ""

cd /Users/ishwaryasridharan/Desktop/Hackathon_2025/Agentic_AI/agent404-proactive-csi

API_KEY="8c593427-3768-4ae1-a695-b9bcbe84b21e"

echo "📋 Please provide the CORRECT instance ID from your AU web UI URL"
echo ""
echo "   When you're on: https://au-syd.watson-orchestrate.cloud.ibm.com/build/manage"
echo "   Check the URL - it might show something like:"
echo "   /instances/XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"
echo ""
read -p "Enter the instance ID (or press Enter to try current one): " INSTANCE_ID

if [ -z "$INSTANCE_ID" ]; then
    INSTANCE_ID="f16c2181-a811-4d84-8e15-33cfebe50928"
    echo "Using default: $INSTANCE_ID"
fi

echo ""
echo "📍 Removing existing environment..."
orchestrate env remove --name production-au 2>/dev/null || true

echo ""
echo "📍 Adding environment with instance ID: $INSTANCE_ID"
orchestrate env add -n production-au \
  -u "https://api.au-syd.watson-orchestrate.cloud.ibm.com/instances/$INSTANCE_ID" \
  --type mcsp

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Environment added!"
    echo ""
    echo "📍 Activating environment with API key..."
    echo "$API_KEY" | orchestrate env activate production-au 2>&1 | grep -v "Warning: Password input"
    
    if [ $? -eq 0 ] || orchestrate env list | grep -q "production-au.*active"; then
        echo ""
        echo "✅ Environment activated!"
        echo ""
        echo "📍 Deploying agent..."
        orchestrate agents import -f proactive-csi-agent-orchestrate.yaml
        
        if [ $? -eq 0 ]; then
            echo ""
            echo "╔═══════════════════════════════════════════════════════════════════════════╗"
            echo "║                    ✅ DEPLOYMENT SUCCESSFUL! ✅                          ║"
            echo "╚═══════════════════════════════════════════════════════════════════════════╝"
            echo ""
            orchestrate agents list | head -10
            echo ""
            echo "🌐 Access at: https://au-syd.watson-orchestrate.cloud.ibm.com/build/manage"
        else
            echo "❌ Agent deployment failed"
        fi
    else
        echo ""
        echo "⚠️  Environment activation had issues. Please try manually:"
        echo "   orchestrate env activate production-au"
        echo "   (Enter API key: $API_KEY)"
    fi
else
    echo "❌ Failed to add environment"
fi

