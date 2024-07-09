print("I love pizza!")
print("It's really good!")

#string
name1 = "Angel's "
name2 = "Burger"
print("I love "+name1+name2)

#int
age = 25
age += 1
#convert to str to concatenate
print("Your age is: "+str(age)+" years")

#float
height = 67.7
#convert to str to concatenate
print("Your height is: " +str(height)+" cm")

#bool
human = False 
print(human)


name = "bRoWAE111CeacRC21"
print(len(name)) #find the length of string
print(name.find("1")) #find the position of a string (first only)
print(name.capitalize()) #capitalize the first letter and the rest will be small letters
print(name.lower()) #lowercase all letters
print(name.isdigit()) #returns true if the value is a digit
print(name.isalpha()) #returns true if the value only contains letters
print(name.count("1")) #count how many 1 are in a string
print(name.replace("1","5")) #replace
print(name*5) #display name 5 times

