def chads_function(arg1, arg2):
    print "Hey this is my %s argument" % arg1
    print "And, this is my %s argument" % arg2


chads_function("first","second")

user = raw_input("Please enter 'first' or 'second': ")
user2 = raw_input("Please enter the opposite: ")

chads_function(user,user2)

user_times2 = raw_input("Please enter 'first' or 'second' again: ")
user_times2_again = raw_input("Please enter the opposite again: ")

chads_function(user_times2 * 2,user_times2_again * 3)

def playing(num1, num2):
    print "Hey this is the number %d" % num1
    print "And, this is the number %d" % num2
    
playing(1,2)

ask = int(raw_input("Why don't you give me a number? "))
ask_again = int(raw_input("And, a second one, please? "))

playing(ask, ask_again)

print "I bet I can blow your mind and multiply whatever numbers you give me by 2!"

ask_2 = int(raw_input("Why don't you give me a number? "))
ask_again_2 = int(raw_input("And, a second one, please? "))

print "Ewwww, that is a tough one! Thinking..."

playing(ask_2 * 2,ask_again_2 * 2)

print "I wonder...can I combine a couple of functions without breaking this!?\n"
print "Let's see..."

crazy = raw_input("Why don't you give me 'first' or 'second' again? ")
crazy2 = raw_input("Again, the opposite? ")
crazy3 = int(raw_input("Now, a number? "))
crazy4 = int(raw_input("And, a second number? "))

print "Thank you very much, I appreciate the assistance. Let me see what I can do with this." 

chads_function(crazy,crazy2)
print "Awesome, I am going to add 1 to your first number and multiply your second number by 3!\n"
playing(crazy3 + 1,crazy4 * 3)
