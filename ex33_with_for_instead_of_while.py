user1 = int(raw_input("Please enter your first number -> "))
user2 = int(raw_input("Please enter a bigger second number -> "))

def count(arg1, arg2):
    i = user1
    numbers = []

    for i in range(user1, user2):
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i


        print "The numbers: "

    for i in numbers:
        print i

count(user1, user2)

