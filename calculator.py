num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Choose operation: ")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
choice = input("Enter opertion (1/2/3/4): ")

if choice == '1' or choice == '+':
    result = num1 + num2 
    operation = "+"
elif choice == '2' or choice =='-':
    result = num1 - num2
    operation = "-"
elif choice =='3' or choice =='*':
    result = num1 * num2
    operation = "*"
elif choice =='4' or choice =='/':
    if num2 == 0:
        result = "Error! Divison by zero"
        operation = "/"
    else:
        result = num1 / num2
        operation = "/"
else: 
    result = "Invalid operation!"
    operation = "Not Defined"

print(f"Result: {num1} {operation} {num2} = {result}")


