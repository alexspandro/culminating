import datetime
import pygame
import matplotlib.pyplot as plt
import os

pygame.init()
WINDOW_SIZE = (1000, 800)  # Increased window size for a larger graph
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Body Weight Tracker")

BACKGROUND_COLOR = (255, 255, 255)
TEXT_COLOR = (0, 0, 0)

def draw_graph(weightDay, weightGoal):
    # Clear the window
    window.fill(BACKGROUND_COLOR)

    # Get current day of the week
    now = datetime.datetime.now()
    current_day = now.strftime("%A")

    # Create x-axis values for the days of the week
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # Create y-axis values starting from 20 pounds with increments of 20
    y_values = list(range(20, 420, 20))

    # Set figure size to match window size
    plt.figure(figsize=(WINDOW_SIZE[0] / 100, WINDOW_SIZE[1] / 100))

    # Plot scatter plot graph using Matplotlib
    plt.scatter(days_of_week, weightDay)
    plt.xticks(rotation=5)
    plt.yticks(y_values, fontsize=10)  # Adjust font size of y-axis labels

    # Add grid lines
    plt.grid(color='gray', linestyle='--', linewidth=0.5)

    # Add x-axis and y-axis labels with increased font size
    plt.xlabel('Days', fontsize=12)
    plt.ylabel('Weight in Pounds', fontsize=12)

    # Plot the goal line
    plt.axhline(y=weightGoal, color='r', linestyle='-')

    # Save the graph as an image file
    graph_file = "graph.png"
    plt.savefig(graph_file)
    plt.close()

    # Load the image file into Pygame
    graph_image = pygame.image.load(graph_file)
    os.remove(graph_file)

    # Display the graph in the center of the window
    graph_rect = graph_image.get_rect()
    graph_rect.center = window.get_rect().center
    window.blit(graph_image, graph_rect)

    # Update the display
    pygame.display.flip()


weightDay = [var]
weightGoal = []

# Access the 7th element (index 6) of the weightDay list
daySeven = weightDay[6]

if daySeven == weightGoal or daySeven < weightGoal:
    print("Congratulations, you met your goal of", weightGoal, "lbs!")
else:
    print("Keep up the good work, you are", daySeven - weightGoal, "lbs away from your goal.")

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Call the draw_graph() function to update the graph
    draw_graph(weightDay, weightGoal)

pygame.quit()
