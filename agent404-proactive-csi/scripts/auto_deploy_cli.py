#!/usr/bin/env python3
"""
ProActive CSI - Automated CLI Deployment v1.2.0
Automatically deploys agent to IBM watsonx Orchestrate via CLI/API
"""

import requests
import json
import os
import sys
import subprocess
import webbrowser
from pathlib import Path

# Colors for terminal output
class Colors:
    GREEN = '\033[0;32m'
    BLUE = '\033[0;34m'
    RED = '\033[0;31m'
    YELLOW = '\033[1;33m'
    NC = '\033[0m'  # No Color

def print_header():
    print("\n" + "="*70)
    print("🚀 ProActive CSI - Automated CLI Deployment v1.2.0")
    print("   STT & TTS Audio Integration")
    print("="*70 + "\n")

def load_credentials():
    """Load IBM watsonx Orchestrate credentials"""
    print(f"{Colors.BLUE}📋 Loading credentials...{Colors.NC}")
    
    # Try multiple credential file locations
    cred_paths = [
        "../ibm-credentials_Orchestrate_data_Updated.json",
        "../ibm-credentials_Orchestrate_data.json",
        "config/orchestrate_credentials.json",
        os.path.join(os.path.dirname(os.path.dirname(__file__)), "..", "ibm-credentials_Orchestrate_data_Updated.json")
    ]
    
    credentials = None
    for path in cred_paths:
        try:
            full_path = os.path.abspath(path)
            if os.path.exists(full_path):
                with open(full_path, 'r') as f:
                    content = f.read().strip()
                    # Skip RTF files
                    if content.startswith('{\\rtf'):
                        continue
                    # Try parsing as JSON
                    if content.startswith('{'):
                        credentials = json.loads(content)
                    else:
                        # Might be quoted JSON string
                        credentials = json.loads(content.strip('"'))
                    print(f"{Colors.GREEN}✅ Credentials loaded from: {path}{Colors.NC}")
                    break
        except Exception as e:
            continue
    
    if not credentials:
        # Use hardcoded credentials as fallback
        print(f"{Colors.YELLOW}⚠️  Using fallback credentials{Colors.NC}")
        credentials = {
            "watsonx_orchestrate": {
                "api_key": "azE6dXNyXzBhYzkzMjI4LTE5YWMtMzhmNi1hY2VmLWRhYTEzYmU1NzYzYjpNUzNVUnVycVB6NWpBcTd5dUc5VEhreGduVWRLNndkY0I5TFhRMWpDRXdnPTpwczVM",
                "service_url": "https://api.au-syd.watson-orchestrate.cloud.ibm.com/instances/f16c2181-a811-4d84-8e15-33cfebe50928"
            }
        }
    
    return credentials.get('watsonx_orchestrate', {})

def check_orchestrate_cli():
    """Check if Orchestrate CLI is installed"""
    print(f"\n{Colors.BLUE}🔍 Checking for IBM watsonx Orchestrate CLI...{Colors.NC}")
    
    # Try different CLI commands
    cli_commands = ['orchestrate', 'orchestrate-cli', 'ibmcloud', 'watsonx']
    
    for cmd in cli_commands:
        try:
            result = subprocess.run([cmd, '--version'], 
                                  capture_output=True, 
                                  timeout=5)
            if result.returncode == 0:
                print(f"{Colors.GREEN}✅ Found: {cmd}{Colors.NC}")
                return cmd
        except:
            continue
    
    print(f"{Colors.YELLOW}⚠️  Orchestrate CLI not found{Colors.NC}")
    return None

def install_orchestrate_cli():
    """Try to install Orchestrate CLI"""
    print(f"\n{Colors.BLUE}📦 Attempting to install Orchestrate CLI...{Colors.NC}")
    
    try:
        # Try installing ibm-watsonx-orchestrate
        subprocess.run([sys.executable, '-m', 'pip', 'install', '--quiet', 
                       'ibm-watsonx-orchestrate'], 
                      check=False, timeout=30)
        print(f"{Colors.GREEN}✅ Installation attempted{Colors.NC}")
        return True
    except Exception as e:
        print(f"{Colors.YELLOW}⚠️  Could not install CLI: {str(e)}{Colors.NC}")
        return False

def verify_config_file():
    """Verify agent configuration file exists and is valid"""
    print(f"\n{Colors.BLUE}📋 Verifying configuration file...{Colors.NC}")
    
    config_file = "proactive-csi-agent-orchestrate.yaml"
    
    # Try to find config file
    search_paths = [
        config_file,
        os.path.join("..", config_file),
        os.path.join(os.path.dirname(__file__), "..", config_file)
    ]
    
    config_path = None
    for path in search_paths:
        full_path = os.path.abspath(path)
        if os.path.exists(full_path):
            config_path = full_path
            print(f"{Colors.GREEN}✅ Configuration file found: {config_path}{Colors.NC}")
            break
    
    if not config_path:
        print(f"{Colors.RED}❌ Configuration file not found: {config_file}{Colors.NC}")
        return None
    
    # Check file size
    file_size = os.path.getsize(config_path)
    print(f"{Colors.BLUE}   File size: {file_size:,} bytes{Colors.NC}")
    
    # Check STT/TTS references
    try:
        with open(config_path, 'r') as f:
            content = f.read()
            stt_count = content.lower().count('stt') + content.lower().count('speech-to-text') + content.lower().count('speech to text')
            tts_count = content.lower().count('tts') + content.lower().count('text-to-speech') + content.lower().count('text to speech')
            print(f"{Colors.GREEN}   STT references: {stt_count}{Colors.NC}")
            print(f"{Colors.GREEN}   TTS references: {tts_count}{Colors.NC}")
    except:
        pass
    
    return config_path

