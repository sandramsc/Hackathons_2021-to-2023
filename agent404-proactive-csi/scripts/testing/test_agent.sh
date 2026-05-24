#!/bin/bash

# Quick Agent Testing Script
# Tests ProActive_CSI_Agent_404 via CLI

echo "╔═══════════════════════════════════════════════════════════════════════════╗"
echo "║              🧪 Testing ProActive_CSI_Agent_404 🧪                       ║"
echo "╚═══════════════════════════════════════════════════════════════════════════╝"
echo ""

cd /Users/ishwaryasridharan/Desktop/Hackathon_2025/Agentic_AI/agent404-proactive-csi

# Check environment
echo "📍 Checking environment..."
orchestrate env list | grep "production-au" | grep "active" > /dev/null
if [ $? -eq 0 ]; then
    echo "✅ AU environment is active"
else
    echo "⚠️  Activating AU environment..."
    echo "9-atsNvf8mx0ymZLaGgZwe28rhyZvLcX_QUQlyDb12rg" | orchestrate env activate production-au 2>&1 | grep -E "active|ERROR" | head -2
fi

echo ""
echo "📍 Verifying agent exists..."
orchestrate agents list 2>&1 | grep -i "proactive" > /dev/null
if [ $? -eq 0 ]; then
    echo "✅ ProActive_CSI_Agent_404 found"
else
    echo "❌ Agent not found!"
    exit 1
fi

echo ""
echo "═══════════════════════════════════════════════════════════════════════════"
echo "🧪 TEST QUERIES"
echo "═══════════════════════════════════════════════════════════════════════════"
echo ""
echo "Choose a test query:"
echo ""
echo "1. Basic greeting"
echo "2. Priority check"
echo "3. Churn prediction"
echo "4. Revenue analysis"
echo "5. Procurement impact"
echo "6. Custom query"
echo ""
read -p "Enter choice (1-6): " choice

case $choice in
    1)
        query="Hello, what can you do?"
        ;;
    2)
        query="What's my priority today?"
        ;;
    3)
        query="Which customers are at high churn risk?"
        ;;
    4)
        query="Calculate ARR at risk"
        ;;
    5)
        query="Show me procurement-customer impact analysis"
        ;;
    6)
        read -p "Enter your query: " query
        ;;
    *)
        query="What's my priority today?"
        ;;
esac

echo ""
echo "📤 Sending query: \"$query\""
echo ""
echo "═══════════════════════════════════════════════════════════════════════════"
echo "📥 AGENT RESPONSE:"
echo "═══════════════════════════════════════════════════════════════════════════"
echo ""

orchestrate agents chat --name "ProActive_CSI_Agent_404" --message "$query" 2>&1

echo ""
echo ""
echo "═══════════════════════════════════════════════════════════════════════════"
echo "✅ Test complete!"
echo ""
echo "💡 Tip: For better experience, use the web UI:"
echo "   https://au-syd.watson-orchestrate.cloud.ibm.com/build/manage"
echo "═══════════════════════════════════════════════════════════════════════════"

