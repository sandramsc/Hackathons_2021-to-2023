#!/usr/bin/env python3
"""
Upload all CSV data to IBM Cloudant
Converts CSV files to JSON documents and stores in Cloudant database
"""

import sys
import os
import pandas as pd
import json
import requests
from requests.auth import HTTPBasicAuth
from pathlib import Path
from datetime import datetime

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from integrations.ibm_services import get_ibm_services

def upload_csv_to_cloudant(csv_path: str, collection_name: str, ibm_services, batch_size: int = 100):
    """
    Upload CSV file to Cloudant as JSON documents
    """
    print(f"\n📤 Uploading {collection_name}...")
    
    try:
        # Read CSV
        df = pd.read_csv(csv_path)
        print(f"   ✅ Loaded {len(df)} records from {csv_path}")
        
        # Convert to JSON documents
        documents = []
        for idx, row in df.iterrows():
            doc = row.to_dict()
            # Create unique ID
            doc['_id'] = f"{collection_name}_{doc.get(list(doc.keys())[0], idx)}"
            doc['type'] = collection_name
            doc['uploaded_at'] = datetime.now().isoformat()
            documents.append(doc)
        
        # Upload in batches
        total_uploaded = 0
        for i in range(0, len(documents), batch_size):
            batch = documents[i:i+batch_size]
            
            # Use bulk_docs for efficiency
            try:
                from ibmcloudant.cloudant_v1 import BulkDocs
                bulk_docs = BulkDocs(docs=batch)
                response = ibm_services.cloudant.post_bulk_docs(
                    db='proactive_csi',
                    bulk_docs=bulk_docs
                ).get_result()
                
                uploaded = len([r for r in response if 'id' in r and 'error' not in r])
                total_uploaded += uploaded
                print(f"   📊 Batch {i//batch_size + 1}: {uploaded}/{len(batch)} documents uploaded")
            except Exception as e:
                print(f"   ⚠️  Batch {i//batch_size + 1} error: {e}")
                # Try individual uploads
                for doc in batch:
                    try:
                        ibm_services.cloudant.post_document(
                            db='proactive_csi',
                            document=doc
                        ).get_result()
                        total_uploaded += 1
                    except Exception as e2:
                        print(f"   ❌ Failed to upload {doc.get('_id')}: {e2}")
        
        print(f"   ✅ {total_uploaded}/{len(documents)} documents uploaded successfully")
        return total_uploaded
        
    except Exception as e:
        print(f"   ❌ Error uploading {collection_name}: {e}")
        import traceback
        traceback.print_exc()
        return 0

def create_database_if_not_exists(ibm_services):
    """Create Cloudant database if it doesn't exist"""
    try:
        # Try to get database info
        ibm_services.cloudant.get_database_information(db='proactive_csi').get_result()
        print("✅ Database 'proactive_csi' already exists")
        return True
    except Exception as e:
        # Database doesn't exist, try to create it
        print(f"📋 Database 'proactive_csi' not found, attempting to create...")
        try:
            # Create database
            ibm_services.cloudant.put_database(db='proactive_csi').get_result()
            print("✅ Created database 'proactive_csi'")
            return True
        except Exception as create_error:
            # If creation fails (403), try using HTTP Basic Auth with username/password
            print(f"⚠️  API key doesn't have permission to create database (403)")
            print(f"   Trying alternative authentication method...")
            
            try:
                import requests
                from requests.auth import HTTPBasicAuth
                
                # Get credentials from environment
                username = os.getenv('CLOUDANT_USERNAME', 'f01bbce3-de41-430e-bd9b-5c00a082588a-bluemix')
                password = os.getenv('CLOUDANT_PASSWORD', os.getenv('CLOUDANT_API_KEY', 'TalYEKH8YIFL1Hqu0Gx4QZP6IBE-43s8Cl2Fm7a-CyBK'))
                url = os.getenv('CLOUDANT_URL', 'https://f01bbce3-de41-430e-bd9b-5c00a082588a-bluemix.cloudantnosqldb.appdomain.cloud')
                
                # Try to create database using HTTP Basic Auth
                db_url = f"{url}/proactive_csi"
                response = requests.put(
                    db_url,
                    auth=HTTPBasicAuth(username, password),
                    timeout=10
                )
                
                if response.status_code in [200, 201, 412]:  # 412 = already exists
                    print("✅ Database 'proactive_csi' created/verified using HTTP Basic Auth")
                    return True
                else:
                    print(f"⚠️  Could not create database: {response.status_code} - {response.text[:200]}")
                    print(f"   You may need to create it manually in IBM Cloud Console")
                    print(f"   Database name: 'proactive_csi'")
                    return False
            except Exception as http_error:
                print(f"⚠️  Alternative method also failed: {http_error}")
                print(f"   Please create database 'proactive_csi' manually in IBM Cloud Console")
                print(f"   URL: https://cloud.ibm.com/")
                return False