def deploy_via_api(api_key, service_url, config_path):
    """Attempt to deploy via REST API"""
    print(f"\n{Colors.BLUE}🚀 Attempting API-based deployment...{Colors.NC}")
    
    # Read configuration file
    try:
        with open(config_path, 'r') as f:
            agent_config = f.read()
    except Exception as e:
        print(f"{Colors.RED}❌ Failed to read config file: {str(e)}{Colors.NC}")
        return False
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    # Try different API endpoints for skill/agent deployment
    endpoints = [
        f"{service_url}/api/v1/skills",
        f"{service_url}/v1/skills",
        f"{service_url}/skills",
        f"{service_url}/api/v1/agents",
        f"{service_url}/v1/agents",
        f"{service_url}/agents",
    ]
    
    # Create deployment payload
    payload = {
        "name": "ProActive_CSI_Agent_404",
        "version": "1.2.0",
        "description": "Enterprise Revenue & Risk Intelligence Agent with STT & TTS integration",
        "configuration": agent_config
    }
    
    for endpoint in endpoints:
        try:
            print(f"{Colors.BLUE}   Trying: {endpoint}{Colors.NC}")
            response = requests.post(
                endpoint,
                headers=headers,
                json=payload,
                timeout=30
            )
            
            if response.status_code in [200, 201, 202]:
                print(f"{Colors.GREEN}✅ Deployment successful!{Colors.NC}")
                print(f"{Colors.GREEN}   Status: {response.status_code}{Colors.NC}")
                try:
                    result = response.json()
                    print(f"{Colors.BLUE}   Response: {json.dumps(result, indent=2)[:200]}...{Colors.NC}")
                except:
                    print(f"{Colors.BLUE}   Response received{Colors.NC}")
                return True
            else:
                print(f"{Colors.YELLOW}   Status {response.status_code}: {response.text[:100]}{Colors.NC}")
        except requests.exceptions.RequestException as e:
            print(f"{Colors.YELLOW}   Connection error: {str(e)[:50]}...{Colors.NC}")
            continue
    
    return False

def deploy_via_cli(cli_cmd, config_path, api_key, service_url):
    """Attempt to deploy via CLI"""
    print(f"\n{Colors.BLUE}🚀 Attempting CLI-based deployment...{Colors.NC}")
    
    # Set environment variables
    env = os.environ.copy()
    env['ORCHESTRATE_API_KEY'] = api_key
    env['ORCHESTRATE_URL'] = service_url
    env['ORCHESTRATE_INSTANCE_ID'] = service_url.split('/')[-1]
    
    # Try different CLI commands
    cli_commands = [
        [cli_cmd, 'skill', 'create', '--file', config_path],
        [cli_cmd, 'agent', 'create', '--file', config_path],
        [cli_cmd, 'deploy', '--config', config_path],
        [cli_cmd, 'import', '--file', config_path],
    ]
    
    for cmd in cli_commands:
        try:
            print(f"{Colors.BLUE}   Trying: {' '.join(cmd)}{Colors.NC}")
            result = subprocess.run(cmd, env=env, capture_output=True, timeout=30)
            
            if result.returncode == 0:
                print(f"{Colors.GREEN}✅ CLI deployment successful!{Colors.NC}")
                print(f"{Colors.GREEN}   Output: {result.stdout.decode()[:200]}{Colors.NC}")
                return True
            else:
                print(f"{Colors.YELLOW}   CLI returned code {result.returncode}{Colors.NC}")
                if result.stderr:
                    print(f"{Colors.YELLOW}   Error: {result.stderr.decode()[:100]}{Colors.NC}")
        except subprocess.TimeoutExpired:
            print(f"{Colors.YELLOW}   Command timeout{Colors.NC}")
            continue
        except Exception as e:
            print(f"{Colors.YELLOW}   Error: {str(e)[:50]}...{Colors.NC}")
            continue
    
    return False

