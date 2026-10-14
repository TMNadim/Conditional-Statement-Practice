import random
import streamlit as st

st.set_page_config(page_title="Conditionals Playground", page_icon="🎮")

st.title("🎮 Python Conditionals Playground")
st.caption("Every decision in this app is made with `if`, `elif` and `else` 🐍")

tab1, tab2, tab3 = st.tabs(["🎟️ Ticket Booth", "✊ Rock Paper Scissors", "🦸 Hero Rank"])


# ============================================================
# TAB 1 : CINEMA TICKET BOOTH
# ============================================================
with tab1:
    st.header("🎟️ Cinema Ticket Booth")
    st.write("Answer a few questions and I'll calculate your ticket price.")

    name = st.text_input("What's your name?", value="Alex")
    age = st.number_input("How old are you?", min_value=0, max_value=120, value=15)
    day = st.selectbox(
        "Which day are you watching?",
        ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    )
    is_student = st.checkbox("I am a student")

    # ---------- Step 1: base price comes from AGE ----------
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

    # ---------- Step 2: discount comes from DAY / STUDENT ----------
    price = base_price
    message = "No discount today."

    if day == "Tuesday":
        price = base_price * 0.5
        message = "🎉 Tuesday Special! 50% off."
    elif is_student:
        price = base_price - 2
        message = "🎓 Student discount! $2 off."

    # ---------- Step 3: price can never be negative ----------
    if price < 0:
        price = 0

    st.divider()
    st.subheader(f"Hello {name}!")
    st.write(f"Category: **{category}**  |  Base price: **${base_price}**")
    st.write(message)

    if price == 0:
        st.success("Your ticket is FREE! 🎊")
    else:
        st.success(f"Your final price is **${price:.2f}**")


# ============================================================
# TAB 2 : ROCK PAPER SCISSORS
# ============================================================
with tab2:
    st.header("✊✋✌️ Rock Paper Scissors")
    st.write("Beat the computer!")

    user_choice = st.radio(
        "Choose your move:", ["Rock", "Paper", "Scissors"], horizontal=True
    )

    if st.button("Play! 🎲"):
        computer_choice = random.choice(["Rock", "Paper", "Scissors"])

        col1, col2 = st.columns(2)
        col1.metric("You", user_choice)
        col2.metric("Computer", computer_choice)

        if user_choice == computer_choice:
            st.warning("It's a tie! 🤝")
        elif user_choice == "Rock" and computer_choice == "Scissors":
            st.success("You win! Rock crushes Scissors 🪨✂️")
        elif user_choice == "Paper" and computer_choice == "Rock":
            st.success("You win! Paper covers Rock 📄🪨")
        elif user_choice == "Scissors" and computer_choice == "Paper":
            st.success("You win! Scissors cut Paper ✂️📄")
        else:
            st.error("Computer wins! 🤖")


# ============================================================
# TAB 3 : HERO RANK GENERATOR
# ============================================================
with tab3:
    st.header("🦸 Hero Rank Generator")
    st.write("Build your own hero identity!")

    hero_name = st.text_input("Hero name", value="Shadow")
    power = st.slider("Power level", min_value=0, max_value=100, value=55)
    element = st.selectbox("Element", ["Fire", "Water", "Earth", "Air", "Lightning"])
    has_cape = st.checkbox("Do you have a cape? 🧣")

    # ---------- rank from POWER ----------
    if power >= 90:
        rank = "S"
        rank_word = "Legendary"
    elif power >= 70:
        rank = "A"
        rank_word = "Elite"
    elif power >= 50:
        rank = "B"
        rank_word = "Strong"
    elif power >= 30:
        rank = "C"
        rank_word = "Rookie"
    else:
        rank = "D"
        rank_word = "Beginner"

    # ---------- word from ELEMENT ----------
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

    st.divider()
    st.subheader(f"⚡ {element_word} {hero_name}")
    st.write(f"Rank **{rank}** — {rank_word}  |  Power: **{power}/100**")

    if has_cape:
        st.write("Cape: ✅ +10 style points")
    else:
        st.write("Cape: ❌ -5 style points")

    if (rank == "S" or rank == "A") and has_cape:
        st.balloons()
        st.success("You are ready to save the world! 🌍")
    elif rank == "S" or rank == "A":
        st.info("Very strong! But a real hero needs a cape... 🧣")
    elif rank == "B":
        st.info("Promising hero. Keep training! 💪")
    else:
        st.warning("Back to hero school! 📚")



# --- Your Signature ---
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: grey; font-size: 0.8em;'>"
    "Built with ❤️ by <b>Tanvir Mahatab Nadim</b>"
    "</p>",
    unsafe_allow_html=True
)
