# ============================================================
#  PASSWORD CHECKER  -  made with if / elif / else only
#
#  Created by: Tanvir Mahatab Nadim
#  Run with  : streamlit run app.py
# ============================================================

import streamlit as st

st.set_page_config(page_title="Password Checker", page_icon="🔐", layout="centered")

# ------------------------------------------------------------
# LOOK AND FEEL (students can skip this part)
# ------------------------------------------------------------
st.markdown("""
<style>
.stApp { background:#0d1117; }
header, footer, [data-testid="stToolbar"], [data-testid="stSidebar"] { display:none !important; }
.block-container { padding-top:1.5rem; max-width:720px; }

html, body, p, li, label, span, div { color:#e6edf3; font-size:16px; }

.title  { font-size:30px; font-weight:700; color:#fff !important; margin:0; }
.sub    { color:#8b949e !important; margin:2px 0 14px 0; }

.step   { display:flex; align-items:center; gap:10px; margin:22px 0 8px 0; }
.num    { background:#238636; color:#fff !important; font-weight:700; width:28px; height:28px;
          border-radius:50%; display:flex; align-items:center; justify-content:center; }
.stitle { font-size:19px; font-weight:700; color:#fff !important; }

div[data-testid="stTextInput"] input {
    background:#010409 !important; color:#7ee787 !important; font-size:18px !important;
    font-family:'Courier New', monospace !important; border:1px solid #30363d !important;
}
div[data-testid="stTextInput"] label { display:none; }

.win     { border:1px solid #30363d; border-radius:8px; overflow:hidden; }
.winbar  { background:#21262d; padding:6px 12px; color:#8b949e !important; font-size:13px; }
.dot     { display:inline-block; width:10px; height:10px; border-radius:50%; margin-right:6px; }
.winbody { background:#010409; padding:14px 16px; font-family:'Courier New', monospace;
           font-size:16px; line-height:1.7; white-space:pre-wrap; }
.g { color:#7ee787 !important; } .r { color:#ff7b72 !important; }
.y { color:#f2cc60 !important; } .w { color:#e6edf3 !important; } .d { color:#8b949e !important; }

.sign { text-align:center; color:#8b949e !important; font-size:13px; margin-top:36px;
        border-top:1px solid #30363d; padding-top:14px; }
</style>
""", unsafe_allow_html=True)


def step(number, title):
    st.markdown(
        f'<div class="step"><div class="num">{number}</div><div class="stitle">{title}</div></div>',
        unsafe_allow_html=True,
    )


# ------------------------------------------------------------
# TITLE
# ------------------------------------------------------------
st.markdown('<p class="title">🔐 Password Checker</p>', unsafe_allow_html=True)
st.markdown('<p class="sub">Made with <b>if / elif / else</b></p>', unsafe_allow_html=True)

# ------------------------------------------------------------
# STEP 1 - TYPE PASSWORD (plain text, no hidden characters)
# ------------------------------------------------------------
step(1, "Type a password")
password = st.text_input("password", placeholder="Type here and press Enter...")

# ------------------------------------------------------------
# THE PROGRAM (this is the part your students must build)
# ------------------------------------------------------------
length = len(password)

if password == "":
    strength, tip, color = "", "", "d"
elif length < 6:
    strength, tip, color = "VERY WEAK", "Use at least 6 characters.", "r"
elif password.isdigit():
    strength, tip, color = "WEAK", "Only numbers. Add some letters.", "r"
elif password.isalpha():
    strength, tip, color = "MEDIUM", "Only letters. Add numbers too.", "y"
elif length >= 10:
    strength, tip, color = "STRONG", "Great password!", "g"
else:
    strength, tip, color = "GOOD", "Make it 10+ characters to be STRONG.", "g"

# ------------------------------------------------------------
# STEP 2 - OUTPUT
# ------------------------------------------------------------
step(2, "Output")

if password == "":
    body = '<span class="d">waiting for input...</span>'
else:
    body = (
        f'<span class="w">Password : {"*" * length}</span>\n'
        f'<span class="w">Length   : {length}</span>\n'
        f'<span class="{color}">Strength : {strength}</span>\n'
        f'<span class="{color}">Tip      : {tip}</span>'
    )

st.markdown(
    '<div class="win"><div class="winbar">'
    '<span class="dot" style="background:#ff5f56"></span>'
    '<span class="dot" style="background:#ffbd2e"></span>'
    '<span class="dot" style="background:#27c93f"></span> Run: password_checker</div>'
    f'<div class="winbody">{body}</div></div>',
    unsafe_allow_html=True,
)

# ------------------------------------------------------------
# SIGNATURE
# ------------------------------------------------------------
st.markdown('<div class="sign">Created by <b>Tanvir Mahatab Nadim</b></div>',
            unsafe_allow_html=True)
