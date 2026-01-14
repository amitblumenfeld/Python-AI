from dotenv import load_dotenv
import os

import streamlit as st
from select import error

from pages.HomeworkBot import api_key

all_models = ["gemini-3.0-flash","gemini-2.5-flash", "gemini-2.0-flash", "gemini-2.5-flash-lite", "gemini-2.0-flash-lite"]

def createClient():
    st.session_state.client = genai.Client(api_key=loadAPIKEY())

def sendMessage(text,history=[]):
    if "client" not in st.session_state:
        createClient()
    for model in all_models:
        client = st.session_state.client
        try:
            chat = client.chats.create(
                model=model
            )

            ai = chat.send_message(text)
            print(ai.text)
            return ai.text
        except Exception as e:
            error = str(e)
            print(e)
            if "429" in error:
                st.error("נסה שוב מחר")
                return
            if "503" in error:
                st.info(f"נסה בפעם אחרת")
            print(f"{model} not working...")



def loadAPIKEY():
    load_dotenv()
    API_KEY = os.getenv("API_KEY") or st.secrets["API_KEY"]
    return API_KEY


def showMessage(sender, text):
    newMessage = st.chat_message(sender)
    newMessage.write(text)