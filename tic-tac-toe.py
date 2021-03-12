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

# Main Menu Music
pygame.mixer.music.load(r"C:\Users\Admin\Downloads\19th Floor - Bobby Richards.mp3")
pygame.mixer.music.play(-1)

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
<<<<<<< Updated upstream
                running = False
=======
                game_running = False
        pygame.display.update()

# Help Screen
def help_screen():
    help_running = True
    while help_running: 
        screen.fill(dodger_blue)
        screen.blit(youtube_star_title.render('Instructions', True, lime), (74, 20))
        instructions_text(70)
        back_button(10, 278, 100, 50)gg
        mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                help_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                help_running = False
                if mouse_pos_x >= 10 and mouse_pos_x <= 109 and mouse_pos_y >= 277 and mouse_pos_y <= 328:
                    main_menu()
        pygame.display.update()

# Settings Screen
def settings_screen():
    settings_running = True
    while settings_running:
        screen.fill(dodger_blue)
        back_button(10, 278, 100, 50)
        mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                settings_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                settings_running = False
                if mouse_pos_x >= 10 and mouse_pos_x <= 109 and mouse_pos_y >= 277 and mouse_pos_y <= 328:
                    main_menu()
>>>>>>> Stashed changes
        pygame.display.update()

def main_menu(): # Create a Main Menu
    running = True
    button_y = 120
    while running:
        # Background Color
        screen.fill((0,0,205))
        # Title
        screen.blit(title, (73, 20))
        # Rectangle Buttons
        game_button(69, button_y, 200, 50)
        help_button(69, button_y + 70, 200, 50)
        # Circle Button
        settings_button(37, 305, 30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos) # Don't forget to change this
        pygame.display.update()

main_menu()



