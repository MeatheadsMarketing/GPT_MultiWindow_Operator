import streamlit as st
from thread_commander_tab import *
from shortcut_launcher_tab import *

st.set_page_config(page_title="🧠 GPT MultiWindow Operator", layout="wide")

st.sidebar.title("🧭 Navigation")
page = st.sidebar.radio("Choose a view:", [
    "Thread Commander",
    "Shortcut Launcher"
])

if page == "Thread Commander":
    thread_commander_tab()

elif page == "Shortcut Launcher":
    shortcut_launcher_tab()
