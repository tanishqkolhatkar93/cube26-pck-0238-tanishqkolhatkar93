import streamlit as st
import requests
import json
import time

st.set_page_config(page_title="Pack Manager AI", layout="wide")
API_URL = "http://localhost:8000"

st.markdown("""
    <style>
    .seal-banner { background-color: #d4edda; color: #155724; padding: 20px; border-radius: 5px; text-align: center; font-size: 24px; font-weight: bold; }
    .stop-banner { background-color: #f8d7da; color: #721c24; padding: 20px; border-radius: 5px; text-align: center; font-size: 24px; font-weight: bold; }
    .uncertain-banner { background-color: #fff3cd; color: #856404; padding: 20px; border-radius: 5px; text-align: center; font-size: 24px; font-weight: bold; }
    .pending-banner { background-color: #e2e3e5; color: #383d41; padding: 20px; border-radius: 5px; text-align: center; font-size: 24px; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.header("⚙️ Station Config")
    operator_id = st.text_input("Operator ID", value="OP-992")
    org_id = st.selectbox("Tenant (org_id)", ["org_demo_alpha", "org_demo_bravo"])

st.title("Pack Manager AI")
col1, col2 = st.columns(2)
with col1:
    unit_id = st.text_input("Unit ID", value="UNIT-0042")
with col2:
    order_id = st.text_input("Order ID", value="ORD-77382")

expected_lines = st.text_area("Expected Order Lines (SKU:qty)", value="BLUE-SHIRT-M:1; RED-MUG:2")

uploaded_file = st.file_uploader("Upload open box photo", type=["jpg", "jpeg", "png"])

if uploaded_file and st.button("🔍 Verify Package", type="primary"):
    with st.spinner("Analyzing package with Vision AI..."):
        files = {"image": (uploaded_file.name, uploaded_file, uploaded_file.type)}
        data = {
            "unit_id": unit_id,
            "operator_id": operator_id,
            "order_id": order_id,
            "expected_order_lines": expected_lines
        }
        headers = {"x-org-id": org_id}
        
        try:
            start_time = time.time()
            response = requests.post(f"{API_URL}/verify", files=files, data=data, headers=headers)
            processing_time = time.time() - start_time
            
            if response.status_code == 200:
                result = response.json()
                verdict = result["verdict"]
                
                st.subheader("3. Verification Verdict")
                if verdict == "SEAL":
                    st.markdown('<div class="seal-banner">✅ SEAL BOX</div>', unsafe_allow_html=True)
                elif verdict == "STOP_AND_FIX":
                    st.markdown('<div class="stop-banner">❌ STOP & FIX</div>', unsafe_allow_html=True)
                elif verdict == "UNCERTAIN":
                    st.markdown('<div class="uncertain-banner">⚠️ UNCERTAIN (Human Review Required)</div>', unsafe_allow_html=True)
                else:
                    st.markdown('<div class="pending-banner">⎔ PENDING (Fail Open / Network Error)</div>', unsafe_allow_html=True)
                
                st.write(f"⛱️ Processing Time: {processing_time:.2f} seconds")
                st.info(result["reasoning"])
            else:
                st.error(f"API Error: {response.text}")
        except requests.exceptions.ConnectionError:
            st.error("Backend server is not running.")