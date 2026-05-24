<!-- PROJECT TITLE -->
  <h1 align="center">RETENX</h1>
 <div id="header" align="center">
</div>
<h2 align="center">
 Description
</h2>
<p align="center"> <strong>Introducing RETENX:</strong>
  An AI-powered multi-agent system that proactively detects hidden customer, procurement, and financial risks before they escalate, enabling enterprise teams to act intelligently and prevent revenue loss. With early churn prediction, risk correlation across departments, and autonomous workflow execution, RetenX transforms manual intervention into proactive action—delivering alerts, task automation, and executive briefings to protect customer relationships and business growth. </p>

  <p align="center"> <strong>Built to Win | Built for Enterprise | Built on IBM watsonx</strong></p>

<p align="center"> 
  
[![IBM watsonx](https://img.shields.io/badge/IBM-watsonx-blue)]()
[![Multi-Agent](https://img.shields.io/badge/Architecture-Multi--Agent-green)]()
[![Workflows](https://img.shields.io/badge/Workflows-6-orange)]()
[![Revenue Protected](https://img.shields.io/badge/Revenue%20Protected-%24612K-success)]() </p>

## Table of Contents

<details>
<summary>RETENX</summary>
  
- [Application Description](#application-description)
- [Table of Contents](#table-of-contents)
- [Contributing](#contributing)
- [Authors](#authors)
- [License](#license)

</details>

## TRY the prototype
[RETENX](https://RETENX.vercel.app/)

---

## 🎯 Problem Statement

Enterprises are losing **millions in revenue** because:

- 💔 **Churn signals are invisible** until it's too late
- 📦 **Procurement risks** trigger customer frustration  
- 👥 **Customer Success teams operate manually** with no unified intelligence
- 💰 **No proactive revenue protection** system exists
- 🔗 **Disconnected systems** lead to slow, scattered interventions

**Result:** 18% annual churn rate, $millions lost, reactive (not proactive) customer success.

---

## 💡 Solution Statement
A **three-agent AI system** built on **IBM watsonx Orchestrate** that:

✅ **Predicts customer churn** 30-60 days early (89% accuracy)  
✅ **Detects procurement risks** that affect customers  
✅ **Calculates revenue at risk** in real-time  
✅ **Triggers autonomous interventions** across 13+ enterprise systems  
✅ **Coordinates 3 intelligent agents** (CS, Procurement, Revenue)  
✅ **Generates executive briefings** automatically  
✅ **Voice-first operations** for hands-free management

---

## Technology Stack

| Technology | Description                 |
| ---------- | --------------------------- |
| Python     | Programming Language        |
| watsonx.ai      | Churn prediction, LLM reasoning, intervention recommendations.           |
| watsonx Orchestrate     | Multi-agent coordination & workflow execution.  |
| Natural Language Understanding (NLU)	    |Sentiment & emotion analysis. |
| Speech-to-Text    | Voice-first operations. |
|Text-to-Speech| Voice responses & briefings.|
|Cloudant|  Customer health data & analytics storage.|

## Features

### 1️⃣ **Customer Success Intelligence Agent**
- Predicts churn probability using watsonx.ai
- Analyzes sentiment using IBM NLU
- Extracts customer health signals
- Recommends interventions automatically
- Voice-first operations (STT/TTS)

### 2️⃣ **Procurement Intelligence Agent**
- Monitors vendor performance
- Predicts delivery delays
- Flags contract risks
- Correlates vendor issues → customer impact
- Triggers cross-team escalation tasks

### 3️⃣ **Revenue Protection Agent**
- Calculates ARR/MRR at risk
- Monitors contract value exposure
- Generates CFO briefings
- 🎯 Recommends intervention investments
- Models financial scenarios

**Orchestration Layer:** IBM watsonx Orchestrate coordinates all 3 agents
  

---

## 🚀 Quick Start

### **Option 1: Run Demo Locally (2 minutes)**

```bash
cd agent404-proactive-csi
./scripts/run_demo.sh
```

Open: **http://localhost:8501**

### **Option 2: Deploy to IBM watsonx Orchestrate (5 minutes)**

```bash
cd agent404-proactive-csi
./scripts/deploy_to_ibm.sh
```

Then open: **https://dl.watson-orchestrate.ibm.com/**

### **Option 3: Test Agents Only**

```bash
cd agent404-proactive-csi
./scripts/test_agents.sh
```

---

## 🧪 Testing

### **Run All Tests**

```bash
python3 -m pytest tests/
```

### **Test Individual Agents**

```python
# Test Customer Success Agent
from agents.customer_success_agent import CustomerSuccessAgent
cs_agent = CustomerSuccessAgent()
critical = cs_agent.get_critical_customers()
print(f"Critical customers: {len(critical)}")

# Test churn prediction
churn_prob = cs_agent.predict_churn_probability("C-001")
print(f"Churn probability: {churn_prob*100:.1f}%")
```

### **Test Workflows**

```python
from workflows.orchestrator import WorkflowOrchestrator
orchestrator = WorkflowOrchestrator()

# Execute churn prediction workflow
result = orchestrator.workflow_churn_prediction("C-001")
print(f"Workflow completed: {len(result['steps'])} steps")

# Execute daily executive brief
brief = orchestrator.workflow_daily_executive_brief()
print(brief['executive_brief'])
```

---

## 🙏 Acknowledgments

- **IBM watsonx Team** - For incredible AI services
- **IBM watsonx Orchestrate Team** - For the powerful orchestration platform
- **Hackathon Organizers** - For the opportunity


## Authors

| Name                   | Link                                                              | Role                                           |
| ---------------------- | ---------------------------------------------------------------  | ---------------------------------------------- |
| Sridharan Kaliyamoorthy | [GitHub](https://github.com/sridharankaliyamoorthy)              | Project Lead, AI Automation Engineer & Python Developer |
| Sandra Ashipala        | [GitHub](https://github.com/sandramsc)                           | Project Manager                                |
| Piotr Karmelita        | [GitHub](https://github.com/p-karmelita)                         | Backend & Data                                 |

Sources


⭐ **If ProActive CSI inspired you, please star this repo!** ⭐

## License

[![GitLicense](https://img.shields.io/badge/License-MIT-lime.svg)](https://github.com/sandramsc/RETENX/blob/main/LICENSE)
