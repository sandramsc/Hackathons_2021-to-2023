# 🚀 Final Deployment Instructions - ProActive CSI Agent 404

**Version:** 2.0  
**Last Updated:** November 22, 2025  
**Platform:** IBM watsonx Orchestrate

---

## 📋 Quick Start

### Prerequisites
- IBM Cloud account with watsonx Orchestrate service
- watsonx Orchestrate API key
- Instance URL for your watsonx Orchestrate instance
- `orchestrate` CLI installed and configured

---

## 🔑 Step 1: Get Your Credentials

### 1.1 Get API Key
1. Go to: https://cloud.ibm.com/watsonx/orchestrate
2. Click on your instance
3. Go to: **Settings** → **API details**
4. Copy the **API Key** (format: `d3B-zanJJ0WbVz2tHDehEEXBUKaJ-xhSVlUdBT52XKF1`)

### 1.2 Get Instance URL
1. In the same **Settings** → **API details** page
2. Copy the **Service instance URL**
   - Format: `https://api.{region}.watson-orchestrate.cloud.ibm.com/instances/{instance-id}`
   - Example: `https://api.au-syd.watson-orchestrate.cloud.ibm.com/instances/f16c2181-a811-4d84-8e15-33cfebe50928`

---

## 🛠️ Step 2: Setup Environment

### 2.1 Set Environment Variables
```bash
export API_KEY="your-api-key-here"
export INSTANCE_URL="your-instance-url-here"
```

### 2.2 Activate Environment
```bash
cd agent404-proactive-csi

# Activate environment
orchestrate env activate --api-key "$API_KEY" production-au
```

**Note:** If environment doesn't exist, create it first:
```bash
orchestrate env add -n production-au -u "$INSTANCE_URL" --type ibm_iam
orchestrate env activate --api-key "$API_KEY" production-au
```

---

## 📦 Step 3: Deploy Agent

### 3.1 Validate YAML
```bash
python3 -c "import yaml; yaml.safe_load(open('proactive-csi-agent-orchestrate.yaml')); print('✅ YAML Valid')"
```

### 3.2 Deploy Agent
```bash
orchestrate agents import -f proactive-csi-agent-orchestrate.yaml
```

**Expected Output:**
```
[INFO] - Existing Agent 'ProActive_CSI_Agent_404' found. Updating...
[INFO] - Agent 'ProActive_CSI_Agent_404' updated successfully
```

---

## ✅ Step 4: Verify Deployment

### 4.1 List Agents
```bash
orchestrate agents list
```

**Expected:** You should see `ProActive_CSI_Agent_404` in the list

### 4.2 Verify in Portal
1. Go to: https://cloud.ibm.com/watsonx/orchestrate
2. Click: **Build** → **Agent Builder**
3. Find: **ProActive_CSI_Agent_404**
4. Click to open and verify

---

## 🎯 Step 5: Update UI Description (Optional)

The YAML description and UI description are separate fields. To update the UI:

1. Go to: https://cloud.ibm.com/watsonx/orchestrate
2. Open: **ProActive_CSI_Agent_404**
3. Click: **Profile** tab
4. Click: **Edit** on Description field
5. Copy content from: `DESCRIPTION_TO_COPY.txt`
6. Paste into Description field
7. Click: **Save**

---

## 🔄 Complete Deployment Script

Save this as `deploy.sh` for one-command deployment:

```bash
#!/bin/bash

# Configuration
API_KEY="your-api-key-here"
INSTANCE_URL="your-instance-url-here"
ENV_NAME="production-au"

echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║  🚀 Deploying ProActive CSI Agent 404                        ║"
echo "╚═══════════════════════════════════════════════════════════════╝"

# Step 1: Activate environment
echo ""
echo "📋 Step 1: Activating environment..."
orchestrate env activate --api-key "$API_KEY" "$ENV_NAME" 2>&1 | grep -E "INFO|active|ERROR"

# Step 2: Validate YAML
echo ""
echo "📋 Step 2: Validating YAML..."
python3 -c "import yaml; yaml.safe_load(open('proactive-csi-agent-orchestrate.yaml')); print('✅ YAML Valid')" || exit 1

# Step 3: Deploy agent
echo ""
echo "📋 Step 3: Deploying agent..."
orchestrate agents import -f proactive-csi-agent-orchestrate.yaml 2>&1 | grep -E "INFO|ERROR"

# Step 4: Verify
echo ""
echo "📋 Step 4: Verifying deployment..."
orchestrate agents list 2>&1 | grep -A 2 "ProActive"

echo ""
echo "✅ Deployment complete!"
echo ""
echo "🔗 Access your agent: https://cloud.ibm.com/watsonx/orchestrate"
```

