#init var x
x = "There are %d types of people." % 10
#init var binary
binary = "binary"
#init do_not
do_not = "don't"
#init var y
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x #reprints var x
print "I also said: '%s'." % y #reprints var y

hilarous = False #init hilarous 
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarous

w = "This is the left side of..."
e = "a string with a right side."

print w + e