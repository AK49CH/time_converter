import datetime
import pytz
from pytz import timezone
import streamlit as st
import pandas as pd
import numpy as np

#Timezones
est = timezone("US/Eastern")
zulu = timezone("GMT")
amman = timezone("Asia/Amman")
dubai = timezone("Asia/Dubai")

#Streamlit
st.title("Spartan Chronos:")
st.header("SOCCENT Time Conversion Tool")
st.markdown("#")

#date, time, and timezone input
d = st.date_input("When day is your meeting?", datetime.datetime.now())
# t = st.time_input("What time is your meeting", datetime.datetime.now())
t = st.time_input("What time is your meeting in your prefered timezone?", datetime.time(9, 00))
z = st.selectbox(
    "What timezone would you like your meeting in?",
    ("Eastern", "Zulu", "Amman", "Dubai")
)

#date conversion function
def meeting(d, t, z):
    local_time = datetime.datetime.combine(d, t)
    if z == "Eastern":
        meeting_time = local_time.astimezone(est)
    elif z == "Zulu":
        meeting_time = local_time.astimezone(zulu)
    elif z == "Amman":
        meeting_time = local_time.astimezone(amman)
    elif z == "Dubai":
        meeting_time = local_time.astimezone(dubai)
    return meeting_time

#run date conversion function
if st.button("Run"):
    meeting_time = meeting(d, t, z)
    st.write("Your meeting is at", meeting_time)