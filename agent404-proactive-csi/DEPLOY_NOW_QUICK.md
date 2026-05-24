# 🚀 DEPLOY NOW - Quick Guide (5 Minutes)

## ✅ Pre-Deployment Checklist

- ✅ YAML file ready: `proactive-csi-agent-orchestrate.yaml` (20KB)
- ✅ Agent name: `ProActive_CSI_Agent_404`
- ✅ Version: 1.2.0 (with STT & TTS)
- ✅ All services configured

---

## 🎯 Step-by-Step Deployment

### Step 1: Open IBM Portal (1 minute)

**Click this link or copy to browser:**
```
https://cloud.ibm.com/watsonx/orchestrate
```

**Or direct link:**
```
https://au-syd.watson-orchestrate.cloud.ibm.com/build/manage
```

**Login with your IBM Cloud credentials**

---

### Step 2: Navigate to Agents (30 seconds)

1. **In the left sidebar**, look for:
   - **"All agents"** or
   - **"Skills"** or
   - **"AI Assistants"** or
   - **"Agents"**

2. **Click on it**

---

### Step 3: Import Agent (1 minute)

**Option A: Agent doesn't exist yet**
1. Click **"Create agent"** or **"Import agent"** or **"Add agent"**
2. Click **"Import from file"** or **"Upload"**
3. Navigate to:
   ```
   /Users/ishwaryasridharan/Desktop/Hackathon_2025/Agentic_AI/agent404-proactive-csi/
   ```
4. Select: **`proactive-csi-agent-orchestrate.yaml`**
5. Click **"Open"** or **"Upload"**
6. Wait for upload (5-10 seconds)

**Option B: Agent already exists**
1. Find **"ProActive_CSI_Agent_404"** in the list
2. Click on it
3. Click **"Edit"** or **"Settings"**
4. Click **"Import"** or **"Replace configuration"**
5. Upload the YAML file

---

### Step 4: Verify Configuration (1 minute)

After upload, you should see:
- ✅ Agent name: **ProActive_CSI_Agent_404**
- ✅ Description visible
- ✅ Instructions loaded
- ✅ Model configured: `watsonx/meta-llama/llama-3-2-90b-vision-instruct`

---

### Step 5: Connect IBM Services (1 minute)

1. **Go to "Connections"** or **"Integrations"** tab
2. **Verify/Add these services:**

   **Speech-to-Text (STT):**
   - API Key: `qzNRq16Io8Dap9VR57CMw5jvbH3LUIWEQTEv20hJ-tc1`
   - URL: `https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/ffcdbb0a-ca7b-4361-838b-cc8b6e4ac34c`

   **Text-to-Speech (TTS):**
   - API Key: `FLukjnaT1rf9qFnAhVbpi5D7HPMrvUst9POK8A-JShpz`
   - URL: `https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/298e2b63-de83-427c-b77d-156c0976eed7`

   **Natural Language Understanding (NLU):**
   - API Key: `JD1cdPcLQdymkID4sHav18lDXLd7U1FrTKDB2yllVLar`
   - URL: `https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/79459c2d-4e21-4593-963e-6e9964afe1a3`

3. **If services show red/error:**
   - Click **"Add Connection"** or **"Connect Service"**
   - Enter API key and URL
   - Click **"Save"** or **"Connect"**

---

### Step 6: Save and Activate (30 seconds)

1. **Click "Save"** button (top right)
2. **Wait for confirmation** (green checkmark)
3. **Click "Activate"** or **"Publish"** or **"Deploy"**
4. **Wait for activation** (10-30 seconds)
5. **Status should show:** ✅ **Active** or ✅ **Deployed**

---

### Step 7: Test Agent (1 minute)

1. **Click on your agent** to open chat interface
2. **Type this test query:**
   ```
   Good morning, what's my priority today?
   ```
3. **Expected response:**
   - Should mention critical customers
   - Should show churn risks
   - Should provide recommendations

4. **Try another test:**
   ```
   Tell me about Acme Corporation
   ```

---

## ✅ Success Indicators

After successful deployment, you should see:

- ✅ **Agent Status:** Active/Deployed
- ✅ **Services Connected:** STT, TTS, NLU (green status)
- ✅ **Agent Responds:** Correctly to test queries
- ✅ **Chat Interface:** Works smoothly

---

## 🔗 Get Your Deployment URL

1. **In IBM Portal**, find your agent
2. **Click on the agent** to open chat
3. **Copy the URL** from browser address bar
4. **Format:** `https://[region].watson-orchestrate.cloud.ibm.com/[path]`
5. **Save this URL** - this is your Application URL for submission!

---

## 🧪 Test Queries (Copy-Paste)

Once deployed, try these:

```
Good morning, what's my priority today?
```

```
Tell me about Acme Corporation
```

```
Show churn trends this quarter
```

```
What vendors have delays?
```

```
Calculate revenue at risk
```

```
Generate executive briefing
```

```
Read me the executive briefing aloud using Text-to-Speech
```

---

## 🚨 Troubleshooting

### Issue: Can't find "Agents" or "Skills"
**Solution:** Look for "Apps", "Custom skills", "Builder", or "AI Assistants" in sidebar

### Issue: Upload failed
**Solution:**
- Check file is `proactive-csi-agent-orchestrate.yaml`
- File size should be ~20KB
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

## 📍 Quick Access

- **IBM Portal:** https://cloud.ibm.com/watsonx/orchestrate
- **Direct Portal:** https://au-syd.watson-orchestrate.cloud.ibm.com/build/manage
- **Config File:** `/Users/ishwaryasridharan/Desktop/Hackathon_2025/Agentic_AI/agent404-proactive-csi/proactive-csi-agent-orchestrate.yaml`

---

## 🎉 You're Ready!

**Once deployed:**
1. ✅ Agent is live in IBM watsonx Orchestrate
2. ✅ Copy the deployment URL
3. ✅ Test all queries
4. ✅ Ready for submission!

**GO DEPLOY! 🚀**

