#Batting Strike Rate Calculator
#Runs per 100 balls

print("Welcome To The Batting Strike Rate Calculator created by Parth")
user_name = input("Please enter the name of the Batsman:")
r = input("Please enter the Runs scored by the Batsman:")
b = input("Please enter the number of Balls played by the Batsman:")
r = int(r)
b = int(b)
avg= r/b
sr=avg*100
print("The strike rate of", user_name, "is", sr)