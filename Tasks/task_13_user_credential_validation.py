# Q4**  - Check if the user can log in based on correct username and password.**

# I/p
# username = "admin"
# password = "1234"

# O/p
# ✅ Login Successful

# For the Fail condition Other O/P = ❌ Invalid Credentials
print("Username and Password are case sensitive","-"*100,sep="\n")
user_name = input("Enter your username: ").strip()
password = input("Enter your password: ").strip()

if user_name == "admin" and password == "1234":
    print("✅ Login Successful")
else:
    print("❌ Invalid Credentials")