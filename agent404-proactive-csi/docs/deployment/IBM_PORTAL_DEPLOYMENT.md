# 🚀 IBM watsonx Orchestrate Portal Deployment Guide

**Deploy ProActive CSI to IBM watsonx Orchestrate**

---

## 📋 Prerequisites

Before deploying to IBM, ensure you have:

- ✅ IBM Cloud account
- ✅ IBM watsonx Orchestrate access
- ✅ IBM Cloud CLI installed
- ✅ All IBM service credentials (already configured)

---

## 🔑 Step 1: Login to IBM Cloud

### **Option A: Using IBM Cloud CLI**

```bash
# Login with SSO
ibmcloud login --sso

# Select your account
ibmcloud target -g Default

# Verify login
ibmcloud target
```

### **Option B: Using Web Browser**

Go to: **https://cloud.ibm.com/**
- Login with your IBM ID
- Navigate to your dashboard

---

## 🎯 Step 2: Access watsonx Orchestrate Portal

1. **Open watsonx Orchestrate:**
   - URL: **https://cloud.ibm.com/watsonx/orchestrate**
   - Or: **https://api.au-syd.watson-orchestrate.cloud.ibm.com/** (Australia Sydney region)

2. **Login with your IBM credentials**

3. **Verify your instance:**
   - Check you're in the correct workspace
   - Note your instance ID

---

## 📦 Step 3: Prepare Deployment Package

Your project is already packaged and ready! Let's verify:

```bash
cd /Users/ishwaryasridharan/Desktop/Hackathon_2025/Agentic_AI/agent404-proactive-csi

# Verify all files are present
ls -la

# Check the YAML configuration
cat proactive-csi-agent.yaml
```

---

## 🔧 Step 4: Deploy Skills to watsonx Orchestrate

### **Method 1: Upload via Web UI** (RECOMMENDED)

1. **Navigate to Skills:**
   - In watsonx Orchestrate portal
   - Click "Skills" in left sidebar
   - Click "Add skill" or "Import skill"

2. **Upload Configuration:**
   - Click "Upload from file"
   - Select: `proactive-csi-agent.yaml`
   - Or drag and drop the YAML file

3. **Configure Skill:**
   - Name: "ProActive CSI - Agent 404"
   - Description: "Enterprise Revenue & Risk Intelligence Agent"
   - Version: 1.0.0

4. **Click "Import" or "Create"**

### **Method 2: Using Orchestrate CLI**

```bash
# Install Orchestrate CLI (if not already installed)
pip install ibm-watsonx-orchestrate

# Configure credentials (Updated)
export ORCHESTRATE_API_KEY="azE6dXNyXzBhYzkzMjI4LTE5YWMtMzhmNi1hY2VmLWRhYTEzYmU1NzYzYjpNUzNVUnVycVB6NWpBcTd5dUc5VEhreGduVWRLNndkY0I5TFhRMWpDRXdnPTpwczVM"
export ORCHESTRATE_URL="https://api.au-syd.watson-orchestrate.cloud.ibm.com/instances/f16c2181-a811-4d84-8e15-33cfebe50928"
export ORCHESTRATE_INSTANCE_ID="f16c2181-a811-4d84-8e15-33cfebe50928"
export ORCHESTRATE_REGION="au-syd"

# Deploy skill
orchestrate-cli skill create \
  --name "ProActive CSI" \
  --config proactive-csi-agent.yaml
```

---

## 🔗 Step 5: Connect IBM Services

In watsonx Orchestrate portal, connect your IBM services:

### **5.1 Natural Language Understanding (NLU)**

1. Go to: **Integrations → IBM Watson**
2. Click "Add Connection"
3. Select "Natural Language Understanding"
4. Enter credentials:
   ```
   API Key: JD1cdPcLQdymkID4sHav18lDXLd7U1FrTKDB2yllVLar
   URL: https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/79459c2d-4e21-4593-963e-6e9964afe1a3
   ```

### **5.2 Speech to Text**

1. Add another connection
2. Select "Speech to Text"
3. Enter credentials:
   ```
   API Key: qzNRq16Io8Dap9VR57CMw5jvbH3LUIWEQTEv20hJ-tc1
   URL: https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/ffcdbb0a-ca7b-4361-838b-cc8b6e4ac34c
   ```

### **5.3 Text to Speech**

1. Add connection
2. Select "Text to Speech"
3. Enter credentials:
   ```
   API Key: FLukjnaT1rf9qFnAhVbpi5D7HPMrvUst9POK8A-JShpz
   URL: https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/298e2b63-de83-427c-b77d-156c0976eed7
   ```

### **5.4 Cloudant Database**

