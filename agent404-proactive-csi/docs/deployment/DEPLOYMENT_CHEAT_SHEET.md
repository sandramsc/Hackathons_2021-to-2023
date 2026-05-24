# 📋 Deployment Cheat Sheet

**Quick reference for deploying ProActive CSI Agent 404**

---

## 🚀 One-Command Deployment

```bash
cd /Users/ishwaryasridharan/Desktop/Hackathon_2025/Agentic_AI/agent404-proactive-csi && ./scripts/deployment/quick_deploy.sh
```

When prompted, enter API key: `9-atsNvf8mx0ymZLaGgZwe28rhyZvLcX_QUQlyDb12rg`

---

## 📝 Manual Deployment Steps

### 1. Activate Environment
```bash
cd /Users/ishwaryasridharan/Desktop/Hackathon_2025/Agentic_AI/agent404-proactive-csi
orchestrate env activate production-au
# Enter API key: 9-atsNvf8mx0ymZLaGgZwe28rhyZvLcX_QUQlyDb12rg
```

### 2. Deploy Agent
```bash
orchestrate agents import -f proactive-csi-agent-orchestrate.yaml
```

### 3. Verify
```bash
orchestrate agents list | grep proactive
```

### 4. Access
Open: https://au-syd.watson-orchestrate.cloud.ibm.com/build/manage

---

## 🔑 Credentials Quick Reference

**Orchestrate (AU):**
- API Key: `9-atsNvf8mx0ymZLaGgZwe28rhyZvLcX_QUQlyDb12rg`
- URL: `https://api.au-syd.watson-orchestrate.cloud.ibm.com/instances/f16c2181-a811-4d84-8e15-33cfebe50928`
- Web UI: https://au-syd.watson-orchestrate.cloud.ibm.com/build/manage

**TTS:**
- API Key: `FLukjnaT1rf9qFnAhVbpi5D7HPMrvUst9POK8A-JShpz`
- Instance ID: `298e2b63-de83-427c-b97d-156c0976eed7` (⚠️ note: `b97d` not `b77d`)

---

## ⚠️ Common Mistakes to Avoid

1. ❌ **Don't use `--type mcsp`** - Use default authentication
2. ❌ **Don't forget `watsonx/` prefix** - LLM must be `watsonx/meta-llama/...`
3. ❌ **Wrong instance ID** - TTS must be `b97d` not `b77d`
4. ❌ **Wrong environment** - Must be `production-au` for AU region

---

## ✅ Success Checklist

- [ ] Environment activated: `orchestrate env list` shows `production-au (active)`
- [ ] Agent deployed: `orchestrate agents list` shows `ProActive_CSI_Agent_404`
- [ ] Agent accessible: Visible in web UI at AU-Sydney URL
- [ ] Agent responds: Test query returns response
- [ ] Services mentioned: Agent mentions IBM Watson services

---

## 🆘 Quick Troubleshooting

**"Scope not found":**
- ✅ Remove `--type mcsp` flag
- ✅ Use default authentication

**"Invalid provider value":**
- ✅ Add `watsonx/` prefix to LLM model

**Agent not visible:**
- ✅ Hard refresh browser (Cmd+Shift+R)
- ✅ Check correct URL (AU-Sydney)
- ✅ Verify environment: `orchestrate env list`

---

## 📚 Full Documentation

See: `docs/deployment/IBM_DEPLOYMENT_GUIDE.md` for complete guide

---

**Quick Deploy Script:** `./scripts/deployment/quick_deploy.sh`

