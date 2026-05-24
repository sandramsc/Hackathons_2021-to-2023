# 🚀 COMPLETE DEPLOYMENT GUIDE - Follow These Steps

**Status:** ✅ All files ready, proceed with deployment

---

## 📋 PRE-DEPLOYMENT CHECKLIST

✅ Agent configuration file: `proactive-csi-agent-orchestrate.yaml` (20KB)  
✅ YAML syntax: Valid  
✅ Data files: 2,993 records across 6 CSV files  
✅ IBM Services: All 6 services configured  
✅ Documentation: Complete  

---

## 🎯 STEP-BY-STEP DEPLOYMENT

### Step 1: Login to IBM Cloud

1. **Open browser** (already opened to login page)
2. **Enter your IBM Cloud credentials**
3. **Complete 2FA** if required
4. **Wait for redirect** to Orchestrate portal

**URL:** https://cloud.ibm.com/login

---

### Step 2: Navigate to watsonx Orchestrate

After login, you should be redirected to:
```
https://au-syd.watson-orchestrate.cloud.ibm.com/build/manage
```

If not, manually navigate to:
- Click **"watsonx"** in the top menu
- Select **"Orchestrate"** from the dropdown
- Or go directly to: https://cloud.ibm.com/watsonx/orchestrate

---

### Step 3: Find Agents Section

Look for one of these in the left sidebar:
- **"All agents"**
- **"Skills"**
- **"Agents"**
- **"Custom skills"**

Click on it.

---

### Step 4: Import Agent Configuration

1. **Click "Create agent"** or **"Import agent"** button
2. **Select "Import from file"** option
3. **Click "Upload"** or **"Choose file"**
4. **Navigate to this file:**
   ```
   /Users/ishwaryasridharan/Desktop/Hackathon_2025/Agentic_AI/agent404-proactive-csi/proactive-csi-agent-orchestrate.yaml
   ```
5. **Select the file** and click **"Open"**
6. **Wait for upload** (5-10 seconds)

**Expected Result:**
- Agent name: **ProActive_CSI_Agent_404**
- Configuration loaded successfully
- All instructions visible

---

### Step 5: Connect IBM Services

Go to **"Connections"**, **"Integrations"**, or **"Services"** tab:

#### Service 1: Speech-to-Text (STT)
- **Click "Add Connection"** or **"Connect Service"**
- **Service:** Speech-to-Text
- **API Key:** `qzNRq16Io8Dap9VR57CMw5jvbH3LUIWEQTEv20hJ-tc1`
- **URL:** `https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/ffcdbb0a-ca7b-4361-838b-cc8b6e4ac34c`
- **Click "Connect"** or **"Save"**

#### Service 2: Text-to-Speech (TTS)
- **Click "Add Connection"**
- **Service:** Text-to-Speech
- **API Key:** `FLukjnaT1rf9qFnAhVbpi5D7HPMrvUst9POK8A-JShpz`
- **URL:** `https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/298e2b63-de83-427c-b97d-156c0976eed7`
- **Click "Connect"**

#### Service 3: Natural Language Understanding (NLU)
- **Click "Add Connection"**
- **Service:** Natural Language Understanding
- **API Key:** `JD1cdPcLQdymkID4sHav18lDXLd7U1FrTKDB2yllVLar`
- **URL:** `https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/79459c2d-4e21-4593-963e-6e9964afe1a3`
- **Click "Connect"**

#### Service 4: watsonx.ai
- **Click "Add Connection"**
- **Service:** watsonx.ai
- **Project ID:** `aa39fafa-2f20-47a3-b6d5-a84ff6cefa0e`
- **Region:** us-south
- **Click "Connect"**

**Expected Result:**
- All 4 services show ✅ **Connected** or green status
- No error messages

---

### Step 6: Save Agent Configuration

1. **Click "Save"** button (usually top-right)
2. **Wait for confirmation** message
3. **Verify** no errors appear

---

### Step 7: Activate/Deploy Agent

1. **Click "Activate"** or **"Publish"** button
2. **Wait 10-30 seconds** for activation
3. **Check status** - should show:
   - ✅ **Active**
   - ✅ **Deployed**
   - ✅ **Published**

**Expected Result:**
- Agent status: **Active/Deployed**
- All services: **Connected** (green indicators)
- No error messages

---

### Step 8: Get Deployment URL

1. **Look for one of these buttons:**
   - **"Share"**
   - **"Chat URL"**
   - **"Test URL"**
   - **"Deployment URL"**
   - **"Copy Link"**

2. **Click the button** to get the URL

3. **Copy the URL** - this is your **Application URL** for submission

