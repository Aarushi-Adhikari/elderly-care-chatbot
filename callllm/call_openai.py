from openai import OpenAI
from prompt import bot_prompt


def get_openai_response(user_prompt):
    OPENAI_API_KEY = ""

    client = OpenAI(api_key=OPENAI_API_KEY)

    chat_completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=bot_prompt.get_prompt(user_prompt)
    )
    return chat_completion
