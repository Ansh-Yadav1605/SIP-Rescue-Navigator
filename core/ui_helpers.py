"""
core/ui_helpers.py — Shared styling and UI helper components for SIP Rescue Navigator.
"""

import streamlit as st

CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

h1, h2, h3, h4, h5, h6 {
    font-family: 'Outfit', sans-serif !important;
    font-weight: 700 !important;
    letter-spacing: -0.02em !important;
}

.glass-card {
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 12px;
    padding: 18px 22px;
    margin-bottom: 16px;
    backdrop-filter: blur(8px);
    transition: all 0.2s ease-in-out;
}

.glass-card:hover {
    border-color: rgba(16, 185, 129, 0.35);
    background: rgba(255, 255, 255, 0.06);
}

.hero-header {
    background: linear-gradient(135deg, rgba(16, 185, 129, 0.15) 0%, rgba(59, 130, 246, 0.12) 100%);
    border: 1px solid rgba(16, 185, 129, 0.25);
    border-radius: 14px;
    padding: 24px 28px;
    margin-bottom: 24px;
}

.hero-title {
    font-size: 1.8rem;
    font-weight: 800;
    margin-bottom: 6px;
    background: linear-gradient(90deg, #FFFFFF 0%, #CBD5E1 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-subtitle {
    color: #94A3B8;
    font-size: 0.95rem;
    margin: 0;
}

.badge {
    display: inline-block;
    padding: 3px 10px;
    border-radius: 9999px;
    font-size: 0.72rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    margin-right: 6px;
}

.badge-relevant {
    background: rgba(16, 185, 129, 0.18);
    color: #34D399;
    border: 1px solid rgba(16, 185, 129, 0.35);
}

.badge-source {
    background: rgba(139, 92, 246, 0.16);
    color: #A78BFA;
    border: 1px solid rgba(139, 92, 246, 0.3);
}

.metric-pill {
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 10px;
    padding: 14px 18px;
    text-align: center;
}

.metric-pill-val {
    font-family: 'Outfit', sans-serif;
    font-size: 1.8rem;
    font-weight: 700;
    color: #F8FAFC;
    line-height: 1.1;
}

.metric-pill-label {
    font-size: 0.78rem;
    color: #94A3B8;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-top: 4px;
}

.evidence-box {
    border-left: 3px solid #10B981;
    background: rgba(16, 185, 129, 0.08);
    padding: 8px 14px;
    border-radius: 0 8px 8px 0;
    margin: 8px 0;
    font-style: italic;
    color: #E2E8F0;
    font-size: 0.92rem;
}

.missing-box {
    border-left: 3px solid #F59E0B;
    background: rgba(245, 158, 11, 0.08);
    padding: 8px 14px;
    border-radius: 0 8px 8px 0;
    margin: 8px 0;
    color: #FDE68A;
    font-size: 0.88rem;
}
</style>
"""

def apply_custom_styles():
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

def render_sidebar_status():
    st.sidebar.markdown("### 🛟 SIP Rescue Navigator")
    st.sidebar.markdown(
        """
        <div style="background: rgba(16, 185, 129, 0.12); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 8px; padding: 10px 12px; margin-bottom: 12px;">
            <strong style="color: #34D399;">Continuity Assistant</strong>
            <div style="font-size: 0.78rem; color: #94A3B8; margin-top: 4px;">Engine: <code>Verified Rules 2026</code></div>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.sidebar.caption("Prototype simulation only. Does not connect to live bank accounts or modify real mandates.")
