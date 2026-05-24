import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
import random
import time

load_dotenv()

# Cloudant configuration - Use your Service Credentials
CLOUDANT_URL = os.getenv("CLOUDANT_URL")
IAM_API_KEY = os.getenv("IAM_API_KEY")


def get_iam_token(api_key):
    """Get IAM access token"""
    url = "https://iam.cloud.ibm.com/identity/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "grant_type": "urn:ibm:params:oauth:grant-type:apikey",
        "apikey": api_key
    }
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        raise Exception(f"Failed to get IAM token: {response.text}")


# Authentication with IAM
iam_token = get_iam_token(IAM_API_KEY)
session = requests.Session()
session.headers.update({
    'Authorization': f'Bearer {iam_token}',
    'Content-Type': 'application/json'
})

# Database names
DATABASES = {
    'customers': 'customer_table',
    'procurement': 'procurement_table',
    'revenue': 'revenue_table'
}


def create_database(db_name):
    """Create a database in Cloudant"""
    url = f"{CLOUDANT_URL}/{db_name}"
    response = session.put(url)
    if response.status_code == 201:
        print(f"✓ Database '{db_name}' created successfully")
    elif response.status_code == 412:
        print(f"! Database '{db_name}' already exists")
    else:
        print(f"✗ Error creating '{db_name}': {response.text}")
    return response.status_code in [201, 412]


def generate_customer_data(num_records=500):
    """Generate mock customer data"""
    customers = []
    customer_names = [
        "Acme Corp", "TechStart Inc", "GlobalSolutions Ltd", "InnovateCo",
        "DataDriven LLC", "CloudFirst Systems", "AgileWorks", "NextGen Tech",
        "SmartBiz Solutions", "Enterprise Plus", "Digital Dynamics",
        "FutureTech Industries", "Quantum Ventures", "Synergy Group",
        "Alpha Enterprises", "Beta Systems", "Gamma Corporation",
        "Velocity Systems", "Nexus Solutions", "Pinnacle Tech", "Apex Industries",
        "Zenith Corp", "Horizon Ventures", "Eclipse Systems", "Stellar Group",
        "Prime Solutions", "Vanguard Tech", "Summit Enterprises", "Fusion Inc"
    ]

    for i in range(num_records):
        usage_drop = round(random.uniform(0, 0.8), 2)  # 0-80% drop
        sentiment = round(random.uniform(1, 10), 1)  # 1-10 score
        tickets = random.randint(0, 50)
        arr = random.randint(10000, 500000)

        # Churn score based on other factors
        churn_factors = (usage_drop * 0.4) + ((10 - sentiment) / 10 * 0.3) + (min(tickets, 30) / 30 * 0.3)
        churn_score = round(min(churn_factors, 1.0), 3)

        customer = {
            "_id": f"customer_{i + 1:04d}",
            "customer_name": random.choice(customer_names) + f" - {i + 1}",
            "usage_drop": usage_drop,
            "sentiment_score": sentiment,
            "ticket_volume": tickets,
            "arr": arr,
            "churn_score": churn_score,
            "last_updated": datetime.now().isoformat(),
            "account_status": "active" if churn_score < 0.7 else "at_risk"
        }
        customers.append(customer)

    return customers


def generate_procurement_data(num_records=500):
    """Generate mock procurement data"""
    procurements = []
    vendors = [
        "CloudProvider A", "Infrastructure Co", "Software Supplier B",
        "Hardware Vendor C", "Service Provider D", "Tech Distributor E",
        "Equipment Supplier F", "Platform Provider G", "Network Systems Inc",
        "Data Center Solutions", "Storage Vendor H", "Security Provider I",
        "Analytics Supplier J", "Integration Partner K", "Hosting Provider L"
    ]

    for i in range(num_records):
        delay = random.randint(0, 45)
        num_impacted = random.randint(0, 15)

        # Generate list of impacted customers
        impacted_customers = [f"customer_{random.randint(1, 500):04d}"
                              for _ in range(num_impacted)]

        procurement = {
            "_id": f"procurement_{i + 1:04d}",
            "vendor_name": random.choice(vendors),
            "order_id": f"PO-2024-{random.randint(1000, 9999)}",
            "vendor_deliveries": random.randint(1, 10),
            "delay_days": delay,
            "customer_impact_list": list(set(impacted_customers)),  # Remove duplicates
            "delivery_date": (datetime.now() - timedelta(days=delay)).isoformat(),
            "expected_date": (datetime.now() - timedelta(days=random.randint(0, 5))).isoformat(),
            "status": "delayed" if delay > 7 else "on_time",
            "impact_severity": "high" if delay > 20 else "medium" if delay > 7 else "low"
        }
        procurements.append(procurement)

    return procurements


