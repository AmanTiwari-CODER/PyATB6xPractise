# **Q2**

# **In automation, you often compare expected and actual outputs.
# Write code to check if a test case passed or failed.**

# expected_title = "Dashboard"
# actual_title = "Dashboard "

# ✅ Test Passed – Title matches
# True - why > Strip and convert them into the lowercase = both of them are equal.

expected_title = input("Enter Expected title: ").lower()
actual_title = input("Enter Actual title: ").lower()

if expected_title.strip() == actual_title.strip():
    print("✅ Test Passed – Title matches")
else:
    print("❌Test Failed – Title mismatches")