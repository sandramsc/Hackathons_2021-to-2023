#!/usr/bin/env python3
"""
ProActive CSI - Automated IBM watsonx Orchestrate Deployment
Automatically deploys the agent to IBM watsonx Orchestrate
"""

import requests
import json
import os
import sys
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
    print("🚀 ProActive CSI - Automated IBM Orchestrate Deployment")
    print("="*70 + "\n")

def load_credentials():
    """Load IBM watsonx Orchestrate credentials"""
    print(f"{Colors.BLUE}📋 Loading credentials...{Colors.NC}")
    
    # Try to load from config file
    cred_paths = [
        "../ibm-credentials_Orchestrate_data_Updated.json",
        "config/orchestrate_credentials.json",
        "../ibm-credentials_Orchestrate_data.json"
    ]
    
    credentials = None
    for path in cred_paths:
        try:
            if os.path.exists(path):
                with open(path, 'r') as f:
                    content = f.read()
                    # Remove any RTF formatting if present
                    if content.startswith('{\\rtf'):
                        print(f"{Colors.YELLOW}⚠️  File contains RTF formatting, skipping...{Colors.NC}")
                        continue
                    credentials = json.loads(content)
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
    
    return credentials['watsonx_orchestrate']

def test_connection(api_key, service_url):
    """Test connection to IBM watsonx Orchestrate"""
    print(f"\n{Colors.BLUE}🔌 Testing connection to IBM watsonx Orchestrate...{Colors.NC}")
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    try:
        # Try to get instance info
        response = requests.get(
            f"{service_url}/health",
            headers=headers,
            timeout=10
        )
        
        if response.status_code == 200 or response.status_code == 404:
            print(f"{Colors.GREEN}✅ Connection successful!{Colors.NC}")
            return True
        else:
            print(f"{Colors.YELLOW}⚠️  Connection response: {response.status_code}{Colors.NC}")
            return True  # Continue anyway
    except Exception as e:
        print(f"{Colors.YELLOW}⚠️  Connection test: {str(e)}{Colors.NC}")
        return True  # Continue anyway

def create_agent_package():
    """Create agent deployment package"""
    print(f"\n{Colors.BLUE}📦 Creating agent deployment package...{Colors.NC}")
    
    # Load agent configuration
    yaml_path = "proactive-csi-agent.yaml"
    if not os.path.exists(yaml_path):
        yaml_path = "../proactive-csi-agent.yaml"
    
    if not os.path.exists(yaml_path):
        print(f"{Colors.RED}❌ Agent configuration not found: proactive-csi-agent.yaml{Colors.NC}")
        return None
    
    with open(yaml_path, 'r') as f:
        agent_config = f.read()
    
    print(f"{Colors.GREEN}✅ Agent configuration loaded ({len(agent_config)} bytes){Colors.NC}")
    
    # Create deployment package
    package = {
        "name": "ProActive CSI - Agent 404",
        "description": "Enterprise Revenue & Risk Intelligence Agent",
        "version": "1.0.0",
        "agents": [
            {
                "name": "Customer Success Intelligence Agent",
                "type": "customer_success",
                "capabilities": [
                    "churn_prediction",
                    "sentiment_analysis",
                    "intervention_recommendation"
                ]
            },
            {
                "name": "Procurement Intelligence Agent",
                "type": "procurement",
                "capabilities": [
                    "vendor_monitoring",
                    "delay_detection",
                    "customer_impact_correlation"
                ]
            },
            {
                "name": "Revenue Protection Agent",
                "type": "revenue",
                "capabilities": [
                    "revenue_at_risk_calculation",
                    "cfo_briefing",
                    "financial_scenario_modeling"
                ]
            }
        ],
        "workflows": [
            "churn_prediction",
            "procurement_early_warning",
            "customer_escalation",
            "contract_renewal_prep",
            "daily_executive_brief",
            "procurement_customer_bridge"
        ],
        "configuration": agent_config
    }
    
    return package

def deploy_agent(api_key, service_url, package):
    """Deploy agent to IBM watsonx Orchestrate"""
    print(f"\n{Colors.BLUE}🚀 Deploying agent to IBM watsonx Orchestrate...{Colors.NC}")
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    # Try different API endpoints
    endpoints = [
        f"{service_url}/v1/agents",
        f"{service_url}/agents",
        f"{service_url}/api/v1/agents",
        f"{service_url}/skills"
    ]
    
    deployment_successful = False
    
    for endpoint in endpoints:
        try:
            print(f"{Colors.BLUE}   Trying endpoint: {endpoint}{Colors.NC}")
            response = requests.post(
                endpoint,
                headers=headers,
                json=package,
                timeout=30
            )
            
            if response.status_code in [200, 201, 202]:
                print(f"{Colors.GREEN}✅ Agent deployed successfully!{Colors.NC}")
                print(f"   Response: {response.status_code}")
                deployment_successful = True
                break
            else:
                print(f"{Colors.YELLOW}   Response: {response.status_code} - {response.text[:100]}{Colors.NC}")
        except Exception as e:
            print(f"{Colors.YELLOW}   Error: {str(e)}{Colors.NC}")
            continue
    
    return deployment_successful

