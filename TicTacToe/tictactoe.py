# Tic Tac Toe game using PyGame
# First PyGame self attempt
#  SUCCESS!!!

# BUGS
# Text Rendering may be a bit Buggy
# No Tie Indicator
# Game Crashes when clicking outside of grid

import pygame
import pygame.freetype
import pygame.font
from pygame.locals import *


# General Setup
pygame.init()
clock = pygame.time.Clock()



# Setting Main Window
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Tic-Tac-Toe')

# Rectangles
again_rect = Rect(screen_width//2-110, screen_height//2+10, 230, 45)

# Colors
background = (0,255,255)
pink = (255,192,203)
red = (255,0,255)
black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
blue = (0,0,255)

# Variables
markers = []
clicked = False
pos = []
player = 1
winner = 0
game_over = False
for i in range(3):
    row = [0] * 3
    markers.append(row)



# Functions
def set_text(string, size):
    global textrect
    global font
    font = pygame.font.Font(pygame.font.get_default_font(), size)
    text = font.render(string, True, black)
    textrect = text.get_rect()
    textrect.center = (screen_width//2, 50)
    return (text, textrect)

def draw_grid():
    for x in range(0, 4):
        pygame.draw.line(screen, black, (100, x*100+100), (screen_width-100, x*100+100), 4)
        pygame.draw.line(screen, black, (x*100+100, 100), (x*100+100, screen_height-100), 4)

def draw_markers():
    x_pos = 1
    for x in markers:
        y_pos = 1
        for y in x:
            if y == 1:
                pygame.draw.line(screen, white, (x_pos*100+15, y_pos*100+15), (x_pos*100+85, y_pos*100+85), 4)
                pygame.draw.line(screen, white, (x_pos*100+15, y_pos*100+85), (x_pos*100+85, y_pos*100+15), 4)
            if y == -1:
                pygame.draw.circle(screen, red, (x_pos*100+50, y_pos*100+50), 30, 4)
            y_pos += 1
        x_pos += 1

def check_winner():
    global winner
    global game_over

    y_pos = 0
    for x in markers:
        # Check Columns
        if sum(x) == 3:
            winner = 1
            game_over = True
        if sum(x) == -3:
            winner = 2
            game_over = True
        # Check Rows
        if markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == 3:
            winner = 1
            game_over = True
        if markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == -3:
            winner = 2
            game_over = True
        y_pos += 1

    # Check Cross
    if markers[0][0] + markers[1][1] + markers[2][2] == 3 or markers[2][0] + markers[1][1] + markers[0][2] == 3:
        winner = 1
        game_over = True
    if markers[0][0] + markers[1][1] + markers[2][2] == -3 or markers[2][0] + markers[1][1] + markers[0][2] == -3:
        winner = 2
        game_over = True


def draw_winner():
    win = "Player " + str(winner) +  " Wins!"
    win_text = set_text(win, 40)
    textrect.center = (screen_width//2+4, screen_height//2-10)
    pygame.draw.rect(screen, green, textrect)
    screen.blit(win_text[0], (screen_width//2-135, screen_height//2-30))

    again_text = 'Play Again?'
    again_img = font.render(again_text, True, white)
    pygame.draw.rect(screen, blue, again_rect)
    screen.blit(again_img, (screen_width//2-110, screen_height//2 +10))





# Loop runs the Game
run = True
while run:
    # Visuals
    totaltext = set_text("Tic Tac Toe", 60)
    screen.fill(background)
    pygame.draw.rect(screen, background, textrect)
    screen.blit(totaltext[0], totaltext[1])
    draw_grid()
    draw_markers()

    # Handling Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if game_over == 0:
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False
                pos = pygame.mouse.get_pos()
                cell_x = pos[0]
                cell_y = pos[1]
                if markers[(cell_x // 100)-1][(cell_y // 100)-1] == 0:
                    markers[(cell_x // 100)-1][(cell_y // 100)-1] = player
                    player *= -1
                    check_winner()

    if game_over == True:
        draw_winner()
        # Check Mouse Click for Play Again
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            clicked = False
            pos = pygame.mouse.get_pos()
            if again_rect.collidepoint(pos):
                # Reset Variables
                markers = []
                pos = []
                player = 1
                winner = 0
                game_over = False
                for i in range(3):
                    row = [0] * 3
                    markers.append(row)

            

    


    # Updating the Window
    pygame.display.flip()
    clock.tick()