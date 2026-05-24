#!/usr/bin/env python3
"""
Fully Automated Deployment via IBM watsonx Orchestrate REST API
- Uploads data to Cloudant automatically
- Deploys agent via REST API
- Verifies deployment
"""

import requests
import json
import os
import sys
from pathlib import Path

# Colors
GREEN = '\033[0;32m'
BLUE = '\033[0;34m'
RED = '\033[0;31m'
YELLOW = '\033[1;33m'
NC = '\033[0m'

def print_header():
    print("\n╔═══════════════════════════════════════════════════════════════╗")
    print("║  🚀 AUTOMATED DEPLOYMENT VIA REST API                        ║")
    print("╚═══════════════════════════════════════════════════════════════╝\n")

def load_env():
    """Load environment variables"""
    env_file = Path(__file__).parent.parent / ".env"
    if env_file.exists():
        with open(env_file, 'r') as f:
            for line in f:
                if '=' in line and not line.strip().startswith('#'):
                    key, value = line.strip().split('=', 1)
                    os.environ[key] = value.strip().strip('"').strip("'")
        print(f"{GREEN}✅ Environment variables loaded{NC}")
        return True
    return False

def upload_data_to_cloudant():
    """Upload CSV data to Cloudant"""
    print(f"\n{BLUE}📊 Step 1: Uploading data to Cloudant...{NC}")
    print("━" * 70)
    
    upload_script = Path(__file__).parent / "scripts" / "upload_data_to_cloudant.py"
    if upload_script.exists():
        import subprocess
        result = subprocess.run(
            [sys.executable, str(upload_script)],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            print(f"{GREEN}✅ Data uploaded to Cloudant{NC}")
            return True
        else:
            print(f"{YELLOW}⚠️  Data upload had issues: {result.stderr[:200]}{NC}")
            return False
    else:
        print(f"{YELLOW}⚠️  Upload script not found, skipping{NC}")
        return False

def get_iam_token(api_key):
    """Get IAM token from API key"""
    print(f"\n{BLUE}🔑 Step 2: Getting IAM token...{NC}")
    print("━" * 70)
    
    try:
        response = requests.post(
            "https://iam.cloud.ibm.com/identity/token",
            data={
                "grant_type": "urn:ibm:params:oauth:grant-type:apikey",
                "apikey": api_key
            },
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            timeout=10
        )
        
        if response.status_code == 200:
            token = response.json().get("access_token")
            print(f"{GREEN}✅ IAM token obtained{NC}")
            return token
        else:
            print(f"{RED}❌ Failed to get IAM token: {response.status_code}{NC}")
            return None
    except Exception as e:
        print(f"{RED}❌ Error getting IAM token: {e}{NC}")
        return None

def deploy_agent_via_api(api_key, service_url, agent_file):
    """Deploy agent using REST API"""
    print(f"\n{BLUE}🚀 Step 3: Deploying agent via REST API...{NC}")
    print("━" * 70)
    
    # Get IAM token
    token = get_iam_token(api_key)
    if not token:
        print(f"{YELLOW}⚠️  Could not get IAM token, trying direct API key...{NC}")
        token = api_key
    
    # Read agent YAML file
    if not agent_file.exists():
        print(f"{RED}❌ Agent file not found: {agent_file}{NC}")
        return False
    
    with open(agent_file, 'r') as f:
        agent_yaml = f.read()
    
    print(f"{BLUE}  Agent file loaded: {len(agent_yaml)} bytes{NC}")
    
    # Try different API endpoints
    endpoints = [
        f"{service_url}/v1/skills",
        f"{service_url}/api/v1/skills",
        f"{service_url}/skills",
        f"{service_url}/v1/agents",
    ]
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/yaml"
    }
    
    for endpoint in endpoints:
        try:
            print(f"{BLUE}  Trying endpoint: {endpoint}{NC}")
            response = requests.post(
                endpoint,
                headers=headers,
                data=agent_yaml,
                timeout=30
            )
            
            print(f"{BLUE}  Response: {response.status_code}{NC}")
            
            if response.status_code in [200, 201, 202]:
                print(f"{GREEN}✅ Agent deployed successfully!{NC}")
                try:
                    result = response.json()
                    print(f"{BLUE}  Deployment ID: {result.get('id', 'N/A')}{NC}")
                except:
                    print(f"{BLUE}  Response: {response.text[:200]}{NC}")
                return True
            elif response.status_code == 401:
                print(f"{YELLOW}  Authentication failed, trying next endpoint...{NC}")
                continue
            elif response.status_code == 404:
                print(f"{YELLOW}  Endpoint not found, trying next...{NC}")
                continue
            else:
                print(f"{YELLOW}  Response: {response.status_code} - {response.text[:200]}{NC}")
        except Exception as e:
            print(f"{YELLOW}  Error: {str(e)[:200]}{NC}")
            continue
    
    print(f"{YELLOW}⚠️  API deployment not available, agent file is ready for manual upload{NC}")
    return False

def main():
    """Main deployment function"""
    print_header()
    
    # Load environment
    load_env()
    
    # Get credentials
    api_key = os.getenv('ORCHESTRATE_API_KEY', 'IYKkTGru14JfJWkl_G7xh6Y4UTa4qSPYPZE5M0Smk4AV')
    service_url = os.getenv('ORCHESTRATE_ENDPOINT', 
                           'https://api.au-syd.watson-orchestrate.cloud.ibm.com/instances/f16c2181-a811-4d84-8e15-33cfebe50928')
    
    if not api_key:
        print(f"{RED}❌ ORCHESTRATE_API_KEY not found{NC}")
        return 1
    
    # Upload data
    upload_data_to_cloudant()
    
    # Deploy agent
    agent_file = Path(__file__).parent / "proactive-csi-agent-orchestrate.yaml"
    deploy_agent_via_api(api_key, service_url, agent_file)
    
    # Summary
    print(f"\n{GREEN}═══════════════════════════════════════════════════════════════{NC}")
    print(f"{GREEN}✅ AUTOMATED DEPLOYMENT ATTEMPT COMPLETE!{NC}")
    print(f"{GREEN}═══════════════════════════════════════════════════════════════{NC}")
    print("")
    print(f"{BLUE}Note: IBM watsonx Orchestrate may require manual upload via Web UI{NC}")
    print(f"{BLUE}Your agent file is ready: proactive-csi-agent-orchestrate.yaml{NC}")
    print("")
    print(f"{BLUE}Access Portal:{NC}")
    print("  https://cloud.ibm.com/watsonx/orchestrate")
    print("")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())

