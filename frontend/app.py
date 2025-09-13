import streamlit as st
import requests

st.set_page_config(page_title="Wysa Clone", page_icon="🧠")
st.title("🧠 Wysa-like AI Mental Health Assistant")

USER_ID = 1  # For now, fixed user ID

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

user_input = st.text_input("How are you feeling today?")

if st.button("Send") and user_input:
    res = requests.post("http://127.0.0.1:8000/chat",
                        json={"user_id": USER_ID, "message": user_input})
    bot_reply = res.json()["response"]
    st.session_state["chat_history"].append(("You", user_input))
    st.session_state["chat_history"].append(("AI", bot_reply))

st.subheader("Chat History")
for speaker, text in st.session_state["chat_history"]:
    st.write(f"**{speaker}:** {text}")

if st.button("🏅 View My Badges"):
    res = requests.get(f"http://127.0.0.1:8000/badges/{USER_ID}")
    st.write("Your badges:", res.json()["badges"])