**Usage:**
```bash
chmod +x deploy.sh
./deploy.sh
```

---

## 🔧 Troubleshooting

### Issue: "No active environment set"
**Solution:**
```bash
orchestrate env activate --api-key "$API_KEY" production-au
```

### Issue: "Scope not found" or "404 Error"
**Solution:**
- Verify your instance URL is correct
- Check that you're using `--type ibm_iam` (not `mcsp`)
- Verify API key has access to the instance

### Issue: "Error: Bad Request, Status code: 400"
**Solution:**
- Verify API key is correct and not expired
- Ensure API key is from watsonx Orchestrate (not general IBM Cloud API key)

### Issue: YAML validation fails
**Solution:**
```bash
python3 -c "import yaml; yaml.safe_load(open('proactive-csi-agent-orchestrate.yaml'))"
```
Check for syntax errors in the output

### Issue: Agent not appearing in portal
**Solution:**
- Wait 1-2 minutes for sync
- Hard refresh browser (Cmd+Shift+R or Ctrl+Shift+R)
- Verify you're in the correct region

---

## 📊 Current Configuration

### Environment Details
- **Environment Name:** production-au
- **Region:** au-syd (Australia Sydney)
- **Instance ID:** f16c2181-a811-4d84-8e15-33cfebe50928
- **Auth Type:** ibm_iam

### Agent Details
- **Name:** ProActive_CSI_Agent_404
- **Version:** 2.0
- **LLM:** watsonx/meta-llama/llama-3-2-90b-vision-instruct
- **Description:** 4,113 characters

### Files
- **Agent YAML:** `proactive-csi-agent-orchestrate.yaml`
- **Description Copy:** `DESCRIPTION_TO_COPY.txt`
- **Deployment Script:** `deploy.sh` (create from template above)

---

## 🎯 Quick Reference Commands

```bash
# Activate environment
orchestrate env activate --api-key "$API_KEY" production-au

# List environments
orchestrate env list

# Validate YAML
python3 -c "import yaml; yaml.safe_load(open('proactive-csi-agent-orchestrate.yaml'))"

# Deploy agent
orchestrate agents import -f proactive-csi-agent-orchestrate.yaml

# List agents
orchestrate agents list

# Remove agent (if needed)
orchestrate agents remove --name ProActive_CSI_Agent_404 --kind native
```

---

## 📝 Deployment Checklist

- [ ] API key obtained from IBM Portal
- [ ] Instance URL obtained from IBM Portal
- [ ] Environment variables set
- [ ] Environment activated
- [ ] YAML file validated
- [ ] Agent deployed successfully
- [ ] Agent verified in portal
- [ ] UI description updated (optional)

---

## 🔗 Important Links

- **IBM Portal:** https://cloud.ibm.com/watsonx/orchestrate
- **Agent Builder:** https://cloud.ibm.com/watsonx/orchestrate/build/manage
- **Repository:** https://github.com/sridharankaliyamoorthy/agent404-proactive-csi
- **Version Tag:** v2.0

---

## 📚 Additional Documentation

- `DEPLOYMENT_COMPLETE_GUIDE.md` - Detailed deployment guide
- `TEST_IN_IBM_PORTAL.md` - Testing instructions
- `DESCRIPTION_TO_COPY.txt` - UI description content
- `IBM_TEST_QUERIES.md` - Test queries for the agent

---

## ✅ Success Criteria

Deployment is successful when:
1. ✅ Agent appears in `orchestrate agents list`
2. ✅ Agent is visible in IBM Portal
3. ✅ Agent responds to test queries
4. ✅ All IBM services are connected
5. ✅ Description shows Version 2.0 (if UI updated)

---

**🎉 Ready to deploy! Follow the steps above for a successful deployment.**

**Last Updated:** November 22, 2025  
**Version:** 2.0

