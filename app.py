# ============================================================
#  PASSWORD CHECKER - raw terminal style
#  Made with if / elif / else only
#
#  Created by: Tanvir Mahatab Nadim
#  Run with  : streamlit run app.py
# ============================================================

import html
import streamlit as st

st.set_page_config(page_title="password_checker.py", page_icon=">_", layout="centered")

# ---------- raw terminal look (students can skip this part) ----------
st.markdown("""
<style>
.stApp { background:#000; }
header, footer, [data-testid="stToolbar"], [data-testid="stSidebar"] { display:none !important; }
.block-container { padding-top:2rem; max-width:760px; }
html, body, p, span, div, label, input {
    font-family: 'Courier New', Consolas, monospace !important;
    color:#d0d0d0; font-size:15px;
}
.t { white-space:pre-wrap; line-height:1.55; margin:0; }
.g { color:#33ff66 !important; }  /* green  */
.r { color:#ff5555 !important; }  /* red    */
.y { color:#ffd24d !important; }  /* yellow */
.c { color:#6c6c6c !important; }  /* grey comment */
div[data-testid="stTextInput"] input {
    background:#000 !important; color:#33ff66 !important;
    border:none !important; border-bottom:1px solid #33ff66 !important;
    border-radius:0 !important; box-shadow:none !important; padding-left:0;
}
div[data-testid="stTextInput"] label p { color:#d0d0d0 !important; }
div[data-testid="stCheckbox"] p { color:#6c6c6c !important; }
</style>
""", unsafe_allow_html=True)


def line(text, color=""):
    """Print one line of text in the terminal."""
    st.markdown(f'<pre class="t {color}">{html.escape(text)}</pre>', unsafe_allow_html=True)


# ---------- the "terminal" ----------
line("tanvir@lab:~$ python password_checker.py", "g")

password = st.text_input("Enter password:", type="password")
show_hints = st.checkbox("show hints", value=True)

if show_hints:
    line("# HINT 1: get the length first ->  length = len(password)", "c")

if password == "":
    line("waiting for input...", "y")
else:
    length = len(password)
    stars = "*" * length

    # ---- THE CONDITIONS ----
    if length < 6:
        strength, tip, color = "VERY WEAK", "Use at least 6 characters.", "r"
    elif password.isdigit():
        strength, tip, color = "WEAK", "Only numbers. Add some letters.", "r"
    elif password.isalpha():
        strength, tip, color = "MEDIUM", "Only letters. Add numbers too.", "y"
    elif length >= 10:
        strength, tip, color = "STRONG", "Great password!", "g"
    else:
        strength, tip, color = "GOOD", "Make it 10+ characters to be STRONG.", "g"

    if show_hints:
        line("# HINT 2: check the worst cases first (short, only numbers, only letters)", "c")
        line("# HINT 3: .isdigit() = only numbers | .isalpha() = only letters", "c")
        line("# HINT 4: order matters! the first True condition wins, the rest are skipped", "c")

    line(f"Password : {stars}")
    line(f"Length   : {length}")
    line(f"Strength : {strength}", color)
    line(f"Tip      : {tip}", color)

line("tanvir@lab:~$ _", "g")
line("\n# Created by Tanvir Mahatab Nadim", "c")
