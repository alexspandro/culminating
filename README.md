# culminating
this is our code .
import matplotlib.pyplot as plth
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set window size
window_width = 800
window_height = 400
window_size = (window_width, window_height)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Weight Tracker")

# Define colors
background_color = (255, 255, 255)
line_color = (0, 0, 0)
point_color = (255, 0, 0)
text_color = (0, 0, 0)

# Define graph settings
graph_width = 600
graph_height = 300
graph_origin = (100, 50)
graph_spacing = 50

# Create an empty list to store weight data
weight_data = []

# Function to draw the graph
def draw_graph():
    # Clear the window
    window.fill(background_color)

    # Draw the x-axis
    pygame.draw.line(window, line_color, graph_origin, (graph_origin[0] + graph_width, graph_origin[1]))

    # Draw the y-axis
    pygame.draw.line(window, line_color, graph_origin, (graph_origin[0], graph_origin[1] - graph_height))

    # Draw the broken line graph
    if len(weight_data) > 1:
        for i in range(1, len(weight_data)):
            x1 = graph_origin[0] + (i - 1) * graph_spacing
            y1 = graph_origin[1] - ((weight_data[i - 1] - min(weight_data)) / (max(weight_data) - min(weight_data))) * graph_height
            x2 = graph_origin[0] + i * graph_spacing
            y2 = graph_origin[1] - ((weight_data[i] - min(weight_data)) / (max(weight_data) - min(weight_data))) * graph_height
            pygame.draw.line(window, line_color, (x1, y1), (x2, y2))

    # Draw the data points
    for i in range(len(weight_data)):
        x = graph_origin[0] + i * graph_spacing
        y = graph_origin[1] - ((weight_data[i] - min(weight_data)) / (max(weight_data) - min(weight_data))) * graph_height
        pygame.draw.circle(window, point_color, (x, y), 5)

    # Update the display
    pygame.display.update()

# Function to handle user input
def handle_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if len(weight_data) >= graph_width // graph_spacing:
                    weight_data.pop(0)
                weight_data.append(int(input_text))
                input_text = ""
                draw_graph()
            elif event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode

# Main loop
input_text = ""
weight_prompt = True
goal_prompt = True
while True:
    handle_input()
    draw_graph()
    
    # Prompt for weight input
    if weight_prompt:
        weight_text = "What is your weight today? (in kg)"
        weight_font = pygame.font.Font(None, 30)
        weight_surface = weight_font.render(weight_text, True, text_color)
        weight_rect = weight_surface.get_rect(center=(window_width // 2, window_height // 2))
        window.blit(weight_surface, weight_rect)
        weight_prompt = False



    # Prompt for goal weight input
    if not weight_prompt and not goal_prompt:
        goal_text = "What is your goal weight? (in kg)"
        goal_font = pygame.font.Font(None, 30)
        goal_surface = goal_font.render(goal_text, True, text_color)
        goal_rect = goal_surface.get_rect(center=(window_width // 2, window_height // 2 + 50))
        window.blit(goal_surface, goal_rect)
    
    # Update the display
    pygame.display.update()
   
