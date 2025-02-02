def validate_input_and_output(input_string):
    banned_list = ["suicide", "killing myself", "life isn't worth living"]
    input_string = input_string.lower()
    for banned_word in banned_list:
        if banned_word in input_string:
            return True