1. Add connection
2. Select "Cloudant"
3. Parse credentials from: `../ibm-credentials_Cloudant_data.json`
   ```
   API Key: TalYEKH8YIFL1Hqu0Gx4QZP6IBE-43s8Cl2Fm7a-CyBK
   URL: https://f01bbce3-de41-430e-bd9b-5c00a082588a-bluemix.cloudantnosqldb.appdomain.cloud
   ```

### **5.5 Create Cloudant Database**

```bash
# Install Cloudant CLI or use web interface
curl -X PUT \
  "https://f01bbce3-de41-430e-bd9b-5c00a082588a-bluemix.cloudantnosqldb.appdomain.cloud/proactive_csi" \
  -u "f01bbce3-de41-430e-bd9b-5c00a082588a-bluemix:TalYEKH8YIFL1Hqu0Gx4QZP6IBE-43s8Cl2Fm7a-CyBK"
```

Or via web UI:
1. Go to: https://cloud.ibm.com/
2. Navigate to Cloudant instance
3. Click "Create Database"
4. Name: `proactive_csi`
5. Type: Standard

---

## 🧪 Step 6: Test Your Deployment

### **Test 1: Basic Skill Test**

In watsonx Orchestrate portal:

1. **Navigate to "Skills"**
2. **Find "ProActive CSI"**
3. **Click "Test"**
4. **Try these commands:**
   ```
   "What's my priority today?"
   "Show critical customers"
   "Analyze customer C-001"
   "Generate executive brief"
   ```

### **Test 2: Agent Communication Test**

Test multi-agent coordination:

1. **Go to "Workflows"**
2. **Find "Churn Prediction" workflow**
3. **Click "Run"**
4. **Input:** Customer ID: C-001
5. **Verify output:**
   - Churn probability calculated
   - Risk level identified
   - Interventions recommended

### **Test 3: Full Workflow Test**

Execute the complete Procurement-Customer Bridge workflow:

1. **Go to "Workflows"**
2. **Select "Procurement-Customer Impact Bridge"**
3. **Input:** Vendor ID: V-101
4. **Expected results:**
   - Vendor delay detected: 14 days
   - Affected customers identified: 2
   - ARR at risk: $107,171
   - Tasks created: 4
   - Execution time: <45 seconds

---

## 📊 Step 7: Upload Mock Data (Optional)

If you want to upload data to Cloudant:

```bash
cd /Users/ishwaryasridharan/Desktop/Hackathon_2025/Agentic_AI/agent404-proactive-csi

# Upload customer data
python3 << 'EOF'
import json
import pandas as pd
import requests
from requests.auth import HTTPBasicAuth

# Cloudant credentials
url = "https://f01bbce3-de41-430e-bd9b-5c00a082588a-bluemix.cloudantnosqldb.appdomain.cloud"
username = "f01bbce3-de41-430e-bd9b-5c00a082588a-bluemix"
apikey = "TalYEKH8YIFL1Hqu0Gx4QZP6IBE-43s8Cl2Fm7a-CyBK"

# Load customer data
customers = pd.read_csv('data/customer_success_data.csv')

# Upload each customer
for _, row in customers.iterrows():
    doc = row.to_dict()
    doc['_id'] = f"customer_{row['customer_id']}"
    doc['type'] = 'customer'
    
    response = requests.post(
        f"{url}/proactive_csi",
        auth=HTTPBasicAuth(username, apikey),
        json=doc
    )
    print(f"Uploaded {row['customer_id']}: {response.status_code}")

print("\n✅ Data upload complete!")
EOF
```

---

## 🎤 Step 8: Test Voice Commands (Optional)

If you want to test voice-first operations:

1. **In watsonx Orchestrate portal:**
   - Click microphone icon
   - Speak: "What's my priority today?"
   - Verify voice transcription works

2. **Test voice response:**
   - Enable audio output in settings
   - Run workflow
   - Listen for AI-generated voice responses

---

## 🔍 Step 9: Verify Deployment

### **Verification Checklist:**

- [ ] Skills uploaded to watsonx Orchestrate
- [ ] All 6 IBM services connected
- [ ] Cloudant database created
- [ ] Test workflows execute successfully
- [ ] Multi-agent coordination working
- [ ] Voice commands functional (if enabled)
- [ ] Data uploads successful (if done)

### **Quick Verification Commands:**

```bash
# Check Orchestrate connection
curl -X GET "$ORCHESTRATE_URL/skills" \
  -H "Authorization: Bearer $ORCHESTRATE_API_KEY"

# Check Cloudant database
curl -X GET \
  "https://f01bbce3-de41-430e-bd9b-5c00a082588a-bluemix.cloudantnosqldb.appdomain.cloud/proactive_csi/_all_docs" \
  -u "f01bbce3-de41-430e-bd9b-5c00a082588a-bluemix:TalYEKH8YIFL1Hqu0Gx4QZP6IBE-43s8Cl2Fm7a-CyBK"
```

