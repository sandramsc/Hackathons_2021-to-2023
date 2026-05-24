#!/bin/bash

# Deploy to IBM watsonx Orchestrate from Docker container

set -e

echo "╔═══════════════════════════════════════════════════════════════════════════╗"
echo "║     🐳 Deploy to IBM Orchestrate from Docker Container 🐳                 ║"
echo "╚═══════════════════════════════════════════════════════════════════════════╝"
echo ""

cd /Users/ishwaryasridharan/Desktop/Hackathon_2025/Agentic_AI/agent404-proactive-csi

# Check if container is running
if ! docker-compose ps | grep -q "Up"; then
    echo "⚠️  Container is not running. Starting container..."
    docker-compose up -d
    sleep 5
fi

# Deploy agent using orchestrate CLI from container
echo "📍 Deploying agent to IBM watsonx Orchestrate..."
echo ""

docker-compose exec -T proactive-csi-agent bash -c "
    cd /app && \
    echo '9-atsNvf8mx0ymZLaGgZwe28rhyZvLcX_QUQlyDb12rg' | orchestrate env activate production-au && \
    orchestrate agents import -f proactive-csi-agent-orchestrate.yaml
"

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Agent deployed successfully from Docker container!"
    echo ""
    echo "🌐 Access your agent at:"
    echo "   https://au-syd.watson-orchestrate.cloud.ibm.com/build/manage"
else
    echo ""
    echo "❌ Deployment failed"
    exit 1
fi

