def validate_input_and_output(input_string):
    banned_list = ["terrorist", "suicide", "killing myself"]
    input_string = input_string.lower()
    for banned_word in banned_list:
        if banned_word in input_string:
            return True
        else:
            return False
