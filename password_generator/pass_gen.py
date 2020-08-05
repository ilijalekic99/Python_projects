import random
import string

print("Welcome to password generator")

def passlength():
	print("How long do you want the password to be?")
	global passlen
	try:
		input1 = input()
		passlen = int(input1)
	except:
		print("Chose a number")
		passlength()
	if passlen<5:
		print("Too short, try again")
		passlength()
	elif passlen>30:
		print("That is to long, try again")
		passlength()
	else:
		print("OK")
passlength()

def passwordgen():
	chars = string.ascii_letters + string.digits + "@$*!?/"
	password=""
	for x in range(passlen):
		password=password+random.choice(chars)
	print("Your password is: "+password)
passwordgen()
