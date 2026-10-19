# ============================================================
#  LOOP LAB - demo for the assignment "for loop and while loop"
#
#  Created by: Tanvir Mahatab Nadim
#  Run with  : streamlit run app_loops.py
# ============================================================

import html
import random
import streamlit as st

st.set_page_config(page_title="Loop Lab", page_icon="🔁", layout="centered")

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
.step   { display:flex; align-items:center; gap:10px; margin:20px 0 8px 0; }
.num    { background:#238636; color:#fff !important; font-weight:700; width:28px; height:28px;
          border-radius:50%; display:flex; align-items:center; justify-content:center; }
.stitle { font-size:19px; font-weight:700; color:#fff !important; }

div[data-testid="stTextInput"] input, div[data-testid="stNumberInput"] input {
    background:#010409 !important; color:#7ee787 !important; font-size:17px !important;
    font-family:'Courier New', monospace !important; border:1px solid #30363d !important;
}
button[data-baseweb="tab"] p { font-weight:700; }

.win     { border:1px solid #30363d; border-radius:8px; overflow:hidden; }
.winbar  { background:#21262d; padding:6px 12px; color:#8b949e !important; font-size:13px; }
.dot     { display:inline-block; width:10px; height:10px; border-radius:50%; margin-right:6px; }
.winbody { background:#010409; padding:14px 16px; font-family:'Courier New', monospace;
           font-size:16px; line-height:1.6; white-space:pre-wrap; }
.sign { text-align:center; color:#8b949e !important; font-size:13px; margin-top:36px;
        border-top:1px solid #30363d; padding-top:14px; }
</style>
""", unsafe_allow_html=True)


def step(number, title):
    st.markdown(
        f'<div class="step"><div class="num">{number}</div><div class="stitle">{title}</div></div>',
        unsafe_allow_html=True,
    )


def terminal(title, lines):
    """Shows a list of text lines inside a black terminal window."""
    text = "\n".join(lines)
    st.markdown(
        '<div class="win"><div class="winbar">'
        '<span class="dot" style="background:#ff5f56"></span>'
        '<span class="dot" style="background:#ffbd2e"></span>'
        '<span class="dot" style="background:#27c93f"></span> ' + title + '</div>'
        f'<div class="winbody">{html.escape(text)}</div></div>',
        unsafe_allow_html=True,
    )


# ------------------------------------------------------------
# TITLE
# ------------------------------------------------------------
st.markdown('<p class="title">🔁 Loop Lab</p>', unsafe_allow_html=True)
st.markdown('<p class="sub">Made with <b>for</b> loops and a <b>while</b> loop</p>',
            unsafe_allow_html=True)

tab1, tab2 = st.tabs(["Part 1 · for loop", "Part 2 · while loop"])

# ============================================================
# PART 1 - FOR LOOP
# ============================================================
with tab1:
    step(1, "Choose a task")
    task = st.selectbox(
        "task",
        ["Task 1 - Print 1 to 10",
         "Task 2 - Multiplication table",
         "Task 3 - Sum of numbers",
         "Task 4 - Countdown"],
        label_visibility="collapsed",
    )

    lines = []     # the lines we will show in the terminal

    # ---------- Task 1 ----------
    if task == "Task 1 - Print 1 to 10":
        for i in range(1, 11):
            lines.append(str(i))

    # ---------- Task 2 ----------
    elif task == "Task 2 - Multiplication table":
        number = st.number_input("Enter a number:", min_value=-1000, max_value=1000, value=5, step=1)
        lines.append(f"Enter a number: {number}")
        for i in range(1, 11):
            lines.append(f"{number} x {i} = {number * i}")

    # ---------- Task 3 ----------
    elif task == "Task 3 - Sum of numbers":
        n = st.number_input("Enter n:", min_value=1, max_value=1000, value=5, step=1)
        total = 0                       # BEFORE the loop!
        for i in range(1, n + 1):
            total = total + i
        lines.append(f"Enter n: {n}")
        lines.append(f"Sum of 1 to {n} = {total}")

    # ---------- Task 4 ----------
    else:
        for i in range(5, 0, -1):
            lines.append(str(i))
        lines.append("Go!")              # AFTER the loop (no indent)

    step(2, "Output")
    terminal("Run: loop_lab.py", ["$ python loop_lab.py"] + lines)

# ============================================================
# PART 2 - WHILE LOOP (Number Guessing Game)
# ============================================================
with tab2:
    step(1, "Settings")

    test_mode = st.checkbox("Test mode: secret = 7 (like in the assignment tests)", value=True)

    # Streamlit runs the file again and again, so we save the random secret.
    if "secret" not in st.session_state:
        st.session_state.secret = random.randint(1, 20)
    if st.button("🎲 New random number"):
        st.session_state.secret = random.randint(1, 20)

    if test_mode:
        secret = 7
    else:
        secret = st.session_state.secret

    step(2, "Type your guesses")
    st.caption("Type up to 5 guesses with commas. Example:  10, 15, 13")
    guess_text = st.text_input("guesses", value="10, 5, 7", label_visibility="collapsed")

    # ---------- turn the text into a list of numbers ----------
    guesses = []
    bad_input = False
    for part in guess_text.split(","):
        part = part.strip()
        if part == "":
            continue
        if part.lstrip("-").isdigit():
            guesses.append(int(part))
        else:
            bad_input = True

    # ---------- THE GAME (this is the part students must build) ----------
    lines = ["=== Number Guessing Game ===",
             "I am thinking of a number from 1 to 20.",
             "You have 5 tries.",
             ""]

    attempts = 0
    max_attempts = 5
    won = False

    # NOTE: in PyCharm the guess comes from input().
    # Here we read it from the list, so the loop also checks "attempts < len(guesses)".
    while attempts < max_attempts and attempts < len(guesses):
        guess = guesses[attempts]
        lines.append(f"Try {attempts + 1} - Your guess: {guess}")
        attempts = attempts + 1

        if guess == secret:
            lines.append(f"Correct! You won in {attempts} tries.")
            won = True
            break
        elif guess < secret:
            lines.append("Too low!")
        else:
            lines.append("Too high!")

    # ---------- after the loop (no indent) ----------
    if won:
        pass                                    # the player already saw the win message
    elif attempts == max_attempts:
        lines.append(f"Game over! The number was {secret}.")
    else:
        lines.append(f"Try {attempts + 1} - Your guess: _   (type more guesses above)")

    step(3, "Output")
    if bad_input:
        st.warning("Please type only numbers and commas. Example: 3, 5, 7")
    terminal("Run: loop_lab.py", ["$ python loop_lab.py"] + lines)

# ------------------------------------------------------------
# SIGNATURE
# ------------------------------------------------------------
st.markdown('<div class="sign">Created by <b>Tanvir Mahatab Nadim</b></div>',
            unsafe_allow_html=True)
