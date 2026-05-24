# 🔧 Create watsonx Orchestrate Instance

## Problem

The instance ID `f16c2181-a811-4d84-8e15-33cfebe50928` doesn't exist (404 error).

## Solution: Create New Instance

### Step 1: Go to IBM Cloud Catalog

1. **Open:** https://cloud.ibm.com/catalog/services/watsonx-orchestrate
2. **Or search:** "watsonx Orchestrate" in IBM Cloud catalog

### Step 2: Create Instance

1. **Click:** "Create" or "Get started" button
2. **Fill in:**
   - **Service name:** ProActive-CSI (or any name)
   - **Region:** Choose a region (e.g., Australia Sydney, US South)
   - **Resource group:** Default (or your preferred group)
3. **Click:** "Create" button
4. **Wait** for instance to be created (1-2 minutes)

### Step 3: Get Instance URL

1. **Go to:** https://cloud.ibm.com/watsonx/orchestrate
2. **Click** on your newly created instance
3. **Click:** Settings (gear icon) → **API details** tab
4. **Copy** the "Service instance URL"
   - Format: `https://api.[region].watson-orchestrate.cloud.ibm.com/instances/[new-id]`

### Step 4: Deploy Agent

```bash
cd /Users/ishwaryasridharan/Desktop/Hackathon_2025/Agentic_AI/agent404-proactive-csi
./deploy_final.sh
```

When prompted, paste the new instance URL.

## Alternative: Check Existing Instances

If you think you have an instance:

1. **Go to:** https://cloud.ibm.com/resources
2. **Filter by:** "watsonx Orchestrate"
3. **Click** on any instance you see
4. **Get URL** from Settings → API details

---

**Status:** Need to create instance or find existing one  
**API Key:** Ready (`f4493b99-f0b5-47ff-b80c-51b437c02f30`)  
**Agent File:** Ready (`proactive-csi-agent-orchestrate.yaml`)

