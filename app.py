import streamlit as st

st.set_page_config(page_title="Terminal Escape Room", layout="centered")

# Custom CSS to simulate a retro terminal
st.markdown("""
    <style>
    .stApp {background-color: #0c0c0c;}
    h1, p, div, label {color: #00ff00 !important; font-family: 'Courier New', monospace !important;}
    .stTextInput>div>div>input {background-color: #000000 !important; color: #00ff00 !important; border: 1px solid #00ff00 !important; font-family: 'Courier New', monospace;}
    </style>
""", unsafe_allow_html=True)

st.title("Terminal: The Haunted Castle")

# Initialize game state
if 'stage' not in st.session_state:
    st.session_state.stage = 'start'
    st.session_state.history = [
        "Welcome to the Haunted Castle!",
        "You are in a dark hallway. There are two doors in front of you: 'red' and 'blue'."
    ]

# Display terminal history
for line in st.session_state.history:
    st.write(f"> {line}")

# Logic to process the student's input
def process_command():
    cmd = st.session_state.cmd_input.lower().strip()
    st.session_state.history.append(f"[{cmd}]")
    
    if st.session_state.stage == 'start':
        if cmd == "red":
            st.session_state.history.append("You enter the red room. A sleeping dragon blocks the exit!")
            st.session_state.history.append("Do you try to 'sneak' past it or 'attack' it?")
            st.session_state.stage = 'red_room'
        elif cmd == "blue":
            st.session_state.history.append("You enter the blue room. It is filled with treasure!")
            st.session_state.history.append("Do you take the 'gold' or the glowing 'sword'?")
            st.session_state.stage = 'blue_room'
        else:
            st.session_state.history.append("Invalid choice. The floor collapses. GAME OVER.")
            st.session_state.stage = 'game_over'
            
    elif st.session_state.stage == 'red_room':
        if cmd == "sneak":
            st.session_state.history.append("You quietly tip-toe past the dragon and escape. YOU WIN!")
        elif cmd == "attack":
            st.session_state.history.append("Your attack wakes the dragon. It eats you. GAME OVER.")
        else:
            st.session_state.history.append("You hesitate. The dragon wakes up. GAME OVER.")
        st.session_state.stage = 'game_over'
            
    elif st.session_state.stage == 'blue_room':
        if cmd == "gold":
            st.session_state.history.append("The gold is cursed! You turn into a golden statue. GAME OVER.")
        elif cmd == "sword":
            st.session_state.history.append("The sword is magical! It opens a secret passage to safety. YOU WIN!")
        else:
            st.session_state.history.append("You stare at the treasure too long. Ghosts get you. GAME OVER.")
        st.session_state.stage = 'game_over'
        
    elif st.session_state.stage == 'game_over':
        st.session_state.history.append("Type 'restart' to play again.")
        if cmd == "restart":
            st.session_state.stage = 'start'
            st.session_state.history = ["Welcome back to the Haunted Castle!", "There are two doors: 'red' and 'blue'."]

    # Clear the input box
    st.session_state.cmd_input = ""

st.text_input("Enter command:", key="cmd_input", on_change=process_command)
