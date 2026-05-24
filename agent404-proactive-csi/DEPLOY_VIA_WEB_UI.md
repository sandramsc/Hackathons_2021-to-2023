# 🚀 Deploy via Web UI - Recommended Method

## Why Web UI?

The CLI authentication is having issues with API keys. **Web UI deployment is easier and more reliable!**

## Quick Steps (5 Minutes)

### Step 1: Open IBM Portal

**Open this URL:**
```
https://cloud.ibm.com/watsonx/orchestrate
```

Or direct link:
```
https://au-syd.watson-orchestrate.cloud.ibm.com/build/manage
```

**Login with your IBM Cloud credentials**

---

### Step 2: Find Your Agent (or Create New)

1. **In the left sidebar**, click **"All agents"** or **"Skills"**
2. **Look for:** "ProActive_CSI_Agent_404"
   - If found: Click on it, then click **"Edit"**
   - If not found: Click **"Create agent"** or **"Import agent"**

---

### Step 3: Upload Configuration File

1. **Click "Edit"** (if agent exists) or **"Import from file"** (if new)
2. **Click "Upload"** or **"Import from file"**
3. **Navigate to this folder:**
   ```
   /Users/ishwaryasridharan/Desktop/Hackathon_2025/Agentic_AI/agent404-proactive-csi/
   ```
4. **Select this file:**
   ```
   proactive-csi-agent-orchestrate.yaml
   ```
5. **Click "Open"** or **"Upload"**
6. **Wait for upload** (5-10 seconds)

---

### Step 4: Verify Services are Connected

1. **Go to "Connections"** or **"Integrations"** tab
2. **Verify these services are connected** (should show green/active):

   ✅ **Speech-to-Text (STT)**
   - API Key: `qzNRq16Io8Dap9VR57CMw5jvbH3LUIWEQTEv20hJ-tc1`
   - URL: `https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/ffcdbb0a-ca7b-4361-838b-cc8b6e4ac34c`

   ✅ **Text-to-Speech (TTS)**
   - API Key: `FLukjnaT1rf9qFnAhVbpi5D7HPMrvUst9POK8A-JShpz`
   - URL: `https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/298e2b63-de83-427c-b77d-156c0976eed7`

   ✅ **Natural Language Understanding (NLU)**
   - API Key: `JD1cdPcLQdymkID4sHav18lDXLd7U1FrTKDB2yllVLar`
   - URL: `https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/79459c2d-4e21-4593-963e-6e9964afe1a3`

3. **If NOT connected**, click **"Add Connection"** and add them

---

### Step 5: Save and Activate

1. **Click "Save"** button (wait for confirmation)
2. **Click "Activate"** or **"Publish"** button
3. **Wait for activation** (10-30 seconds)
4. **Status should show:** ✅ **Active** or ✅ **Deployed**

---

### Step 6: Test STT/TTS

1. **Click on your agent** to open chat interface
2. **Type this test query:**
   ```
   "Read me the executive briefing aloud using Text-to-Speech"
   ```
3. **Expected response should mention:**
   - ✅ "IBM Text-to-Speech"
   - ✅ "POST /v1/synthesize"
   - ✅ "en-US_MichaelV3Voice"
   - ✅ Executive briefing content

---

## Configuration File Details

**File:** `proactive-csi-agent-orchestrate.yaml`  
**Location:** `/Users/ishwaryasridharan/Desktop/Hackathon_2025/Agentic_AI/agent404-proactive-csi/`  
**Version:** 1.2.0 (with STT & TTS integration)  
**Size:** 19KB  
**Status:** ✅ Ready

---

## Test Queries After Deployment

### Test 1: TTS
```
"Read me the executive briefing aloud using Text-to-Speech"
```

### Test 2: STT
```
"I'm driving, what's my priority today? Process via voice command."
```

### Test 3: Combined
```
"Using voice commands, give me a voice briefing on vendor delays"
```

---

## Troubleshooting

### Issue: Can't find "All agents" or "Skills"
**Solution:** Look for "Apps", "Custom skills", or "Builder" in the sidebar

### Issue: Upload failed
**Solution:**
- Check file is `proactive-csi-agent-orchestrate.yaml`
- File size should be < 100KB
- YAML syntax is valid

### Issue: Services not connecting
**Solution:**
- Double-check API keys (no extra spaces)
- Verify URLs are complete
- Try reconnecting each service

### Issue: Agent not responding
**Solution:**
- Make sure agent is "Active" or "Published"
- Check service connections are green/active
- Try simple command first: "Hello"

---

## Success Indicators

After successful deployment, you should see:

✅ **Agent Active:** ProActive_CSI_Agent_404 visible and active  
✅ **Services Connected:** STT, TTS, NLU all connected (green status)  
✅ **Test Queries Work:** Agent responds correctly  
✅ **STT/TTS Working:** Agent mentions STT/TTS in voice-related queries  

---

## Quick Access URLs

- **IBM Portal:** https://cloud.ibm.com/watsonx/orchestrate
- **Direct Portal:** https://au-syd.watson-orchestrate.cloud.ibm.com/build/manage
- **Config File:** `/Users/ishwaryasridharan/Desktop/Hackathon_2025/Agentic_AI/agent404-proactive-csi/proactive-csi-agent-orchestrate.yaml`

---

**✅ This method is more reliable than CLI! Use the Web UI to deploy!** 🚀

