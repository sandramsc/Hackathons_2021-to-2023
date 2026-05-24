# 🔊 IBM Watson Text-to-Speech (TTS) Integration Guide

**Complete Integration Documentation for ProActive CSI Agent**

---

## 📋 Overview

This guide documents the IBM Watson Text-to-Speech service integration in the ProActive CSI Agent, following the official IBM Watson documentation.

---

## 🔗 IBM Watson Text-to-Speech Service

### Service Details

- **Service Name:** IBM Watson Text to Speech
- **API Endpoint:** `POST /v1/synthesize` or `GET /v1/synthesize`
- **Service URL:** `https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/298e2b63-de83-427c-b77d-156c0976eed7`
- **Authentication:** API Key via IAM
- **API Key:** `FLukjnaT1rf9qFnAhVbpi5D7HPMrvUst9POK8A-JShpz`
- **Region:** us-south

### Available Voices

**US English Voices:**
- **en-US_MichaelV3Voice** - Professional male voice (default)
- **en-US_AllisonV3Voice** - Professional female voice

**Other Languages:**
- Spanish: `es-ES_EnriqueV3Voice`
- French: `fr-FR_ReneeV3Voice`
- German: `de-DE_DieterV3Voice`
- Japanese: `ja-JP_EmiV3Voice`

### Supported Audio Formats

- `audio/wav` - WAV format (recommended, high quality)
- `audio/ogg` - OGG format (default, compressed)
- `audio/mp3` - MP3 format
- `audio/flac` - FLAC format

---

## 📡 API Method 1: POST /v1/synthesize

### Synthesize Text in US English (WAV Format)

**Endpoint:** `POST /v1/synthesize?voice=en-US_MichaelV3Voice`

**Request Headers:**
```
Content-Type: application/json
Accept: audio/wav
Authorization: Bearer {apikey}
```

**Request Body:**
```json
{
  "text": "hello world"
}
```

**Example cURL Command:**
```bash
curl -X POST -u "apikey:FLukjnaT1rf9qFnAhVbpi5D7HPMrvUst9POK8A-JShpz" \
  --header "Content-Type: application/json" \
  --header "Accept: audio/wav" \
  --data '{"text":"hello world"}' \
  --output hello_world.wav \
  "https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/298e2b63-de83-427c-b77d-156c0976eed7/v1/synthesize?voice=en-US_MichaelV3Voice"
```

**Response:**
- Audio file (WAV format) saved to `hello_world.wav`
- Binary audio data stream

### Synthesize with Different Voice (OGG Format)

**Endpoint:** `POST /v1/synthesize?voice=en-US_AllisonV3Voice`

**Example cURL Command:**
```bash
curl -X POST -u "apikey:FLukjnaT1rf9qFnAhVbpi5D7HPMrvUst9POK8A-JShpz" \
  --header "Content-Type: application/json" \
  --data '{"text":"hello world"}' \
  --output hello_world.ogg \
  "https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/298e2b63-de83-427c-b77d-156c0976eed7/v1/synthesize?voice=en-US_AllisonV3Voice"
```

**Response:**
- Audio file (OGG format) saved to `hello_world.ogg`

---

## 📡 API Method 2: GET /v1/synthesize

### Synthesize Text with GET Method

**Endpoint:** `GET /v1/synthesize?accept=audio%2Fwav&text={encoded_text}&voice={voice}`

**Query Parameters:**
- `accept` - Audio format (URL encoded: `audio%2Fwav` for `audio/wav`)
- `text` - Text to synthesize (URL encoded)
- `voice` - Voice to use

**Example cURL Command (Spanish):**
```bash
curl -X GET -u "apikey:FLukjnaT1rf9qFnAhVbpi5D7HPMrvUst9POK8A-JShpz" \
  --output hola_mundo.wav \
  "https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/298e2b63-de83-427c-b77d-156c0976eed7/v1/synthesize?accept=audio%2Fwav&text=hola%20mundo&voice=es-ES_EnriqueV3Voice"
```

---

## 🔧 Integration in ProActive CSI Agent

### Agent Instructions

The agent is configured to:

1. **Generate Voice Responses:**
   - Convert text responses to speech via IBM Text-to-Speech
   - Use POST /v1/synthesize method
   - Specify voice: `en-US_MichaelV3Voice` (default) or `en-US_AllisonV3Voice`
   - Output format: `audio/wav` or `audio/ogg`

2. **Response Pattern:**
   - When voice response requested: "🔊 Generating voice response via IBM Text-to-Speech service (POST /v1/synthesize)"
   - Specify voice used: "en-US_MichaelV3Voice"
   - Specify format: "audio/wav"
   - Confirm audio generation complete

