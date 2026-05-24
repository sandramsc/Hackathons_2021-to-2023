# 🔧 Fix API Key Issue

## Problem

The error shows:
```
Error: Provided API key could not be found., Status code: 400
Error getting IBM_IAM Token
```

This means the API key in your credentials file is invalid or expired.

## Solution

### Option 1: Use the Fix Script (Recommended)

Run the automated fix script:

```bash
cd /Users/ishwaryasridharan/Desktop/Hackathon_2025/Agentic_AI/agent404-proactive-csi
./scripts/fix_api_key.sh
```

This script will:
1. Guide you to get a valid IBM Cloud API key
2. Update the environment configuration
3. Activate the environment with the new API key
4. Update the credentials file
5. Deploy the agent

### Option 2: Manual Fix

#### Step 1: Get IBM Cloud API Key

1. Go to: **https://cloud.ibm.com/iam/apikeys**
2. Click **"Create an IBM Cloud API key"**
3. Name it: `watsonx-orchestrate-api-key`
4. **Copy the API key** (you'll only see it once!)

#### Step 2: Update Environment

```bash
cd /Users/ishwaryasridharan/Desktop/Hackathon_2025/Agentic_AI/agent404-proactive-csi

# Remove old environment
echo "y" | orchestrate env remove --name production-au

# Add environment with correct type
orchestrate env add -n production-au \
  -u "https://api.au-syd.watson-orchestrate.cloud.ibm.com/instances/f16c2181-a811-4d84-8e15-33cfebe50928" \
  --type mcsp_v2
```

#### Step 3: Activate Environment

```bash
# Activate with your API key
orchestrate env activate production-au
# Paste your API key when prompted
```

#### Step 4: Update Credentials File

Edit `../ibm-credentials_Orchestrate_data_Updated.json`:

```json
{
  "watsonx_orchestrate": {
    "api_key": "YOUR_VALID_IBM_CLOUD_API_KEY_HERE",
    "service_url": "https://api.au-syd.watson-orchestrate.cloud.ibm.com/instances/f16c2181-a811-4d84-8e15-33cfebe50928"
  }
}
```

#### Step 5: Deploy Agent

```bash
orchestrate agents import --file proactive-csi-agent-orchestrate.yaml
```

## What Changed

1. ✅ **Updated credentials file** with placeholder API key
2. ✅ **Created fix script** (`scripts/fix_api_key.sh`)
3. ✅ **Documented the fix process**

## Next Steps

1. **Get a valid IBM Cloud API key** from https://cloud.ibm.com/iam/apikeys
2. **Run the fix script** or follow the manual steps
3. **Deploy your agent** once authenticated

---

**Quick Command:**
```bash
./scripts/fix_api_key.sh
```

This will guide you through the entire process!

