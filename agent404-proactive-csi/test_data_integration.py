#!/usr/bin/env python3
"""
Test Data Integration
Verifies all CSV data files are loaded correctly by agents
"""

import sys
import os
import pandas as pd
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from agents.customer_success_agent import CustomerSuccessAgent
from agents.procurement_agent import ProcurementAgent
from agents.revenue_agent import RevenueAgent

def test_data_files():
    """Test that all data files exist and are readable"""
    print("="*70)
    print("📊 Testing Data File Integration")
    print("="*70)
    print()
    
    data_path = project_root / "data"
    required_files = [
        "contracts.csv",
        "customer_comms.csv",
        "customer_success_data.csv",
        "procurement_vendor_data.csv",
        "revenue_exposure_data.csv",
        "support_tickets.csv"
    ]
    
    print("📁 Checking data files...")
    all_exist = True
    for file in required_files:
        file_path = data_path / file
        if file_path.exists():
            try:
                df = pd.read_csv(file_path)
                print(f"  ✅ {file:30s} - {len(df):5d} rows, {len(df.columns):2d} columns")
            except Exception as e:
                print(f"  ❌ {file:30s} - Error reading: {e}")
                all_exist = False
        else:
            print(f"  ❌ {file:30s} - File not found")
            all_exist = False
    
    print()
    return all_exist

def test_customer_success_agent():
    """Test Customer Success Agent data loading"""
    print("="*70)
    print("🧪 Testing Customer Success Agent")
    print("="*70)
    print()
    
    try:
        agent = CustomerSuccessAgent(data_path="data/")
        
        # Test data loaded
        if agent.customers_df is not None:
            print(f"  ✅ Customer Success Data: {len(agent.customers_df)} customers")
        else:
            print("  ❌ Customer Success Data: Not loaded")
            return False
            
        if agent.tickets_df is not None:
            print(f"  ✅ Support Tickets: {len(agent.tickets_df)} tickets")
        else:
            print("  ❌ Support Tickets: Not loaded")
            return False
            
        if agent.comms_df is not None:
            print(f"  ✅ Customer Communications: {len(agent.comms_df)} messages")
        else:
            print("  ❌ Customer Communications: Not loaded")
            return False
        
        # Test churn prediction
        test_customer = agent.customers_df.iloc[0]['customer_id']
        churn_prob = agent.predict_churn_probability(test_customer)
        print(f"  ✅ Churn Prediction Test: Customer {test_customer} = {churn_prob:.2%}")
        
        print()
        return True
    except Exception as e:
        print(f"  ❌ Error: {e}")
        import traceback
        traceback.print_exc()
        print()
        return False

def test_procurement_agent():
    """Test Procurement Agent data loading"""
    print("="*70)
    print("🧪 Testing Procurement Agent")
    print("="*70)
    print()
    
    try:
        agent = ProcurementAgent(data_path="data/")
        
        # Test data loaded
        if agent.vendors_df is not None:
            print(f"  ✅ Vendor Data: {len(agent.vendors_df)} vendors")
        else:
            print("  ❌ Vendor Data: Not loaded")
            return False
            
        if agent.contracts_df is not None:
            print(f"  ✅ Contracts: {len(agent.contracts_df)} contracts")
        else:
            print("  ❌ Contracts: Not loaded")
            return False
        
        # Test vendor delay detection
        delays = agent.detect_vendor_delays(threshold_days=5)
        print(f"  ✅ Vendor Delay Detection: {len(delays)} vendors with delays")
        
        print()
        return True
    except Exception as e:
        print(f"  ❌ Error: {e}")
        import traceback
        traceback.print_exc()
        print()
        return False