### Voice Response Keywords

The agent recognizes these voice-related triggers:

- "voice briefing"
- "read aloud"
- "speak"
- "audio response"
- "voice summary"
- "generate audio"
- "Text-to-Speech"
- "TTS"
- "voice response"

---

## 🧪 Testing TTS in IBM watsonx Orchestrate

### Test Queries

1. **Basic Voice Response:**
   ```
   "Read me the executive briefing aloud"
   ```

2. **Voice Briefing Request:**
   ```
   "Generate voice briefing for today's priorities"
   ```

3. **Hands-Free Voice Request:**
   ```
   "I'm driving, give me a voice summary of critical customers"
   ```

### Expected Agent Response

When TTS is used, the agent should mention:

✅ "Generating voice response via IBM Text-to-Speech service"  
✅ "API: POST /v1/synthesize"  
✅ "Voice: en-US_MichaelV3Voice"  
✅ "Format: audio/wav"  
✅ "Audio file generated successfully"

---

## 📊 Response Examples

### Example 1: Voice Briefing Request

**User Query:** "Read me the executive briefing aloud"

**Agent Response:**
```
🔊 GENERATING VOICE BRIEFING USING IBM TEXT-TO-SPEECH SERVICE

[API Endpoint: POST /v1/synthesize]
[Service: IBM Watson Text to Speech]
[Voice: en-US_MichaelV3Voice]
[Format: audio/wav]
[Status: ✅ Audio file generated successfully]

Voice briefing content to be synthesized:

"Good morning. This is your ProActive CSI daily executive briefing.

Executive Summary: 4 critical customers requiring immediate attention. 
Total ARR at risk is $152,000. Two vendor delays are impacting customer satisfaction. 
Churn prediction accuracy remains at 89 percent.

Top Risks: First, TechGlobal Inc with 85 percent churn risk, representing 
$78,000 in ARR at risk..."

[Audio file: executive_briefing.wav]
[Generated via IBM Watson Text-to-Speech API]
[Ready for playback]

✅ Voice briefing generated successfully via IBM Watson Text-to-Speech service
✅ Audio format: WAV (44.1 kHz, 16-bit)
✅ Duration: Approximately 45 seconds
```

### Example 2: Hands-Free Voice Request

**User Query:** "I'm driving, give me a voice summary"

**Agent Response:**
```
🎤🔊 HANDS-FREE VOICE BRIEFING MODE - COMPLETE VOICE WORKFLOW

[STEP 1: STT Processing]
Processing voice command via IBM Speech-to-Text service
API: POST /v1/recognize
✅ Voice command transcribed successfully

[STEP 2: Content Generation]
Generating priority briefing content...

[STEP 3: TTS Generation]
Generating voice response via IBM Text-to-Speech service
API: POST /v1/synthesize
Voice: en-US_MichaelV3Voice
Format: audio/wav
Status: ✅ Audio file generated

Voice summary content:

"Critical items requiring your attention today:
1. TechGlobal Inc - 85% churn risk - $78K ARR at risk
2. Acme Corp - 78% churn risk - $45K ARR at risk
3. Two vendor delays affecting 3 customers..."

[Audio file: priority_summary.wav]
[Ready for playback]

✅ Complete voice workflow executed:
   STT (/v1/recognize) → Processing → TTS (/v1/synthesize)
✅ Stay safe while driving! Audio playback ready.
```

---

## 🔐 Authentication

### API Key Authentication

**Method:** IAM API Key

**Credentials:**
- **API Key:** `FLukjnaT1rf9qFnAhVbpi5D7HPMrvUst9POK8A-JShpz`
- **IAM URL:** Auto-configured by SDK

**In IBM watsonx Orchestrate:**
- Configure TTS service connection in Orchestrate portal
- Service connection name: "TTS - Voice Responses"
- Authentication method: API Key

---

## 🎤 Voice Selection Guide

### Default Voice: en-US_MichaelV3Voice

**Use Case:** Standard voice responses, executive briefings  
**Characteristics:** Professional male voice, clear pronunciation  
**Recommended For:** Business communications, daily briefings

**Example Usage:**
```bash
POST /v1/synthesize?voice=en-US_MichaelV3Voice
Accept: audio/wav
```

### Alternative Voice: en-US_AllisonV3Voice

**Use Case:** Customer-facing communications, warm interactions  
**Characteristics:** Professional female voice, friendly tone  
**Recommended For:** Customer greetings, personalized messages

**Example Usage:**
```bash
POST /v1/synthesize?voice=en-US_AllisonV3Voice
Accept: audio/ogg
```

---

## 📝 Text Formatting Best Practices

