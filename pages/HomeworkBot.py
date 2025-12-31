import streamlit as st
from helper import *

st.set_page_config(
    page_title="HomeWork Bot",
    page_icon="🤖"
)

st.title("בוט שיעורי בית")

api_key = loadAPIKEY()


showMessage("היי אני כאן בשביל לעזור לך")


user = st.chat_input("your massage")

if user:
    showMessage("user",user)
