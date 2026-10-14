import streamlit as st

# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(page_title="ticket_booth.py", page_icon=">_", layout="centered")

# ============================================================
# TERMINAL CSS - pure console look
# ============================================================
st.markdown("""
<style>
    .stApp {
        background-color: #000000;
        color: #00ff00;
    }
    html, body, [class*="css"], p, label, span, div {
        font-family: 'Courier New', Courier, monospace !important;
        color: #00ff00 !important;
    }
    h1, h2, h3, h4 {
        color: #00ff00 !important;
        font-family: 'Courier New', monospace !important;
        font-weight: normal !important;
    }
    .stTextInput input, .stNumberInput input {
        background-color: #000000 !important;
        color: #00ff00 !important;
        border: 1px solid #00ff00 !important;
        border-radius: 0 !important;
        font-family: 'Courier New', monospace !important;
    }
    .stSelectbox div[data-baseweb="select"] > div {
        background-color: #000000 !important;
        color: #00ff00 !important;
        border: 1px solid #00ff00 !important;
        border-radius: 0 !important;
    }
    .stCheckbox {
        color: #00ff00 !important;
    }
    .stButton > button {
        background-color: #000000;
        color: #00ff00;
        border: 1px solid #00ff00;
        border-radius: 0;
        font-family: 'Courier New', monospace;
    }
    .stButton > button:hover {
        background-color: #00ff00;
        color: #000000;
    }
    .stAlert {
        background-color: #000000 !important;
        border: 1px solid #00ff00 !important;
        color: #00ff00 !important;
        border-radius: 0 !important;
        font-family: 'Courier New', monospace !important;
    }
    hr {
        border-color: #00ff00 !important;
        opacity: 0.4;
    }
    pre {
        color: #00ff00;
        font-family: 'Courier New', monospace;
        white-space: pre-wrap;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================
# HEADER
# ============================================================
st.markdown("""
<pre>
$ python ticket_booth.py
> booting ticket-booth engine .......... OK
> loading module: none required ....... OK
> status: READY
</pre>
""", unsafe_allow_html=True)

st.markdown("---")
st.markdown("## MISSION: Cinema Ticket Booth")
st.markdown("---")

# ============================================================
# TASK HINTS
# ============================================================
st.markdown("""
<pre>
[ YOUR TASK ]
Build a ticket price calculator. Ask the user for:
    1. their age
    2. the day of the week
    3. whether they are a student

[ HINTS ]
Step 1 -> Set a BASE PRICE from age using if / elif / else:
        age < 5      -> $0   (Baby)
        age <= 12    -> $5   (Child)
        age <= 17    -> $8   (Teen)
        age < 65     -> $12  (Adult)
        else         -> $6   (Senior)

Step 2 -> Apply a DISCOUNT with another if / elif:
        if day == "Tuesday"    -> 50% off
        elif is_student        -> $2 off
        else                   -> no discount

Step 3 -> Make sure the final price is never below 0.
</pre>
""", unsafe_allow_html=True)

st.markdown("---")

# ============================================================
# INPUTS
# ============================================================
name = st.text_input("enter your name:", value="guest")
age = st.number_input("enter your age:", min_value=0, max_value=120, value=15)
day = st.selectbox(
    "select day of the week:",
    ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
)
is_student = st.checkbox("i am a student")

# ============================================================
# LOGIC - step 1: base price from age
# ============================================================
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

# ============================================================
# LOGIC - step 2: discount from day / student
# ============================================================
price = base_price
if day == "Tuesday":
    price = base_price * 0.5
    discount = "TUESDAY SPECIAL - 50% OFF"
elif is_student:
    price = base_price - 2
    discount = "STUDENT DISCOUNT - $2 OFF"
else:
    discount = "NONE"

# ============================================================
# LOGIC - step 3: no negative price
# ============================================================
if price < 0:
    price = 0

# ============================================================
# OUTPUT
# ============================================================
st.markdown("---")
st.markdown("### OUTPUT")
st.markdown(f"""
<pre>
> name ........... {name}
> age ............ {age}
> day ............ {day}
> student ........ {"yes" if is_student else "no"}
-------------------------------------
> category ....... {category}
> base price ..... ${base_price}
> discount ....... {discount}
> FINAL PRICE .... ${price:.2f}
-------------------------------------
</pre>
""", unsafe_allow_html=True)

if price == 0:
    st.markdown("<pre>>> ticket is FREE. enjoy the show.</pre>", unsafe_allow_html=True)
else:
    st.markdown(f"<pre>>> please pay ${price:.2f} at the counter.</pre>", unsafe_allow_html=True)

# ============================================================
# SIGNATURE
# ============================================================
st.markdown("---")
st.markdown("""
<pre>
$ echo "Built by Tanvir Mahatab Nadim"
Built by Tanvir Mahatab Nadim
$
</pre>
""", unsafe_allow_html=True)
