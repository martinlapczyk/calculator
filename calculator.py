print("Choices: 1. Addition 2.Subtraction 3. Multiplication 4. Division 5. Raising one number by the power of the second")
choice=int(input("Please choose a function"))
match choice:
    case 1:
        a=float(input("Please input first number:"))
        b=float(input("Please input second number:"))
        c=a+b
        print(c)
    case 2:
        a=float(input("Please input first number:"))
        b=float(input("Please input second number:"))
        c=a-b
        print(c)
    case 3:
        a=float(input("Please input first number:"))
        b=float(input("Please input second number:"))
        c=a*b
        print(c)
    case 4:
        a=float(input("Please input first number:"))
        b=float(input("Please input second number:"))
        c=a/b
        print(c)
    case 5:
        a=float(input("Please input first number:"))
        b=float(input("Please input second number:"))
        c=a**b
        print(c)

