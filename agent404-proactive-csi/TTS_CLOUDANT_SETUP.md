# 🔊 TTS Audio Storage in Cloudant - Setup Guide

## ✅ Implementation Complete!

The TTS audio upload to Cloudant feature has been implemented. Here's what was added:

### 📋 What Was Implemented

1. **Enhanced `synthesize_speech()` method:**
   - Now returns a dictionary with audio content AND Cloudant download URL
   - Automatically uploads audio to Cloudant when `upload_to_cloudant=True`
   - Gracefully handles Cloudant failures

2. **New `upload_audio_to_cloudant()` method:**
   - Uploads audio files as Cloudant attachments
   - Generates public download URLs
   - Creates database if it doesn't exist (if permissions allow)

3. **Updated Agent Instructions:**
   - Agent now includes download links in TTS responses
   - Format: `[Click here to download]({cloudant_url})`

---

## 🔧 Setup Required

### Step 1: Create Cloudant Database

The `proactive_csi` database needs to exist. Create it via:

**Option A: IBM Cloud Console (Recommended)**
1. Go to: https://cloud.ibm.com/
2. Navigate to your Cloudant instance
3. Click "Create Database"
4. Name: `proactive_csi`
5. Type: Standard

**Option B: Via API (if you have permissions)**
```bash
curl -X PUT \
  "https://f01bbce3-de41-430e-bd9b-5c00a082588a-bluemix.cloudantnosqldb.appdomain.cloud/proactive_csi" \
  -u "f01bbce3-de41-430e-bd9b-5c00a082588a-bluemix:TalYEKH8YIFL1Hqu0Gx4QZP6IBE-43s8Cl2Fm7a-CyBK"
```

**Option C: The code will try to create it automatically**
- If your API key has permissions, it will create the database
- If not, you'll see a 403 error and need to create it manually

---

## 🧪 Testing

### Test the Feature:

```bash
cd agent404-proactive-csi
python3 scripts/test_tts_cloudant_upload.py
```

### Expected Output (Success):
```
✅ Audio generated successfully
✅ Audio uploaded to Cloudant
   Document ID: tts_audio_1234567890
   Download URL: https://f01bbce3-de41-430e-bd9b-5c00a082588a-bluemix.cloudantnosqldb.appdomain.cloud/proactive_csi/tts_audio_1234567890/audio.wav
```

### Expected Output (Database Missing):
```
⚠️  Could not create database: Error: forbidden: Access denied, Status code: 403
✅ Audio generated successfully (but upload failed)
```

**Solution:** Create the database manually (see Step 1 above)

---

## 📝 How It Works

### Flow:
1. User requests: "Read me the executive briefing aloud"
2. Agent calls `synthesize_speech(text, upload_to_cloudant=True)`
3. IBM TTS generates audio (WAV format)
4. Audio is base64-encoded and uploaded to Cloudant as attachment
5. Cloudant returns document ID
6. Agent generates download URL
7. Agent responds with download link

### Download URL Format:
```
https://{account}.cloudantnosqldb.appdomain.cloud/proactive_csi/{doc_id}/audio.wav
```

Example:
```
https://f01bbce3-de41-430e-bd9b-5c00a082588a-bluemix.cloudantnosqldb.appdomain.cloud/proactive_csi/tts_audio_1732312345/audio.wav
```

---

## 🎯 Agent Response Format

When user asks for TTS audio, the agent will now respond:

```
🔊 GENERATING VOICE BRIEFING USING IBM TEXT-TO-SPEECH SERVICE

[API Endpoint: POST /v1/synthesize]
[Service: IBM Watson Text to Speech]
[Voice: en-US_MichaelV3Voice]
[Format: audio/wav]

[Audio file generated: executive_briefing.wav]
[Uploading to Cloudant for download...]

✅ Voice briefing generated successfully
✅ Audio format: WAV (44.1 kHz, 16-bit)
✅ Audio uploaded to Cloudant

🔊 **DOWNLOAD AUDIO FILE:**
[Click here to download and play the audio briefing](https://f01bbce3-de41-430e-bd9b-5c00a082588a-bluemix.cloudantnosqldb.appdomain.cloud/proactive_csi/tts_audio_1732312345/audio.wav)

The audio file is stored in Cloudant and ready for download. 
Click the link above to listen to your executive briefing.
```

---

## 🔒 Security Notes

- **Public URLs:** Cloudant attachment URLs are publicly accessible if you have the full URL
- **Access Control:** Consider implementing:
  - Cloudant API keys for authentication
  - Time-limited URLs
  - Access control lists (ACLs)

For hackathon/demo purposes, public URLs are fine.

---

## ✅ Status

- ✅ Code implemented
- ✅ Agent instructions updated
- ✅ Test script created
- ⚠️  Database needs to be created (one-time setup)
- ✅ Ready for deployment

---

## 🚀 Next Steps

1. **Create the database** (if not exists):
   - Use IBM Cloud Console (easiest)
   - Or use the API if you have permissions

2. **Test the feature:**
   ```bash
   python3 scripts/test_tts_cloudant_upload.py
   ```

3. **Deploy updated agent:**
   ```bash
   orchestrate agents import -f proactive-csi-agent-orchestrate.yaml
   ```

4. **Test in watsonx Orchestrate:**
   - Ask: "Read me the executive briefing aloud"
   - Verify download link appears
   - Click link to download and play audio

---

## 📊 Files Modified

1. `integrations/ibm_services.py`
   - Enhanced `synthesize_speech()` method
   - Added `upload_audio_to_cloudant()` method

2. `proactive-csi-agent-orchestrate.yaml`
   - Updated TTS response format
   - Added Cloudant download link instructions

3. `scripts/test_tts_cloudant_upload.py` (new)
   - Test script for TTS + Cloudant integration

---

**🎉 Feature Ready!** Once the database is created, TTS audio will automatically upload to Cloudant and provide download links!

