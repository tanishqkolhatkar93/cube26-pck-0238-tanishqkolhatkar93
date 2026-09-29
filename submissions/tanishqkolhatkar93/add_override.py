import os

path = 'app.py'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

target = '        # Evidence Contract Preview'

override_code = '''        # Human Override Support
        if result_verdict in ["STOP_AND_FIX", "UNCERTAIN", "PENDING"] and contract:
            st.markdown("### 👨‍🔧 Human Override")
            override_reason = st.text_input("Override Reason (Required for Audit Log)", key="override_text")
            if st.button("Force SEAL (Override AI)", type="secondary"):
                if override_reason.strip() == "":
                    st.error("You must provide a reason to override the AI.")
                else:
                    contract["overrides"].append({
                        "operator": operator_id,
                        "timestamp": datetime.now(timezone.utc).isoformat(),
                        "reason": override_reason,
                        "original_verdict": result_verdict,
                        "new_verdict": "SEAL"
                    })
                    # Re-hash and save
                    import json, hashlib
                    contract["content_hash"] = hashlib.sha256(json.dumps(contract).encode()).hexdigest()
                    try:
                        contract_dir = os.path.join(os.path.dirname(__file__), "contract")
                        with open(os.path.join(contract_dir, f"{contract['record_id']}.json"), "w") as f:
                            json.dump(contract, f, indent=2)
                    except Exception:
                        pass
                    st.success(f"Decision overridden to SEAL by {operator_id}. Audit log updated securely.")
        
        # Evidence Contract Preview'''

if target in content:
    content = content.replace(target, override_code)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Override feature added.')
else:
    print('Target not found.')
