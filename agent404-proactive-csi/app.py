"""
ProActive CSI - Streamlit Web UI
Enterprise Revenue & Risk Intelligence Agent Demo
"""

import streamlit as st
import pandas as pd
import sys
import os
from datetime import datetime
import json

# Add agents to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from agents.customer_success_agent import CustomerSuccessAgent
from agents.procurement_agent import ProcurementAgent
from agents.revenue_agent import RevenueAgent
from workflows.orchestrator import WorkflowOrchestrator

# Page configuration
st.set_page_config(
    page_title="ProActive CSI - Agent 404",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #0f62fe;
        margin-bottom: 0;
    }
    .sub-header {
        text-align: center;
        color: #666;
        margin-top: 0;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 10px;
        color: white;
        text-align: center;
    }
    .risk-critical {
        color: #da1e28;
        font-weight: bold;
    }
    .risk-high {
        color: #ff832b;
        font-weight: bold;
    }
    .risk-medium {
        color: #f1c21b;
        font-weight: bold;
    }
    .risk-low {
        color: #24a148;
        font-weight: bold;
    }
    .workflow-box {
        border: 2px solid #0f62fe;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'orchestrator' not in st.session_state:
    st.session_state.orchestrator = WorkflowOrchestrator()
    st.session_state.cs_agent = st.session_state.orchestrator.cs_agent
    st.session_state.proc_agent = st.session_state.orchestrator.procurement_agent
    st.session_state.revenue_agent = st.session_state.orchestrator.revenue_agent

# Header
st.markdown('<h1 class="main-header">🚀 ProActive CSI</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Enterprise Revenue & Risk Intelligence Agent | Powered by IBM watsonx Orchestrate</p>', unsafe_allow_html=True)

# Sidebar
st.sidebar.title("🎛️ Control Panel")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigate",
    ["🏠 Dashboard", "🔮 Customer Intelligence", "📦 Procurement Monitor", 
     "💰 Revenue Protection", "⚡ Workflows", "📊 Executive Brief"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 🤖 Multi-Agent System")
st.sidebar.success("✅ Customer Success Agent")
st.sidebar.success("✅ Procurement Agent")
st.sidebar.success("✅ Revenue Protection Agent")
st.sidebar.markdown("---")
st.sidebar.info("**IBM watsonx Services**\n- watsonx.ai\n- watsonx Orchestrate\n- NLU\n- Speech-to-Text\n- Text-to-Speech\n- Cloudant")

# ===== PAGE: Dashboard =====
if page == "🏠 Dashboard":
    st.title("📊 Executive Dashboard")
    
    # Get all critical customers
    critical_customers = st.session_state.cs_agent.get_critical_customers(threshold=0.5)
    
    # Get procurement issues
    vendor_delays = st.session_state.proc_agent.detect_vendor_delays(threshold_days=5)
    
    # Calculate revenue exposure
    churn_predictions = {c['customer_id']: c['churn_probability'] for c in critical_customers}
    revenue_exposure = st.session_state.revenue_agent.get_total_revenue_exposure(churn_predictions)
    
    # Top metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "🚨 Critical Customers",
            len([c for c in critical_customers if c['churn_probability'] >= 0.7]),
            delta=f"-{len([c for c in critical_customers if c['churn_probability'] >= 0.7])} need action",
            delta_color="inverse"
        )
    
    with col2:
        st.metric(
            "💰 ARR at Risk",
            f"${revenue_exposure['total_arr_at_risk']:,.0f}",
            delta=f"{revenue_exposure['portfolio_risk_percentage']:.1f}% of portfolio",
            delta_color="inverse"
        )
    
    with col3:
        st.metric(
            "📦 Vendor Delays",
            len(vendor_delays),
            delta=f"{sum(v['num_affected'] for v in vendor_delays)} customers affected",
            delta_color="inverse"
        )
    
    with col4:
        st.metric(
            "🎯 Interventions Needed",
            len(critical_customers),
            delta="Immediate action required"
        )
    
    st.markdown("---")
    
    # Two column layout
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.subheader("🔴 Top At-Risk Customers")
        if critical_customers:
            for i, customer in enumerate(critical_customers[:5], 1):
                risk_class = "risk-critical" if customer['churn_probability'] >= 0.7 else "risk-high"
                st.markdown(f"""
                <div class="workflow-box">
                    <strong>{i}. {customer['name']}</strong><br>
                    Churn Risk: <span class="{risk_class}">{customer['churn_probability']*100:.0f}%</span><br>
                    Contract Value: ${customer['contract_value']:,}<br>
                    Renewal: {customer['renewal_date']}
                </div>
                """, unsafe_allow_html=True)
        else:
            st.success("✅ No critical customers at this time!")
    
    with col_right:
        st.subheader("⚠️ Procurement Alerts")
        if vendor_delays:
            for vendor in vendor_delays[:5]:
                st.markdown(f"""
                <div class="workflow-box">
                    <strong>{vendor['vendor_name']}</strong><br>
                    Delay: {vendor['delay_days']} days<br>
                    Affected Customers: {vendor['num_affected']}<br>
                    Severity: <span class="risk-high">{vendor['severity']:.2f}</span>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.success("✅ No vendor delays detected!")
    
    st.markdown("---")
    st.subheader("📈 Revenue Protection Breakdown")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("🔴 Critical Risk ARR", f"${revenue_exposure['risk_breakdown']['critical']:,.0f}")
    with col2:
        st.metric("🟠 High Risk ARR", f"${revenue_exposure['risk_breakdown']['high']:,.0f}")
    with col3:
        st.metric("🟡 Medium Risk ARR", f"${revenue_exposure['risk_breakdown']['medium']:,.0f}")

# ===== PAGE: Customer Intelligence =====
elif page == "🔮 Customer Intelligence":
    st.title("🔮 Customer Success Intelligence")
    
    # Customer selection
    customers_df = st.session_state.cs_agent.customers_df
    customer_list = customers_df['customer_id'].tolist()
    
    selected_customer = st.selectbox(
        "Select Customer",
        customer_list,
        format_func=lambda x: f"{x} - {customers_df[customers_df['customer_id']==x]['name'].values[0]}"
    )
    
    if st.button("🔍 Analyze Customer Health", type="primary"):
        with st.spinner("Analyzing customer health..."):
            health = st.session_state.cs_agent.analyze_customer_health(selected_customer)
            
            st.markdown(f"## {health['risk_color']} {health['name']}")
            
            # Risk overview
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Churn Probability", f"{health['churn_probability']*100:.1f}%")
            with col2:
                st.metric("Risk Level", health['risk_level'])
            with col3:
                st.metric("Contract Value", f"${health['contract_info']['value']:,}")
            
            st.markdown("---")
            
            # Health metrics
            st.subheader("📊 Health Metrics")
            metrics = health['health_metrics']
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Usage Drop", f"{metrics['usage_drop_pct']}%")
                st.metric("Ticket Volume (30d)", metrics['ticket_volume'])
            with col2:
                st.metric("Sentiment Score", f"{metrics['sentiment_score']:.2f}")
                st.metric("NPS Score", metrics['nps_score'])
            
            # Intervention recommendations
            st.markdown("---")
            st.subheader("🎯 Recommended Interventions")
            intervention = st.session_state.cs_agent.recommend_intervention(selected_customer)
            
            st.info(f"**Priority:** {intervention['priority']}")
            st.info(f"**Success Probability:** {intervention['success_probability']*100:.0f}%")
            
            for i, action in enumerate(intervention['recommended_interventions'], 1):
                st.markdown(f"{i}. {action}")
            
            # Recent activity
            st.markdown("---")
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("🎫 Recent Tickets")
                if health['recent_tickets']:
                    for ticket in health['recent_tickets']:
                        st.markdown(f"**{ticket['ticket_id']}** - {ticket['category']}")
                        st.caption(f"{ticket['description'][:100]}...")
                        st.caption(f"Sentiment: {ticket['sentiment']}")
                        st.markdown("---")
            
            with col2:
                st.subheader("💬 Recent Communications")
                if health['recent_communications']:
                    for comm in health['recent_communications']:
                        st.markdown(f"**{comm['channel'].upper()}** - {comm['date']}")
                        st.caption(f"{comm['message'][:100]}...")
                        st.caption(f"Sentiment: {comm['sentiment']}")
                        st.markdown("---")

# ===== PAGE: Procurement Monitor =====
elif page == "📦 Procurement Monitor":
    st.title("📦 Procurement Intelligence")
    
    vendor_delays = st.session_state.proc_agent.detect_vendor_delays(threshold_days=1)
    
    st.subheader(f"⚠️ Vendor Performance Overview ({len(vendor_delays)} vendors with delays)")
    
    if vendor_delays:
        for vendor in vendor_delays:
            with st.expander(f"{vendor['vendor_name']} - {vendor['delay_days']} days late"):
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.metric("Delay Days", vendor['delay_days'])
                    st.metric("Defect Rate", f"{vendor['defect_rate']*100:.1f}%")
                
                with col2:
                    st.metric("Contract Value", f"${vendor['contract_value']:,}")
                    st.metric("Customers Affected", vendor['num_affected'])
                
                with col3:
                    st.metric("Severity Score", f"{vendor['severity']:.2f}")
                
                st.markdown("---")
                st.markdown("**Affected Customers:**")
                st.write(", ".join(vendor['affected_customers']))
                
                # Correlation analysis
                if st.button(f"🔗 Analyze Customer Impact", key=f"analyze_{vendor['vendor_id']}"):
                    correlation = st.session_state.proc_agent.correlate_vendor_to_customer_risk(vendor['vendor_id'])
                    
                    st.warning(f"**Risk Level:** {correlation['risk_color']} {correlation['risk_level']}")
                    
                    st.markdown("**Recommended Actions:**")
                    for action in correlation['customer_impact_prediction']['recommended_actions']:
                        st.markdown(f"• {action}")
                    
                    if correlation['penalties_triggered']:
                        st.error("🚨 **Contract Penalties Triggered:**")
                        for penalty in correlation['penalties_triggered']:
                            st.markdown(f"• Contract {penalty['contract_id']}: {penalty['penalty']}")
    else:
        st.success("✅ All vendors are performing on schedule!")
    
    st.markdown("---")
    st.subheader("📊 Vendor Scorecard")
    
    vendors_df = st.session_state.proc_agent.vendors_df
    vendor_id = st.selectbox("Select Vendor", vendors_df['vendor_id'].tolist())
    
    if st.button("📈 Generate Scorecard"):
        scorecard = st.session_state.proc_agent.get_vendor_performance_scorecard(vendor_id)
        
        st.markdown(f"### {scorecard['vendor_name']}")
        st.markdown(f"**Overall Rating:** {scorecard['rating']}")
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Overall Score", f"{scorecard['overall_score']:.1f}/100")
            st.metric("On-Time Delivery", f"{scorecard['performance_metrics']['on_time_delivery_score']:.1f}")
        with col2:
            st.metric("Quality Score", f"{scorecard['performance_metrics']['quality_score']:.1f}")
            st.metric("Contract Value", f"${scorecard['contract_value']:,}")
        
        st.info(f"**Recommendation:** {scorecard['recommendation']}")

# ===== PAGE: Revenue Protection =====
elif page == "💰 Revenue Protection":
    st.title("💰 Revenue Protection Dashboard")
    
    # Get critical customers for revenue analysis
    critical_customers = st.session_state.cs_agent.get_critical_customers(threshold=0.3)
    churn_predictions = {c['customer_id']: c['churn_probability'] for c in critical_customers}
    
    # Generate CFO briefing
    cfo_briefing = st.session_state.revenue_agent.generate_cfo_briefing(churn_predictions)
    
    st.subheader("📊 Executive Summary")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Annual Revenue", f"${cfo_briefing['executive_summary']['total_annual_revenue']:,.0f}")
    with col2:
        st.metric("Revenue at Risk", f"${cfo_briefing['executive_summary']['revenue_at_risk']:,.0f}")
    with col3:
        st.metric("Portfolio Risk", f"{cfo_briefing['executive_summary']['portfolio_risk_percentage']:.1f}%")
    with col4:
        st.metric("Customers at Risk", cfo_briefing['executive_summary']['customers_at_risk'])
    
    st.markdown("---")
    
    st.subheader("💵 Financial Scenarios")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Best Case Loss", f"${cfo_briefing['financial_scenarios']['best_case_loss']:,.0f}", 
                 help="Assuming 80% retention success rate")
    with col2:
        st.metric("Expected Case Loss", f"${cfo_briefing['financial_scenarios']['expected_case_loss']:,.0f}",
                 help="Assuming 50% retention success rate")
    with col3:
        st.metric("Worst Case Loss", f"${cfo_briefing['financial_scenarios']['worst_case_loss']:,.0f}",
                 help="Assuming 20% retention success rate")
    
    st.markdown("---")
    
    st.subheader("💼 Intervention Economics")
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("Recommended Investment", f"${cfo_briefing['intervention_economics']['recommended_investment']:,.0f}")
        st.metric("Expected Revenue Saved", f"${cfo_briefing['intervention_economics']['expected_revenue_saved']:,.0f}")
    
    with col2:
        st.metric("Estimated ROI", f"{cfo_briefing['intervention_economics']['estimated_roi']:.0f}%")
        st.metric("Payback Period", f"{cfo_briefing['intervention_economics']['payback_period_months']} months")
    
    st.markdown("---")
    
    st.subheader("🎯 Top Revenue Risks")
    for i, risk in enumerate(cfo_briefing['top_revenue_risks'][:5], 1):
        st.markdown(f"""
        <div class="workflow-box">
            <strong>{i}. {risk['customer_name']}</strong><br>
            ARR at Risk: ${risk['arr_at_risk']:,.0f}<br>
            Churn Probability: {risk['churn_probability']*100:.0f}%<br>
            Days to Renewal: {risk['days_to_renewal']}<br>
            Urgency: <span class="risk-{risk['urgency'].lower()}">{risk['urgency']}</span>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.subheader("📋 Strategic Recommendations")
    for rec in cfo_briefing['strategic_recommendations']:
        st.markdown(f"• {rec}")

# ===== PAGE: Workflows =====
elif page == "⚡ Workflows":
    st.title("⚡ Workflow Execution Center")
    
    st.info("🤖 **Powered by IBM watsonx Orchestrate** - Multi-agent workflow coordination")
    
    workflow_type = st.selectbox(
        "Select Workflow",
        [
            "Workflow 1: Churn Prediction",
            "Workflow 2: Procurement Early-Warning",
            "Workflow 3: Customer Escalation Auto-Resolution",
            "Workflow 4: Contract Renewal Prep",
            "Workflow 5: Daily Executive Brief",
            "Workflow 6: Procurement-Customer Impact Bridge"
        ]
    )
    
    # Workflow 1: Churn Prediction
    if "Workflow 1" in workflow_type:
        st.markdown("### 🔮 Workflow 1: Churn Prediction")
        st.markdown("*Predicts customer churn and triggers automated interventions*")
        
        customers_df = st.session_state.cs_agent.customers_df
        customer = st.selectbox("Select Customer", customers_df['customer_id'].tolist())
        
        if st.button("▶️ Execute Workflow", type="primary"):
            with st.spinner("Executing churn prediction workflow..."):
                result = st.session_state.orchestrator.workflow_churn_prediction(customer)
                
                st.success("✅ Workflow completed successfully!")
                
                st.json(result)
    
    # Workflow 2: Procurement Early-Warning
    elif "Workflow 2" in workflow_type:
        st.markdown("### 📦 Workflow 2: Procurement Early-Warning")
        st.markdown("*Detects vendor delays and correlates customer impact*")
        
        vendors_df = st.session_state.proc_agent.vendors_df
        vendor = st.selectbox("Select Vendor", vendors_df['vendor_id'].tolist())
        
        if st.button("▶️ Execute Workflow", type="primary"):
            with st.spinner("Executing procurement early-warning workflow..."):
                result = st.session_state.orchestrator.workflow_procurement_early_warning(vendor)
                
                st.success("✅ Workflow completed successfully!")
                st.json(result)
    
    # Workflow 3: Customer Escalation
    elif "Workflow 3" in workflow_type:
        st.markdown("### 🚨 Workflow 3: Customer Escalation Auto-Resolution")
        st.markdown("*Automatically escalates high-risk customers and creates action plans*")
        
        customers_df = st.session_state.cs_agent.customers_df
        customer = st.selectbox("Select Customer", customers_df['customer_id'].tolist())
        
        if st.button("▶️ Execute Workflow", type="primary"):
            with st.spinner("Executing escalation workflow..."):
                result = st.session_state.orchestrator.workflow_customer_escalation(customer)
                
                st.success("✅ Workflow completed successfully!")
                st.json(result)
    
    # Workflow 4: Renewal Prep
    elif "Workflow 4" in workflow_type:
        st.markdown("### 📄 Workflow 4: Contract Renewal Prep")
        st.markdown("*Prepares renewal packages with AI-generated content*")
        
        customers_df = st.session_state.cs_agent.customers_df
        customer = st.selectbox("Select Customer", customers_df['customer_id'].tolist())
        
        if st.button("▶️ Execute Workflow", type="primary"):
            with st.spinner("Preparing renewal package..."):
                result = st.session_state.orchestrator.workflow_contract_renewal_prep(customer)
                
                st.success("✅ Workflow completed successfully!")
                st.json(result)
    
    # Workflow 5: Executive Brief
    elif "Workflow 5" in workflow_type:
        st.markdown("### 📊 Workflow 5: Daily Executive Brief")
        st.markdown("*Generates comprehensive executive briefing from all agents*")
        
        if st.button("▶️ Execute Workflow", type="primary"):
            with st.spinner("Generating executive brief..."):
                result = st.session_state.orchestrator.workflow_daily_executive_brief()
                
                st.success("✅ Workflow completed successfully!")
                
                st.markdown("### Executive Brief")
                st.code(result['executive_brief'])
                
                with st.expander("View Full Results"):
                    st.json(result)
    
    # Workflow 6: Procurement-Customer Bridge
    elif "Workflow 6" in workflow_type:
        st.markdown("### 🔗 Workflow 6: Procurement-Customer Impact Bridge")
        st.markdown("*Bridges vendor issues to customer impact with cross-team coordination*")
        
        vendors_df = st.session_state.proc_agent.vendors_df
        vendor = st.selectbox("Select Vendor", vendors_df['vendor_id'].tolist())
        
        if st.button("▶️ Execute Workflow", type="primary"):
            with st.spinner("Executing bridge workflow..."):
                result = st.session_state.orchestrator.workflow_procurement_customer_bridge(vendor)
                
                st.success("✅ Workflow completed successfully!")
                st.json(result)

# ===== PAGE: Executive Brief =====
elif page == "📊 Executive Brief":
    st.title("📊 Executive Briefing")
    
    if st.button("📄 Generate Daily Executive Brief", type="primary"):
        with st.spinner("Generating comprehensive executive brief..."):
            result = st.session_state.orchestrator.workflow_daily_executive_brief()
            
            st.success("✅ Executive brief generated!")
            
            st.markdown("## 🎯 Daily Executive Brief")
            st.code(result['executive_brief'])
            
            st.markdown("---")
            
            st.subheader("📊 Risk Summary")
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown("### 👥 Customer Success")
                st.metric("Critical Customers", result['risk_summary']['customer_success']['critical_customers'])
                st.metric("High Risk Customers", result['risk_summary']['customer_success']['high_risk_customers'])
            
            with col2:
                st.markdown("### 📦 Procurement")
                st.metric("Delayed Vendors", result['risk_summary']['procurement']['delayed_vendors'])
                st.metric("Customers Affected", result['risk_summary']['procurement']['customers_affected'])
            
            with col3:
                st.markdown("### 💰 Revenue")
                st.metric("ARR at Risk", f"${result['risk_summary']['revenue']['total_arr_at_risk']:,.0f}")
                st.metric("Portfolio Risk", f"{result['risk_summary']['revenue']['portfolio_risk_pct']:.1f}%")
            
            st.markdown("---")
            
            st.subheader("💡 Revenue Insight")
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric("Total ARR at Risk", f"${result['revenue_insight']['total_arr_at_risk']:,.0f}")
                st.metric("Expected Loss", f"${result['revenue_insight']['expected_loss']:,.0f}")
            
            with col2:
                st.metric("Recommended Investment", f"${result['revenue_insight']['recommended_investment']:,.0f}")
                st.metric("Estimated ROI", f"{result['revenue_insight']['estimated_roi']:.0f}%")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <strong>ProActive CSI - Agent 404</strong><br>
    Enterprise Revenue & Risk Intelligence Agent<br>
    Powered by IBM watsonx Orchestrate | Built for IBM Hackathon 2025
</div>
""", unsafe_allow_html=True)

