# 🧪 Testing Guide for ProActive_CSI_Agent_404

## 📍 Quick Access

**Web UI:** https://au-syd.watson-orchestrate.cloud.ibm.com/build/manage

---

## 🚀 Method 1: Web UI Testing (Recommended)

### Step 1: Open the Agent
1. Go to: https://au-syd.watson-orchestrate.cloud.ibm.com/build/manage
2. Click **"All agents"** in the left sidebar
3. Find and click on **"ProActive_CSI_Agent_404"** card
4. The agent chat interface will open

### Step 2: Test Queries

#### 🎯 Priority & Overview Queries
```
What's my priority today?
Show me critical customers at risk
What are the top 3 revenue risks?
Generate daily executive brief
```

#### 📊 Customer Success Intelligence
```
Which customers are at high churn risk?
Show me customers with negative sentiment
Analyze customer support ticket trends
What's the churn prediction for customer Acme Corp?
```

#### 💰 Revenue Protection
```
Calculate ARR at risk
Show me contract renewals coming up
What's the total revenue exposure?
Generate CFO briefing for this month
```

#### 🛒 Procurement Intelligence
```
Are there any vendor delays?
Show me procurement-customer impact analysis
Which vendors are causing customer issues?
What's the procurement early warning status?
```

#### 🔄 Workflow Testing
```
Run churn prediction workflow
Execute procurement early-warning workflow
Generate customer escalation report
Create contract renewal analysis
```

---

## 🖥️ Method 2: CLI Testing

### Test via Command Line

```bash
# Navigate to project
cd /Users/ishwaryasridharan/Desktop/Hackathon_2025/Agentic_AI/agent404-proactive-csi

# Ensure AU environment is active
orchestrate env activate production-au

# Test agent with a query
orchestrate agents chat --name "ProActive_CSI_Agent_404" --message "What's my priority today?"
```

### Example CLI Test Session

```bash
# Activate environment
orchestrate env activate production-au

# Start interactive chat
orchestrate agents chat --name "ProActive_CSI_Agent_404"
```

---

## 🧪 Method 3: Local Testing (Streamlit Demo)

### Run Local Demo

```bash
cd /Users/ishwaryasridharan/Desktop/Hackathon_2025/Agentic_AI/agent404-proactive-csi

# Install dependencies (if not already done)
pip install -r requirements.txt

# Run Streamlit demo
streamlit run app.py
```

Then open: http://localhost:8501

---

## 📋 Test Scenarios

### Scenario 1: Daily Executive Brief
**Query:** `Generate daily executive brief`

**Expected Response:**
- Summary of critical customers at risk
- Revenue exposure metrics
- Procurement delays and impact
- Action items and recommendations

### Scenario 2: Churn Prediction
**Query:** `Which customers are at high churn risk?`

**Expected Response:**
- List of customers with churn probability scores
- Risk factors identified
- Recommended interventions

### Scenario 3: Revenue Analysis
**Query:** `Calculate ARR at risk`

**Expected Response:**
- Total ARR at risk calculation
- Breakdown by customer
- Time-based risk analysis

### Scenario 4: Procurement Impact
**Query:** `Show me procurement-customer impact analysis`

**Expected Response:**
- Vendor delays identified
- Affected customers
- Revenue impact assessment
- Recommended actions

---

## ✅ Verification Checklist

- [ ] Agent appears in dashboard
- [ ] Agent chat interface opens
- [ ] Agent responds to queries
- [ ] Responses are relevant and contextual
- [ ] Multi-agent workflows execute correctly
- [ ] IBM service integrations work (NLU, Cloudant, etc.)

---

## 🐛 Troubleshooting

### Agent Not Responding
1. Check environment is active: `orchestrate env list`
2. Verify agent exists: `orchestrate agents list`
3. Check API key is valid

### No Response or Errors
1. Check browser console for errors
2. Verify IBM service credentials are correct
3. Check agent logs in Orchestrate UI

### Slow Responses
- Normal for complex multi-agent workflows
- First response may take 10-30 seconds
- Subsequent queries should be faster

---

## 📞 Support

If you encounter issues:
1. Check agent logs in Orchestrate UI
2. Verify all IBM service credentials
3. Ensure environment is correctly configured

---

## 🎯 Quick Test Commands

```bash
# Quick CLI test
orchestrate agents chat --name "ProActive_CSI_Agent_404" --message "Hello, what can you do?"

# List all agents
orchestrate agents list

# Check environment
orchestrate env list
```

---

**Happy Testing! 🚀**

