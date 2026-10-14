import random
import streamlit as st

# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(page_title="Terminal Playground", page_icon="💻", layout="centered")

# ============================================================
# TERMINAL-STYLE CSS
# ============================================================
st.markdown("""
<style>
    /* Full page background */
    .stApp {
        background-color: #0d1117;
        color: #00ff88;
        font-family: 'Courier New', Courier, monospace;
    }

    /* All text default */
    html, body, [class*="css"] {
        font-family: 'Courier New', Courier, monospace !important;
        color: #00ff88;
    }

    /* Headings */
    h1, h2, h3, h4 {
        color: #00ff88 !important;
        font-family: 'Courier New', Courier, monospace !important;
        text-shadow: 0 0 5px #00ff88;
    }

    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        background-color: #161b22;
        border-radius: 4px;
    }
    .stTabs [data-baseweb="tab"] {
        color: #00ff88;
        font-family: 'Courier New', monospace;
        font-weight: bold;
        background-color: transparent;
    }
    .stTabs [aria-selected="true"] {
        background-color: #00ff88 !important;
        color: #0d1117 !important;
    }

    /* Inputs, select boxes, text areas */
    .stTextInput input, .stNumberInput input, .stTextArea textarea {
        background-color: #0d1117 !important;
        color: #00ff88 !important;
        border: 1px solid #00ff88 !important;
        font-family: 'Courier New', monospace !important;
    }
    .stSelectbox div[data-baseweb="select"] > div {
        background-color: #0d1117 !important;
        color: #00ff88 !important;
        border: 1px solid #00ff88 !important;
    }

    /* Buttons */
    .stButton > button {
        background-color: #0d1117;
        color: #00ff88;
        border: 2px solid #00ff88;
        font-family: 'Courier New', monospace;
        font-weight: bold;
        letter-spacing: 1px;
        transition: all 0.2s;
    }
    .stButton > button:hover {
        background-color: #00ff88;
        color: #0d1117;
        box-shadow: 0 0 15px #00ff88;
    }

    /* Success / Info / Warning / Error boxes */
    .stAlert {
        background-color: #161b22 !important;
        border-left: 4px solid #00ff88 !important;
        color: #00ff88 !important;
        font-family: 'Courier New', monospace !important;
    }

    /* Divider */
    hr {
        border-color: #00ff88 !important;
        opacity: 0.3;
    }

    /* Task hint box */
    .task-box {
        background-color: #161b22;
        border: 1px dashed #00ff88;
        border-radius: 6px;
        padding: 12px 16px;
        color: #00ff88;
        font-family: 'Courier New', monospace;
        font-size: 0.9em;
        margin-bottom: 15px;
    }

    /* Output panel */
    .output-panel {
        background-color: #000000;
        border: 1px solid #00ff88;
        border-radius: 6px;
        padding: 16px;
        color: #00ff88;
        font-family: 'Courier New', monospace;
        font-size: 1em;
        line-height: 1.6;
        box-shadow: 0 0 12px rgba(0, 255, 136, 0.3);
    }

    /* Labels */
    label, .stMarkdown, p {
        color: #00ff88 !important;
        font-family: 'Courier New', monospace !important;
    }
</style>
""", unsafe_allow_html=True)


# ============================================================
# HEADER — looks like a terminal boot screen
# ============================================================
st.markdown("""
<div class="output-panel">
<pre>
$ python terminal_playground.py
> Booting conditional-logic engine.......... OK
> Loading modules: random, streamlit...... OK
> Status: READY

Welcome, user. Choose a mission below.
</pre>
</div>
""", unsafe_allow_html=True)

st.markdown("### 💻 CONDITIONALS TERMINAL")
st.caption("Every mission uses only `if`, `elif`, and `else`. Build them yourself!")
st.markdown("---")


tab1, tab2, tab3 = st.tabs(["🎟️ MISSION 1: Ticket Booth",
                            "✊ MISSION 2: Rock Paper Scissors",
                            "🦸 MISSION 3: Hero Rank"])