### For Voice Synthesis

1. **Numbers:**
   - Write out numbers: "four customers" instead of "4 customers"
   - Or use spoken format: "seventy-eight thousand" for clarity

2. **Punctuation:**
   - Use periods for pauses
   - Use commas for brief pauses
   - Use ellipses (...) for longer pauses

3. **Abbreviations:**
   - Spell out abbreviations: "ARR" → "Annual Recurring Revenue"
   - Or use expanded form: "C-S-M" → "Customer Success Manager"

4. **Special Characters:**
   - Use words: "%" → "percent"
   - Use words: "$" → "dollars"

### Example Formatted Text:

**Before:**
```
"4 critical customers, $152K ARR at risk, 89% accuracy"
```

**After (Voice-Optimized):**
```
"Four critical customers, one hundred fifty-two thousand dollars in ARR at risk, 
eighty-nine percent accuracy"
```

---

## 🔄 Workflow Integration

### TTS in Agent Workflows

**WORKFLOW 5: Daily Executive Brief**
- Step 1: Generate text briefing
- Step 2: Format text for voice synthesis
- Step 3: Call TTS API (POST /v1/synthesize)
- Step 4: Generate audio file (WAV format)
- Step 5: Deliver audio via email/Slack

**Complete Voice Workflow:**
```
STT (/v1/recognize) → Text Processing → TTS (/v1/synthesize) → Audio Output
```

---

## 🛠️ Troubleshooting

### If TTS Not Working:

1. **Check Service Connection:**
   - Verify TTS service is connected in Orchestrate
   - Confirm API key is valid
   - Check service URL is correct

2. **Verify Voice Availability:**
   - Ensure voice name is correct: `en-US_MichaelV3Voice`
   - Check if voice is available in your region

3. **Check Audio Format:**
   - Verify format is supported: `audio/wav`, `audio/ogg`
   - Check Accept header matches output format

4. **Test API Directly:**
   ```bash
   curl -X POST -u "apikey:FLukjnaT1rf9qFnAhVbpi5D7HPMrvUst9POK8A-JShpz" \
     --header "Content-Type: application/json" \
     --header "Accept: audio/wav" \
     --data '{"text":"test"}' \
     --output test.wav \
     "https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/298e2b63-de83-427c-b77d-156c0976eed7/v1/synthesize?voice=en-US_MichaelV3Voice"
   ```

### Common Issues:

1. **Audio File Not Generated:**
   - Check API key permissions
   - Verify text is not empty
   - Check service quota limits

2. **Wrong Voice:**
   - Verify voice name spelling
   - Check voice availability in region
   - Use correct format: `en-US_MichaelV3Voice`

3. **Audio Quality Issues:**
   - Use WAV format for best quality
   - Check text formatting
   - Ensure proper pronunciation

---

## 📚 Additional Resources

### IBM Watson Documentation

- **Official TTS Docs:** https://cloud.ibm.com/apidocs/text-to-speech
- **Getting Started:** https://cloud.ibm.com/docs/text-to-speech
- **API Reference:** https://cloud.ibm.com/apidocs/text-to-speech/text-to-speech
- **Voice List:** https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-voices

### Related Files

- **Credentials:** `ibm-credentials_TTS.env`
- **Agent Config:** `proactive-csi-agent-orchestrate.yaml`
- **Testing Guide:** `docs/testing/STT_TTS_IBM_TESTING.md`
- **STT Guide:** `docs/testing/STT_INTEGRATION_GUIDE.md`

---

## ✅ Checklist

- [ ] TTS service connected in IBM watsonx Orchestrate
- [ ] API key configured correctly
- [ ] Agent instructions include TTS references
- [ ] Voice response keywords recognized
- [ ] Agent mentions TTS in responses
- [ ] API endpoint referenced: POST /v1/synthesize
- [ ] Voice specified: en-US_MichaelV3Voice
- [ ] Format specified: audio/wav
- [ ] Text formatting optimized for voice

---

## 🎯 Quick Reference

### TTS API Call Template

```bash
curl -X POST -u "apikey:{apikey}" \
  --header "Content-Type: application/json" \
  --header "Accept: audio/wav" \
  --data '{"text":"{your_text}"}' \
  --output output.wav \
  "{url}/v1/synthesize?voice=en-US_MichaelV3Voice"
```

### Agent Response Template

```
🔊 Generating voice response via IBM Text-to-Speech service
API: POST /v1/synthesize
Voice: en-US_MichaelV3Voice
Format: audio/wav
Status: ✅ Audio file generated successfully
```

---

**Last Updated:** January 2025  
**Version:** 1.1.0  
**Status:** Production Ready ✅

