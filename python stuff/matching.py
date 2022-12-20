pipi = input("Enter a number ")
pipo = input("Enter another number ")

match pipi:
	case big if pipi > pipo:
		print("The number " + pipi + " is bigger than " + pipo)
	case smol if pipi < pipo:
		print("The number " + pipi + " is smaller than " + pipo)
