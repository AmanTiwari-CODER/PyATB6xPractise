# **Q3

# You want to check whether a web page loads within 3 seconds (performance test condition).

# load_time = 4.2
# ⚠️ Page load too slow: 4.2 seconds

load_time = float(input("Enter the load time from response: ").strip())

if load_time <= 0 :
    print("❌ Invalid load time, Enter valid value must be a postive")
else:
    if load_time <=1:
        print("Great performance")
    elif load_time <=2:
        print("Good performance")
    elif load_time <=3:
        print("Acceptable but need improvement")
    elif load_time <=4:
        print("⚠️ Page load too slow")
    else:
        print("Bad performance need to Restart the server.")