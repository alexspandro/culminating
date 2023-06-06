import os
import matplotlib.pyplot as plt

folder = os.getcwd()
WeightGoal = int(input("What is the weight goal you are trying to achieve?"))
print("The tracking timeframe is set to 7 days.")

dates = ['day 1', 'day 2', 'day 3', 'day 4', 'day 5', 'day 6', 'day 7']
weights = [40, 45, 70, 20, 60, 65, 40]

plt.scatter(dates, weights)
plt.title('Tracker Graph')
plt.xlabel('Day')
plt.ylabel('Weight')
plt.legend(['Weight', 'WeightGoal (red)'])
plt.grid(True)
plt.axhline(y=WeightGoal, color='r', linestyle='-')
plt.show()

weightDay = []
for i in range(1, 8):
weight = int(input("how much did you weight on day {i} ?")
#uses an appended list to ask user's weight for 7 days

print("Your information is currently being saved to a file named 'userWeightInfo.csv'.")
folderName = input("Which existing folder would you like to assign the file to? ")
fileCreateNew = folder + folderName + "\\userWeightInfo.csv"

#file is opened, written on, and closed
with open ("userWeightinfo.csv", "w") as file:
  file.writelines("NEW WEIGHT PROFILE (LBS)\n-------------")
  file.writelines("Day 1: " + oneW + "lbs\n")
  file.writelines("Day 2: " + twoW + "lbs\n")
  file.writelines("Day 3: " + threeW + "lbs\n")
  file.writelines("Day 4: " + fourW + "lbs\n")
  file.writelines("Day 5: " + fiveW + "lbs\n")
  file.writelines("Day 6: " + sixW + "lbs\n")
  file.writelines("Day 7: " + sevenW + "lbs\n")
  
print("FILE SAVED IN FOLDER:", folderName)

print("Congratulations, you met your goal of", WeightGoal , "lbs!")
print("Keep up the good work, you are ", sevenW - WeightGoal , "lbs away from your goal!")
