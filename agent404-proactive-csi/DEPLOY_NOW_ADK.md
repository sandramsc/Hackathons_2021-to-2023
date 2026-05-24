# 🚀 Deploy Now - Using ADK (Official Method)

## Quick Deploy Command

Run this single command to deploy (you'll be prompted for API key):

```bash
cd /Users/ishwaryasridharan/Desktop/Hackathon_2025/Agentic_AI/agent404-proactive-csi
./deploy_with_adk.sh
```

## Or Deploy Manually (Step by Step)

### Step 1: Get API Key from watsonx Orchestrate

1. **Go to:** https://cloud.ibm.com/watsonx/orchestrate
2. **Click:** Profile icon (top-right) → **Settings**
3. **Go to:** **API details** tab
4. **Click:** **Generate API key** button
5. **Copy** the API key (save it - you won't see it again!)

### Step 2: Setup Environment

```bash
cd /Users/ishwaryasridharan/Desktop/Hackathon_2025/Agentic_AI/agent404-proactive-csi

# Remove old environment
echo "y" | orchestrate env remove --name production-au 2>/dev/null || true

# Add environment with mcsp type (as per IBM docs)
orchestrate env add -n production-au \
  -u "https://api.au-syd.watson-orchestrate.cloud.ibm.com/instances/f16c2181-a811-4d84-8e15-33cfebe50928" \
  --type mcsp

# Activate environment (paste your API key when prompted)
orchestrate env activate production-au
# Paste your API key from Step 1
```

### Step 3: Deploy Agent

```bash
# Deploy the agent
orchestrate agents import -f proactive-csi-agent-orchestrate.yaml
```

### Step 4: Verify Deployment

```bash
# List agents to verify
orchestrate agents list
```

You should see: **ProActive_CSI_Agent_404**

## ✅ Success!

After deployment:

1. **Go to:** https://cloud.ibm.com/watsonx/orchestrate
2. **Click:** Build → **Agent Builder**
3. **Find:** **ProActive_CSI_Agent_404**
4. **Click** to open and test

## 🧪 Test Your Agent

In the Agent Builder test chat, try:

```
Good morning, what's my priority today?
```

```
Tell me about Acme Corporation
```

```
What vendors have delays?
```

## 📋 Important Notes

- **API Key:** Must be from watsonx Orchestrate Settings (not IBM Cloud API key)
- **Type:** Use `mcsp` type (as per IBM documentation)
- **File:** `proactive-csi-agent-orchestrate.yaml` (20KB, ready)

---

**Status:** ✅ Ready to deploy  
**Method:** IBM watsonx Orchestrate ADK (Official)  
**File:** `deploy_with_adk.sh` or follow steps above

