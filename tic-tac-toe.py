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

# Help Screen Text
def instructions(y): # Continue to format the paragraph 
    regular = pygame.font.Font(r'C:\WINDOWS\Fonts\TIMES.TTF', 14)
    help_screen_txt = '''Tic-tac-toe, noughts and crosses, or Xs and Os/“X’y O’sies”, |is a paper-and-pencil game for two players, |X and O, who take turns marking the |spaces in a 3×3 grid. |The player who succeeds in placing |three of their marks in a |diagonal, horizontal, or vertical row is the winner.'''
    for item in help_screen_txt.split('|'):
        y += 20
        screen.blit(regular.render(item, True, lime), (10, y))

# Board
board = pygame.image.load(r'C:\Users\Admin\OneDrive\Desktop\All Python Projects\Tic-tac-toe\All Images\ultimate-tic-tac-toe12-01.png')

# Marks
x_mark = pygame.image.load(r'C:\Users\Admin\OneDrive\Desktop\All Python Projects\Tic-tac-toe\All Images\close.png')

dodger_blue = (0, 0, 205)
white = (255, 255, 255)

# Tic_tac_toe Screen
def tic_tac_toe():
    game_running = True
    while game_running: 
        screen.fill(white)
        screen.blit(board, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
        pygame.display.update()


# Help Screen
def help_screen():
    help_running = True
    while help_running: 
        screen.fill(dodger_blue)
        instructions(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                help_running = False
        pygame.display.update()

# Main Menu Screen
def main_menu():
    main_running = True
    button_y = 120
    while main_running:
        # Background Color
        screen.fill((0, 0, 205))
        # Title
        screen.blit(title, (73, 20))
        # Rectangle Buttons
        game_button(69, button_y, 200, 50)
        help_button(69, button_y + 70, 200, 50)
        # Circle Button
        settings_button(37, 305, 30)
        # Events / Actions
        mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                main_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_pos_x >= 69 and mouse_pos_x <= 270 and mouse_pos_y >= 189 and mouse_pos_y <= 239:
                    main_running = False
                    help_screen()
        pygame.display.update()

main_menu()



