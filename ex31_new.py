print "You are about to make the biggest decision of your life."

decision = raw_input("Please enter 1 or 2 -> ")

if decision == "1":
    print "OH crap! Seriously!?\n"
    print "Are you sure you want to select %s?" % decision

    new_selection = raw_input("Yes or No -> ")

    if new_selection == "Yes":
        print "Ok, well good luck with that, I guess! See ya!"

    elif new_selection == "No":
        print "Ok let's check out number 3!...\n"
        print "You WIN!!!! Good job!!"

elif decision == "2":
    print "Hmm, that is interesting..."
    print "Perhaps, you might like 3 better. Would you like to give that a shot?"

    new_selection2 = raw_input("Yes or No -> ")

    if new_selection2 == "No":
        print "Ok, well good luck with that, I guess! See ya!"
    
    elif new_selection2 == "Yes":
        print "You WIN! Great job!"

else:
    print "For real, you can't even get this right?!?!"
