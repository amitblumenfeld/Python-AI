import streamlit as st
from helper import *
import PIL.Image


st.set_page_config(
    page_title="HomeWork Bot",
    page_icon="🤖"
)

st.title("בוט שיעורי בית")

api_key = loadAPIKEY()


showMessage("HomeWork_Bot", "היי אני כאן בשביל לעזור לך")

if "homework" not in st.session_state:
    newPage("homework")

system_prompt = """"
    #תפקיד
    אתה בוט שיעורי בית
    
    #משימה
    המשימה שלך היא לעזור בשיעורי בית
    תסביר ברור
    תכוון לתשובה הנכונה
    
    #מגבלות
    אם אתה לא יודע תבדוק בגוגל
    **אל תמציא תשובה**
    ענה כמו בן אדם בצורה אנושית
    אנחנו בשנת 2026
"""

st.session_state["homework"]["system_prompt"] = system_prompt

history = st.session_state["homework"]["history"]
for line in history:
    sender = line["role"]
    if sender == "model":
        sender = "ai"

    text = line["parts"][0]["text"]
    showMessage(sender, text)

user = st.chat_input("your massage")

image_button = st.file_uploader("העלאת תמונה", type=["png","jpg","jpeg"])

if user:
    showMessage("user",user)
    image = None
    if image_button:
        image = PIL.Image.open(image_button)
    save_to_history("homework","user",user)
    history = st.session_state["homework"]["history"]
    print(history)
    answer = sendMessage(user,system_prompt,history, image)
    showMessage("ai",answer)
    save_to_history("homework","model",answer)