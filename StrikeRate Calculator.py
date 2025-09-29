# Batting Strike Rate Calculator
# Runs per 100 balls

print("Welcome To The Batting Strike Rate Calculator created by Parth")

# Keep asking until a valid name (only alphabets) is entered
while True:
    user_name = input("Please enter the name of the Batsman: ")
    if user_name.isalpha():   # checks if only letters
        break
    else:
        print("⚠️ Invalid input! Please enter only alphabets (no numbers or symbols).")

runs = int(input("Please enter the Runs scored by the Batsman: "))
balls = int(input("Please enter the number of Balls played by the Batsman: "))

avg = runs / balls
strike_rate = avg * 100

print("The strike rate of", user_name, "is", strike_rate)
