# ============================================================
#  PYTHON TERMINAL LAB  -  a project made ONLY with conditionals
#  (if / elif / else)
#
#  Created by: Tanvir Mahatab Nadim
#  Run with  : streamlit run app.py
# ============================================================

import random          # only used for Rock-Paper-Scissors
import html            # makes user text safe to show on the page
import streamlit as st

st.set_page_config(page_title="Python Terminal Lab", page_icon=">_", layout="centered")

# ------------------------------------------------------------
# 1) TERMINAL LOOK (CSS) - students do NOT need to build this part
# ------------------------------------------------------------
st.markdown("""
<style>
.stApp { background-color: #0c0c0c; }
html, body, [class*="css"], .stMarkdown, label, p, span, div {
    font-family: 'Courier New', monospace !important;
    color: #33ff66;
}
[data-testid="stSidebar"] { background-color: #050505; border-right: 1px solid #1f6f3a; }
header, footer { visibility: hidden; }
.term-bar { background:#1c1c1c; padding:6px 12px; border-radius:8px 8px 0 0;
            color:#aaa !important; font-size:13px; border:1px solid #1f6f3a; }
.term-bar .dot { display:inline-block; width:10px; height:10px; border-radius:50%; margin-right:6px; }
.term-box { background:#000; border:1px solid #1f6f3a; border-top:none; padding:14px 16px;
            border-radius:0 0 8px 8px; margin-bottom:14px; line-height:1.6; white-space:pre-wrap; }
.out-good { color:#33ff66 !important; }
.out-bad  { color:#ff5555 !important; }
.out-warn { color:#ffd24d !important; }
.hint { border:1px dashed #ffd24d; padding:8px 12px; margin:10px 0; border-radius:6px;
        color:#ffd24d !important; background:#1a1500; }
.hint * { color:#ffd24d !important; }
.sign { text-align:center; color:#6c6c6c !important; margin-top:30px; font-size:13px; }
input, textarea { background:#000 !important; color:#33ff66 !important;
                  border:1px solid #1f6f3a !important; }
div[data-baseweb="select"] > div { background:#000 !important; border:1px solid #1f6f3a !important; }
.stButton > button { background:#000; color:#33ff66; border:1px solid #33ff66; border-radius:4px; }
.stButton > button:hover { background:#33ff66; color:#000; }
</style>
""", unsafe_allow_html=True)


# ------------------------------------------------------------
# 2) SMALL HELPER FUNCTIONS (they only help us display things)
# ------------------------------------------------------------
def terminal(title, text, style="good"):
    """Shows a black terminal window with some text inside."""
    safe = html.escape(text)
    st.markdown(
        f'<div class="term-bar"><span class="dot" style="background:#ff5f56"></span>'
        f'<span class="dot" style="background:#ffbd2e"></span>'
        f'<span class="dot" style="background:#27c93f"></span> {title}</div>'
        f'<div class="term-box out-{style}">{safe}</div>',
        unsafe_allow_html=True,
    )


def hint(text):
    """Shows a yellow hint box - only if the teacher/student turned hints ON."""
    if show_hints:
        st.markdown(f'<div class="hint">💡 HINT: {text}</div>', unsafe_allow_html=True)


# ------------------------------------------------------------
# 3) SIDEBAR - the MAIN MENU (this menu is also if / elif / else!)
# ------------------------------------------------------------
st.sidebar.markdown("### >_ MAIN MENU")
show_hints = st.sidebar.checkbox("Show hints for students", value=True)

choice = st.sidebar.radio(
    "Choose a program:",
    [
        "1. Grade Calculator",
        "2. Ticket Price Machine",
        "3. Rock Paper Scissors",
        "4. Leap Year Checker",
        "5. Password Strength Checker",
    ],
)
st.sidebar.markdown("---")
st.sidebar.markdown("**Student task:** build every program yourself using `if`, `elif`, `else`.")

# ------------------------------------------------------------
# 4) HEADER
# ------------------------------------------------------------
terminal(
    "tanvir@python-lab: ~",
    "PYTHON TERMINAL LAB v1.0\n"
    "Made with if / elif / else only.\n"
    "Author : Tanvir Mahatab Nadim\n"
    "Pick a program from the menu on the left.",
)

hint("The menu on the left is ALSO a conditional: "
     "`if choice == '1...': ... elif choice == '2...': ... else: ...`")

# ============================================================
# 5) THE PROGRAMS  (every one of them is built with conditionals)
# ============================================================

# ---------------- PROGRAM 1: GRADE CALCULATOR ----------------
if choice == "1. Grade Calculator":
    st.subheader("> grade_calculator.py")
    name = st.text_input("Enter student name:", "Rahim")
    marks = st.number_input("Enter marks (0 - 100):", min_value=0, max_value=100, value=75)

    hint("Ask for `marks`, then check from the HIGHEST grade to the lowest. "
         "Use `if marks >= 80:` first, then `elif marks >= 70:` ... and `else:` for fail.")

    if marks >= 80:
        grade, remark, style = "A+", "Outstanding! Keep it up.", "good"
    elif marks >= 70:
        grade, remark, style = "A", "Excellent work.", "good"
    elif marks >= 60:
        grade, remark, style = "B", "Good job.", "good"
    elif marks >= 50:
        grade, remark, style = "C", "Fair. You can do better.", "warn"
    elif marks >= 40:
        grade, remark, style = "D", "Just passed. Study more.", "warn"
    else:
        grade, remark, style = "F", "Failed. Do not give up!", "bad"

    hint("Why check the highest first? If you checked `marks >= 40` first, "
         "even 95 marks would stop there! ORDER MATTERS in elif.")

    terminal("output",
             f"$ python grade_calculator.py\n"
             f"Student : {name}\nMarks   : {marks}\nGrade   : {grade}\nRemark  : {remark}",
             style)

