#Print the entered number is even or odd

num = int(input("Enter your number: ").strip())

if num ==1:
    print(f"{num} is composite neither even nor odd.")
else:
    if num > 1:
        if num % 2 == 0:
            print(f"{num} is EVEN")
        else:
            print(f"{num} is ODD")
    else:
        print("Enter a number greater than or equal to 2.")