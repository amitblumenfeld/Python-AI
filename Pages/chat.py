import os
from lib2to3.fixes.fix_input import context

from dotenv import load_dotenv
from google import genai
import streamlit as st

st.title("my chat")

st.set_page_config(
    page_title="צאט עם בוט",
    page_icon='🤖'
)

load_dotenv()
API_KEY = os.getenv("API_KEY")


# gemini = genai.Client(api_key=API_KEY)

def saveToHistory(sender, text):
    st.session_state.history.append({
        "sender": sender,
        "text": text
    })


def send(prompt):
    saveToHistory("user", prompt)

    all_models = ["gemini-2.5-flash", "gemini-2.0-flash", "gemini-2.5-flash-lite", "gemini-2.0-flash-lite"]

    context = ""
    for line in st.session_state.history:
        context += f"{line['sender']}: {line['text']} \n"

    for model in all_models:
        chat = st.session_state.gemini.chats.create(model=model)
        try:
            message = chat.send_message(context)

            saveToHistory("assistant", message.text)

            return message
        except:
            print(f"מודל{model}לא עבד - מנסה את המודל הבא ")


# chat = gemini.chats.create(model="gemini-2.5-flash")

prompt = "hi, how are you"


def start():
    st.session_state.gemini = genai.Client(api_key=API_KEY)
    st.session_state.history = []

    message = send(prompt)
    print(message.text)


#  ai_msg = st.chat_message("assistant")
# ai_msg.write(message.text)

if "gemini" not in st.session_state:
    start()

if 'history' in st.session_state:
    for line in st.session_state.history[1:]:
        chat = st.chat_message(line["sender"])
        chat.write(line["text"])

prompt = st.chat_input("say something")
if prompt:
    user_msg = st.chat_message("user")
    user_msg.write(prompt)

    message = send(prompt)
    ai_msg = st.chat_message("assistant")
    ai_msg.write(message.text)

# st.text(message.text)