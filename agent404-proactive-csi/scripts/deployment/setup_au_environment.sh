#!/bin/bash

# Setup and deploy to Australia Sydney environment

echo "╔═══════════════════════════════════════════════════════════════════════════╗"
echo "║     Setting up Australia Sydney (AU) Environment                        ║"
echo "╚═══════════════════════════════════════════════════════════════════════════╝"
echo ""

cd /Users/ishwaryasridharan/Desktop/Hackathon_2025/Agentic_AI/agent404-proactive-csi

# Remove existing AU environment if it exists
echo "📍 Step 1: Setting up environment..."
orchestrate env remove production-au 2>/dev/null || true

# Add AU environment
echo "📍 Step 2: Adding production-au environment..."
echo "   URL: https://api.au-syd.watson-orchestrate.cloud.ibm.com/instances/f16c2181-a811-4d84-8e15-33cfebe50928"
echo ""
orchestrate env add -n production-au \
  -u "https://api.au-syd.watson-orchestrate.cloud.ibm.com/instances/f16c2181-a811-4d84-8e15-33cfebe50928" \
  --type mcsp

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Environment added!"
    echo ""
    echo "📍 Step 3: Activating environment..."
    echo "   You'll be prompted for your IBM Cloud API key"
    echo "   (Get it from: https://cloud.ibm.com/iam/apikeys)"
    echo ""
    orchestrate env activate production-au
    
    if [ $? -eq 0 ]; then
        echo ""
        echo "✅ Environment activated!"
        echo ""
        echo "📍 Step 4: Deploying agent..."
        orchestrate agents import -f proactive-csi-agent-orchestrate.yaml
        
        if [ $? -eq 0 ]; then
            echo ""
            echo "╔═══════════════════════════════════════════════════════════════════════════╗"
            echo "║                    ✅ DEPLOYMENT SUCCESSFUL! ✅                          ║"
            echo "╚═══════════════════════════════════════════════════════════════════════════╝"
            echo ""
            echo "🎉 Your agent is now deployed to Australia Sydney!"
            echo ""
            echo "📍 Step 5: Verifying deployment..."
            orchestrate agents list | head -10
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
        echo "❌ Environment activation failed"
        echo "   Make sure you're using an IBM Cloud API key (not service key)"
        echo "   Get it from: https://cloud.ibm.com/iam/apikeys"
    fi
else
    echo "❌ Failed to add environment"
fi

