#!/bin/bash

# ProActive CSI Agent 404 - Deployment Script
# Version: 2.0
# Usage: ./deploy.sh

# ============================================
# CONFIGURATION - UPDATE THESE VALUES
# ============================================
API_KEY="d3B-zanJJ0WbVz2tHDehEEXBUKaJ-xhSVlUdBT52XKF1"
INSTANCE_URL="https://api.au-syd.watson-orchestrate.cloud.ibm.com/instances/f16c2181-a811-4d84-8e15-33cfebe50928"
ENV_NAME="production-au"

# ============================================
# DEPLOYMENT SCRIPT
# ============================================

echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║  🚀 Deploying ProActive CSI Agent 404 - Version 2.0          ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""

# Step 1: Activate environment
echo "📋 Step 1: Activating environment..."
orchestrate env activate --api-key "$API_KEY" "$ENV_NAME" 2>&1 | grep -E "INFO|active|ERROR" || {
    echo "⚠️  Environment not found. Creating..."
    orchestrate env add -n "$ENV_NAME" -u "$INSTANCE_URL" --type ibm_iam 2>&1 | grep -E "INFO|ERROR"
    orchestrate env activate --api-key "$API_KEY" "$ENV_NAME" 2>&1 | grep -E "INFO|active|ERROR"
}

# Step 2: Validate YAML
echo ""
echo "📋 Step 2: Validating YAML..."
python3 -c "import yaml; yaml.safe_load(open('proactive-csi-agent-orchestrate.yaml')); print('✅ YAML Valid')" || {
    echo "❌ YAML validation failed!"
    exit 1
}

# Step 3: Deploy agent
echo ""
echo "📋 Step 3: Deploying agent..."
orchestrate agents import -f proactive-csi-agent-orchestrate.yaml 2>&1 | grep -E "INFO|ERROR"

# Step 4: Verify
echo ""
echo "📋 Step 4: Verifying deployment..."
orchestrate agents list 2>&1 | grep -A 2 "ProActive" || echo "⚠️  Agent not found in list"

echo ""
echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║  ✅ DEPLOYMENT COMPLETE                                       ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""
echo "🔗 Access your agent: https://cloud.ibm.com/watsonx/orchestrate"
echo ""
