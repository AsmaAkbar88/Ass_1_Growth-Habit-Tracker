import streamlit as st
import pandas as pd

st.set_page_config(page_title="✤ Growth Habit", layout="wide" )

# Title
st.title("🌱 Growth Habit Tracker")

# Sidebar
st.sidebar.title("📌 Select Your Habits")
habits = ["Learn something new", "Write self-reflection", "Accept challenges", "Read a book", "Exercise"]
selected_habits = st.sidebar.multiselect("Select your habits:", habits)

# Data Storage
if "habit_data" not in st.session_state:
    st.session_state.habit_data = {habit: [] for habit in habits}

# Motivational Messages
motivational_notes = {
    "Learn something new": "📖 Learning is a lifelong journey! Keep exploring new things. 🚀",
    "Write self-reflection": "📝 Self-reflection helps you grow and understand yourself better. Keep it up! 💡",
    "Accept challenges": "🔥 Challenges make you stronger! You are becoming unstoppable. 💪",
    "Read a book": "📚 Reading is a great habit! Every book gives you a new perspective. 🌎",
    "Exercise": "🏋️‍♂️ Staying active keeps you healthy and strong. Keep moving! 💖"
}

# Mark Completion
st.subheader("✅ Mark Today's Completed Habits")
for habit in selected_habits:
    done = st.checkbox(f"{habit} Completed")
    if done:
        st.success(f"🎉 Great! You completed '{habit}' today! 👍")
        st.info(motivational_notes[habit])  
        st.session_state.habit_data[habit].append(1)  
    else:
        st.session_state.habit_data[habit].append(0)  

# Equal Lengths
max_length = max(len(v) for v in st.session_state.habit_data.values())  
for habit in st.session_state.habit_data:
    while len(st.session_state.habit_data[habit]) < max_length:
        st.session_state.habit_data[habit].append(0)
         

# Reset Data
if st.button("Reset Progress"):
    st.session_state.clear()  
    st.success("Progress Reset Successfully!")
    st.rerun() 
    # Footer
st.write("⛔ **Created by Asma Akbar**")

   
