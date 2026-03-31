#SIMPLE CALCULATOR

print("Simple Calculator")
print("1.ADDITION")
print("2.SUBTRACTION")
print("3.MULTIPLICATION")
print("4.DIVISION")

choice=int(input("Enter your choice:"))

a=float(input("Enter first number:"))
b=float(input("Enter second number:"))

if choice==1:
    answer=a+b
    print("Result:",answer)

elif choice==2:
    answer=a-b
    print("Result:",answer)

elif choice==3:
    answer=a*b
    print("Result:",answer)

elif choice==4:
    if b!=0:
        answer=a/b
        print("Result:",answer)
    else:
        print("Division by zero is not possible")

else:
    print("Invalid choice")

