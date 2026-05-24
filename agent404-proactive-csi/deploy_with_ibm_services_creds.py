#!/usr/bin/env python3
"""
ProActive CSI - Deployment using credentials from ibm_services.py
Extracts all credentials and deploys to IBM watsonx Orchestrate
"""

import os
import sys
import re
import subprocess
from pathlib import Path

# Colors
GREEN = '\033[0;32m'
BLUE = '\033[0;34m'
RED = '\033[0;31m'
YELLOW = '\033[1;33m'
NC = '\033[0m'

def extract_credentials():
    """Extract credentials from ibm_services.py"""
    print(f"{BLUE}📋 Extracting credentials from ibm_services.py...{NC}")
    
    services_file = Path("integrations/ibm_services.py")
    if not services_file.exists():
        print(f"{RED}❌ ibm_services.py not found{NC}")
        return None
    
    with open(services_file, 'r') as f:
        content = f.read()
    
    credentials = {}
    
    # Extract NLU
    nlu_key_match = re.search(r"NATURAL_LANGUAGE_UNDERSTANDING_APIKEY.*?'([^']+)'", content)
    nlu_url_match = re.search(r"NATURAL_LANGUAGE_UNDERSTANDING_URL.*?'([^']+)'", content)
    if nlu_key_match and nlu_url_match:
        credentials['nlu'] = {
            'apikey': nlu_key_match.group(1),
            'url': nlu_url_match.group(1)
        }
    
    # Extract STT
    stt_key_match = re.search(r"SPEECH_TO_TEXT_APIKEY.*?'([^']+)'", content)
    stt_url_match = re.search(r"SPEECH_TO_TEXT_URL.*?'([^']+)'", content)
    if stt_key_match and stt_url_match:
        credentials['stt'] = {
            'apikey': stt_key_match.group(1),
            'url': stt_url_match.group(1)
        }
    
    # Extract TTS
    tts_key_match = re.search(r"TEXT_TO_SPEECH_APIKEY.*?'([^']+)'", content)
    tts_url_match = re.search(r"TEXT_TO_SPEECH_URL.*?'([^']+)'", content)
    if tts_key_match and tts_url_match:
        credentials['tts'] = {
            'apikey': tts_key_match.group(1),
            'url': tts_url_match.group(1)
        }
    
    # Extract Cloudant
    cloudant_key_match = re.search(r'"apikey":\s*"([^"]+)"', content)
    cloudant_url_match = re.search(r'"url":\s*"([^"]+)"', content)
    if cloudant_key_match and cloudant_url_match:
        credentials['cloudant'] = {
            'apikey': cloudant_key_match.group(1),
            'url': cloudant_url_match.group(1)
        }
    
    # Orchestrate credentials from config file
    config_file = Path("config/orchestrate_credentials.json")
    if config_file.exists():
        import json
        with open(config_file, 'r') as f:
            config = json.load(f)
            if 'watsonx_orchestrate' in config:
                credentials['orchestrate'] = config['watsonx_orchestrate']
    
    print(f"{GREEN}✅ Credentials extracted{NC}")
    return credentials

def display_credentials(creds):
    """Display extracted credentials (masked)"""
    print(f"\n{BLUE}📋 Service Credentials:{NC}")
    if 'nlu' in creds:
        print(f"  ✅ NLU: {creds['nlu']['url']}")
        print(f"     API Key: {creds['nlu']['apikey'][:10]}...")
    if 'stt' in creds:
        print(f"  ✅ STT: {creds['stt']['url']}")
        print(f"     API Key: {creds['stt']['apikey'][:10]}...")
    if 'tts' in creds:
        print(f"  ✅ TTS: {creds['tts']['url']}")
        print(f"     API Key: {creds['tts']['apikey'][:10]}...")
    if 'cloudant' in creds:
        print(f"  ✅ Cloudant: {creds['cloudant']['url']}")
        print(f"     API Key: {creds['cloudant']['apikey'][:10]}...")
    if 'orchestrate' in creds:
        print(f"  ✅ Orchestrate: {creds['orchestrate']['service_url']}")
        print(f"     API Key: {creds['orchestrate']['api_key'][:20]}...")
    print("")

