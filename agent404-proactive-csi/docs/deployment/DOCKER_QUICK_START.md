# 🐳 Docker Quick Start - Deploy to IBM

**Fastest way to deploy ProActive CSI Agent 404 to IBM using Docker**

---

## ⚡ One-Command Deployment

```bash
cd /Users/ishwaryasridharan/Desktop/Hackathon_2025/Agentic_AI/agent404-proactive-csi
./scripts/docker/deploy_ibm_docker.sh
```

**That's it!** The script handles everything.

---

## 📋 What You Need

1. ✅ Docker installed and running
2. ✅ Credentials file: `ibm-credentials_Orchestrate_data_Updated.json`
3. ✅ Agent config: `proactive-csi-agent-orchestrate.yaml`

---

## 🚀 Quick Commands

### Deploy to IBM
```bash
./scripts/docker/deploy_ibm_docker.sh
```

### Build Only
```bash
docker-compose -f docker-compose.ibm.yml build
```

### Deploy Manually
```bash
docker-compose -f docker-compose.ibm.yml up
```

### Clean Up
```bash
docker-compose -f docker-compose.ibm.yml down
```

---

## ✅ Success

After deployment, you'll see:
```
✅ Agent deployed successfully!
🌐 Access your agent at:
   https://au-syd.watson-orchestrate.cloud.ibm.com/build/manage
```

---

## 🆘 Troubleshooting

**Docker not running?**
```bash
# Mac/Windows: Start Docker Desktop
# Linux: sudo systemctl start docker
```

**Permission denied?**
```bash
chmod +x scripts/docker/*.sh
```

---

**Full Guide:** `docs/deployment/DOCKER_IBM_DEPLOYMENT.md`

