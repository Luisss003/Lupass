#handle user initially logging into password manager
import time
import pwinput

#set up for user 
def first_time_login():
    pass

#Basic login screen for user:
def login():
    seconds = time.time()
    local_time = time.ctime(seconds)

    login_prompt = f'''
###########################Lupass###########################
####################Secure Password Manager#################

Local Time: {local_time}

Enter your password: '''

    password = pwinput.pwinput(prompt = login_prompt, mask='*')

    auth = auth_check(password)

    return auth

#Check user password
def auth_check(password):
    test_password = "password"
    
    return password == test_password

