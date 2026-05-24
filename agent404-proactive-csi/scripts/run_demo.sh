#!/bin/bash

# ProActive CSI - Launch Demo Script
# Quick start script to run the Streamlit demo

echo "🚀 ProActive CSI - Agent 404"
echo "================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed. Please install pip."
    exit 1
fi

# Install dependencies if not already installed
echo "📦 Checking dependencies..."
pip3 install -q -r requirements.txt 2>/dev/null || {
    echo "Installing dependencies..."
    pip3 install -r requirements.txt
}

echo "✅ Dependencies installed"
echo ""

# Set environment variables from credential files
export NATURAL_LANGUAGE_UNDERSTANDING_APIKEY="JD1cdPcLQdymkID4sHav18lDXLd7U1FrTKDB2yllVLar"
export NATURAL_LANGUAGE_UNDERSTANDING_URL="https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/79459c2d-4e21-4593-963e-6e9964afe1a3"
export SPEECH_TO_TEXT_APIKEY="qzNRq16Io8Dap9VR57CMw5jvbH3LUIWEQTEv20hJ-tc1"
export SPEECH_TO_TEXT_URL="https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/ffcdbb0a-ca7b-4361-838b-cc8b6e4ac34c"
export TEXT_TO_SPEECH_APIKEY="FLukjnaT1rf9qFnAhVbpi5D7HPMrvUst9POK8A-JShpz"
export TEXT_TO_SPEECH_URL="https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/298e2b63-de83-427c-b77d-156c0976eed7"

echo "🌐 Starting Streamlit demo..."
echo ""
echo "📊 Demo will open at: http://localhost:8501"
echo ""
echo "Press Ctrl+C to stop the demo"
echo ""

# Run Streamlit
streamlit run app.py

