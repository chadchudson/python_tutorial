from sys import argv

script, filename = argv

print "We are going to show you the new contents of ex15_sample.txt"
print "Since we modified that in ex16."

txt = open(filename)


print "Here is your file %r:" % filename
print txt.read()
txt.close()
