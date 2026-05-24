# 🚀 IBM watsonx Orchestrate Deployment Guide

**Complete step-by-step guide for deploying ProActive CSI Agent 404 to IBM watsonx Orchestrate**

---

## 📋 Prerequisites

Before deploying, ensure you have:

- ✅ IBM Cloud account
- ✅ IBM watsonx Orchestrate CLI installed (`orchestrate-cli`)
- ✅ Access to Australia Sydney (AU) region instance
- ✅ API key and Service URL for Orchestrate
- ✅ All IBM service credentials (NLU, STT, TTS, Cloudant)

---

## 🔑 Credentials Required

### 1. IBM watsonx Orchestrate (AU-Sydney)

**Credentials File:** `ibm-credentials_Orchestrate_data_Updated.json`

```json
{
  "watsonx_orchestrate": {
    "api_key": "9-atsNvf8mx0ymZLaGgZwe28rhyZvLcX_QUQlyDb12rg",
    "service_url": "https://api.au-syd.watson-orchestrate.cloud.ibm.com/instances/f16c2181-a811-4d84-8e15-33cfebe50928"
  }
}
```

**Web UI:** https://au-syd.watson-orchestrate.cloud.ibm.com/build/manage

---

### 2. IBM Natural Language Understanding (NLU)

**Credentials File:** `ibm-credentials_NLU.env`

```
NATURAL_LANGUAGE_UNDERSTANDING_APIKEY=JD1cdPcLQdymkID4sHav18lDXLd7U1FrTKDB2yllVLar
NATURAL_LANGUAGE_UNDERSTANDING_URL=https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/79459c2d-4e21-4593-963e-6e9964afe1a3
```

---

### 3. IBM Speech-to-Text (STT)

**Credentials File:** `ibm-credentials_STT.env`

```
SPEECH_TO_TEXT_APIKEY=qzNRq16Io8Dap9VR57CMw5jvbH3LUIWEQTEv20hJ-tc1
SPEECH_TO_TEXT_URL=https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/ffcdbb0a-ca7b-4361-838b-cc8b6e4ac34c
```

---

### 4. IBM Text-to-Speech (TTS)

**Credentials File:** `ibm-credentials_TTS.env`

```
TEXT_TO_SPEECH_APIKEY=FLukjnaT1rf9qFnAhVbpi5D7HPMrvUst9POK8A-JShpz
TEXT_TO_SPEECH_URL=https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/298e2b63-de83-427c-b97d-156c0976eed7
```

**Important:** Instance ID must be `b97d` (not `b77d`)

---

### 5. IBM Cloudant

**Credentials File:** `ibm-credentials_Cloudant_data.json`

```json
{
  "apikey": "TalYEKH8YIFL1Hqu0Gx4QZP6IBE-43s8Cl2Fm7a-CyBK",
  "url": "https://f01bbce3-de41-430e-bd9b-5c00a082588a-bluemix.cloudantnosqldb.appdomain.cloud"
}
```

---

## 🚀 Deployment Steps

### Step 1: Navigate to Project Directory

```bash
cd /Users/ishwaryasridharan/Desktop/Hackathon_2025/Agentic_AI/agent404-proactive-csi
```

---

### Step 2: Verify Agent Configuration File

**File:** `proactive-csi-agent-orchestrate.yaml`

**Verify these settings:**
- ✅ `spec_version: v1`
- ✅ `kind: native`
- ✅ `name: ProActive_CSI_Agent_404`
- ✅ `llm: watsonx/meta-llama/llama-3-2-90b-vision-instruct` (with `watsonx/` prefix)

**Check the file exists:**
```bash
ls -la proactive-csi-agent-orchestrate.yaml
```

---

### Step 3: Check Orchestrate CLI Installation

```bash
orchestrate --version
```

If not installed:
```bash
pip install watsonx-orchestrate-cli
```

---

### Step 4: Activate AU Environment

**Important:** Use default authentication (NOT `--type mcsp`)

```bash
# Activate environment (will prompt for API key)
orchestrate env activate production-au

# When prompted, enter this API key:
9-atsNvf8mx0ymZLaGgZwe28rhyZvLcX_QUQlyDb12rg
```

**Expected output:**
```
[INFO] - Environment 'production-au' is now active
```

**Troubleshooting:**
- ❌ If you see "Scope not found" - Don't use `--type mcsp` flag
- ✅ Use default authentication (no `--type` flag)
- ✅ Use the API key: `9-atsNvf8mx0ymZLaGgZwe28rhyZvLcX_QUQlyDb12rg`

---

### Step 5: Verify Environment Configuration

**Check if environment exists:**
```bash
orchestrate env list
```

**Expected output:**
```
production-au  https://api.au-syd.watson-orchestrate.cloud.ibm.com/…  (active)
```

