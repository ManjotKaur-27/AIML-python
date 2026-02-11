# #First program
# print("Hello World!")

# #Variables and user input
# print("What is your name?")
# name = input("My name is=")
# print("Hello " + name)

# #Type convertions
# old_age = 18
# new_age = int(old_age)+2
# print(new_age)
# num = 8
# print(float(num))

#Add two numbers
first = input("num1= ")
second = input("num2= ")
print("Sum is= ", int(first)+int(second))
print("Sum is= "+ str(int(first)+int(second)) )

#Strings
name = "Manjot Kaur"
print(name.upper())     
print(name.lower())
print(name.find('m'))             #finds if it exists, gived index if does else gives -1, python is case sensitive
print(name.replace('a','t'))      #replaces first input with second
print(name.replace('a', 't', 1))  #replaces only first a with t
print('j' in name)                #returns bool value 