---

## 🎬 Step 10: Run Demo on IBM Portal

### **Demo Scenario on IBM Portal:**

1. **Open watsonx Orchestrate chat interface**

2. **Start with greeting:**
   ```
   "Good morning, what's my priority today?"
   ```

3. **Analyze specific customer:**
   ```
   "Tell me about customer C-001"
   ```

4. **Check procurement issues:**
   ```
   "Show vendor delays"
   ```

5. **Execute full workflow:**
   ```
   "Run procurement impact analysis for vendor V-101"
   ```

6. **Generate executive brief:**
   ```
   "Generate daily executive brief"
   ```

### **What Judges Will See:**

- ✅ Natural language interaction
- ✅ Multi-agent coordination in real-time
- ✅ Data from actual IBM Cloudant
- ✅ Real NLU sentiment analysis
- ✅ Voice commands (if enabled)
- ✅ Professional IBM cloud deployment

---

## 🚨 Troubleshooting

### **Issue: Skill Upload Failed**

**Solution:**
- Check YAML syntax: `python3 -c "import yaml; yaml.safe_load(open('proactive-csi-agent.yaml'))"`
- Reduce YAML size if needed
- Try uploading in smaller sections

### **Issue: Service Connection Failed**

**Solution:**
- Verify credentials are correct
- Check service URLs are accessible
- Test credentials with curl:
  ```bash
  curl -u "apikey:YOUR_API_KEY" "SERVICE_URL/v1/analyze"
  ```

### **Issue: Workflow Execution Failed**

**Solution:**
- Check logs in Orchestrate portal
- Verify all services are connected
- Test individual agents locally first
- Check data format matches expected schema

### **Issue: Cloudant Connection Failed**

**Solution:**
- Verify database exists
- Check credentials
- Test with curl:
  ```bash
  curl "https://YOUR-CLOUDANT-URL.cloudantnosqldb.appdomain.cloud/_all_dbs" \
    -u "username:apikey"
  ```

---

## 📱 Alternative: Test with IBM Cloud Functions

If you want to deploy as serverless functions:

```bash
# Install IBM Cloud Functions CLI
ibmcloud plugin install cloud-functions

# Deploy Customer Success Agent
ibmcloud fn action create cs_agent \
  --kind python:3.11 \
  agents/customer_success_agent.py

# Deploy Procurement Agent
ibmcloud fn action create procurement_agent \
  --kind python:3.11 \
  agents/procurement_agent.py

# Deploy Revenue Agent
ibmcloud fn action create revenue_agent \
  --kind python:3.11 \
  agents/revenue_agent.py

# Test invocation
ibmcloud fn action invoke cs_agent --result
```

---

## 📊 Monitoring & Logs

### **View Logs in IBM Portal:**

1. Navigate to "Activity" or "Logs" section
2. Filter by skill: "ProActive CSI"
3. View execution logs
4. Monitor performance metrics

### **Enable Debug Mode:**

In your YAML config, add:
```yaml
debug: true
logging:
  level: debug
  output: cloudwatch
```

---

## 🎯 Success Metrics

After deployment, you should see:

- ✅ Skills appearing in watsonx Orchestrate
- ✅ Workflows executing successfully
- ✅ <2 second response time
- ✅ Multi-agent coordination visible
- ✅ Data flowing through Cloudant
- ✅ NLU sentiment analysis working
- ✅ Executive brief generation

---

## 🏆 Demo on IBM Portal for Judges

When presenting to judges:

1. **Show IBM watsonx Orchestrate interface** (professional!)
2. **Execute workflows directly on IBM portal**
3. **Demonstrate real-time multi-agent coordination**
4. **Show data in IBM Cloudant dashboard**
5. **Display NLU sentiment analysis results**
6. **Generate executive brief on-demand**

This proves:
- ✅ Production deployment (not just local)
- ✅ Real IBM integration (not mocked)
- ✅ Enterprise-ready (cloud-native)
- ✅ Scalable (IBM infrastructure)

---

## 📞 Quick Commands Reference

```bash
# Deploy to IBM
cd agent404-proactive-csi
./scripts/deploy_to_ibm.sh

# Check deployment status
ibmcloud fn action list

# View logs
ibmcloud fn activation logs --last

# Test on portal
# Go to: https://dl.watson-orchestrate.ibm.com/

# View Cloudant data
# Go to: https://cloud.ibm.com/ → Cloudant instance
```

---

## 🎉 You're Ready for IBM Portal Testing!

Follow these steps and you'll have ProActive CSI running on the actual IBM watsonx Orchestrate platform, ready to impress the judges!

---

<div align="center">

**ProActive CSI - Agent 404**  
*Deployed on IBM watsonx Orchestrate*

**🟢 READY FOR PRODUCTION**

</div>

