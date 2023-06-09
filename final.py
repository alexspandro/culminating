# This code should do everything it's supposed to do, possible to submit, though there is no
# congratulations message

import pygame
import csv
import matplotlib.pyplot as plt
import datetime
import os
pygame.init()

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

first = True
validFile = False

X = 500
Y = 500

warning = 0
stage = 0
backTextDisplay = False
optionsAvailable = True

screen = pygame.display.set_mode([500,500])

display_surface = pygame.display.set_mode((X, Y))
pygame.display.set_caption('Show Text')
font = pygame.font.Font('freesansbold.ttf', 20)
smallerFont = pygame.font.Font('freesansbold.ttf', 15)

# TEXT BOX VARIABLES
# TBscreen = pygame.display.set_mode((640, 480))
# TBfont = pygame.font.Font(None, 32)
TBclock = pygame.time.Clock()

TBinput_box = pygame.Rect(100, 100, 140, 32) # responsible for the location of the text box
TBcsv_box = pygame.Rect(100, 100, 140, 32)
TBgoal_box = pygame.Rect(100, 100, 140, 32)

TBcolor_inactive = pygame.Color('lightskyblue3')
TBcolor_active = pygame.Color('red')
TBcolor = TBcolor_inactive
TBactive = False

TBtext = ''
TBcsv = ''
TBgoal = ''

TBdone = False
goal_weight = 0

welcomeTextTut = font.render('Please enter csv file name.', True, green, blue)
welcomeText = font.render('Welcome. Press "1" to continue.', True, green, blue)
menuText = font.render('Press 2 to log weight.', True, green, blue)
menuText2 = font.render('Press 3 to change weight goal.', True, green, blue)
menuText3 = font.render('Press 4 to re-type csv file.', True, green, blue)
menuText4 = font.render('Press 5 to display progress.', True, green, blue)
backText = font.render('Press 0 to return.', True, green, blue)
testText = font.render('', True, green, TBcolor)
logText = font.render('Enter your weight', True, green, blue)
goalText = font.render('Enter your goal weight', True, green, blue)
warningText = smallerFont.render("You have hit 7 days, please make a new file", True, green, blue)

textTutRect = welcomeTextTut.get_rect()
textRect = welcomeText.get_rect()
textRect2 = welcomeText.get_rect()
textRect3 = welcomeText.get_rect()
textRect4 = welcomeText.get_rect()
optionText = backText.get_rect()
inputBox = testText.get_rect() # INPUT TEXT BOX TESTING

