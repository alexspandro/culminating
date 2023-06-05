import matplotlib as plt

WeightGoal = int(input("What is the weight goal you are trying to achieve?"))

TrackDuration = int(input("How many days would you like to track your weight for?"))

dates = [day 1, day 2, day 3, day 4, day 5, day 6, day 7]

weights = [, , , , , , ]
plt.scatter(dates, weights)
plt.title('Tracker Graph')
plt.xlabel('Day')
plt.ylabel('Weight')
plt.legend(['Weight', 'WeightGoal'])
plt.grid(True)
plt.axhline(y=WeightGoal , color='r', linestyle='-')
plt.show()

print("Congratulations, you met your goal of", WeightGoal , "lbs!"
print("Keep up the good work, you are ", CurrentWeight - WeightGoal , "lbs away from your goal!"

with open 
