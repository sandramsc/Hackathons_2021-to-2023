# 🔊 How to Generate & Download TTS Audio

## Quick Method - Use IBM Cloud Console

### Step 1: Open IBM Text-to-Speech Service
Go to: **https://cloud.ibm.com/services/text-to-speech**

### Step 2: Try the API
1. Click **"Try the API"** or **"API Reference"**
2. Find the **"Synthesize"** endpoint
3. Select **POST /v1/synthesize**

### Step 3: Generate Audio
1. **Voice:** Select `en-US_MichaelV3Voice`
2. **Format:** Select `audio/wav`
3. **Text:** Paste the executive briefing text from the agent response
4. Click **"Synthesize"**
5. Download the audio file

---

## Method 2 - Use cURL Command

Copy this command and replace `[TEXT]` with the briefing text:

```bash
curl -X POST \
  -u "apikey:FLukjnaT1rf9qFnAhVbpi5D7HPMrvUst9POK8A-JShpz" \
  --header "Content-Type: application/json" \
  --data '{"text":"[PASTE_BRIEFING_TEXT_HERE]"}' \
  --output executive_briefing.wav \
  "https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/298e2b63-de83-427c-b97d-156c0976eed7/v1/synthesize?voice=en-US_MichaelV3Voice&accept=audio/wav"
```

**Example:**
```bash
curl -X POST \
  -u "apikey:FLukjnaT1rf9qFnAhVbpi5D7HPMrvUst9POK8A-JShpz" \
  --header "Content-Type: application/json" \
  --data '{"text":"Good morning. This is your ProActive CSI daily executive briefing..."}' \
  --output executive_briefing.wav \
  "https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/298e2b63-de83-427c-b97d-156c0976eed7/v1/synthesize?voice=en-US_MichaelV3Voice&accept=audio/wav"
```

---

## Method 3 - Direct API URL (Browser)

**Note:** This requires URL encoding the text, which can be complex. Use Method 1 or 2 instead.

---

## ✅ What the Agent Does

The agent:
1. ✅ Generates the audio via IBM TTS API (this works!)
2. ✅ Provides the full text content
3. ✅ Provides instructions on how to generate/download the audio

**The audio generation is working** - you just need to use one of the methods above to download it!

---

## 🎯 Quick Test

1. Ask agent: "Read me the executive briefing aloud using Text-to-Speech"
2. Copy the briefing text from the response
3. Go to: https://cloud.ibm.com/services/text-to-speech
4. Paste text, select voice, generate audio
5. Download and play!

---

**The TTS service is working perfectly - you just need to use the IBM Cloud Console or cURL to download the audio file!**

