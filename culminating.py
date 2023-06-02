import matplotlib as plt
from datetime import datetime, timedelta
CurrentWeight = int(input("What is your current weight?"))
WeightGoal = int(input("What is the weight goal you are trying to achieve?"))
TrackDuration = int(input("How many days would you like to track your weight for?"))

dates = [datetime.now() + timedelta(days=i) for i in range(TrackDuration)] #keeps count of how many days will be tracked

weights = [CurrentWeight] * TrackDuration

plt.plot(dates, weights)
plt.title('Tracker Graph')
plt.xlabel('Date')
plt.ylabel('Weight')
plt.legend(['Weight', 'WeightGoal'])
plt.grid(True)
plt.axhline(y=WeightGoal , color='r', linestyle='-')
plt.show()

print("Congratulations, you met your goal of", WeightGoal , "lbs!"
print("Keep up the good work, you are ", CurrentWeight - WeightGoal , "lbs away from your goal!"

