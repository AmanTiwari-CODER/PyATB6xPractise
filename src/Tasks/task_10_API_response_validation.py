# **Q - You receive an API response code from your test script.
# Write an if-else block to check whether the response is successful (status code 200) or not.**

# ```
# I/P response = 404 , O/P ❌ Failed API Request
# I/P response = 200 , O/P ✅ Passed API Request

status_code = int(input("Enter the response status_code from the API resquest: "))

if status_code > 0 and status_code < 600:
    if status_code == 200:
        print(f"✅ Passed API Request")
    else:
        print(f"❌ Failed API Request")
else:
    print("Entered response status code is invalid.")