def test_revenue_agent():
    """Test Revenue Agent data loading"""
    print("="*70)
    print("🧪 Testing Revenue Agent")
    print("="*70)
    print()
    
    try:
        agent = RevenueAgent(data_path="data/")
        
        # Test data loaded
        if agent.revenue_df is not None:
            print(f"  ✅ Revenue Data: {len(agent.revenue_df)} revenue records")
        else:
            print("  ❌ Revenue Data: Not loaded")
            return False
            
        if agent.customers_df is not None:
            print(f"  ✅ Customer Data: {len(agent.customers_df)} customers")
        else:
            print("  ❌ Customer Data: Not loaded")
            return False
        
        # Test revenue at risk calculation
        test_customer = agent.revenue_df.iloc[0]['customer_id']
        risk = agent.calculate_revenue_at_risk(test_customer, 0.5)
        if 'error' not in risk:
            print(f"  ✅ Revenue at Risk Test: Customer {test_customer}")
            print(f"     ARR at Risk: ${risk.get('arr_at_risk', 0):,.2f}")
        else:
            print(f"  ⚠️  Revenue at Risk Test: {risk.get('error')}")
        
        print()
        return True
    except Exception as e:
        print(f"  ❌ Error: {e}")
        import traceback
        traceback.print_exc()
        print()
        return False

def test_data_relationships():
    """Test relationships between data files"""
    print("="*70)
    print("🔗 Testing Data Relationships")
    print("="*70)
    print()
    
    try:
        data_path = project_root / "data"
        
        # Load all data
        customers = pd.read_csv(data_path / "customer_success_data.csv")
        contracts = pd.read_csv(data_path / "contracts.csv")
        vendors = pd.read_csv(data_path / "procurement_vendor_data.csv")
        revenue = pd.read_csv(data_path / "revenue_exposure_data.csv")
        tickets = pd.read_csv(data_path / "support_tickets.csv")
        comms = pd.read_csv(data_path / "customer_comms.csv")
        
        # Test customer ID consistency
        customer_ids = set(customers['customer_id'].unique())
        contract_customers = set(contracts['customer_id'].unique())
        revenue_customers = set(revenue['customer_id'].unique())
        ticket_customers = set(tickets['customer_id'].unique())
        comms_customers = set(comms['customer_id'].unique())
        
        print(f"  📊 Customer IDs in Customer Success Data: {len(customer_ids)}")
        print(f"  📊 Customer IDs in Contracts: {len(contract_customers)}")
        print(f"  📊 Customer IDs in Revenue Data: {len(revenue_customers)}")
        print(f"  📊 Customer IDs in Support Tickets: {len(ticket_customers)}")
        print(f"  📊 Customer IDs in Communications: {len(comms_customers)}")
        print()
        
        # Check overlaps
        all_customers = customer_ids | contract_customers | revenue_customers | ticket_customers | comms_customers
        print(f"  ✅ Total unique customers across all datasets: {len(all_customers)}")
        
        # Test vendor-customer relationships
        vendor_customers = set()
        for _, vendor in vendors.iterrows():
            if pd.notna(vendor.get('affected_customers')):
                import ast
                try:
                    affected = ast.literal_eval(vendor['affected_customers'])
                    vendor_customers.update(affected)
                except:
                    pass
        
        print(f"  ✅ Customers affected by vendors: {len(vendor_customers)}")
        print()
        
        return True
    except Exception as e:
        print(f"  ❌ Error: {e}")
        import traceback
        traceback.print_exc()
        print()
        return False

def main():
    """Run all tests"""
    print("\n" + "="*70)
    print("🚀 ProActive CSI - Data Integration Test Suite")
    print("="*70)
    print()
    
    results = []
    
    # Test 1: Data files exist
    results.append(("Data Files", test_data_files()))
    
    # Test 2: Customer Success Agent
    results.append(("Customer Success Agent", test_customer_success_agent()))
    
    # Test 3: Procurement Agent
    results.append(("Procurement Agent", test_procurement_agent()))
    
    # Test 4: Revenue Agent
    results.append(("Revenue Agent", test_revenue_agent()))
    
    # Test 5: Data relationships
    results.append(("Data Relationships", test_data_relationships()))
    
    # Summary
    print("="*70)
    print("📋 Test Summary")
    print("="*70)
    print()
    
    all_passed = True
    for test_name, passed in results:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"  {status} - {test_name}")
        if not passed:
            all_passed = False
    
    print()
    if all_passed:
        print("🎉 All tests passed! Data integration successful!")
        return 0
    else:
        print("⚠️  Some tests failed. Please check the errors above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())

