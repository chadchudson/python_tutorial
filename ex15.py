#Imports argv from the sys module
from sys import argv

#specifies the parameters for argv (i.e., ex15.py, ex15_sample.txt)
script, filename = argv

#txt is opening the file
txt = open(filename)

#prints our what is in the file
print "Here's your file %r:" % filename
print txt.read()


#Obtains the filename from the user
print "Type the filename again:"
file_again = raw_input("> ")

#opens the file again with the new data from the user
txt_again = open(file_again)

#prints out the contents of the file
print txt_again.read()

