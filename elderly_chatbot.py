import streamlit as st
from callllm import call_openai

st.title("Your friend Levina")
st.header("Let's talk!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_prompt = st.chat_input(placeholder="Message Levina")

if user_prompt:
    with st.chat_message("user"):
        st.markdown(user_prompt)

    st.session_state.messages.append({"role": "user", "content": user_prompt})

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        response = call_openai.get_openai_response(user_prompt)
        full_response = response.choices[0].message.content
        message_placeholder.markdown(full_response)

    st.session_state.messages.append({"role": "assistant", "content": full_response})