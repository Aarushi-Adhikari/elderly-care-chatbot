# These statements will import packages from streamlit and the llm layer of my project
import streamlit as st
from callllm import call_openai
from validation.input_output_validator import validate_input_and_output

# This will set the title and header of my streamlit web page
st.title("Your friend Levina")
st.header("Let's talk!")

# Session management: If there are no messages in the session when the web page is opened,
# an empty list will be created called messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Printing of previous chats: This goes through all previous messages and prints them on the screen
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input box placeholder: This displays 'Message Levina' in the input box
user_prompt = st.chat_input(placeholder="Message Levina")

# User input: If the user has entered anything, it is stored in the variable user_prompt
if user_prompt:
    if validate_input_and_output(user_prompt):
        st.error("This is an inappropriate conversation topic to discuss with me. Please enter a "
                 "less sensitive input and then we will resume our conversation.")
    else:
        with st.chat_message("user"):
            st.markdown(user_prompt)
    # Appending user query: The content of the input text box is appended to the list
        st.session_state.messages.append({"role": "user", "content": user_prompt})

    # Generating response: The placeholder for the assistant is empty, then openai is called with
        # an engineered prompt and the generated response is assigned to the empty placeholder
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            response = call_openai.get_openai_response(user_prompt)
            full_response = response.choices[0].message.content
            message_placeholder.markdown(full_response)

    # Appending assistant response: The content of the response is appended to the messages list
        st.session_state.messages.append({"role": "assistant", "content": full_response})
