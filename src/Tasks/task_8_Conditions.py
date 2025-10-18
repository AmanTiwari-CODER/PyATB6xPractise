# Problem find the max between two number entered by the user.

num_1 = float(input("Enter a number: "))
num_2 = float(input("Enter another number: "))

if num_1 - num_2 == 0:
    print(f"Both {num_1} and {num_2} are equal.")
elif num_1 > num_2:
    print(f"{num_1} is greater than {num_2}.")
else:
    print(f"{num_1} is less than {num_2}.")