
name = input("What's your name? ")


while True:
    try:
        num1 = int(input("First number: "))
    except:
        print("Not a number. Try again")
        continue
    else:
        break


while True:
    try:
        num2 = int(input("Second number: "))
    except:
        print("Not a number. Try again")
        continue
    else:
        break

result = int (num1) + int (num2)
print("Hello " + name + "!, the correct answer of ", num1 ," + ", num2 ," is : ", result)
   
# num2 = input("First number: ")
# result = int (num1) + int (num2)
# print("Hello " + name + ", the correct answer of " + num1 + " and " + num2 + " is : ", result) 

