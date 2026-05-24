#!/usr/bin/env python3
"""
ProActive CSI - Fully Automated Deployment
Tries all methods to deploy automatically
"""

import os
import sys
import json
import requests
import subprocess
from pathlib import Path

# Colors
GREEN = '\033[0;32m'
BLUE = '\033[0;34m'
RED = '\033[0;31m'
YELLOW = '\033[1;33m'
NC = '\033[0m'

def print_header():
    print(f"\n{BLUE}{'='*70}{NC}")
    print(f"{BLUE}🚀 ProActive CSI - Fully Automated Deployment{NC}")
    print(f"{BLUE}{'='*70}{NC}\n")

def get_credentials():
    """Get all credentials"""
    creds = {}
    
    # From ibm_services.py
    creds['nlu'] = {
        'apikey': 'JD1cdPcLQdymkID4sHav18lDXLd7U1FrTKDB2yllVLar',
        'url': 'https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/79459c2d-4e21-4593-963e-6e9964afe1a3'
    }
    creds['stt'] = {
        'apikey': 'qzNRq16Io8Dap9VR57CMw5jvbH3LUIWEQTEv20hJ-tc1',
        'url': 'https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/ffcdbb0a-ca7b-4361-838b-cc8b6e4ac34c'
    }
    creds['tts'] = {
        'apikey': 'FLukjnaT1rf9qFnAhVbpi5D7HPMrvUst9POK8A-JShpz',
        'url': 'https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/298e2b63-de83-427c-b77d-156c0976eed7'
    }
    creds['cloudant'] = {
        'apikey': 'TalYEKH8YIFL1Hqu0Gx4QZP6IBE-43s8Cl2Fm7a-CyBK',
        'url': 'https://f01bbce3-de41-430e-bd9b-5c00a082588a-bluemix.cloudantnosqldb.appdomain.cloud'
    }
    
    # Orchestrate from config
    config_file = Path("config/orchestrate_credentials.json")
    if config_file.exists():
        with open(config_file, 'r') as f:
            config = json.load(f)
            if 'watsonx_orchestrate' in config:
                creds['orchestrate'] = config['watsonx_orchestrate']
    
    # Try .env file
    env_file = Path("../.env")
    if not env_file.exists():
        env_file = Path(".env")
    if env_file.exists():
        with open(env_file, 'r') as f:
            for line in f:
                if 'WATSONX_API_KEY' in line or 'ORCHESTRATE_API_KEY' in line:
                    key = line.split('=')[1].strip()
                    if 'orchestrate' not in creds:
                        creds['orchestrate'] = {}
                    creds['orchestrate']['api_key'] = key
    
    return creds

def deploy_via_curl(creds, yaml_file):
    """Try deploying via curl/HTTP"""
    print(f"{BLUE}🌐 Attempting HTTP API deployment...{NC}")
    
    if 'orchestrate' not in creds:
        print(f"{RED}❌ No Orchestrate credentials found{NC}")
        return False
    
    api_key = creds['orchestrate'].get('api_key', '')
    service_url = creds['orchestrate'].get('service_url', '')
    
    if not api_key or not service_url:
        print(f"{RED}❌ Missing Orchestrate credentials{NC}")
        return False
    
    # Read YAML file
    with open(yaml_file, 'r') as f:
        yaml_content = f.read()
    
    # Try different endpoints
    endpoints = [
        f"{service_url}/api/v1/agents",
        f"{service_url}/v1/agents",
        f"{service_url}/agents",
        f"{service_url}/api/v1/skills",
        f"{service_url}/v1/skills",
    ]
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/yaml"
    }
    
    for endpoint in endpoints:
        try:
            print(f"{BLUE}   Trying: {endpoint}{NC}")
            response = requests.post(
                endpoint,
                headers=headers,
                data=yaml_content,
                timeout=30
            )
            
            if response.status_code in [200, 201, 202]:
                print(f"{GREEN}✅ Deployment successful via HTTP!{NC}")
                print(f"{GREEN}   Status: {response.status_code}{NC}")
                return True
            else:
                print(f"{YELLOW}   Status {response.status_code}: {response.text[:100]}{NC}")
        except Exception as e:
            print(f"{YELLOW}   Error: {str(e)[:50]}...{NC}")
            continue
    
    return False

