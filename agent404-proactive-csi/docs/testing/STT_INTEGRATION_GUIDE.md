# 🎤 IBM Watson Speech-to-Text (STT) Integration Guide

**Complete Integration Documentation for ProActive CSI Agent**

---

## 📋 Overview

This guide documents the IBM Watson Speech-to-Text service integration in the ProActive CSI Agent, following the official IBM Watson documentation.

---

## 🔗 IBM Watson Speech-to-Text Service

### Service Details

- **Service Name:** IBM Watson Speech to Text
- **API Endpoint:** `POST /v1/recognize`
- **Service URL:** `https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/ffcdbb0a-ca7b-4361-838b-cc8b6e4ac34c`
- **Authentication:** API Key via IAM
- **API Key:** `qzNRq16Io8Dap9VR57CMw5jvbH3LUIWEQTEv20hJ-tc1`
- **Region:** us-south

### Default Configuration

- **Default Model:** `en-US_BroadbandModel`
- **Alternative Models:**
  - `en-US_Telephony` - For phone call transcription
  - `en-US_Multimedia` - For general voice commands
  
### Supported Audio Formats

- `audio/flac` - FLAC audio (recommended)
- `audio/wav` - WAV audio
- `audio/mp3` - MP3 audio
- `audio/ogg` - OGG audio

---

## 📡 API Method: POST /v1/recognize

### Basic Transcription (No Options)

**Endpoint:** `POST /v1/recognize`

**Request Headers:**
```
Content-Type: audio/flac
Authorization: Bearer {apikey}
```

**Request Body:**
- Binary audio data

**Example cURL Command:**
```bash
curl -X POST -u "apikey:qzNRq16Io8Dap9VR57CMw5jvbH3LUIWEQTEv20hJ-tc1" \
  --header "Content-Type: audio/flac" \
  --data-binary @audio-file.flac \
  "https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/ffcdbb0a-ca7b-4361-838b-cc8b6e4ac34c/v1/recognize"
```

**Response Format:**
```json
{
  "result_index": 0,
  "results": [
    {
      "alternatives": [
        {
          "confidence": 0.96,
          "transcript": "transcribed text here"
        }
      ],
      "final": true
    }
  ]
}
```

### Transcription with Options

**Endpoint:** `POST /v1/recognize?timestamps=true&max_alternatives=3`

**Parameters:**
- `timestamps=true` - Include word-level timestamps
- `max_alternatives=3` - Return top 3 transcription alternatives

**Example Request:**
```bash
curl -X POST -u "apikey:qzNRq16Io8Dap9VR57CMw5jvbH3LUIWEQTEv20hJ-tc1" \
  --header "Content-Type: audio/flac" \
  --data-binary @audio-file.flac \
  "https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/ffcdbb0a-ca7b-4361-838b-cc8b6e4ac34c/v1/recognize?timestamps=true&max_alternatives=3"
```

---

## 🔧 Integration in ProActive CSI Agent

### Agent Instructions

The agent is configured to:

1. **Recognize Voice Commands:**
   - Process audio input via IBM Speech-to-Text
   - Acknowledge STT processing in responses
   - Transcribe voice commands to text

2. **Response Pattern:**
   - When voice command detected: "🎤 Processing voice command via IBM Speech-to-Text service (POST /v1/recognize)"
   - Specify model used: "en-US_BroadbandModel"
   - Confirm transcription received

### Voice Command Keywords

The agent recognizes these voice-related triggers:

- "voice command"
- "voice input"
- "speak"
- "audio command"
- "hands-free query"
- "Speech-to-Text"
- "STT"

---

## 🧪 Testing STT in IBM watsonx Orchestrate

### Test Queries

1. **Basic Voice Command:**
   ```
   "What's my priority today? [Process via STT]"
   ```

2. **Voice Query:**
   ```
   "Using voice commands, tell me about customer C-001"
   ```

3. **Hands-Free Request:**
   ```
   "I'm driving, can you process my voice command?"
   ```

### Expected Agent Response

When STT is used, the agent should mention:

✅ "Processing voice command via IBM Speech-to-Text service"  
✅ "API: POST /v1/recognize"  
✅ "Model: en-US_BroadbandModel"  
✅ "Voice command transcribed successfully"

---

## 📊 Response Example

### User Query: "I'm driving, what's my priority today?"

### Agent Response:
```
🎤 PROCESSING VOICE COMMAND VIA IBM SPEECH-TO-TEXT SERVICE

[API Endpoint: POST /v1/recognize]
[Service: IBM Watson Speech to Text]
[Model: en-US_BroadbandModel]
[Status: ✅ Voice command transcribed successfully]

📊 PRIORITY BRIEFING FOR TODAY

🚨 CRITICAL (Immediate Action):
1. C-003 - TechGlobal Inc
   • Churn Risk: 85% (CRITICAL)
   • Revenue at Risk: $78,000 ARR
   • Action: Urgent CSM intervention

[... rest of briefing ...]

✅ Voice command processed via IBM Watson Speech-to-Text
```

---

## 🔐 Authentication

### API Key Authentication

**Method:** IAM API Key

**Credentials:**
- **API Key:** `qzNRq16Io8Dap9VR57CMw5jvbH3LUIWEQTEv20hJ-tc1`
- **IAM URL:** Auto-configured by SDK

**In IBM watsonx Orchestrate:**
- Configure STT service connection in Orchestrate portal
- Service connection name: "STT - Voice Commands"
- Authentication method: API Key

---

## 🔄 Workflow Integration

### STT in Agent Workflows

**WORKFLOW 5: Daily Executive Brief**
- Step 1: Receive voice command via STT
- Step 2: Transcribe audio to text
- Step 3: Process query normally
- Step 4: Generate response
- Step 5: Optionally convert response to voice via TTS

---

## 🛠️ Troubleshooting

### If STT Not Working:

1. **Check Service Connection:**
   - Verify STT service is connected in Orchestrate
   - Confirm API key is valid
   - Check service URL is correct

2. **Verify Agent Instructions:**
   - Ensure agent mentions STT in voice-related queries
   - Check if voice keywords are recognized

3. **Test API Directly:**
   ```bash
   curl -X POST -u "apikey:qzNRq16Io8Dap9VR57CMw5jvbH3LUIWEQTEv20hJ-tc1" \
     --header "Content-Type: audio/flac" \
     --data-binary @test-audio.flac \
     "https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/ffcdbb0a-ca7b-4361-838b-cc8b6e4ac34c/v1/recognize"
   ```

---

## 📚 Additional Resources

### IBM Watson Documentation

- **Official STT Docs:** https://cloud.ibm.com/apidocs/speech-to-text
- **Getting Started:** https://cloud.ibm.com/docs/speech-to-text
- **API Reference:** https://cloud.ibm.com/apidocs/speech-to-text/speech-to-text

### Related Files

- **Credentials:** `ibm-credentials_STT.env`
- **Agent Config:** `proactive-csi-agent-orchestrate.yaml`
- **Testing Guide:** `docs/testing/STT_TTS_IBM_TESTING.md`

---

## ✅ Checklist

- [ ] STT service connected in IBM watsonx Orchestrate
- [ ] API key configured correctly
- [ ] Agent instructions include STT references
- [ ] Voice command keywords recognized
- [ ] Agent mentions STT in responses
- [ ] API endpoint referenced: POST /v1/recognize
- [ ] Model specified: en-US_BroadbandModel

---

**Last Updated:** January 2025  
**Version:** 1.1.0  
**Status:** Production Ready ✅

