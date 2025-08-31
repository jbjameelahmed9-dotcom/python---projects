# calculator 2 digit
num_1 = 4
operation = "+"
num_2 = 12

if operation == "+":
    result = num_1 + num_2
elif operation == "-":
    result = num_1 - num_2
elif operation == "*":
    result = num_1 * num_2
elif operation == "/":
    result = num_1 / num_2
else:
    print("Error")
print(result)