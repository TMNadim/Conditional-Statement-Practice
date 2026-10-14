# ============================================================
#  PASSWORD CHECKER  -  made with if / elif / else only
#
#  Created by: Tanvir Mahatab Nadim
#  Run with  : streamlit run app.py
# ============================================================

import html
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
h1, h2, h3 { color:#ffffff !important; }

.title  { font-size:30px; font-weight:700; color:#fff !important; margin:0; }
.sub    { color:#8b949e !important; margin:2px 0 14px 0; }

.step   { display:flex; align-items:center; gap:10px; margin:22px 0 8px 0; }
.num    { background:#238636; color:#fff !important; font-weight:700; width:28px; height:28px;
          border-radius:50%; display:flex; align-items:center; justify-content:center; }
.stitle { font-size:19px; font-weight:700; color:#fff !important; }
.sdesc  { color:#8b949e !important; font-size:14px; margin:-4px 0 8px 38px; }

/* input box */
div[data-testid="stTextInput"] input {
    background:#010409 !important; color:#7ee787 !important; font-size:18px !important;
    font-family:'Courier New', monospace !important; border:1px solid #30363d !important;
}
div[data-testid="stTextInput"] label { display:none; }

/* terminal output window */
.win     { border:1px solid #30363d; border-radius:8px; overflow:hidden; }
.winbar  { background:#21262d; padding:6px 12px; color:#8b949e !important; font-size:13px; }
.dot     { display:inline-block; width:10px; height:10px; border-radius:50%; margin-right:6px; }
.winbody { background:#010409; padding:14px 16px; font-family:'Courier New', monospace;
           font-size:16px; line-height:1.7; white-space:pre-wrap; }
.g { color:#7ee787 !important; } .r { color:#ff7b72 !important; }
.y { color:#f2cc60 !important; } .w { color:#e6edf3 !important; } .d { color:#8b949e !important; }

/* rules list */
.rule { display:flex; justify-content:space-between; align-items:center; gap:10px;
        border:1px solid #30363d; background:#161b22; border-radius:8px;
        padding:10px 14px; margin-bottom:8px; }
.rule code { font-family:'Courier New', monospace; font-size:15px; color:#e6edf3; }
.rule .res { font-size:14px; font-weight:700; white-space:nowrap; }
.rule.hit  { border-color:#238636; background:#0f2a18; }
.rule.skip { opacity:0.45; }

/* hints */
[data-testid="stExpander"] details { background:#161b22; border:1px solid #30363d; border-radius:8px; }
[data-testid="stExpander"] summary p { color:#f2cc60 !important; font-weight:600; }

.sign { text-align:center; color:#8b949e !important; font-size:13px; margin-top:36px;
        border-top:1px solid #30363d; padding-top:14px; }
</style>
""", unsafe_allow_html=True)


# ------------------------------------------------------------
# SMALL HELPER FUNCTIONS (they only show things on the page)
# ------------------------------------------------------------
def step(number, title, description):
    st.markdown(
        f'<div class="step"><div class="num">{number}</div><div class="stitle">{title}</div></div>'
        f'<div class="sdesc">{description}</div>',
        unsafe_allow_html=True,
    )


def rule_row(order, condition, answer, state):
    """state = 'false', 'true' or 'skip' - decides the colour and the label."""
    if state == "true":
        css, label = "rule hit", '<span class="res g">✔ TRUE → stop here</span>'
    elif state == "false":
        css, label = "rule", '<span class="res r">✘ False → next</span>'
    else:
        css, label = "rule skip", '<span class="res d">not checked</span>'
    st.markdown(
        f'<div class="{css}"><span><b>{order}.</b> <code>{html.escape(condition)}</code>'
        f' &nbsp;→&nbsp; {answer}</span>{label}</div>',
        unsafe_allow_html=True,
    )


# ------------------------------------------------------------
# PAGE TITLE
# ------------------------------------------------------------
st.markdown('<p class="title">🔐 Password Checker</p>', unsafe_allow_html=True)
st.markdown('<p class="sub">A small program made with <b>if / elif / else</b>. '
            'Type a password and see how Python decides.</p>', unsafe_allow_html=True)

# ------------------------------------------------------------
# STEP 1 - INPUT
# ------------------------------------------------------------
step(1, "Type a password", "In your PyCharm code this is the <b>input()</b> line.")
password = st.text_input("password", type="password", placeholder="Type here and press Enter...")

# ------------------------------------------------------------
# THE PROGRAM (this is the part your students must build)
# ------------------------------------------------------------
length = len(password)
matched = 0          # which rule was TRUE (0 = no password yet)

if password == "":
    matched = 0
    strength, tip, color = "", "", "y"
elif length < 6:
    matched = 1
    strength, tip, color = "VERY WEAK", "Use at least 6 characters.", "r"
elif password.isdigit():
    matched = 2
    strength, tip, color = "WEAK", "Only numbers. Add some letters.", "r"
elif password.isalpha():
    matched = 3
    strength, tip, color = "MEDIUM", "Only letters. Add numbers too.", "y"
elif length >= 10:
    matched = 4
    strength, tip, color = "STRONG", "Great password!", "g"
else:
    matched = 5
    strength, tip, color = "GOOD", "Make it 10+ characters to be STRONG.", "g"

# ------------------------------------------------------------
# STEP 2 - OUTPUT (your students' program must print this)
# ------------------------------------------------------------
step(2, "Program output", "Your program must print <b>exactly</b> this.")

if matched == 0:
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
# STEP 3 - HOW PYTHON DECIDED
# ------------------------------------------------------------
step(3, "How Python decided",
     "Python checks the rules <b>from top to bottom</b> and stops at the first TRUE.")

if matched == 0:
    s1 = s2 = s3 = s4 = s5 = "skip"
elif matched == 1:
    s1, s2, s3, s4, s5 = "true", "skip", "skip", "skip", "skip"
elif matched == 2:
    s1, s2, s3, s4, s5 = "false", "true", "skip", "skip", "skip"
elif matched == 3:
    s1, s2, s3, s4, s5 = "false", "false", "true", "skip", "skip"
elif matched == 4:
    s1, s2, s3, s4, s5 = "false", "false", "false", "true", "skip"
else:
    s1, s2, s3, s4, s5 = "false", "false", "false", "false", "true"

rule_row(1, "if length < 6:",             "VERY WEAK", s1)
rule_row(2, "elif password.isdigit():",   "WEAK",      s2)
rule_row(3, "elif password.isalpha():",   "MEDIUM",    s3)
rule_row(4, "elif length >= 10:",         "STRONG",    s4)
rule_row(5, "else:",                      "GOOD",      "true" if matched == 5 else "skip")

# ------------------------------------------------------------
# STEP 4 - HINTS
# ------------------------------------------------------------
step(4, "Need help? Open a hint", "Try first. Open a hint only if you are stuck.")

with st.expander("💡 Hint 1 – How do I count the characters?"):
    st.write("Use `len()`. Example: `len(\"hello\")` gives `5`.")
    st.code('length = len(password)', language="python")

with st.expander("💡 Hint 2 – How do I check only numbers or only letters?"):
    st.write("`password.isdigit()` is True if the password has **only numbers**.")
    st.write("`password.isalpha()` is True if the password has **only letters**.")

with st.expander("💡 Hint 3 – Why is the order important?"):
    st.write("Python stops at the **first** True condition. "
             "So put the worst cases first: too short, only numbers, only letters.")

with st.expander("💡 Hint 4 – How do I make the stars?"):
    st.write("`\"*\" * 3` gives `***`. Use your `length` variable.")
    st.code('print(f"Password : {\'*\' * length}")', language="python")

with st.expander("💡 Hint 5 – What if the user types nothing?"):
    st.write("An empty password is `\"\"`. Check it first: `if password == \"\":`")

# ------------------------------------------------------------
# SIGNATURE
# ------------------------------------------------------------
st.markdown('<div class="sign">Created by <b>Tanvir Mahatab Nadim</b> · '
            'Python Basics · Conditional Statements</div>', unsafe_allow_html=True)
