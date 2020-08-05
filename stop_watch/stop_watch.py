print("Enter number of seconds")
import time
a = int(input())
while a!=0:
	print(str(a) + "    seconds reamining")
	time.sleep(1)
	a=a-1

print("TIME IS UP")	
time.sleep(1)

print("END")
