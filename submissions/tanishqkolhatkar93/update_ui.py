import os

path = 'app.py'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update CSS
css_old = '.main-header { font-size: 42px; font-weight: 800; color: #1E3A8A; margin-bottom: 0px; }\n    .sub-header { font-size: 18px; color: #6B7280; margin-top: -10px; margin-bottom: 30px; }'
css_new = '.main-header { font-size: 72px; font-weight: 900; background: -webkit-linear-gradient(45deg, #1E3A8A, #3B82F6, #93C5FD); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 0px; text-align: center; padding-top: 10px; text-shadow: 2px 2px 4px rgba(0,0,0,0.1); line-height: 1.2; }\n    .sub-header { font-size: 24px; color: #6B7280; margin-top: 5px; margin-bottom: 40px; text-align: center; font-weight: 600; letter-spacing: 1px; }\n    .section-title { font-size: 28px; font-weight: 800; color: #1E3A8A; margin-bottom: 20px; border-bottom: 3px solid #E5E7EB; padding-bottom: 10px; }\n    .stButton>button { border-radius: 12px; height: 60px; font-size: 22px; font-weight: 900; text-transform: uppercase; letter-spacing: 1.5px; transition: all 0.3s; box-shadow: 0 4px 6px -1px rgba(37,99,235,0.4); }\n    .stButton>button:hover { transform: translateY(-2px); box-shadow: 0 10px 15px -3px rgba(37,99,235,0.6); }'
content = content.replace(css_old, css_new)

# 2. Update Manifest Header
content = content.replace('st.markdown("### 📋 1. Order Manifest")', 'st.markdown(\'<div class="section-title">📋 1. Order Manifest</div>\', unsafe_allow_html=True)')

# 3. Update Visual Inspection Section
old_visual = '''st.markdown("### 📸 2. Visual Inspection")
    uploaded_file = st.file_uploader("Upload open box overhead photo", type=["jpg", "jpeg", "png"], help="Ensure good lighting and top-down angle.")
    verify_clicked = False
    if uploaded_file:
        st.image(uploaded_file, caption="Captured Image Preview", use_container_width=True)
        verify_clicked = st.button("🚀 VERIFY PACKAGE", type="primary")'''

new_visual = '''st.markdown('<div class="section-title">📸 2. Visual Inspection</div>', unsafe_allow_html=True)
    with st.container(border=True):
        uploaded_file = st.file_uploader("Upload open box overhead photo", type=["jpg", "jpeg", "png"], help="Ensure good lighting and top-down angle.")
        verify_clicked = False
        if uploaded_file:
            st.markdown("<br>", unsafe_allow_html=True)
            st.image(uploaded_file, caption="Captured Image Preview", use_container_width=True)
            st.markdown("<br>", unsafe_allow_html=True)
            verify_clicked = st.button("🚀 VERIFY PACKAGE", type="primary", use_container_width=True)'''

content = content.replace(old_visual, new_visual)

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print('UI Update Applied')