**Expected Format:**
```
https://au-syd.watson-orchestrate.cloud.ibm.com/[agent-path]
```

**Save this URL!** You'll need it for submission.

---

### Step 9: Test the Agent

Click on your agent to open the chat interface, then test with these queries:

#### Test 1: Basic Functionality
```
Query: "Good morning, what's my priority today?"
```
**Expected:** Structured priority briefing with categorized tasks

#### Test 2: Customer Intelligence
```
Query: "Tell me about Acme Corporation"
```
**Expected:** Customer health score, churn risk, activity summary

#### Test 3: Voice Operations (TTS)
```
Query: "Read me the executive briefing aloud using Text-to-Speech"
```
**Expected:** Mentions TTS, provides executive briefing content

#### Test 4: Procurement Intelligence
```
Query: "What vendors have delays?"
```
**Expected:** List of vendors with delays, customer impact analysis

#### Test 5: Revenue Protection
```
Query: "Calculate revenue at risk"
```
**Expected:** ARR/MRR calculations, financial scenarios, CFO briefing

---

## ✅ SUCCESS CRITERIA

Deployment is successful when:

✅ Agent is **Active/Deployed** in IBM Portal  
✅ All services show **Connected** (green status)  
✅ Agent responds to test queries correctly  
✅ Deployment URL is accessible  
✅ All 5 test queries return expected responses  

---

## 📸 PROOF TO CAPTURE

Take screenshots of:

1. **Agent Overview Page**
   - Agent name: "ProActive_CSI_Agent_404"
   - Status: Active/Deployed
   - All services connected (green indicators)

2. **Service Connections**
   - STT: ✅ Connected
   - TTS: ✅ Connected
   - NLU: ✅ Connected
   - watsonx.ai: ✅ Connected

3. **Test Query Results**
   - At least 3 successful test queries
   - Agent responses showing correct functionality

4. **Deployment URL**
   - Copy the full URL
   - Verify it's accessible

---

## 📝 DEPLOYMENT DETAILS TO RECORD

After successful deployment, record:

- **Agent Name:** ProActive_CSI_Agent_404
- **Deployment Status:** Active/Deployed
- **Deployment URL:** `[PASTE URL HERE]`
- **All Services:** Connected (STT, TTS, NLU, watsonx.ai)
- **Test Results:** All 5 queries successful
- **Date/Time:** `[RECORD DATE/TIME]`

---

## 🚨 TROUBLESHOOTING

### Issue: Can't find "All agents" or "Skills"
**Solution:**
- Look for "Apps", "Custom skills", or "Builder" in sidebar
- Try clicking "watsonx" → "Orchestrate" → "Agents"

### Issue: Upload failed
**Solution:**
- Check file is `proactive-csi-agent-orchestrate.yaml`
- File size should be 20KB
- Verify YAML syntax is valid
- Try refreshing the page

### Issue: Services not connecting
**Solution:**
- Double-check API keys (no extra spaces)
- Verify URLs are complete
- Try reconnecting each service
- Check service instances are active in IBM Cloud

### Issue: Agent not responding
**Solution:**
- Make sure agent is "Active" or "Published"
- Check service connections are green/active
- Try simple command first: "Hello"
- Verify YAML file is valid

### Issue: Can't find deployment URL
**Solution:**
- Look for "Share" or "Test" button
- Check agent details page
- Look in "Settings" or "Deployment" section
- Try clicking on the agent name to open details

---

## 📋 QUICK REFERENCE

**File to Upload:**
```
/Users/ishwaryasridharan/Desktop/Hackathon_2025/Agentic_AI/agent404-proactive-csi/proactive-csi-agent-orchestrate.yaml
```

**Portal URLs:**
- Main: https://cloud.ibm.com/watsonx/orchestrate
- Direct: https://au-syd.watson-orchestrate.cloud.ibm.com/build/manage

**Service API Keys:**
- STT: `qzNRq16Io8Dap9VR57CMw5jvbH3LUIWEQTEv20hJ-tc1`
- TTS: `FLukjnaT1rf9qFnAhVbpi5D7HPMrvUst9POK8A-JShpz`
- NLU: `JD1cdPcLQdymkID4sHav18lDXLd7U1FrTKDB2yllVLar`
- watsonx.ai Project ID: `aa39fafa-2f20-47a3-b6d5-a84ff6cefa0e`

---

## 🎉 YOU'RE READY!

All files are verified and ready. Follow the steps above to deploy.

**Estimated Time:** 15-30 minutes  
**Confidence:** High - All components verified ✅

---

**Last Updated:** November 22, 2025  
**Status:** Ready for Deployment 🚀