**If environment doesn't exist, add it:**
```bash
# Add environment (use default authentication, NO --type mcsp)
orchestrate env add -n production-au -u "https://api.au-syd.watson-orchestrate.cloud.ibm.com/instances/f16c2181-a811-4d84-8e15-33cfebe50928"

# Then activate it
orchestrate env activate production-au
# Enter API key when prompted: 9-atsNvf8mx0ymZLaGgZwe28rhyZvLcX_QUQlyDb12rg
```

---

### Step 6: Deploy Agent

**Deploy the agent:**
```bash
orchestrate agents import -f proactive-csi-agent-orchestrate.yaml
```

**Expected output:**
```
[INFO] - Existing Agent 'ProActive_CSI_Agent_404' found. Updating...
[INFO] - Agent 'ProActive_CSI_Agent_404' updated successfully
```

**Or if first time:**
```
[INFO] - Agent 'ProActive_CSI_Agent_404' imported successfully
```

---

### Step 7: Verify Deployment

**List agents:**
```bash
orchestrate agents list
```

**Expected output:**
```
│ ProActive_CSI_Agent_404 │ Enterprise Revenue & Risk Intelligence Agent │ watsonx/meta-llama/... │
```

**Check specific agent:**
```bash
orchestrate agents list | grep -i "proactive"
```

---

### Step 8: Access Agent in Web UI

1. **Open browser:**
   ```
   https://au-syd.watson-orchestrate.cloud.ibm.com/build/manage
   ```

2. **Navigate:**
   - Click "All agents" in left sidebar
   - Find "ProActive_CSI_Agent_404"
   - Click on the agent card

3. **Test agent:**
   - Try: `"What's my priority today?"`
   - Try: `"Show me critical customers at risk"`
   - Try: `"Generate daily executive brief"`

---

## 🔄 Quick Deployment Script

**Save this script:** `scripts/deployment/quick_deploy.sh`

```bash
#!/bin/bash

# Quick deployment script for ProActive CSI Agent 404

echo "╔═══════════════════════════════════════════════════════════════════════════╗"
echo "║  Deploying ProActive CSI Agent to Australia Sydney Environment           ║"
echo "╚═══════════════════════════════════════════════════════════════════════════╝"
echo ""

cd /Users/ishwaryasridharan/Desktop/Hackathon_2025/Agentic_AI/agent404-proactive-csi

# Step 1: Activate environment
echo "📍 Step 1: Activating production-au environment..."
echo "   Enter API key when prompted: 9-atsNvf8mx0ymZLaGgZwe28rhyZvLcX_QUQlyDb12rg"
echo ""
orchestrate env activate production-au

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Environment activated!"
    echo ""
    
    # Step 2: Deploy agent
    echo "📍 Step 2: Importing agent..."
    orchestrate agents import -f proactive-csi-agent-orchestrate.yaml
    
    if [ $? -eq 0 ]; then
        echo ""
        echo "✅ Agent deployed successfully!"
        echo ""
        echo "📍 Step 3: Verifying deployment..."
        orchestrate agents list | grep -i "proactive" | head -3
        echo ""
        echo "🎉 DONE! Your agent is now live!"
        echo ""
        echo "🌐 Access your agent at:"
        echo "   https://au-syd.watson-orchestrate.cloud.ibm.com/build/manage"
    else
        echo "❌ Agent import failed"
        exit 1
    fi
else
    echo "❌ Environment activation failed"
    exit 1
fi
```

**Make it executable:**
```bash
chmod +x scripts/deployment/quick_deploy.sh
```

**Run it:**
```bash
./scripts/deployment/quick_deploy.sh
```

---

## 🐛 Troubleshooting

### Issue: "Scope not found" or "Unauthorized"

**Cause:** Wrong authentication type or incorrect credentials

**Solution:**
1. ✅ DON'T use `--type mcsp` flag
2. ✅ Use default authentication (no `--type` flag)
3. ✅ Verify API key: `9-atsNvf8mx0ymZLaGgZwe28rhyZvLcX_QUQlyDb12rg`
4. ✅ Verify Service URL includes full instance ID

**Correct command:**
```bash
orchestrate env add -n production-au -u "https://api.au-syd.watson-orchestrate.cloud.ibm.com/instances/f16c2181-a811-4d84-8e15-33cfebe50928"
```

**Wrong command:**
```bash
orchestrate env add -n production-au -u "..." --type mcsp  # ❌ DON'T USE THIS
```

---

### Issue: "Field 'spec_version' not provided"

**Cause:** YAML file missing required fields

