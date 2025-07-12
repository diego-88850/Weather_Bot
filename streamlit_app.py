import streamlit as st
from preferences import init_preferences_table, save_preferences
from main import main as run_weatherbot

init_preferences_table()

st.title("Weatherbot preferences")

st.write("Weatherbot will send you useful forecast information for any city to your email however often you like with a custom personality")

city = st.text_input("Enter a city name", "New York")

time = st.time_input("Preferred email time")
frequency = st.selectbox("How often?", ["Daily", "weekly"])

# Conditionally show day-of-week picker
day_of_week = "Monday"
if frequency in ["weekly"]:
    day_of_week = st.selectbox("Preferred day of the week",
                                ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])

personality = st.text_input("Enter a personality type for your person weatherman", "goofy")
email_address = st.text_input("Enter your email address", "diego.sebas2915@gmail.com")

if st.button("Preferences"):
    save_preferences(city, time, day_of_week, frequency, personality, email_address)
    st.success("Preferences saved")

if st.button("Run Weatherbot Now"):
    run_weatherbot()
    st.success("Weatherbot now running")