def deploy_via_cli_auto(creds, yaml_file):
    """Try deploying via CLI with automatic key input"""
    print(f"{BLUE}🤖 Attempting CLI deployment with auto-key...{NC}")
    
    if 'orchestrate' not in creds:
        return False
    
    api_key = creds['orchestrate'].get('api_key', '')
    service_url = creds['orchestrate'].get('service_url', '')
    
    if not api_key:
        return False
    
    # Check if orchestrate CLI exists
    if not subprocess.run(['which', 'orchestrate'], capture_output=True).returncode == 0:
        print(f"{YELLOW}⚠️  Orchestrate CLI not found, installing...{NC}")
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'ibm-watsonx-orchestrate'], 
                      capture_output=True)
    
    # Try to activate environment with API key
    print(f"{BLUE}   Activating environment...{NC}")
    
    # Use environment variable method
    env = os.environ.copy()
    env['ORCHESTRATE_API_KEY'] = api_key
    env['ORCHESTRATE_URL'] = service_url
    
    # Try to set environment and deploy
    try:
        # First, try to add/update environment
        result = subprocess.run(
            ['orchestrate', 'env', 'add', '-n', 'production-au', 
             '-u', service_url, '--type', 'ibm_iam'],
            input=api_key.encode(),
            capture_output=True,
            timeout=30
        )
        
        # Then activate
        result = subprocess.run(
            ['orchestrate', 'env', 'activate', 'production-au'],
            input=api_key.encode(),
            capture_output=True,
            timeout=30
        )
        
        if result.returncode == 0:
            print(f"{GREEN}✅ Environment activated{NC}")
            
            # Deploy
            result = subprocess.run(
                ['orchestrate', 'agents', 'import', '--file', yaml_file],
                capture_output=True,
                timeout=30
            )
            
            if result.returncode == 0:
                print(f"{GREEN}✅ Deployment successful via CLI!{NC}")
                return True
            else:
                print(f"{YELLOW}   CLI deployment error: {result.stderr.decode()[:100]}{NC}")
    except Exception as e:
        print(f"{YELLOW}   Error: {str(e)[:50]}...{NC}")
    
    return False

def deploy_via_ibmcloud_cli(creds, yaml_file):
    """Try deploying via ibmcloud CLI"""
    print(f"{BLUE}☁️  Attempting IBM Cloud CLI deployment...{NC}")
    
    if not subprocess.run(['which', 'ibmcloud'], capture_output=True).returncode == 0:
        print(f"{YELLOW}⚠️  IBM Cloud CLI not found{NC}")
        return False
    
    # Check if logged in
    result = subprocess.run(['ibmcloud', 'target'], capture_output=True, text=True)
    if 'Not logged in' in result.stdout or result.returncode != 0:
        print(f"{YELLOW}⚠️  Not logged in to IBM Cloud{NC}")
        return False
    
    print(f"{GREEN}✅ IBM Cloud CLI ready{NC}")
    # IBM Cloud CLI doesn't have direct orchestrate deployment, so skip
    return False

def main():
    print_header()
    
    # Change to project directory
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    print(f"{BLUE}Project directory: {os.getcwd()}{NC}\n")
    
    # Get credentials
    print(f"{BLUE}📋 Loading credentials...{NC}")
    creds = get_credentials()
    print(f"{GREEN}✅ Credentials loaded{NC}\n")
    
    # Check YAML file
    yaml_file = "proactive-csi-agent-orchestrate.yaml"
    if not Path(yaml_file).exists():
        print(f"{RED}❌ Configuration file not found: {yaml_file}{NC}")
        return 1
    
    print(f"{GREEN}✅ Configuration file found: {yaml_file}{NC}\n")
    
    # Try deployment methods
    success = False
    
    # Method 1: HTTP API
    if not success:
        success = deploy_via_curl(creds, yaml_file)
    
    # Method 2: CLI with auto-key
    if not success:
        success = deploy_via_cli_auto(creds, yaml_file)
    
    # Method 3: IBM Cloud CLI
    if not success:
        success = deploy_via_ibmcloud_cli(creds, yaml_file)
    
    if success:
        print(f"\n{GREEN}{'='*70}{NC}")
        print(f"{GREEN}✅ DEPLOYMENT SUCCESSFUL!{NC}")
        print(f"{GREEN}{'='*70}{NC}\n")
        
        print(f"{BLUE}Next steps:{NC}")
        print("1. Open: https://cloud.ibm.com/watsonx/orchestrate")
        print("2. Find your agent: ProActive_CSI_Agent_404")
        print("3. Test with: 'Good morning, what's my priority today?'")
        return 0
    else:
        print(f"\n{YELLOW}{'='*70}{NC}")
        print(f"{YELLOW}⚠️  Automated deployment not available{NC}")
        print(f"{YELLOW}{'='*70}{NC}\n")
        
        print(f"{BLUE}IBM watsonx Orchestrate requires manual upload via Web UI{NC}\n")
        print(f"{GREEN}Quick steps:{NC}")
        print("1. Go to: https://cloud.ibm.com/watsonx/orchestrate")
        print(f"2. Upload: {os.path.abspath(yaml_file)}")
        print("3. Connect services using credentials from ibm_services.py")
        print("4. Activate and test\n")
        
        # Open browser
        import webbrowser
        webbrowser.open("https://cloud.ibm.com/watsonx/orchestrate")
        print(f"{GREEN}✅ Browser opened with IBM Portal{NC}\n")
        
        return 0

if __name__ == "__main__":
    sys.exit(main())