# ============================================================
# TAB 1 : CINEMA TICKET BOOTH
# ============================================================
with tab1:
    st.markdown("## 🎟️ MISSION 1: Cinema Ticket Booth")

    st.markdown("""
<div class="task-box">
<b>📋 YOUR TASK:</b><br>
Build a ticket price calculator that asks the user for their age,<br>
the day of the week, and whether they are a student.<br><br>

<b>💡 HINTS:</b><br>
• Use <code>if / elif / else</code> to set a <b>base price</b> from age:<br>
&nbsp;&nbsp;&nbsp;&nbsp;- age &lt; 5 → free ($0)<br>
&nbsp;&nbsp;&nbsp;&nbsp;- age ≤ 12 → $5 (Child)<br>
&nbsp;&nbsp;&nbsp;&nbsp;- age ≤ 17 → $8 (Teen)<br>
&nbsp;&nbsp;&nbsp;&nbsp;- age &lt; 65 → $12 (Adult)<br>
&nbsp;&nbsp;&nbsp;&nbsp;- else → $6 (Senior)<br>
• Then use another <code>if / elif</code> to apply discounts:<br>
&nbsp;&nbsp;&nbsp;&nbsp;- If the day is "Tuesday" → 50% off<br>
&nbsp;&nbsp;&nbsp;&nbsp;- Else if the user is a student → $2 off<br>
• Finally, make sure the price never goes below 0.
</div>
""", unsafe_allow_html=True)

    name = st.text_input("Enter your name:", value="guest")
    age = st.number_input("Enter your age:", min_value=0, max_value=120, value=15)
    day = st.selectbox(
        "Select day of the week:",
        ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    )
    is_student = st.checkbox("I am a student")

    # ---------- Step 1: base price from AGE ----------
    if age < 5:
        base_price = 0
        category = "Baby"
    elif age <= 12:
        base_price = 5
        category = "Child"
    elif age <= 17:
        base_price = 8
        category = "Teen"
    elif age < 65:
        base_price = 12
        category = "Adult"
    else:
        base_price = 6
        category = "Senior"

    # ---------- Step 2: discount from DAY / STUDENT ----------
    price = base_price
    message = "No discount today."

    if day == "Tuesday":
        price = base_price * 0.5
        message = "TUESDAY SPECIAL -> 50% OFF"
    elif is_student:
        price = base_price - 2
        message = "STUDENT DISCOUNT -> -$2"

    # ---------- Step 3: no negative prices ----------
    if price < 0:
        price = 0

    st.markdown("### 🖥️ OUTPUT")
    st.markdown(f"""
<div class="output-panel">
<pre>
> USER ............ {name}
> CATEGORY ........ {category}
> BASE PRICE ...... ${base_price}
> DISCOUNT ........ {message}
> FINAL PRICE ..... ${price:.2f}
</pre>
</div>
""", unsafe_allow_html=True)

    if price == 0:
        st.success(">> TICKET IS FREE. ENJOY THE SHOW! 🎊")
    else:
        st.success(f">> PLEASE PAY ${price:.2f} AT THE COUNTER.")


# ============================================================
# TAB 2 : ROCK PAPER SCISSORS
# ============================================================
with tab2:
    st.markdown("## ✊ MISSION 2: Rock Paper Scissors")

    st.markdown("""
<div class="task-box">
<b>📋 YOUR TASK:</b><br>
Build a game where the user picks Rock, Paper, or Scissors,<br>
the computer picks randomly, and you decide the winner.<br><br>

<b>💡 HINTS:</b><br>
• Import <code>random</code> and use <code>random.choice(["Rock","Paper","Scissors"])</code>.<br>
• First check for a <b>tie</b>: <code>if user == computer:</code><br>
• Then use <code>elif</code> for each winning case:<br>
&nbsp;&nbsp;&nbsp;&nbsp;- Rock beats Scissors<br>
&nbsp;&nbsp;&nbsp;&nbsp;- Paper beats Rock<br>
&nbsp;&nbsp;&nbsp;&nbsp;- Scissors beats Paper<br>
• Use <code>else</code> for "computer wins".<br>
• Remember: <b>==</b> compares, <b>=</b> assigns!
</div>
""", unsafe_allow_html=True)

    user_choice = st.radio("Choose your weapon:", ["Rock", "Paper", "Scissors"], horizontal=True)

    if st.button(">> EXECUTE MATCH"):
        computer_choice = random.choice(["Rock", "Paper", "Scissors"])

        st.markdown(f"""
<div class="output-panel">
<pre>
> PLAYER ......... {user_choice}
> COMPUTER ....... {computer_choice}
</pre>
</div>
""", unsafe_allow_html=True)

        if user_choice == computer_choice:
            st.warning(">> RESULT: TIE. Try again, hero.")
        elif user_choice == "Rock" and computer_choice == "Scissors":
            st.success(">> RESULT: YOU WIN! Rock smashes Scissors.")
        elif user_choice == "Paper" and computer_choice == "Rock":
            st.success(">> RESULT: YOU WIN! Paper wraps Rock.")
        elif user_choice == "Scissors" and computer_choice == "Paper":
            st.success(">> RESULT: YOU WIN! Scissors cuts Paper.")
        else:
            st.error(">> RESULT: COMPUTER WINS. Better luck next time.")


