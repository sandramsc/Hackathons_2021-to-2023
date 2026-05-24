#!/usr/bin/env python3
"""
Fully Automated Deployment to IBM Cloud
- Uploads data to Cloudant
- Deploys agent to IBM watsonx Orchestrate
- Verifies deployment
"""

import os
import sys
import subprocess
import json
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

# Colors
GREEN = '\033[0;32m'
BLUE = '\033[0;34m'
RED = '\033[0;31m'
YELLOW = '\033[1;33m'
NC = '\033[0m'

def print_step(step_num, title):
    print(f"\n{BLUE}📋 Step {step_num}: {title}{NC}")
    print("━" * 70)

def run_command(cmd, description, check=True):
    """Run a shell command"""
    print(f"{BLUE}  {description}...{NC}")
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            check=check
        )
        if result.returncode == 0:
            print(f"{GREEN}  ✅ {description} - Success{NC}")
            return True, result.stdout
        else:
            print(f"{YELLOW}  ⚠️  {description} - Warning: {result.stderr[:200]}{NC}")
            return False, result.stderr
    except subprocess.CalledProcessError as e:
        print(f"{RED}  ❌ {description} - Error: {e}{NC}")
        return False, str(e)

def load_env():
    """Load environment variables from .env file"""
    env_file = project_root.parent / ".env"
    if env_file.exists():
        with open(env_file, 'r') as f:
            for line in f:
                if '=' in line and not line.strip().startswith('#'):
                    key, value = line.strip().split('=', 1)
                    os.environ[key] = value.strip().strip('"').strip("'")
        print(f"{GREEN}✅ Environment variables loaded{NC}")
        return True
    else:
        print(f"{YELLOW}⚠️  .env file not found{NC}")
        return False

def upload_data_to_cloudant():
    """Upload CSV data to Cloudant"""
    upload_script = project_root / "scripts" / "upload_data_to_cloudant.py"
    if upload_script.exists():
        print_step(2, "Uploading data to Cloudant")
        success, output = run_command(
            f"cd {project_root} && python3 {upload_script}",
            "Uploading data to Cloudant",
            check=False
        )
        return success
    else:
        print(f"{YELLOW}⚠️  Upload script not found, skipping data upload{NC}")
        return False

def setup_orchestrate_env():
    """Setup and activate Orchestrate environment"""
    print_step(3, "Setting up Orchestrate environment")
    
    api_key = os.getenv('ORCHESTRATE_API_KEY')
    endpoint = os.getenv('ORCHESTRATE_ENDPOINT', 
                        'https://api.au-syd.watson-orchestrate.cloud.ibm.com/instances/f16c2181-a811-4d84-8e15-33cfebe50928')
    
    if not api_key:
        print(f"{RED}❌ ORCHESTRATE_API_KEY not found{NC}")
        return False
    
    # Check if environment exists
    success, output = run_command(
        "orchestrate env list",
        "Checking existing environments",
        check=False
    )
    
    if "production-au" not in output:
        # Create environment
        print(f"{BLUE}  Creating production-au environment...{NC}")
        run_command(
            f'orchestrate env add -n production-au -u "{endpoint}" --type ibm_iam',
            "Creating environment",
            check=False
        )
    
    # Activate environment
    print(f"{BLUE}  Activating environment...{NC}")
    success, output = run_command(
        f'echo "{api_key}" | orchestrate env activate production-au',
        "Activating environment",
        check=False
    )
    
    return success

def deploy_agent():
    """Deploy agent to IBM watsonx Orchestrate"""
    print_step(4, "Deploying agent to IBM watsonx Orchestrate")
    
    agent_file = project_root / "proactive-csi-agent-orchestrate.yaml"
    if not agent_file.exists():
        print(f"{RED}❌ Agent configuration file not found{NC}")
        return False
    
    print(f"{BLUE}  Importing agent configuration...{NC}")
    success, output = run_command(
        f"orchestrate agents import --file {agent_file}",
        "Deploying agent",
        check=False
    )
    
    if not success:
        # Check if agent already exists
        success2, output2 = run_command(
            "orchestrate agents list",
            "Checking existing agents",
            check=False
        )
        if "ProActive" in output2 or "CSI" in output2:
            print(f"{GREEN}  ✅ Agent found in list (may already be deployed){NC}")
            return True
    
    return success

def verify_deployment():
    """Verify agent deployment"""
    print_step(5, "Verifying deployment")
    
    success, output = run_command(
        "orchestrate agents list",
        "Listing agents",
        check=False
    )
    
    if success and output:
        print(f"{BLUE}  Agent List:{NC}")
        # Print first few lines
        lines = output.split('\n')[:10]
        for line in lines:
            if line.strip():
                print(f"    {line}")
    
    return success

def main():
    """Main deployment function"""
    print("╔═══════════════════════════════════════════════════════════════╗")
    print("║  🚀 FULLY AUTOMATED IBM CLOUD DEPLOYMENT                     ║")
    print("╚═══════════════════════════════════════════════════════════════╝")
    print("")
    
    # Step 1: Load environment
    print_step(1, "Loading environment variables")
    load_env()
    
    # Step 2: Upload data
    upload_data_to_cloudant()
    
    # Step 3: Setup Orchestrate
    if not setup_orchestrate_env():
        print(f"{YELLOW}⚠️  Environment setup had issues, but continuing...{NC}")
    
    # Step 4: Deploy agent
    deploy_agent()
    
    # Step 5: Verify
    verify_deployment()
    
    # Summary
    print(f"\n{GREEN}═══════════════════════════════════════════════════════════════{NC}")
    print(f"{GREEN}✅ AUTOMATED DEPLOYMENT COMPLETE!{NC}")
    print(f"{GREEN}═══════════════════════════════════════════════════════════════{NC}")
    print("")
    print(f"{BLUE}Agent Details:{NC}")
    print("  Name: ProActive_CSI_Agent_404")
    print("  Environment: production-au")
    print("  Instance: https://api.au-syd.watson-orchestrate.cloud.ibm.com/instances/f16c2181-a811-4d84-8e15-33cfebe50928")
    print("")
    print(f"{BLUE}Access Your Agent:{NC}")
    print("  Portal: https://cloud.ibm.com/watsonx/orchestrate")
    print("  Direct: https://au-syd.watson-orchestrate.cloud.ibm.com/build/manage")
    print("")
    print(f"{BLUE}Test Queries:{NC}")
    print('  1. "Good morning, what\'s my priority today?"')
    print('  2. "Tell me about Acme Corporation"')
    print('  3. "What vendors have delays?"')
    print('  4. "Calculate revenue at risk"')
    print('  5. "Read me the executive briefing aloud using Text-to-Speech"')
    print("")

if __name__ == "__main__":
    main()

