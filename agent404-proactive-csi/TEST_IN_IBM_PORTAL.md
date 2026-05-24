# 🧪 Testing in IBM watsonx Orchestrate Portal

## ✅ Deployment Status

**Agent:** ProActive_CSI_Agent_404  
**Status:** ✅ Deployed and Updated  
**Environment:** production-au (active)  
**Region:** au-syd  

---

## 🚀 Quick Start - Test Your Agent

### Step 1: Open IBM Portal
1. Go to: **https://cloud.ibm.com/watsonx/orchestrate**
2. Or use direct link: **https://au-syd.watson-orchestrate.cloud.ibm.com/build/manage**

### Step 2: Find Your Agent
1. Click **"Build"** → **"Agent Builder"**
2. Look for: **"ProActive_CSI_Agent_404"**
3. Click on the agent name

### Step 3: Open Chat Interface
1. Click **"Test"** or **"Chat"** button
2. This opens the chat interface

### Step 4: Test TTS Feature
Type this query:
```
Read me the executive briefing aloud using Text-to-Speech
```

---

## 🧪 Test Queries

### 1. TTS Test (Main Feature)
```
Read me the executive briefing aloud using Text-to-Speech
```

**Expected Response:**
- ✅ Mentions IBM Text-to-Speech service
- ✅ Shows API endpoint: POST /v1/synthesize
- ✅ Provides full executive briefing text
- ✅ Attempts Cloudant upload
- ✅ Provides download link (if Cloudant DB exists)
- ⚠️  If Cloudant fails: Shows warning but still provides text

### 2. Basic Functionality
```
Good morning, what's my priority today?
```

### 3. Customer Intelligence
```
Tell me about Acme Corporation
```

### 4. Procurement Intelligence
```
What vendors have delays?
```

### 5. Revenue Protection
```
Calculate revenue at risk
```

---

## 📋 What to Look For

### ✅ Success Indicators:

1. **Agent Responds:**
   - Agent should respond within a few seconds
   - Response should be relevant to the query

2. **TTS Query Response Should Include:**
   - "🔊 GENERATING VOICE BRIEFING USING IBM TEXT-TO-SPEECH SERVICE"
   - "[API Endpoint: POST /v1/synthesize]"
   - "[Service: IBM Watson Text to Speech]"
   - Full executive briefing text
   - Download link (if Cloudant works) or warning (if Cloudant DB missing)

3. **Other Queries:**
   - Should provide relevant information
   - Should mention IBM services when appropriate
   - Should reference customer data, vendors, revenue, etc.

---

## 🔍 Troubleshooting

### Issue: Agent Not Found
**Solution:**
- Verify you're in the correct region (au-syd)
- Check environment is active: `orchestrate env list`
- Try refreshing the page

### Issue: Agent Doesn't Respond
**Solution:**
- Check agent status in portal
- Verify all IBM services are connected
- Check for error messages in portal

### Issue: TTS Query Shows Error
**Solution:**
- This is expected if Cloudant database doesn't exist
- TTS generation still works
- Agent will provide text content
- To enable download links: Create `proactive_csi` database in Cloudant

### Issue: Download Link Doesn't Work
**Solution:**
- Cloudant database `proactive_csi` needs to exist
- Create it in IBM Cloud Console
- See `TTS_CLOUDANT_SETUP.md` for instructions

---

## 📊 Expected TTS Response Format

```
🔊 GENERATING VOICE BRIEFING USING IBM TEXT-TO-SPEECH SERVICE

[API Endpoint: POST /v1/synthesize]
[Service: IBM Watson Text to Speech]
[Voice: en-US_MichaelV3Voice]
[Format: audio/wav]

Voice briefing content to be synthesized:

"Good morning. This is your ProActive CSI daily executive briefing..."

[Audio file generated: executive_briefing.wav]
[Uploading to Cloudant for download...]

✅ Voice briefing generated successfully via IBM Watson Text-to-Speech service
✅ Audio format: WAV (44.1 kHz, 16-bit)
✅ Audio uploaded to Cloudant

🔊 **DOWNLOAD AUDIO FILE:**
[Click here to download and play the audio briefing](https://...cloudantnosqldb.appdomain.cloud/.../audio.wav)

The audio file is stored in Cloudant and ready for download.
```

---

## ✅ Verification Checklist

- [ ] Agent appears in Agent Builder
- [ ] Chat interface opens
- [ ] Basic query works ("Good morning, what's my priority today?")
- [ ] TTS query works ("Read me the executive briefing aloud")
- [ ] Response mentions IBM TTS service
- [ ] Response includes full text content
- [ ] Download link appears (if Cloudant DB exists)
- [ ] Other test queries work

---

## 🎯 Success Criteria

✅ **Agent is working if:**
1. All queries get responses
2. TTS query mentions IBM Text-to-Speech
3. TTS query provides full text content
4. Agent references IBM services correctly
5. Agent provides relevant business intelligence

⚠️ **Cloudant upload is optional:**
- If database exists → Download link appears
- If database doesn't exist → Warning shown, but TTS still works

---

**🎉 Ready to test! Open the portal and try your queries!**

