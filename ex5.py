name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue' 
teeth = 'White'
hair = 'Brown'
in_cm = height * 2.54
lbs_kg = weight * .453592

print "Let's talk about %s." % name
print "He's %d centimeters or %d inches tall." % (in_cm, height)
print "He's %d kilograms or %d lbs heavy." % (lbs_kg, weight)
print "Actually, that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, in_cm, lbs_kg, age + in_cm + lbs_kg)