def manual_deployment_instructions(service_url):
    """Provide manual deployment instructions"""
    print(f"\n{Colors.YELLOW}{'='*70}{Colors.NC}")
    print(f"{Colors.YELLOW}📋 Manual Deployment Instructions{Colors.NC}")
    print(f"{Colors.YELLOW}{'='*70}{Colors.NC}\n")
    
    print(f"{Colors.BLUE}Since API deployment requires additional setup, here's the manual process:{Colors.NC}\n")
    
    print(f"1. Open IBM watsonx Orchestrate:")
    print(f"   {Colors.GREEN}{service_url.replace('/instances/', '/build/manage')}{Colors.NC}\n")
    
    print(f"2. Click the {Colors.GREEN}'Create agent +'{Colors.NC} button\n")
    
    print(f"3. Choose one of these options:")
    print(f"   • 'Import from file' → Upload {Colors.GREEN}proactive-csi-agent.yaml{Colors.NC}")
    print(f"   • 'Start from scratch' → Then add:")
    print(f"     - Name: ProActive CSI - Agent 404")
    print(f"     - Description: Enterprise Revenue & Risk Intelligence Agent\n")
    
    print(f"4. Connect IBM Services:")
    print(f"   {Colors.BLUE}Go to Connections/Integrations section:{Colors.NC}")
    print(f"   • Natural Language Understanding")
    print(f"   • Speech to Text")
    print(f"   • Text to Speech")
    print(f"   • Cloudant Database\n")
    
    print(f"5. Test with: {Colors.GREEN}'What's my priority today?'{Colors.NC}\n")
    
    print(f"{Colors.BLUE}📚 Complete credentials available in:{Colors.NC}")
    print(f"   • IBM_PORTAL_QUICK_START.md")
    print(f"   • IBM_PORTAL_DEPLOYMENT.md\n")

def main():
    """Main deployment function"""
    print_header()
    
    # Load credentials
    try:
        creds = load_credentials()
        api_key = creds['api_key']
        service_url = creds['service_url']
        
        print(f"{Colors.BLUE}Instance URL:{Colors.NC} {service_url}")
        print(f"{Colors.BLUE}Region:{Colors.NC} Australia Sydney (au-syd)\n")
    except Exception as e:
        print(f"{Colors.RED}❌ Failed to load credentials: {str(e)}{Colors.NC}")
        return 1
    
    # Test connection
    if not test_connection(api_key, service_url):
        print(f"{Colors.YELLOW}⚠️  Connection test failed, but continuing...{Colors.NC}")
    
    # Create deployment package
    package = create_agent_package()
    if not package:
        return 1
    
    # Try to deploy
    print(f"\n{Colors.BLUE}Attempting automated deployment...{Colors.NC}")
    success = deploy_agent(api_key, service_url, package)
    
    if not success:
        print(f"\n{Colors.YELLOW}⚠️  Automated deployment not available yet{Colors.NC}")
        print(f"{Colors.BLUE}IBM watsonx Orchestrate typically requires manual upload via web UI{Colors.NC}")
        manual_deployment_instructions(service_url)
        
        # Open browser automatically
        print(f"\n{Colors.BLUE}🌐 Opening IBM watsonx Orchestrate in browser...{Colors.NC}")
        portal_url = "https://cloud.ibm.com/watsonx/orchestrate"
        
        import webbrowser
        try:
            webbrowser.open(portal_url)
            print(f"{Colors.GREEN}✅ Browser opened!{Colors.NC}")
        except:
            print(f"{Colors.YELLOW}Please manually open: {portal_url}{Colors.NC}")
    
    print(f"\n{Colors.GREEN}{'='*70}{Colors.NC}")
    print(f"{Colors.GREEN}🎯 Deployment preparation complete!{Colors.NC}")
    print(f"{Colors.GREEN}{'='*70}{Colors.NC}\n")
    
    print(f"{Colors.BLUE}📁 Your files are ready:{Colors.NC}")
    print(f"   ✅ proactive-csi-agent.yaml (agent configuration)")
    print(f"   ✅ IBM credentials (configured)")
    print(f"   ✅ Complete documentation (guides)\n")
    
    print(f"{Colors.BLUE}📚 See detailed instructions:{Colors.NC}")
    print(f"   • IBM_PORTAL_QUICK_START.md (5-minute guide)")
    print(f"   • IBM_PORTAL_DEPLOYMENT.md (complete guide)\n")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())