textTutRect.center = (X // 2, Y // 2.2)
textRect.center = (X // 2, Y // 2)
textRect2.center = (X // 2, Y // 1.8)
textRect3.center = (X // 2, Y // 1.6)
textRect4.center = (X // 2, Y // 1.4)
optionText.center = (100, 100)
inputBox.center = (200, 200)

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_0,
    K_1,
    K_2,
    K_3,
    K_4,
    K_5,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    MOUSEBUTTONDOWN,
    TEXTINPUT,
)

running = True
while running: #while not done (TB CODE)
    # Background color 
    screen.fill((255, 255, 255))

    # Circle thing
    pygame.draw.circle(screen, (0, 0, 255), (X // 2, X // 2), 75)
    
    # Text display
    if stage == 0:

        # Welcome
        display_surface.blit(welcomeText, textRect)
        display_surface.blit(welcomeTextTut, textTutRect)

        # CSV name input
        txt_surface1 = font.render(TBcsv, True, TBcolor)
        # Resize the box if the text is too long.
        width = max(200, txt_surface1.get_width()+10)
        TBcsv_box.w = width

        # Blit the text.
        screen.blit(txt_surface1, (TBcsv_box.x+5, TBcsv_box.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(screen, TBcolor, TBcsv_box, 2)

    elif stage == 1:

        # Welcome
        display_surface.blit(welcomeTextTut, textTutRect)

        # CSV name input
        txt_surface1 = font.render(TBcsv, True, TBcolor)
        # Resize the box if the text is too long.
        width = max(200, txt_surface1.get_width()+10)
        TBcsv_box.w = width

        # Blit the text.
        screen.blit(txt_surface1, (TBcsv_box.x+5, TBcsv_box.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(screen, TBcolor, TBcsv_box, 2)

    elif stage == 2:

        # Menu
        display_surface.blit(menuText, textRect)
        display_surface.blit(menuText2, textRect2)
        display_surface.blit(menuText3, textRect3)
        display_surface.blit(menuText4, textRect4)

    elif stage == 3:

        # Log weight
        display_surface.blit(logText, textRect)



        txt_surface2 = font.render(TBtext, True, TBcolor)
        # Resize the box if the text is too long.
        width = max(200, txt_surface2.get_width()+10)
        TBinput_box.w = width

        # Blit the text.
        screen.blit(txt_surface2, (TBinput_box.x+5, TBinput_box.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(screen, TBcolor, TBinput_box, 2)

        if warning == 1:
            display_surface.blit(warningText, textRect2)
        
    elif stage == 4:

        # Change goal
        display_surface.blit(goalText, textRect)
    
        # Goal weight input
        txt_surface1 = font.render(TBgoal, True, TBcolor)
        width = max(200, txt_surface1.get_width()+10)
        TBgoal_box.w = width

        # Blit the text.
        screen.blit(txt_surface1, (TBgoal_box.x+5, TBgoal_box.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(screen, TBcolor, TBgoal_box, 2)

        if TBgoal:
            try:
                goal_weight = float(TBgoal)  # Store the entered goal weight as a float
            except ValueError:
                goal_weight = 0  # Reset the goal weight if an invalid value is entered


    elif stage == 5:
    # Load weight data from the CSV file
        weights = []
        with open('weight.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader)  # Skip the header row
            for row in reader:
                weight = float(row[0])
                weights.append(weight)

        # Plot the progress graph
        plt.figure(figsize=(8, 6))  # Adjust the figure size as needed
        plt.plot(weights, marker='o')
        plt.plot(goal_weight, '*')
        plt.title('Weight Progress')
        plt.xlabel('Measurement')
        plt.ylabel('Weight')
        plt.grid(True)

        # Save the graph as an image file
        graph_filename = 'progress_graph.png'
        plt.savefig(graph_filename)
        plt.close()

        # Initialize Pygame
        pygame.init()

        # Set the window size
        X, Y = 1000, 1000  # Adjust the window size as needed
        screen = pygame.display.set_mode((X, Y))

        # Load and display the graph image
        graph_image = pygame.image.load(graph_filename)
        graph_rect = graph_image.get_rect(center=(X // 2, Y // 2))
        screen.blit(graph_image, graph_rect)

        # Update the screen
        pygame.display.flip()

    if backTextDisplay == True:
        display_surface.blit(backText, optionText)



    for event in pygame.event.get():

        # TB collide code
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if TBinput_box.collidepoint(event.pos):
                # Toggle the active variable.
                TBactive = not TBactive
                display_surface.blit(testText, textRect2)

                optionsAvailable = False

            # CSV box collide code
            elif TBcsv_box.collidepoint(event.pos):
                TBactive = not TBactive
                display_surface.blit(testText, textRect2)

                optionsAvailable = False

            else:
                TBactive = False

                optionsAvailable = True

            # Change the current color of the input box.
            TBcolor = TBcolor_active if TBactive else TBcolor_inactive


        if event.type == pygame.KEYDOWN:
                if TBactive:
                    if event.key == pygame.K_RETURN:
                        var = "weight.csv"

                        with open(var, "r") as file:
                            reader = csv.reader(file)
                            count = sum(1 for _ in reader)

                        if stage == 0 or stage == 1:
                            print("1:" + var)

                        if stage == 3:
                            if count + 1 <= 7:
                                print('Total lines', count + 1)
                                with open(var, "a", newline="") as file:
                                    writer = csv.writer(file)
                                    writer.writerow([TBtext])

                                print("2:" + var)

                                warning = 0

                            else:
                                warning = 1

                        if stage == 4:
                            print(TBgoal)
                            goal = TBgoal

                        TBtext = ''
                        TBcsv = ''
                        TBgoal = ''

                    elif event.key == pygame.K_BACKSPACE:
                        TBtext = TBtext[:-1]
                        TBcsv = TBcsv[:-1]
                        TBgoal = TBgoal[:1]

                    else:
                        TBtext += event.unicode
                        TBcsv += event.unicode
                        TBgoal += event.unicode

        


        # NON TB CODE BELOW

        if optionsAvailable == True:
            if event.type == KEYDOWN:

                # End code with esc
                if event.key == K_ESCAPE:
                    running = False

                # Return to menu (does not work if you haven't passed the welcome message)
                if stage != 0:
                    backTextDisplay = True

                    if event.key == K_0:
                        stage = 2

                        TBtext = ''
                        TBcsv = ''

                # From menu go to menu
                if stage == 0:
                    if event.key == K_1:
                        stage = 2

                        TBtext = ''
                        TBcsv = ''

                # From menu go to log weight
                if stage == 2:
                    if event.key == K_2:
                        stage = 3

                        TBtext = ''
                        TBcsv = ''

                # From menu go to goal weight
                if stage == 2:
                    if event.key == K_3:
                        stage = 4

                        TBtext = ''
                        TBcsv = ''
                
                if stage == 2:
                    if event.key == K_4:
                        stage = 1

                        TBtext = ''
                        TBcsv = ''

                if stage == 2:
                    if event.key == K_5:
                        stage = 5

                        TBtext = ''
                        TBcsv = ''
                

                # DISPLAY GRAPH CODE
                # if stage == 2:
                #     if event.key == K_5:
                #         stage = 6

                #         TBtext = ''
                #         TBcsv = ''

                # Testing option
                # if event.key == K_4:
                #     stage = 1

                #     TBtext = ''
                #     TBcsv = ''

    

    TBclock.tick(30)    
    pygame.display.flip()    
    
# Don't even need this because hitting escape will just end the code anyways
# pygame.quit()
