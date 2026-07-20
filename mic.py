import time 
import random 

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&*"

password  = input ("set Password : ")

print ("\n Accending Database .........................................\n")

guess = ""

while guess != password:
    guess = ""

    for i in range (len(password)):
        guess +=random.choice(chars)

    print("\n trying ........!",guess)    
    time.sleep(0.00)

print("\n Password Cracked : ", password)