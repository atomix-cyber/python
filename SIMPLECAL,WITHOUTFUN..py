while True:
    n=int(input("Enter first value = "))
    b=int(input("Enter second value = "))
    print("1.add, 2.sub, 3.multiplication, 4.division")
    choice=input('choose your operation 1,2,3,4= ')
    if choice == '1':
        print(n, '+', b,'=', n+b)
    elif choice == '2':
        print(n, '-', b, '=',n-b)
    elif choice == '3':
        print(n, '*', b, '=', n*b)
    elif choice == '4':
        print(n, '/', b, '=', n/b)
    next_calculation = input("do you need to carry on another operation(y/n)")
    if next_calculation == 'n':
        break
else:
    print("invalid input")

