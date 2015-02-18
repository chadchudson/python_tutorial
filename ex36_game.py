from sys import exit
from random import randint

doors = ["'wealth' management office", "'vault' room", "'lunch' room", "'managers' office"]

'''
random number generator code example 
x = randint(0,10) - inclusive, so maybe 0-9
print x
'''

def start():
    print "\n\tYou are standing at the entrance."
    print "What would you like to do?"
    print "You can 'enter', or 'walk away'"
    
    choice = raw_input("--> ")
    
    if choice == 'enter':
        print "\n\tWelcome to the Hacker's Bank!"
        atrium()
    elif choice == 'walk away':
        print "You chicken! You won't have a very good career as a bank robber!"
        exit(0)
    else:
        print "I'm sorry, I don't understand what you want to do. Are you a little nervous?"
        print "Please, try again."
        start()


def security_guard():
    print "\n\tGood day, how may I be of assistance?"
    print "You can say, 'how' is it going?, 'put' your hands up, 'give' me your gun or 'back'."
    
    choice = raw_input("--> ")
    
    if choice == 'how':
        print "\n\tHe replies, 'Pretty good, thanks.'"
        atrium()
    elif choice == 'back':
        atrium()
    elif choice == 'put':
        print "\n\tHe says, 'okay' and smirks. You wonder why, but shrug it off..."
        print "The security guard slowly raises his hands. Unfortunately, another security guard walked in behind you and shoots you in the back."
        replay = raw_input("Would you like to play again? -->")
    
        if replay == 'no':
            print "\n\tOk, enjoy death!"
        else:
            start()
    elif choice == 'give':
        print "\n\tHe says, 'Seriously!?' then hands you the gun."
        print "What you don't realize is another security guard walked in behind you and shoots you in the back."
        replay = raw_input("Would you like to play again? -->")
    
        if replay == 'no':
            print "\n\tOk, enjoy death!"
        else:
            start()
    elif choice == 'exit':
        print "Please, come back when you are ready."
        exit(0)
    else:
        print "I'm sorry, I don't understand what you want to do. Are you a little nervous?"
        print "Please, try again."
        atrium()


def security_alarm():
    print "\n\tYou see the security alarm. Apparently, it is a very simple alarm for a bank! Would you like to try to hack it? 'Yes/No'"
    
    choice = raw_input("--> ")
    
    if choice == 'Yes' or 'yes':
        password()
    else:
        print "Ok, you return to the manager's office." #Change this
        managers_office()


def password():
    print "\n\tOk, it looks like it is protected by a single digit. You get 5 tries!"
    
    tries = 5
    
    while tries > 0:
        alarm = randint(0,9)
        guess = int(raw_input("Please guess a number between 0-9. --> "))
        if guess == alarm:
            print "\n\tYea!!! Nice job, you have disabled the alarm!!! Much less chance of getting caught now!"
            managers_office() # Need to change this for other areas in the bank.
        else:
            print "Oops, you missed on that one! It was %d" % alarm
        tries = tries - 1

    print "\n\t Congratulations! It looks like you are getting a free trip to jail!"
    replay = raw_input("Would you like to play again? -->")
    
    if replay == 'no' or 'No':
        print "\n\tOk, enjoy the clink!"
    else:
        start()


def lobby_area():
        print "\n\tYou are in the lobby"
        print "Looking around, you see 4 doors, a security guard and a teller window."
             
        print "You can choose the %s on the left or the %s on the right, 'talk' to the security guard, or the 'teller' window." % (doors[0:2], doors[2:4])
        
        choice = raw_input("--> ")
        
        if choice == 'wealth':
            wm_office()
        elif choice == 'vault':
            vault_room()
        elif choice == 'lunch':
            lunch_room()
        elif choice == 'managers':
            managers_office()
        elif choice == 'talk':
            security_guard()
        elif choice == 'teller':
            teller_window()
        elif choice == 'exit':
            print "Please, come back when you are ready."
            exit(0)
        else:
            print "I'm sorry, I don't understand what you want to do. Are you a little nervous?"
            print "Please, try again."
            lobby_area()


def atrium():
    print "You are standing in the atrium."
    print "What would you like to do? Please select 'exit', 'talk' to the security guard or 'enter' the lobby"
    
    choice = raw_input("--> ")
    
    if choice == 'enter':
        lobby_area()
    elif choice == 'talk':
        security_guard()  
    elif choice == 'exit':
        print "You chicken! You won't have a very good career as a bank robber!"
        exit(0)
    else:
        print "I'm sorry, I don't understand what you want to do. Are you a little nervous?"
        print "Please, try again."
        atrium()


