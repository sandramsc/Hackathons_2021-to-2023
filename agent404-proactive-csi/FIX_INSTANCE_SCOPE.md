# 🔧 Fix Instance Scope Error

## Problem

The error shows:
```
Error: Scope not found: Scope{scopeType='SERVICE', scopeId='f16c2181-a811-4d84-8e15-33cfebe50928'}
Status code: 404
```

This means the instance ID doesn't exist or the API key doesn't have access to it.

## Solution: Get Correct Instance URL

### Step 1: Get Instance URL from IBM Portal

1. **Go to:** https://cloud.ibm.com/watsonx/orchestrate
2. **Login** with your IBM Cloud credentials
3. **Click on your instance** (or create a new one if needed)
4. **Go to:** Settings → **API details**
5. **Copy the EXACT Service instance URL**

The URL should look like:
```
https://api.au-syd.watson-orchestrate.cloud.ibm.com/instances/[YOUR-INSTANCE-ID]
```

### Step 2: Update Environment

```bash
cd /Users/ishwaryasridharan/Desktop/Hackathon_2025/Agentic_AI/agent404-proactive-csi

# Remove old environment
echo "y" | orchestrate env remove --name production-au

# Add with correct instance URL
orchestrate env add -n production-au \
  -u "https://api.au-syd.watson-orchestrate.cloud.ibm.com/instances/[YOUR-INSTANCE-ID]" \
  --type mcsp

# Activate with API key
orchestrate env activate production-au
# Paste: OhBxVuewV9Mz0HYlQVl3ZqeHHprOJ5xONqn77CbDF8xK
```

### Step 3: Deploy Agent

```bash
orchestrate agents import -f proactive-csi-agent-orchestrate.yaml
```

## Alternative: Use Production Environment

If you have a `production` environment already set up:

```bash
# Activate production environment
echo "OhBxVuewV9Mz0HYlQVl3ZqeHHprOJ5xONqn77CbDF8xK" | orchestrate env activate production

# Deploy agent
orchestrate agents import -f proactive-csi-agent-orchestrate.yaml
```

## Quick Fix Script

Run this after getting your correct instance URL:

```bash
cd /Users/ishwaryasridharan/Desktop/Hackathon_2025/Agentic_AI/agent404-proactive-csi

# Replace [YOUR-INSTANCE-ID] with the ID from IBM Portal
INSTANCE_ID="[YOUR-INSTANCE-ID]"
API_KEY="OhBxVuewV9Mz0HYlQVl3ZqeHHprOJ5xONqn77CbDF8xK"

# Remove old
echo "y" | orchestrate env remove --name production-au 2>/dev/null || true

# Add new
orchestrate env add -n production-au \
  -u "https://api.au-syd.watson-orchestrate.cloud.ibm.com/instances/${INSTANCE_ID}" \
  --type mcsp

# Activate
echo "$API_KEY" | orchestrate env activate production-au

# Deploy
orchestrate agents import -f proactive-csi-agent-orchestrate.yaml
```

---

**Next Step:** Get the correct instance URL from IBM Portal and update the environment.

