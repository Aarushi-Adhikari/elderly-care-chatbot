from callllm import call_openai

if __name__ == '__main__':

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit","bye","exit","goodbye"]:
            break
        response = call_openai.get_openai_response(user_input)
        print(response.choices[0].message.content)
