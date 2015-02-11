# Defining cheese_and_crackers function, so we can use it to print the 4 following lines by just saying
# cheese_and_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man, that's enough for a party!" 
    print "Get a blanket.\n"

# We are passing in the numbers to the function cheese_count and boxes_of_crackers
print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)

# Set variables directly - if you can assign something with = you can use it in a function
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Obviously, can do math, use variables, or combine both variable and math
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)