def managers_office():
    print "\n\tYou are in the manager's office."
    print "What would you like to do here?"
    print "You can 'look' around, you can choose the door to the %s, or 'talk' to the manager." % doors[2]
    
    choice = raw_input("--> ")
    
    if choice == 'look':
        print "\n\tYou see a desk, the manager and a security alarm."
        print "What would you like to do?"
        print "You can 'stay' in the managers office, go into the %s, 'check out' the desk, or 'inspect' the security alarm." % doors[2]
        
        office_choice = raw_input ("--> ")
        
        if office_choice == 'stay':
            managers_office()
        elif office_choice == 'lunch':
            lunch_room()
        elif office_choice == 'check out':
            managers_desk()
        elif office_choice == 'inspect':
            security_alarm()
        elif choice == 'exit':
            print "You chicken! You won't have a very good career as a bank robber!"
            exit(0)
        else:
            print "I'm sorry, I don't understand what you want to do. Are you a little nervous?"
            print "Please, try again."
            managers_office()
        
    elif choice == 'lunch':
        lunch_room()
    elif choice == 'talk':
        manager()
    elif choice == 'exit':
        print "You chicken! You won't have a very good career as a bank robber!"
        exit(0)
    else:
        print "I'm sorry, I don't understand what you want to do. Are you a little nervous?"
        print "Please, try again."
        managers_office()


def managers_desk():        
    print "\n\tYou are looking at the manager's desk."
    print "You can 'use' the computer, stapler, 'read' notepad, 'drink' coffee, or 'return' to office."
    
    choice = raw_input("--> ")
    
    if choice == 'use':
        computer = raw_input("\n\t\t[manager@localhost]$ ")
        
        if computer == 'ls':
            print "Documents   Desktop   Downloads   Music   Pictures   Notes"
            print "All folders are empty."
            managers_desk()
        else:
            print "error - there really isn't anything to see here."
            managers_desk()
    elif choice == 'read':
        print "There seems to be something writting, then erased - it is not legible."
        managers_desk()
    elif choice == 'drink':
        print "You slam the coffee and immediately regret it. Apparently, the manager drinks on the job, as well."
        managers_desk()
    elif choice == 'return':
        managers_office()
    else:
        print "I'm sorry, I don't understand what you want to do. Are you a little nervous?"
        print "Please, try again."
        managers_desk()        
    

def manager():
    print "\n\tHow may I help you?"
    print "You can say, 'open' a checking account, 'give' me the security alarm code, 'unlock' the vault or 'back'."
    
    choice = raw_input("--> ")
    
    if choice == 'open':
        print "\n\tGreat, you are all set, have a great day!"
        exit(0)
    elif choice == 'give':
        print "\n\tShe says, 'I'm sorry, I cannot do that.'"
        print "The security guard overhears this exchange. He shoots you in the back."
        
        replay = raw_input("Would you like to play again? --> ")
    
        if replay == 'no':
            print "\n\tOk, enjoy death!"
        else:
            start()
    elif choice == 'back':
        managers_office()
    elif choice == 'unlock':
        print "\n\tShe says, 'Seriously, I can't do that!'"
        print "The securirty guard overhears this exchange. He shoots you in the back."
        
        replay = raw_input("Would you like to play again? --> ")
    
        if replay == 'no':
            print "\n\tOk, enjoy death!"
        else:
            start()
    elif choice == 'exit':
        print "Please, come back when you are ready."
        exit(0)
    else:
        print "I'm sorry, I don't understand what you want to do. Are you a little nervous?"
        print "Please, try again."
        manager()


def lunch_room():
    print "\n\tYou are in the lunch room."
    print "You see a table and some employees eating."
    print "You can 'talk' to the employees, go to %s, go to the 'lobby'" % doors[3]
    
    choice = raw_input("--> ")
    
    if choice == 'managers':
        managers_office()
    elif choice == 'lobby':
        lobby_area()
    elif choice == 'talk':
        print "\n\tThey say, 'What's up? Why are you in here?'"
        print "You can go 'back', or say I'm 'robbing' the bank put your hands up."
        
        say = raw_input("--> ")
        
        if say == 'back':
            lunch_room()
        else:
            print "\n\tAn employee grabs their knife and stabs you in the neck."
        
        replay = raw_input("Would you like to play again? --> ")
    
        if replay == 'no':
            print "\n\tOk, enjoy death!"
        else:
            start()    
    elif choice == 'exit':
        print "Please, come back when you are ready."
        exit(0)
    else:
        print "I'm sorry, I don't understand what you want to do. Are you a little nervous?"
        print "Please, try again."
        manager()    
    
       
start()