def deploy_agent(creds):
    """Deploy agent using CLI"""
    print(f"{BLUE}🚀 Deploying agent to IBM watsonx Orchestrate...{NC}\n")
    
    # Check if orchestrate CLI is installed
    if not subprocess.run(['which', 'orchestrate'], capture_output=True).returncode == 0:
        print(f"{RED}❌ Orchestrate CLI not found{NC}")
        print(f"{YELLOW}Installing...{NC}")
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'ibm-watsonx-orchestrate'])
    
    # Check YAML file
    yaml_file = "proactive-csi-agent-orchestrate.yaml"
    if not Path(yaml_file).exists():
        print(f"{RED}❌ Configuration file not found: {yaml_file}{NC}")
        return False
    
    print(f"{GREEN}✅ Configuration file found{NC}\n")
    
    # Check environment
    result = subprocess.run(['orchestrate', 'env', 'list'], capture_output=True, text=True)
    if 'production-au' not in result.stdout:
        print(f"{YELLOW}⚠️  Creating production-au environment...{NC}")
        if 'orchestrate' in creds:
            url = creds['orchestrate']['service_url']
            subprocess.run(['orchestrate', 'env', 'add', '-n', 'production-au', 
                          '-u', url, '--type', 'ibm_iam'])
    
    # Activate environment
    print(f"{BLUE}🔑 Activating environment...{NC}")
    if 'orchestrate' in creds:
        api_key = creds['orchestrate']['api_key']
        print(f"{YELLOW}Using API key from credentials...{NC}")
        print(f"{BLUE}Note: You may need to enter this manually if auto-activation fails{NC}\n")
    
    # Try to deploy
    print(f"{BLUE}Deploying agent...{NC}")
    result = subprocess.run(['orchestrate', 'agents', 'import', '--file', yaml_file], 
                          capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"\n{GREEN}═══════════════════════════════════════════════════════════════{NC}")
        print(f"{GREEN}✅ DEPLOYMENT SUCCESSFUL!{NC}")
        print(f"{GREEN}═══════════════════════════════════════════════════════════════{NC}\n")
        
        # Verify
        print(f"{BLUE}Verifying deployment...{NC}")
        subprocess.run(['orchestrate', 'agents', 'list'])
        
        print(f"\n{GREEN}🎉 Agent deployed successfully!{NC}\n")
        print(f"{BLUE}Next steps:{NC}")
        print("1. Open IBM Portal: https://cloud.ibm.com/watsonx/orchestrate")
        print("2. Find your agent: ProActive_CSI_Agent_404")
        print("3. Connect services in Connections tab")
        print("4. Test with: 'Good morning, what's my priority today?'")
        return True
    else:
        print(f"\n{RED}❌ Deployment failed{NC}")
        print(f"{YELLOW}Error:{NC}")
        print(result.stderr)
        print(f"\n{YELLOW}Note: If API key is invalid, get a new one from:{NC}")
        print("https://cloud.ibm.com/iam/apikeys")
        print(f"\n{YELLOW}Or use Web UI deployment (more reliable):{NC}")
        print("1. Go to: https://cloud.ibm.com/watsonx/orchestrate")
        print("2. Upload: proactive-csi-agent-orchestrate.yaml")
        return False

def main():
    print(f"\n{BLUE}{'='*70}{NC}")
    print(f"{BLUE}🚀 ProActive CSI - Deployment with ibm_services.py Credentials{NC}")
    print(f"{BLUE}{'='*70}{NC}\n")
    
    # Extract credentials
    creds = extract_credentials()
    if not creds:
        return 1
    
    # Display credentials
    display_credentials(creds)
    
    # Deploy
    success = deploy_agent(creds)
    
    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main())

