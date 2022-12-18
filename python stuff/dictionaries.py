print("Personality test, ")
val = int(input("Which character do you like the most? \n 1: Berdly, \n 2: Susie, \n 3: Kris \n 4: None \n"))

personality = {
		"Berdly": "You gamer weeb lmfao",
		"Susie": "Impulse edgy alert",
		"Kris": "You're just a normal edgy kid lol",
}

def plzkillme():
	if val == 1:
		print(personality["Berdly"])
	elif val == 2:
		print(personality["Susie"])
	elif val == 3:
		print(personality["Kris"])
	elif val == 4:
		print("Get out")

plzkillme()

#Cuando sea necesario hacer un diccionario, acordate de poner comas al final

#Como chota se arreglan los elifs???

