print("Hello, please enter your name and age")

name = input()
age = int(input())

def frickyou():
	if age >= 24:
		print("Damn, " + name + " you old as heck lmfao")
	elif age < 18:
			print("why are you still here, do something with your life before its too late")
	else: 
		if age == 18 or 20:
				print("Nice age, you got some time to do stuff yet, congrats!")
				
frickyou()