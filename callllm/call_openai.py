# These statements will import packages from openai and the prompt layer of my project
from openai import OpenAI
from prompt import bot_prompt


# Generate openai response: This function takes the user input and creates a prompt which is sent to openai to generate
# the response
def get_openai_response(user_prompt):
    OPENAI_API_KEY = ""

    client = OpenAI(api_key=OPENAI_API_KEY)

    chat_completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=bot_prompt.get_prompt(user_prompt)
    )
    return chat_completion
