import random 
import time

sleep = time.sleep

print("You have 5 lifes")
sleep(1)

life = 5
pokusaj = 0

while life >= 1:
	if life == 0:
		print("Game over ......")
		sleep(1)
		print("Score:{}".format(tries))
		break
	
	print(" ")
	print("[1] Rock")
	sleep(0.5)
	print("[2] Paper")
	sleep(0.5)
	print("[3] Scissors")
	sleep(0.5)
	print(" ")
	
	izbor = int(input("Chose one: "))
	print(" ")
	sleep(1)
	
	ai = random.randint(1, 3)
	
	if izbor == 1 and ai == 1:
		print("Player: Rock")
		sleep(1)
		print("AI: Rock:")
		sleep(1.5)
		print(" ")
		print("DRAW!!!")
		print(" ")
		print("==================")
		sleep(1)
	
	elif izbor == 1 and ai == 2:
		print("Player: Rock")
		sleep(1)
		print("AI: Paper")
		sleep(1.5)
		print(" ")
		print("Player loses...")
		sleep(0.5)
		life = life - 1
		print("You have {} lives".format(life))
		print(" ")
		print("==================")
		sleep(1)
		
	elif izbor == 1 and ai == 3:
		print("Player: Rock")
		sleep(1)
		print("AI: Scisors:")
		sleep(1.5)
		print(" ")
		print("Player wins!")
		sleep(0.5)
		pokusaj = pokusaj + 1
		print("You have {} lives".format(life))
		print(" ")
		print("===================")
		sleep(1)
		
	
	elif izbor == 2 and ai == 1:
		print("Player: Paper")
		sleep(1)
		print("AI: Rock:")
		sleep(1.5)
		print(" ")
		print("Player wins!")
		sleep(0.5)
		pokusaj = pokusaj + 1
		print("You have {} lives".format(life))
		print(" ")
		print("===================")
		sleep(1)
	
	elif izbor == 2 and ai == 2:
		print("Player: Paper")
		sleep(1)
		print("AI: Paper:")
		sleep(1.5)
		print(" ")
		print("DRAW!!!")
		print(" ")
		print("==================")
		sleep(1)
	
	elif izbor == 3 and ai == 3:
		print("Player: Paper")
		sleep(1)
		print("AI: Scissors")
		sleep(1.5)
		print(" ")
		print("Player loses...")
		sleep(0.5)
		life = life - 1
		print("You have {} lives".format(life))
		print(" ")
		print("==================")
		sleep(1)
	
	elif izbor == 3 and ai == 1:
		print("Player: Scissors")
		sleep(1)
		print("AI: Rock")
		sleep(1.5)
		print(" ")
		print("Player loses...")
		sleep(0.5)
		life = life - 1
		print("You have {} lives".format(life))
		print(" ")
		print("==================")
		sleep(1)
	
	elif izbor == 3 and ai == 2:
		print("Player: Scissors")
		sleep(1)
		print("AI: Paper:")
		sleep(1.5)
		print(" ")
		print("Player wins!")
		sleep(0.5)
		pokusaj = pokusaj + 1
		print("You have {} lives".format(life))
		print(" ")
		print("===================")
		sleep(1)
	
	elif izbor == 3 and ai == 3:
		print("Player: Scissors")
		sleep(1)
		print("AI: Scissors:")
		sleep(1.5)
		print(" ")
		print("DRAW!!!")
		print(" ")
		print("==================")
		sleep(1)
	
	else:
		print("Invalid choice!")
		print(" ")
		print("==================")
		sleep(1)
		