# ============================================================
# TAB 3 : HERO RANK GENERATOR
# ============================================================
with tab3:
    st.markdown("## 🦸 MISSION 3: Hero Rank Generator")

    st.markdown("""
<div class="task-box">
<b>📋 YOUR TASK:</b><br>
Create a system that gives a hero a rank, a title, and a final verdict<br>
based on their power level, element, and whether they have a cape.<br><br>

<b>💡 HINTS:</b><br>
• <b>Rank from power:</b><br>
&nbsp;&nbsp;&nbsp;&nbsp;- ≥ 90 → S (Legendary)<br>
&nbsp;&nbsp;&nbsp;&nbsp;- ≥ 70 → A (Elite)<br>
&nbsp;&nbsp;&nbsp;&nbsp;- ≥ 50 → B (Strong)<br>
&nbsp;&nbsp;&nbsp;&nbsp;- ≥ 30 → C (Rookie)<br>
&nbsp;&nbsp;&nbsp;&nbsp;- else → D (Beginner)<br>
• <b>Title from element:</b> Fire→Blazing, Water→Tidal, Earth→Iron, Air→Swift, Lightning→Thunder.<br>
• <b>Final verdict:</b> use <code>and</code> / <code>or</code> to combine conditions —<br>
&nbsp;&nbsp;&nbsp;&nbsp;e.g. <code>if (rank == "S" or rank == "A") and has_cape:</code>
</div>
""", unsafe_allow_html=True)

    hero_name = st.text_input("Hero name:", value="Shadow")
    power = st.slider("Power level:", min_value=0, max_value=100, value=55)
    element = st.selectbox("Element:", ["Fire", "Water", "Earth", "Air", "Lightning"])
    has_cape = st.checkbox("Do you have a cape?")

    # ---------- rank from POWER ----------
    if power >= 90:
        rank, rank_word = "S", "Legendary"
    elif power >= 70:
        rank, rank_word = "A", "Elite"
    elif power >= 50:
        rank, rank_word = "B", "Strong"
    elif power >= 30:
        rank, rank_word = "C", "Rookie"
    else:
        rank, rank_word = "D", "Beginner"

    # ---------- title from ELEMENT ----------
    if element == "Fire":
        element_word = "Blazing"
    elif element == "Water":
        element_word = "Tidal"
    elif element == "Earth":
        element_word = "Iron"
    elif element == "Air":
        element_word = "Swift"
    else:
        element_word = "Thunder"

    cape_status = "+10 STYLE" if has_cape else "-5 STYLE"

    st.markdown("### 🖥️ HERO DOSSIER")
    st.markdown(f"""
<div class="output-panel">
<pre>
> NAME ............ {element_word} {hero_name}
> RANK ............ {rank} ({rank_word})
> POWER ........... {power}/100
> CAPE ............ {"YES" if has_cape else "NO"}  [{cape_status}]
</pre>
</div>
""", unsafe_allow_html=True)

    if (rank == "S" or rank == "A") and has_cape:
        st.success(">> VERDICT: WORLD-SAVER. The legends will sing of you!")
        st.balloons()
    elif rank == "S" or rank == "A":
        st.info(">> VERDICT: Very strong... but every great hero needs a cape.")
    elif rank == "B":
        st.info(">> VERDICT: Promising. Keep training, young one.")
    else:
        st.warning(">> VERDICT: Back to hero school. Study hard!")


# ============================================================
# FOOTER / SIGNATURE
# ============================================================
st.markdown("---")
st.markdown("""
<div style="text-align:center; font-family:'Courier New', monospace; color:#00ff88; opacity:0.8; font-size:0.85em;">
<pre>
$ echo "Built with <3 by Tanvir Mahatab Nadim"
Built with <3 by Tanvir Mahatab Nadim
$
</pre>
</div>
""", unsafe_allow_html=True)
