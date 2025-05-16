import user_auth
import text_prompts
import os
import sys
import pass_utils

if __name__ == "__main__":
    
    #Prompt user to log in before accessing Lupass
    login_attempt = user_auth.login()

    if login_attempt:
        choice = text_prompts.menu()

        while(1):
            if choice == 5:
                sys.exit("Exiting Lupass...")
            else:
                print("INCORRENT OPTION")
            
            pass_utils.pass_storage(choice)
    else:
        sys.exit("INCORRECT PASSWORD")