def generate_revenue_data(num_records=500):
    """Generate mock revenue data"""
    revenues = []

    for i in range(num_records):
        arr = random.randint(10000, 500000)
        prob_churn = round(random.uniform(0, 1), 3)
        arr_at_risk = round(arr * prob_churn, 2)

        revenue = {
            "_id": f"revenue_{i + 1:04d}",
            "customer_id": f"customer_{i + 1:04d}",
            "arr": arr,
            "arr_at_risk": arr_at_risk,
            "probability_of_churn": prob_churn,
            "mrr": round(arr / 12, 2),
            "contract_end_date": (datetime.now() + timedelta(days=random.randint(30, 730))).isoformat(),
            "renewal_probability": round(1 - prob_churn, 3),
            "revenue_tier": "enterprise" if arr > 200000 else "mid_market" if arr > 50000 else "smb",
            "last_payment_date": (datetime.now() - timedelta(days=random.randint(0, 90))).isoformat()
        }
        revenues.append(revenue)

    return revenues


def bulk_insert_documents(db_name, documents):
    """Bulk insert documents into Cloudant database"""
    url = f"{CLOUDANT_URL}/{db_name}/_bulk_docs"
    payload = {"docs": documents}

    response = session.post(url, json=payload)

    if response.status_code == 201:
        results = response.json()
        success_count = sum(1 for r in results if 'ok' in r and r['ok'])
        print(f"✓ Inserted {success_count}/{len(documents)} documents into '{db_name}'")
        return True
    else:
        print(f"✗ Error inserting documents into '{db_name}': {response.text}")
        return False


def main():
    print("=== Cloudant Mock Tables Setup ===\n")

    # Step 1: Create databases
    print("Step 1: Creating databases...")
    for db_name in DATABASES.values():
        create_database(db_name)

    print("\nStep 2: Generating and inserting mock data...\n")

    # Step 2: Generate and insert Customer data
    print("Generating Customer data...")
    customers = generate_customer_data(500)
    bulk_insert_documents(DATABASES['customers'], customers)

    # Step 3: Generate and insert Procurement data
    print("\nGenerating Procurement data...")
    procurements = generate_procurement_data(500)
    bulk_insert_documents(DATABASES['procurement'], procurements)

    # Step 4: Generate and insert Revenue data
    print("\nGenerating Revenue data...")
    revenues = generate_revenue_data(500)
    bulk_insert_documents(DATABASES['revenue'], revenues)

    # Step 5: Create indexes
    create_indexes()

    print("\n=== Setup Complete! ===")
    print(f"\nDatabases created:")
    print(f"  • {DATABASES['customers']} - {len(customers)} customer records")
    print(f"  • {DATABASES['procurement']} - {len(procurements)} procurement records")
    print(f"  • {DATABASES['revenue']} - {len(revenues)} revenue records")


