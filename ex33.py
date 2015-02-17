user1 = int(raw_input("Please enter your first number -> "))
user2 = int(raw_input("Please enter a bigger second number -> "))
user3 = int(raw_input("Please enter a number you would like to increment by -> "))

def count(arg1, arg2):
    i = user1
    numbers = []

    while i < user2:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + user3
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i


        print "The numbers: "

    for num in numbers:
        print num
            
count(user1, user2)

