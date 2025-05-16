from text_prompts import pass_title

#call on encryption funcs, and storage funcs
def pass_storage(pass_choice):

    password_title = pass_title()

    #either generate or get password from user
    if pass_choice == 1:
        password = pass_input()
    elif pass_choice == 2:
        password = pass_gen()

    #apply leet speak
    leet_password = pass_leetspeak(password)

       
#generate random passphrase
def pass_gen():
    pass

#handles if user inputs their own password
def pass_input():
    pass

#whether user input or python generated password, implement
#leet speak for better security
def pass_leetspeak(password):
    leet_map = {
        "o": "0",
        "a": "@",
        "l": "1",
        "s": "$"
    }
    return ''.join(leet_map.get(char, char) for char in password)
