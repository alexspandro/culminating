import matplotlib as plt

// CurrentWeight = int input("What is your current weight?")
// WeightGoal = int input("What is the weight goal you are trying to achieve?")
x_axis = ['value_1', 'value_2', 'value_3', ...]
y_axis = ['value_1', 'value_2', 'value_3', ...]

plt.plot(x_axis, y_axis)
plt.title('Tracker Graph')
plt.xlabel('Date')
plt.ylabel('Weight')
plt.axhline(y=WeightGoal , color='r', linestyle='-')
plt.show()

print("Congratulations, you met your goal of", WeightGoal , "lbs!"
print("Keep up the good work, you are ", CurrentWeight - WeightGoal , "lbs away from your goal!"

