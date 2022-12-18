value1 = int(input("Enter a number "))
value2 = int(input("Enter another number "))
operation = input("Enter the operation you want to do ")

def check_operation():
	if operation == "+":
		return value1 + value2
	elif operation == "-":
		return value1 - value2
	elif operation == "*":
		return value1 * value2
	elif operation == "/":
		return value1 / value2
	else: 
		if operation == "**":
			return value1 ** value2

print(check_operation())