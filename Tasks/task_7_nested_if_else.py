#Problem to take user input in integer as age and show them if they are eligible to go trip or not.

age = int(input("Enter your age: ").strip())
if age > 0 and age < 125:
    if age >= 21:
        print("Yes you are eligible to go to Trip.")
    else:
        print("You are not eligible to go to Trip.")
else:
    print("Please enter valid age between 1 and 124")
