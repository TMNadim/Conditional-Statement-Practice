import streamlit as st

st.set_page_config(page_title="Space Mission Control", layout="centered")

st.markdown("""
    <style>
    .stApp {background-color: #001100;}
    h1, p, div, label {color: #33ff33 !important; font-family: 'Courier New', monospace !important;}
    .stTextInput>div>div>input {background-color: #000000 !important; color: #33ff33 !important; border: 1px solid #33ff33 !important; font-family: 'Courier New', monospace;}
    </style>
""", unsafe_allow_html=True)

st.title("TERMINAL: Space Mission Control")

if 'stage' not in st.session_state:
    st.session_state.stage = 'start'
    st.session_state.history = [
        "SYSTEM ONLINE. Spaceship fueled.",
        "Set destination coordinates: 'moon' or 'mars'."
    ]

for line in st.session_state.history:
    st.write(f"> {line}")

def process_command():
    cmd = st.session_state.cmd_input.lower().strip()
    st.session_state.history.append(f"[{cmd}]")
    
    if st.session_state.stage == 'start':
        if cmd == "moon":
            st.session_state.history.append("Target: Moon. Approaching lunar surface.")
            st.session_state.history.append("Select landing mode: 'auto' or 'manual'.")
            st.session_state.stage = 'moon_menu'
        elif cmd == "mars":
            st.session_state.history.append("Target: Mars. Long journey ahead.")
            st.session_state.history.append("Select engine speed: 'cruise' or 'warp'.")
            st.session_state.stage = 'mars_menu'
        else:
            st.session_state.history.append("Invalid coordinates. Ship drifts into deep space. MISSION FAILED.")
            st.session_state.stage = 'game_over'
            
    elif st.session_state.stage == 'moon_menu':
        if cmd == "auto":
            st.session_state.history.append("Autopilot engaged. Safe landing achieved. MISSION SUCCESS!")
        elif cmd == "manual":
            st.session_state.history.append("Manual control failed. You crashed into a crater. MISSION FAILED.")
        else:
            st.session_state.history.append("System error. Engines stalled.")
        st.session_state.stage = 'game_over'
            
    elif st.session_state.stage == 'mars_menu':
        if cmd == "cruise":
            st.session_state.history.append("Journey takes 7 months. You ran out of oxygen. MISSION FAILED.")
        elif cmd == "warp":
            st.session_state.history.append("Warp drive engaged! Safe arrival at Mars colony. MISSION SUCCESS!")
        else:
            st.session_state.history.append("Engine overload. Core breach.")
        st.session_state.stage = 'game_over'
        
    elif st.session_state.stage == 'game_over':
        st.session_state.history.append("Type 'reboot' to start a new mission.")
        if cmd == "reboot":
            st.session_state.stage = 'start'
            st.session_state.history = ["SYSTEM ONLINE. Spaceship fueled.", "Set destination coordinates: 'moon' or 'mars'."]

    st.session_state.cmd_input = ""

st.text_input("INPUT COMMAND:", key="cmd_input", on_change=process_command)



# ... (all your existing code for tabs 1, 2, and 3 goes here) ...

# --- Your Signature ---
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: grey; font-size: 0.8em;'>"
    "Built with ❤️ by <b>Tanvir Mahatab Nadim</b>"
    "</p>",
    unsafe_allow_html=True
)
