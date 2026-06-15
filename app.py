import streamlit as st
from chatbot import get_career_guidance
from datetime import datetime

st.set_page_config(
    page_title="AI Career Guidance Chatbot",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 AI Career Guidance Chatbot")

st.markdown("""
Ask anything about:

- Career Paths
- Software Engineering
- Data Science
- AI & ML
- Certifications
- Resume Building
- Interview Preparation
""")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input(
    "Ask a career-related question..."
)

if user_input:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):
        st.write(user_input)

    with st.spinner("Generating career guidance..."):

        response = get_career_guidance(
            user_input
        )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

    with st.chat_message("assistant"):
        st.write(response)

    with open(
        "chat_history.txt",
        "a",
        encoding="utf-8"
    ) as file:

        file.write(
            f"\n[{datetime.now()}]\n"
        )

        file.write(
            f"User: {user_input}\n"
        )

        file.write(
            f"Bot: {response}\n"
        )