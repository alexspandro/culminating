import os
import matplotlib.pyplot as plt

weightGoal = int(input("What is the weight goal, in pounds (lbs), you are trying to achieve? "))
print("The tracker is set to track the next 7 days.")

weightDay = []
for i in range(1, 8):
    weight = int(input(f"How many lbs did you weigh on day {i}? "))
    weightDay.append(weight)

dates = ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5', 'Day 6', 'Day 7']
plt.scatter(dates, weightDay)
plt.title('Tracker Graph')
plt.xlabel('Day')
plt.ylabel('Weight (lbs)')
plt.legend(['Weight', 'weightGoal'])
plt.grid(True)
plt.axhline(y=weightGoal, color='r', linestyle='-')
plt.show()

        while congrats:
            if daySeven == goal_weight:
                goal_reached_text = font.render("Congratulations! You have reached your weight goal.", True, green, blue)
                goal_reached_text_rect = goal_reached_text.get_rect()
                goal_reached_text_rect.center = (X // 2, Y // 2)
                screen.blit(goal_reached_text, goal_reached_text_rect)

                congrats = False
            elif daySeven > goal_weight:
                minus_last_day_text = font.render(f"So close! You are {daySeven - goal_weight} lbs away from your goal!", True, green, blue)
                minus_last_day_text_rect = minus_last_day_text.get_rect()
                minus_last_day_text_rect.center = (X // 2, Y // 2)
                screen.blit(minus_last_day_text, minus_last_day_text_rect)
                congrats = False
            else:
                minus_goal_text = font.render(f"So close! You are {goal_weight - daySeven} lbs away from your goal!", True, green, blue)
                minus_goal_text_rect = minus_goal_text.get_rect()
                minus_goal_text_rect = (X // 2, Y // 2)
                screen.blit(minus_goal_text, minus_goal_text_rect)
                
                congrats = False
                   
        

# The following lines are commented out because the functionality related to saving the file is not implemented.
# folder = os.getcwd()
# print("Your information is currently being saved to a file named 'userWeightInfo.png'.")
# folderName = input("Which existing folder would you like to assign the file to? ")
# fileCreateNew = folder + folderName + "\\userWeightInfo.png"

# Access the 7th element (index 6) of the weightDay list
daySeven = weightDay[6]

if daySeven == weightGoal or daySeven < weightGoal:
    print("Congratulations, you met your goal of", weightGoal, "lbs!")
else:
    print("Keep up the good work, you are", daySeven - weightGoal, "lbs away from your goal.")
