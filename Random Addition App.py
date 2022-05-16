#trying to build a app thats gives a user rans=dom number to prints
from random import randint
x=randint(1,100)
y=randint(1,100)
print('your first number is',x)
print('your second number is y', y)
v=input("what is your answer?: ")
c=x+y
if c==int(v):
    print("well done champ")
else:
  print("Keep pushing harder")
    