def create_indexes():
    """Create indexes for querying"""
    print("\nStep 3: Creating indexes for efficient querying...")

    # Index for customer churn queries - ONLY the sort field
    customer_index = {
        "index": {
            "fields": ["churn_score"]  # Only sort field
        },
        "name": "churn-score-index",
        "type": "json"
    }

    url = f"{CLOUDANT_URL}/{DATABASES['customers']}/_index"
    response = session.post(url, json=customer_index)
    if response.status_code == 200:
        result = response.json().get('result', 'created')
        print(f"✓ Customer index: {result}")
    else:
        print(f"! Customer index: {response.json()}")

    time.sleep(0.5)  # Rate limiting

    # Index for procurement delays
    procurement_index = {
        "index": {
            "fields": ["delay_days"]  # Only sort field
        },
        "name": "delay-index",
        "type": "json"
    }

    url = f"{CLOUDANT_URL}/{DATABASES['procurement']}/_index"    
    response = session.post(url, json=procurement_index)    
    if response.status_code == 200:
        result = response.json().get('result', 'created')
        print(f"✓ Procurement index: {result}")
    else:
        print(f"! Procurement index: {response.json()}")

    time.sleep(0.5)  # Rate limiting

    # Index for revenue at risk
    revenue_index = {
        "index": {
            "fields": ["arr_at_risk"]  # Only sort field
        },
        "name": "revenue-risk-index",
        "type": "json"
    }

    url = f"{CLOUDANT_URL}/{DATABASES['revenue']}/_index"
    response = session.post(url, json=revenue_index)
    if response.status_code == 200:
        result = response.json().get('result', 'created')
        print(f"✓ Revenue index: {result}")
    else:
        print(f"! Revenue index: {response.json()}")

    time.sleep(1)  # Wait before queries


# Example: Query customer data
def query_high_churn_customers():
    """Example query: Find customers with high churn risk"""
    db_name = DATABASES['customers']
    url = f"{CLOUDANT_URL}/{db_name}/_find"

    query = {
        "selector": {
            "churn_score": {"$gt": 0.7}
        },
        "fields": ["customer_name", "churn_score", "arr", "sentiment_score"],
        "sort": [{"churn_score": "desc"}],
        "limit": 10
    }

    response = session.post(url, json=query)
    if response.status_code == 200:
        results = response.json()
        print("\n=== Top 10 High Churn Risk Customers ===")
        for doc in results.get('docs', []):
            print(f"  • {doc['customer_name']}: Churn Score = {doc['churn_score']}, ARR = ${doc['arr']:,}")
    else:
        print(f"Query error: {response.text}")


def query_delayed_procurements():
    """Example query: Find severely delayed procurements"""
    db_name = DATABASES['procurement']
    url = f"{CLOUDANT_URL}/{db_name}/_find"

    query = {
        "selector": {
            "delay_days": {"$gt": 20}
        },
        "fields": ["vendor_name", "delay_days", "impact_severity", "customer_impact_list"],
        "sort": [{"delay_days": "desc"}],
        "limit": 10
    }

    response = session.post(url, json=query)
    if response.status_code == 200:
        results = response.json()
        print("\n=== Top 10 Delayed Procurements ===")
        for doc in results.get('docs', []):
            impacted = len(doc.get('customer_impact_list', []))
            print(f"  • {doc['vendor_name']}: {doc['delay_days']} days delay, {impacted} customers impacted")
    else:
        print(f"Query error: {response.text}")


def query_revenue_at_risk():
    """Example query: Find high revenue at risk"""
    db_name = DATABASES['revenue']
    url = f"{CLOUDANT_URL}/{db_name}/_find"

    query = {
        "selector": {
            "arr_at_risk": {"$gt": 100000}
        },
        "fields": ["customer_id", "arr", "arr_at_risk", "probability_of_churn"],
        "sort": [{"arr_at_risk": "desc"}],
        "limit": 10
    }

    response = session.post(url, json=query)
    if response.status_code == 200:
        results = response.json()
        print("\n=== Top 10 Revenue at Risk ===")
        for doc in results.get('docs', []):
            print(
                f"  • {doc['customer_id']}: ARR ${doc['arr']:,} | At Risk: ${doc['arr_at_risk']:,} ({doc['probability_of_churn'] * 100:.1f}%)")
    else:
        print(f"Query error: {response.text}")


if __name__ == "__main__":
    print("🚀 Starting Cloudant Mock Tables Setup...\n")

    # Run the setup
    main()

    # Run example queries with rate limiting
    print("\n" + "=" * 50)
    print("Running Example Queries...")
    print("=" * 50)

    query_high_churn_customers()
    time.sleep(1.5)  # Prevent rate limiting

    query_delayed_procurements()
    time.sleep(1.5)  # Prevent rate limiting

    query_revenue_at_risk()

    print("\n✅ All done! Your Cloudant database is ready to use.")
    print("\n💡 Tip: If you still see rate limit errors, wait 10-30 seconds and run queries again.")
