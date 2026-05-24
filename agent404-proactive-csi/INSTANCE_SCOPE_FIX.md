# 🔧 Fix "Scope not found" Error

## Problem

The error shows:
```
Error: Scope not found: Scope{scopeType='SERVICE', scopeId='f16c2181-a811-4d84-8e15-33cfebe50928'}
Status code: 404
```

This means:
- ❌ The instance ID `f16c2181-a811-4d84-8e15-33cfebe50928` doesn't exist, OR
- ❌ Your API key doesn't have access to this instance

## Solution

You need to get the **correct Service instance URL** from IBM Portal.

### Step 1: Get Service Instance URL from IBM Portal

1. **Open IBM Portal:**
   ```
   https://cloud.ibm.com/watsonx/orchestrate
   ```

2. **Login with your IBM Cloud credentials**

3. **Go to Settings:**
   - Click on your instance
   - Go to **"Settings"** or **"API details"** tab
   - Find **"Service instance URL"**

4. **Copy the Service instance URL:**
   - It should look like:
   ```
   https://api.au-syd.watson-orchestrate.cloud.ibm.com/instances/XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
   ```

### Step 2: Use the Fix Script

Run the automated fix script:

```bash
cd /Users/ishwaryasridharan/Desktop/Hackathon_2025/Agentic_AI/agent404-proactive-csi
./scripts/fix_instance_scope.sh
```

This script will:
1. Ask you for the correct Service instance URL from IBM Portal
2. Ask for your IBM Cloud API key
3. Update the environment with the correct instance
4. Activate the environment
5. Deploy your agent

### Step 3: Manual Fix (Alternative)

If you prefer to do it manually:

```bash
cd /Users/ishwaryasridharan/Desktop/Hackathon_2025/Agentic_AI/agent404-proactive-csi

# Remove old environment
echo "y" | orchestrate env remove --name production-au

# Add environment with correct Service instance URL
orchestrate env add -n production-au \
  -u "YOUR_SERVICE_INSTANCE_URL_FROM_IBM_PORTAL" \
  --type mcsp_v2

# Activate with your API key
orchestrate env activate production-au
# Paste your API key when prompted

# Deploy agent
orchestrate agents import --file proactive-csi-agent-orchestrate.yaml
```

## Important Notes

1. **Get the Service instance URL from IBM Portal** - Don't use the old one!
2. **Use your IBM Cloud API key** (not the watsonx Orchestrate API key)
3. **Make sure the instance exists** - Check in IBM Portal first

## Where to Find Service Instance URL

1. Go to: https://cloud.ibm.com/watsonx/orchestrate
2. Click on your instance
3. Go to **Settings** → **API details**
4. Copy the **Service instance URL**

## Alternative: Use Web UI Deployment

If CLI continues to have issues, use the Web UI:

1. Open: https://cloud.ibm.com/watsonx/orchestrate
2. Find your agent or create a new one
3. Click "Edit"
4. Click "Import from file"
5. Upload: `proactive-csi-agent-orchestrate.yaml`
6. Click "Save" → "Activate"

---

**Quick Fix Command:**
```bash
./scripts/fix_instance_scope.sh
```

This will guide you through getting the correct instance URL and deploying!

