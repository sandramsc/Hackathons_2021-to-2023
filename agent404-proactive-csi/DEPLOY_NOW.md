# 🚀 DEPLOY NOW - Quick Guide

## Step 1: Open IBM Portal
**URL:** https://cloud.ibm.com/watsonx/orchestrate

The browser should open automatically. If not, click the link above.

---

## Step 2: Login
- Use your IBM Cloud credentials
- Complete any 2FA if required

---

## Step 3: Navigate to Agents
1. Look for **"All agents"** or **"Skills"** in the left sidebar
2. Click on it

---

## Step 4: Import Agent
1. Click **"Create agent"** or **"Import agent"** button
2. Select **"Import from file"**
3. Navigate to this file:
   ```
   /Users/ishwaryasridharan/Desktop/Hackathon_2025/Agentic_AI/agent404-proactive-csi/proactive-csi-agent-orchestrate.yaml
   ```
4. Click **"Open"** or **"Upload"**

---

## Step 5: Connect Services
Go to **"Connections"** or **"Integrations"** tab:

### Speech-to-Text:
- API Key: `qzNRq16Io8Dap9VR57CMw5jvbH3LUIWEQTEv20hJ-tc1`
- URL: `https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/ffcdbb0a-ca7b-4361-838b-cc8b6e4ac34c`

### Text-to-Speech:
- API Key: `FLukjnaT1rf9qFnAhVbpi5D7HPMrvUst9POK8A-JShpz`
- URL: `https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/298e2b63-de83-427c-b97d-156c0976eed7`

### Natural Language Understanding:
- API Key: `JD1cdPcLQdymkID4sHav18lDXLd7U1FrTKDB2yllVLar`
- URL: `https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/79459c2d-4e21-4593-963e-6e9964afe1a3`

### watsonx.ai:
- Project ID: `aa39fafa-2f20-47a3-b6d5-a84ff6cefa0e`

---

## Step 6: Save & Activate
1. Click **"Save"** button
2. Wait for confirmation
3. Click **"Activate"** or **"Publish"**
4. Wait 10-30 seconds
5. Status should show: ✅ **Active** or ✅ **Deployed**

---

## Step 7: Get Deployment URL
1. Look for **"Share"**, **"Chat URL"**, or **"Test URL"** button
2. Copy the URL
3. This is your **Application URL** for submission

---

## Step 8: Test
Try these queries:
1. "Good morning, what's my priority today?"
2. "Tell me about Acme Corporation"
3. "Read me the executive briefing aloud using Text-to-Speech"

---

## ✅ Success!
Once you see:
- Agent status: **Active/Deployed**
- All services: **Connected** (green)
- Test queries: **Working**

**You're done!** 🎉

Save the deployment URL for submission.