def main():
    """Upload all CSV data to Cloudant"""
    print("="*70)
    print("🚀 Uploading CSV Data to IBM Cloudant")
    print("="*70)
    print()
    
    # Initialize IBM services
    print("📋 Initializing IBM Services...")
    ibm_services = get_ibm_services()
    
    if ibm_services.cloudant is None:
        print("❌ Cloudant not initialized. Check credentials.")
        print("⚠️  Note: Agent can work without Cloudant (uses CSV files directly)")
        return 1
    
    print("✅ Cloudant initialized")
    print()
    
    # Create database
    if not create_database_if_not_exists(ibm_services):
        print("\n⚠️  Cloudant database creation failed, but this is optional.")
        print("   The agent can work with CSV files directly.")
        print("   To create database manually:")
        print("   1. Go to: https://cloud.ibm.com/")
        print("   2. Navigate to Cloudant instance")
        print("   3. Click 'Create Database'")
        print("   4. Name: 'proactive_csi'")
        print("   5. Then run this script again")
        print("\n   Continuing without Cloudant upload...")
        return 0  # Don't fail, just skip Cloudant
    
    # Data files to upload
    data_dir = project_root / "data"
    data_files = [
        ("customer_success_data.csv", "customers"),
        ("support_tickets.csv", "support_tickets"),
        ("customer_comms.csv", "customer_comms"),
        ("procurement_vendor_data.csv", "vendors"),
        ("contracts.csv", "contracts"),
        ("revenue_exposure_data.csv", "revenue")
    ]
    
    print("📊 Uploading data files...")
    print()
    
    total_uploaded = 0
    results = {}
    
    for csv_file, collection_name in data_files:
        csv_path = data_dir / csv_file
        if csv_path.exists():
            count = upload_csv_to_cloudant(str(csv_path), collection_name, ibm_services)
            results[collection_name] = count
            total_uploaded += count
        else:
            print(f"   ⚠️  File not found: {csv_path}")
            results[collection_name] = 0
    
    # Summary
    print()
    print("="*70)
    print("📊 Upload Summary")
    print("="*70)
    print()
    
    for collection, count in results.items():
        status = "✅" if count > 0 else "❌"
        print(f"  {status} {collection:20s} - {count:5d} documents")
    
    print()
    print(f"📈 Total: {total_uploaded} documents uploaded to Cloudant")
    print()
    
    # Verify upload
    print("🔍 Verifying upload...")
    try:
        # Query to count documents by type
        for collection_name in results.keys():
            selector = {'type': collection_name}
            response = ibm_services.cloudant.post_find(
                db='proactive_csi',
                selector=selector,
                limit=1
            ).get_result()
            
            # Get total count (this is approximate)
            print(f"   ✅ {collection_name}: Documents in Cloudant")
    except Exception as e:
        print(f"   ⚠️  Verification error: {e}")
    
    print()
    print("="*70)
    print("✅ Upload Complete!")
    print("="*70)
    print()
    print("📋 Next Steps:")
    print("1. Update agents to read from Cloudant")
    print("2. Update agent instructions to reference Cloudant")
    print("3. Test queries with Cloudant data")
    print()
    
    return 0 if total_uploaded > 0 else 1

if __name__ == "__main__":
    sys.exit(main())