**Solution:**
Check `proactive-csi-agent-orchestrate.yaml` has:
```yaml
spec_version: v1
kind: native
name: ProActive_CSI_Agent_404
llm: watsonx/meta-llama/llama-3-2-90b-vision-instruct
```

**Important:** `llm` must include `watsonx/` prefix!

---

### Issue: "Invalid 'provider' value"

**Cause:** LLM model missing `watsonx/` prefix

**Solution:**
Change from:
```yaml
llm: meta-llama/llama-3-2-90b-vision-instruct  # ❌ WRONG
```

To:
```yaml
llm: watsonx/meta-llama/llama-3-2-90b-vision-instruct  # ✅ CORRECT
```

---

### Issue: Agent not appearing in web UI

**Possible causes:**
1. Deployed to wrong environment
2. Browser cache - refresh page (Cmd+Shift+R / Ctrl+Shift+R)
3. Check correct URL: https://au-syd.watson-orchestrate.cloud.ibm.com/build/manage

**Solution:**
1. Verify environment: `orchestrate env list`
2. Verify agent: `orchestrate agents list | grep proactive`
3. Hard refresh browser
4. Check correct region URL

---

### Issue: "Error getting IBM_IAM Token"

**Cause:** Invalid API key

**Solution:**
1. Verify API key: `9-atsNvf8mx0ymZLaGgZwe28rhyZvLcX_QUQlyDb12rg`
2. Check if API key has expired
3. Get new API key from IBM Cloud console

---

## 📋 Deployment Checklist

Use this checklist before deploying:

- [ ] Verify `proactive-csi-agent-orchestrate.yaml` exists
- [ ] Check `spec_version: v1` and `kind: native` in YAML
- [ ] Verify `llm: watsonx/meta-llama/llama-3-2-90b-vision-instruct` (with `watsonx/` prefix)
- [ ] Confirm API key: `9-atsNvf8mx0ymZLaGgZwe28rhyZvLcX_QUQlyDb12rg`
- [ ] Confirm Service URL with correct instance ID: `f16c2181-a811-4d84-8e15-33cfebe50928`
- [ ] Install/verify `orchestrate-cli` is installed
- [ ] Activate `production-au` environment
- [ ] Run `orchestrate agents import -f proactive-csi-agent-orchestrate.yaml`
- [ ] Verify agent in web UI: https://au-syd.watson-orchestrate.cloud.ibm.com/build/manage
- [ ] Test agent with a query

---

## 🔄 Re-deployment (Updates)

When updating the agent:

```bash
# 1. Make changes to proactive-csi-agent-orchestrate.yaml

# 2. Activate environment
orchestrate env activate production-au
# Enter API key when prompted

# 3. Re-deploy (will update existing agent)
orchestrate agents import -f proactive-csi-agent-orchestrate.yaml

# 4. Verify
orchestrate agents list | grep proactive

# 5. Test in web UI (refresh browser)
```

---

## 📊 Deployment Summary

**Environment:** `production-au` (Australia Sydney)  
**Service URL:** `https://api.au-syd.watson-orchestrate.cloud.ibm.com/instances/f16c2181-a811-4d84-8e15-33cfebe50928`  
**API Key:** `9-atsNvf8mx0ymZLaGgZwe28rhyZvLcX_QUQlyDb12rg`  
**Web UI:** https://au-syd.watson-orchestrate.cloud.ibm.com/build/manage  
**Agent Name:** `ProActive_CSI_Agent_404`  
**LLM Model:** `watsonx/meta-llama/llama-3-2-90b-vision-instruct`  

**Authentication:** Default IBM IAM (NOT `mcsp` type)

---

## 📝 Key Learnings

1. ✅ **Don't use `--type mcsp`** - Use default authentication
2. ✅ **LLM must include `watsonx/` prefix** - `watsonx/meta-llama/...`
3. ✅ **YAML must have `spec_version: v1` and `kind: native`**
4. ✅ **TTS instance ID:** Must be `b97d` (not `b77d`)
5. ✅ **Hard refresh browser** after deployment changes

---

## 🆘 Support

If you encounter issues:

1. Check this guide's troubleshooting section
2. Verify credentials match exactly
3. Check `orchestrate env list` for correct environment
4. Verify agent exists: `orchestrate agents list`
5. Check logs in IBM Cloud console

---

## ✅ Success Indicators

You'll know deployment is successful when:

- ✅ `orchestrate agents import` returns: `"Agent 'ProActive_CSI_Agent_404' imported successfully"`
- ✅ Agent appears in web UI at: https://au-syd.watson-orchestrate.cloud.ibm.com/build/manage
- ✅ Agent responds to test queries
- ✅ Agent mentions IBM Watson services in responses

---

**Last Updated:** 2025-01-XX  
**Version:** 1.0.0  
**Status:** ✅ Tested and Working

