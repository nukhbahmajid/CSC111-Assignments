# -----------------------------------------------------------------------------------------------------------------------
#        Name: Nukhbah Majid (I did not collaborate with anyone on this assignment)
#    Filename: Assignment 4.py
#        Date: 10/04/2018
# Description: Building a program simulating a Magic 8 ball
# -----------------------------------------------------------------------------------------------------------------------

import random

def main():
    answers = ["It is certain.", "Mmmh yeah maybe.", "Without a doubt.",
               "Over my dead body.", "I can't even sort out my own life. How am I supposed to help you out?",
               "As I see it, yes.",
               "Most likely.", "That sounds kind of stupid, you sure you want to ask that?",
               "Yeaaaaaap", "I am a saint, and I am gonna take a wild guess and say: yes.",
               "Reply hazy try again.", "Ask again later.",
               "Better not tell you now.", "Cannot predict now.",
               "I'm kind of in the middle of something so don't bother me right now. Shoooo!", "Don't count on it.",
               "Simon says no.", "Fortune-telling is stupid. This is pointless. The answer is no though.",
               "HAHAHA you're funny. yeah nope. lol no. nopeee", "Very doubtful."]
    print("")
    print("""                                                               
                                  .-.                          
 ___ .-. .-.     .---.    .--.   ( __)   .--.         .--.     
(   )   '   \   / .-, \  /    \  (''")  /    \      /  _  \    
 |  .-.  .-. ; (__) ; | ;  ,-. '  | |  |  .'-. ;    . .' `.;   
 | |  | |  | |   .'`  | | |  | |  | |  |  |(___)   | \   | |   
 | |  | |  | |  / .'| | | |  | |  | |  |  |         \ `.(_.'   
 | |  | |  | | | /  | | | |  | |  | |  |  | ___     /`'. '.    
 | |  | |  | | ; |  ; | | '  | |  | |  |  '(   )   | |  `\ |   
 | |  | |  | | ' `-'  | '  `-' |  | |  '  `-' |    ; '._,' '   
(___)(___)(___)`.__.'_.  `.__. | (___)  `.__,'      '.___.'    
                         ( `-' ;                               
                          `.__.                                """)

    print("")
    print("")
    user_question = input("Your Question?: ")
    print("")
    print(answers[random.randint(0, len(answers) - 1)])
    print("")
    another_question = input("Do you have another question? (YES/NO): ")
    another_question = another_question.upper()

    while another_question == "YES":
        print("")
        user_question = input("Your Question?: ")
        print("")
        print(answers[random.randint(0, len(answers) - 1)])
        print("")
        another_question = input("Do you have another question? (YES/NO): ")
        another_question = another_question.upper()

    print("")
    print("Ok bye, boo")
    

        

if __name__ == "__main__":
    main()


#-------------------------------------------------------------------------------------------------------------------------
# REFERENCES: Asked the TAs for help to go over my code. The user interface is produced for ASCII font generator found
#             here: http://patorjk.com/software/taag/#p=display&f=Sweet&t=Magic%208%20
#-------------------------------------------------------------------------------------------------------------------------
