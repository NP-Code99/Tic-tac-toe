import pygame
import sys
pygame.init()

# Basic Screen Stuff
screen = pygame.display.set_mode((340, 340))
pygame.display.set_caption('Tic-tac-toe')
icon = pygame.image.load(r'C:\Users\Admin\OneDrive\Desktop\All Python Projects\Tic-tac-toe\All Images\tic-tac-toe.png')
pygame.display.set_icon(icon)

# Main Menu Title
purpleish = (102, 102, 255)
lime = (0, 255, 0)
title_font = pygame.font.Font(r'C:\WINDOWS\Fonts\IMPACT.TTF', 40)
cartoony_font = pygame.font.Font(r'C:\WINDOWS\Fonts\IMPACT.TTF', 30)
settings_button_font = pygame.font.Font(r'C:\WINDOWS\Fonts\IMPACT.TTF', 15)
title = title_font.render('Tic-Tac-Toe', True, lime)

# Main menu buttons
def game_button(x, y, length, width): 
    game_button = (x, y, length, width) # 70, 60, 200, 50
    game_button_text = cartoony_font.render('Play Game', True, lime)
    pygame.draw.rect(screen, purpleish, game_button)
    screen.blit(game_button_text, (x + 38, y + 5))

def help_button(x, y, length, width):
    help_button = (x, y, length, width) 
    help_button_text = cartoony_font.render('Help', True, lime)
    pygame.draw.rect(screen, purpleish, help_button)
    screen.blit(help_button_text, (x + 69, y + 5))

def settings_button(x, y, radius):
    settings_button_text = settings_button_font.render('Settings', True, lime)
    pygame.draw.circle(screen, purpleish, (x, y), radius) # 27, 305, 30
    screen.blit(settings_button_text, (x - 25, y - 10))

# Board
board = pygame.image.load(r'C:\Users\Admin\OneDrive\Desktop\All Python Projects\Tic-tac-toe\All Images\ultimate-tic-tac-toe12-01.png')

# Marks
x_mark = pygame.image.load(r'C:\Users\Admin\OneDrive\Desktop\All Python Projects\Tic-tac-toe\All Images\close.png')

def tic_tac_toe():
    running = True
    while running: 
        screen.fill((255, 255, 255))
        screen.blit(board, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()

def main_menu(): # Create a Main Menu
    running = True
    button_y = 120
    while running:
        screen.fill((0,0,205))
        screen.blit(title, (73, 20))
        game_button(69, button_y, 200, 50)
        help_button(69, button_y + 70, 200, 50)
        settings_button(37, 305, 30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
        pygame.display.update()

main_menu()



