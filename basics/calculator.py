num1 = int(input("Enter first number= "))
num2 = int(input("Enter second number= "))
operator = input("Enter operator(+,-,*,/):")

if operator == '+':
    print("Sum is=",num1+num2)
elif operator == '-':
    print("Differnce is=",num1-num2)
elif operator == '*':
    print("Product is=",num1*num2)
elif operator == '/':
    print("Division is=",num1/num2)
else:
    print("Invalid")
