def menu():
    menu_string = '''

###########################Lupass###########################
####################Secure Password Manager#################

Options:

1. Enter new password
2. Show password
3. Delete password
4. Delete all passwords
5. Exit

Choice:'''

    choice = int(input(menu_string))
    
    return choice

def prompt_passwd():
    prompt = '''

1. Enter custom password
2. Generate secure passphrase

Choice: '''

    choice = int(input(prompt))

    return choice

def pass_title():
    prompt = "What website will this password be used for?: "

    website = input(prompt)

    return website