def open_portal_and_instructions(service_url, config_path):
    """Open portal and show manual instructions"""
    portal_url = "https://au-syd.watson-orchestrate.cloud.ibm.com/build/manage"
    
    print(f"\n{Colors.YELLOW}{'='*70}{Colors.NC}")
    print(f"{Colors.YELLOW}📋 Manual Deployment Instructions{Colors.NC}")
    print(f"{Colors.YELLOW}{'='*70}{Colors.NC}\n")
    
    print(f"{Colors.BLUE}IBM watsonx Orchestrate typically requires manual upload via web UI{Colors.NC}\n")
    
    print(f"{Colors.GREEN}1. Opening IBM Portal in browser...{Colors.NC}")
    try:
        webbrowser.open(portal_url)
        print(f"{Colors.GREEN}✅ Browser opened: {portal_url}{Colors.NC}")
    except:
        print(f"{Colors.YELLOW}⚠️  Please manually open: {portal_url}{Colors.NC}")
    
    print(f"\n{Colors.GREEN}2. Follow these steps:{Colors.NC}")
    print(f"   • Click 'All agents' or 'Skills' in left sidebar")
    print(f"   • Find 'ProActive_CSI_Agent_404'")
    print(f"   • Click 'Edit' button")
    print(f"   • Click 'Import from file' or 'Upload'")
    print(f"   • Select file: {Colors.GREEN}{config_path}{Colors.NC}")
    print(f"   • Click 'Save' → 'Activate'")
    
    print(f"\n{Colors.GREEN}3. Verify services are connected:{Colors.NC}")
    print(f"   • Go to 'Connections' tab")
    print(f"   • Verify: Speech-to-Text (STT)")
    print(f"   • Verify: Text-to-Speech (TTS)")
    print(f"   • Verify: Natural Language Understanding (NLU)")
    
    print(f"\n{Colors.GREEN}4. Test STT/TTS:{Colors.NC}")
    print(f'   • Type: "Read me the executive briefing aloud using Text-to-Speech"')
    print(f"   • Look for TTS API mentions in response")
    
    print(f"\n{Colors.BLUE}📁 Configuration File:{Colors.NC}")
    print(f"{Colors.GREEN}{config_path}{Colors.NC}")
    print("")

def main():
    """Main deployment function"""
    print_header()
    
    # Get project root directory
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    os.chdir(project_root)
    
    print(f"{Colors.BLUE}Project directory: {project_root}{Colors.NC}\n")
    
    # Step 1: Verify configuration file
    config_path = verify_config_file()
    if not config_path:
        print(f"{Colors.RED}❌ Configuration file not found. Exiting.{Colors.NC}")
        return 1
    
    # Step 2: Load credentials
    try:
        creds = load_credentials()
        api_key = creds.get('api_key', '')
        service_url = creds.get('service_url', '')
        
        if not api_key or not service_url:
            print(f"{Colors.RED}❌ Missing credentials (api_key or service_url){Colors.NC}")
            return 1
        
        print(f"{Colors.BLUE}Instance URL: {service_url}{Colors.NC}")
        print(f"{Colors.BLUE}Region: Australia Sydney (au-syd){Colors.NC}\n")
    except Exception as e:
        print(f"{Colors.RED}❌ Failed to load credentials: {str(e)}{Colors.NC}")
        return 1
    
    # Step 3: Check for CLI
    cli_cmd = check_orchestrate_cli()
    if not cli_cmd:
        print(f"{Colors.YELLOW}⚠️  CLI not found. Attempting installation...{Colors.NC}")
        install_orchestrate_cli()
        cli_cmd = check_orchestrate_cli()
    
    # Step 4: Try CLI deployment first
    deployment_success = False
    
    if cli_cmd:
        print(f"\n{Colors.BLUE}🚀 Attempting CLI deployment...{Colors.NC}")
        deployment_success = deploy_via_cli(cli_cmd, config_path, api_key, service_url)
    
    # Step 5: Try API deployment
    if not deployment_success:
        print(f"\n{Colors.BLUE}🚀 Attempting API deployment...{Colors.NC}")
        deployment_success = deploy_via_api(api_key, service_url, config_path)
    
    # Step 6: Manual instructions if automation fails
    if not deployment_success:
        print(f"\n{Colors.YELLOW}⚠️  Automated deployment not available{Colors.NC}")
        print(f"{Colors.BLUE}IBM watsonx Orchestrate typically requires manual upload via web UI{Colors.NC}")
        open_portal_and_instructions(service_url, config_path)
    else:
        print(f"\n{Colors.GREEN}{'='*70}{Colors.NC}")
        print(f"{Colors.GREEN}✅ DEPLOYMENT COMPLETE!{Colors.NC}")
        print(f"{Colors.GREEN}{'='*70}{Colors.NC}\n")
        
        print(f"{Colors.BLUE}Next steps:{Colors.NC}")
        print(f"1. Open IBM Portal: https://au-syd.watson-orchestrate.cloud.ibm.com/build/manage")
        print(f"2. Verify agent is active")
        print(f"3. Test STT/TTS with: 'Read me the executive briefing aloud'")
        print("")
    
    print(f"{Colors.GREEN}{'='*70}{Colors.NC}")
    print(f"{Colors.GREEN}🎯 Deployment process complete!{Colors.NC}")
    print(f"{Colors.GREEN}{'='*70}{Colors.NC}\n")
    
    return 0 if deployment_success else 0  # Return 0 even if manual required

if __name__ == "__main__":
    sys.exit(main())

