import streamlit as st

st.set_page_config(page_title="Terminal: Ticket Kiosk", layout="centered")

# Custom CSS for Terminal Look
st.markdown("""
    <style>
    .stApp {background-color: #0c0c0c;}
    h1, p, div, label {color: #00ff00 !important; font-family: 'Courier New', monospace !important;}
    .stTextInput>div>div>input {background-color: #000000 !important; color: #00ff00 !important; border: 1px solid #00ff00 !important; font-family: 'Courier New', monospace;}
    </style>
""", unsafe_allow_html=True)

st.title("Auto-Kiosk: Cinema Kiosk")

if 'stage' not in st.session_state:
    st.session_state.stage = 'start'
    st.session_state.history = [
        "Welcome to the Retro Cinema Kiosk!",
        "What genre do you want to watch? Type 'action' or 'comedy'."
    ]

for line in st.session_state.history:
    st.write(f"> {line}")

def process_command():
    cmd = st.session_state.cmd_input.lower().strip()
    st.session_state.history.append(f"[{cmd}]")
    
    if st.session_state.stage == 'start':
        if cmd == "action":
            st.session_state.history.append("Action selected. 'Mad Max' is playing.")
            st.session_state.history.append("Do you want '3d' ($15) or '2d' ($10)?")
            st.session_state.stage = 'action_menu'
        elif cmd == "comedy":
            st.session_state.history.append("Comedy selected. 'Mr. Bean' is playing.")
            st.session_state.history.append("Do you want the 'popcorn' combo ($12) or 'candy' combo ($9)?")
            st.session_state.stage = 'comedy_menu'
        else:
            st.session_state.history.append("Invalid genre. Kiosk locked. GAME OVER.")
            st.session_state.stage = 'game_over'
            
    elif st.session_state.stage == 'action_menu':
        if cmd == "3d":
            st.session_state.history.append("Printing 3D Action Ticket... Total: $15. Enjoy!")
        elif cmd == "2d":
            st.session_state.history.append("Printing 2D Action Ticket... Total: $10. Enjoy!")
        else:
            st.session_state.history.append("Invalid format. Transaction cancelled.")
        st.session_state.stage = 'game_over'
            
    elif st.session_state.stage == 'comedy_menu':
        if cmd == "popcorn":
            st.session_state.history.append("Printing Comedy Ticket + Popcorn receipt... Total: $12. Enjoy!")
        elif cmd == "candy":
            st.session_state.history.append("Printing Comedy Ticket + Candy receipt... Total: $9. Enjoy!")
        else:
            st.session_state.history.append("Invalid snack. Transaction cancelled.")
        st.session_state.stage = 'game_over'
        
    elif st.session_state.stage == 'game_over':
        st.session_state.history.append("Type 'restart' to serve the next customer.")
        if cmd == "restart":
            st.session_state.stage = 'start'
            st.session_state.history = ["Welcome to the Retro Cinema Kiosk!", "Type 'action' or 'comedy'."]

    st.session_state.cmd_input = ""

st.text_input("Enter response:", key="cmd_input", on_change=process_command)
