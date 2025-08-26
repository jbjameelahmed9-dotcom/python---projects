# print function use
print("hello world, i am new!")

# evan number checker
num = [1,2,3,4,5,6,7,8]
for i in num:
    if i % 2 == 0:
        print(i)

# odd number checker
num = [1,2,3,4,5,6,7,8]
for i in num:
    if i % 2 !=0:
        print(i)

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

# table of 5

number = 5
for i in range (1,11):
    print(number, "x", i, "=",  number * i)   

# sum of list

nums = [3,10,77]
total = sum(nums)
print (total)

# sum num using for loop
num = [11,23,45]
total = 0
for i in num:
    total += i
print(total)

# max number found

numbers = [2,3,5,6,7,8,99]
print(max(numbers))

# reverse string using slice
pakistan = "karachi"
print(pakistan[::-1])

# reverse string using slice one more
karachi = "landhi"
print(karachi[::-1])

# word count

pak = "army zindabad"
print(len(pak))


   

