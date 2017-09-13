from random import *

y = randint(1,100)
print y
x = input("What is your guess? ")

while x!=y:
      if x<y:
            print "Choose a bigger value "
      else:
            print "Choose smaller value "
      x = input("What is your guess? ")                  
else:
      print "You are correct "
