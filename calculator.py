print("Simple Python Calculator")
print("Select operation")
print("1.Addition")
print("2.Substraction")
print("3.Multification")
print("4.Division")
choice = input("Enter choice(1/2/3/4):")
num1 = float(input("Enter first number"))
num2 = float(input("Enter second number"))
if choice == "1":
    result = num1 + num2
    print("Result:", result)
elif choice == "2":
    result = num1 - num2
    print("Result:", result)

elif choice == "3":
    result = num1 * num2
    print("Result:", result)

elif choice == "4":
    result = num1 / num2
    print("Result:", result)

else:
    print("Invalid choice")
