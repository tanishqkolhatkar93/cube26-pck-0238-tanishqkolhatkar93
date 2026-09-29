import os

path = 'app.py'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the whole CSS block
css_start = content.find('st.markdown("""\n    <style>')
css_end = content.find('""", unsafe_allow_html=True)') + len('""", unsafe_allow_html=True)')

new_css = '''st.markdown("""
    <style>
    /* Global Font Settings */
    h1 {
        font-size: 3rem !important;
        font-weight: 800 !important;
        color: #1E293B !important;
        padding-bottom: 0px !important;
        margin-bottom: 0px !important;
    }
    h3 {
        font-size: 1.5rem !important;
        font-weight: 600 !important;
        color: #475569 !important;
        margin-top: -5px !important;
    }
    .stButton>button {
        border-radius: 8px;
        height: 50px;
        font-size: 18px;
        font-weight: bold;
        background-color: #2563EB;
        color: white;
        transition: all 0.2s;
        border: none;
    }
    .stButton>button:hover {
        background-color: #1D4ED8;
        box-shadow: 0 4px 6px -1px rgba(37,99,235,0.4);
    }
    .seal-banner { background-color: #F0FDF4; border-left: 6px solid #22C55E; color: #166534; padding: 20px; border-radius: 6px; font-size: 24px; font-weight: bold; }
    .stop-banner { background-color: #FEF2F2; border-left: 6px solid #EF4444; color: #991B1B; padding: 20px; border-radius: 6px; font-size: 24px; font-weight: bold; }
    .pending-banner { background-color: #F8FAFC; border-left: 6px solid #64748B; color: #334155; padding: 20px; border-radius: 6px; font-size: 24px; font-weight: bold; }
    .metric-card { background-color: #FFFFFF; padding: 15px; border-radius: 8px; border: 1px solid #E2E8F0; box-shadow: 0 1px 3px 0 rgba(0,0,0,0.1); }
    </style>
""", unsafe_allow_html=True)'''

if css_start != -1:
    content = content[:css_start] + new_css + content[css_end:]

# Replace Main App Header
header_old_1 = '<p class="main-header">'
header_old_2 = '<p class="sub-header">Autonomous Outbound Packaging Verification Agent</p>'
# We need to find the full line for main-header because it might have weird characters
lines = content.split('\n')
new_lines = []
for line in lines:
    if 'class="main-header"' in line:
        new_lines.append('st.markdown("# 📦 Pack Manager AI")')
    elif 'class="sub-header"' in line:
        new_lines.append('st.markdown("### Autonomous Outbound Packaging Verification Agent")')
    elif '1. Order Manifest' in line and 'markdown' in line:
        new_lines.append('    st.markdown("### 📋 1. Order Manifest")')
    elif '2. Visual Inspection' in line and 'markdown' in line:
        new_lines.append('    st.markdown("### 📸 2. Visual Inspection")')
    elif '3. Verification Verdict' in line and 'markdown' in line:
        new_lines.append('    st.markdown("### 🎯 3. Verification Verdict")')
    elif 'Cryptographic Evidence Contract' in line and 'markdown' in line:
        new_lines.append('            st.markdown("### 🔒 Cryptographic Evidence Contract")')
    elif 'VERIFY PACKAGE' in line and 'st.button' in line:
        new_lines.append('            verify_clicked = st.button("🚀 VERIFY PACKAGE", type="primary", use_container_width=True)')
    elif 'Settings' in line and 'st.title' in line:
        new_lines.append('    st.title("⚙️ Settings")')
    elif 'API Key Config' in line and 'st.expander' in line:
        new_lines.append('    with st.expander("🔑 API Key Config", expanded=False):')
    elif 'Station Config' in line and 'st.expander' in line:
        new_lines.append('    with st.expander("📋 Station Config", expanded=True):')
    elif 'SEAL BOX' in line and 'seal-banner' in line:
        new_lines.append('                st.markdown(\'<div class="seal-banner">✅ SEAL BOX</div>\', unsafe_allow_html=True)')
    elif 'STOP & FIX' in line and 'stop-banner' in line:
        new_lines.append('                st.markdown(\'<div class="stop-banner">❌ STOP & FIX</div>\', unsafe_allow_html=True)')
    elif 'UNCERTAIN' in line and 'uncertain-banner' in line:
        new_lines.append('                st.markdown(\'<div class="stop-banner">❌ STOP & FIX</div>\', unsafe_allow_html=True)')
    elif 'PENDING' in line and 'pending-banner' in line:
        new_lines.append('                st.markdown(\'<div class="pending-banner">⏳ PENDING (Fail Open)</div>\', unsafe_allow_html=True)')
    elif 'End-to-End Latency' in line and 'st.metric' in line:
        new_lines.append('            st.metric(label="⏱️ End-to-End Latency", value=f"{processing_time:.2f}s")')
    else:
        new_lines.append(line)

content = '\n'.join(new_lines)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print('UI Update Applied')