# ---------------- PROGRAM 2: TICKET PRICE MACHINE ----------------
elif choice == "2. Ticket Price Machine":
    st.subheader("> ticket_machine.py")
    age = st.number_input("Enter your age:", min_value=0, max_value=120, value=20)
    is_student = st.checkbox("I have a student card")

    hint("First decide the base price using age: `if age < 3` (free), "
         "`elif age <= 12` (child), `elif age < 60` (adult), `else` (senior).")

    if age < 3:
        price = 0
        category = "Baby"
    elif age <= 12:
        price = 50
        category = "Child"
    elif age < 60:
        price = 100
        category = "Adult"
    else:
        price = 60
        category = "Senior Citizen"

    hint("Then use a SECOND, separate `if` for the student discount. "
         "A student discount only makes sense if the price is above 0 and the person is an adult.")

    discount_msg = "No discount."
    if is_student and category == "Adult":
        price = price - 30
        discount_msg = "Student discount applied: -30 tk"
    elif is_student and price > 0:
        discount_msg = "Student card noticed, but you already have a cheap ticket!"

    if price == 0:
        style = "good"
    else:
        style = "warn"

    terminal("output",
             f"$ python ticket_machine.py\n"
             f"Age      : {age}\nCategory : {category}\n"
             f"{discount_msg}\nTotal    : {price} tk",
             style)

# ---------------- PROGRAM 3: ROCK PAPER SCISSORS ----------------
elif choice == "3. Rock Paper Scissors":
    st.subheader("> rock_paper_scissors.py")
    player = st.selectbox("Your move:", ["rock", "paper", "scissors"])

    hint("The computer picks with `random.choice(['rock', 'paper', 'scissors'])`. "
         "Then compare: `if player == computer:` it is a tie.")

    if st.button("▶ PLAY"):
        computer = random.choice(["rock", "paper", "scissors"])

        hint("Winning rules: rock beats scissors, scissors beats paper, paper beats rock. "
             "Use `elif (player == 'rock' and computer == 'scissors') or (...) or (...)`. "
             "Everything else is a loss - that is your `else`.")

        if player == computer:
            result, style = "It's a TIE!", "warn"
        elif (player == "rock" and computer == "scissors") or \
             (player == "scissors" and computer == "paper") or \
             (player == "paper" and computer == "rock"):
            result, style = "YOU WIN! 🎉", "good"
        else:
            result, style = "COMPUTER WINS! 💻", "bad"

        terminal("output",
                 f"$ python rock_paper_scissors.py\n"
                 f"You      : {player}\nComputer : {computer}\nResult   : {result}",
                 style)
    else:
        terminal("output", "$ python rock_paper_scissors.py\nPress PLAY to start...", "warn")

# ---------------- PROGRAM 4: LEAP YEAR CHECKER ----------------
elif choice == "4. Leap Year Checker":
    st.subheader("> leap_year.py")
    year = st.number_input("Enter a year:", min_value=1, max_value=9999, value=2024, step=1)

    hint("Rules: divisible by 400 -> leap. Else divisible by 100 -> NOT leap. "
         "Else divisible by 4 -> leap. Else -> NOT leap. "
         "Use the remainder operator: `year % 400 == 0`.")

    if year % 400 == 0:
        result, style = f"{year} is a LEAP year (divisible by 400).", "good"
    elif year % 100 == 0:
        result, style = f"{year} is NOT a leap year (divisible by 100, not 400).", "bad"
    elif year % 4 == 0:
        result, style = f"{year} is a LEAP year (divisible by 4).", "good"
    else:
        result, style = f"{year} is NOT a leap year.", "bad"

    hint("Try testing: 2000 (leap), 1900 (not leap), 2024 (leap), 2023 (not leap).")

    terminal("output", f"$ python leap_year.py\nYear   : {year}\nResult : {result}", style)

# ---------------- PROGRAM 5: PASSWORD STRENGTH CHECKER ----------------
else:
    st.subheader("> password_checker.py")
    password = st.text_input("Type a password to test:", type="password")

    hint("Use `len(password)` to count characters. "
         "`password.isdigit()` is True if ONLY numbers, `password.isalpha()` is True if ONLY letters.")

    if password == "":
        terminal("output", "$ python password_checker.py\nWaiting for input...", "warn")
    else:
        length = len(password)

        hint("Check the WORST cases first: too short, only numbers, only letters. "
             "Then check for a strong one (long + has letters AND numbers).")

        if length < 6:
            strength, tip, style = "VERY WEAK", "Use at least 6 characters.", "bad"
        elif password.isdigit():
            strength, tip, style = "WEAK", "Only numbers! Add some letters.", "bad"
        elif password.isalpha():
            strength, tip, style = "MEDIUM", "Only letters. Add numbers too.", "warn"
        elif length >= 10:
            strength, tip, style = "STRONG", "Great password!", "good"
        else:
            strength, tip, style = "GOOD", "Make it 10+ characters to be STRONG.", "good"

        terminal("output",
                 f"$ python password_checker.py\n"
                 f"Length   : {length}\nStrength : {strength}\nTip      : {tip}",
                 style)

# ------------------------------------------------------------
# 6) SIGNATURE
# ------------------------------------------------------------
st.markdown(
    '<div class="sign">────────────────────────────<br>'
    '© Created by <b>Tanvir Mahatab Nadim</b><br>'
    'Python Terminal Lab · Conditional Statements Project</div>',
    unsafe_allow_html=True,
)
