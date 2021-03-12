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

# Buttons
button_length = 200
button_width = 50
def game_button(x, y, length, width): 
    purpleish = (102, 102, 255)
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

def back_button(x, y, length, width):
    back_button = (x, y, length, width) 
    back_button_text = cartoony_font.render('Back', True, lime)
    pygame.draw.rect(screen, purpleish, back_button)
    screen.blit(back_button_text, (x + 18, y + 6))

# Instructions Text
youtube_star_title = pygame.font.SysFont('youtube star', 40)
youtube_star_title.set_bold(True)
youtube_star_text = pygame.font.SysFont('youtube star', 18)
def instructions_text(y): # Continue to format the paragraph 
    help_screen_txt = '''1. The game is played on a grid that's 3 squares by 3 |squares. |2. You are X, your friend (or the computer in this |case) is O. Players take turns putting their marks in |empty squares. |3. The first player to get 3 of her marks in a row |(up, down, across, or diagonally) is the winner. |4. When all 9 squares are full, the game is over. |If no player has 3 marks in a row, the game ends in a tie.'''
    for item in help_screen_txt.split('|'):
        y += 20
        screen.blit(youtube_star_text.render(item, True, lime), (10, y))

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
        screen.blit(youtube_star_title.render('Instructions', True, lime), (74, 20))
        instructions_text(70)
        back_button(10, 278, 100, 50)
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
        pygame.display.update()

# Main Menu Screen
def main_menu():
    main_running = True
    button_y = 120
    cursor = pygame.cursors.compile(pygame.cursors.textmarker_strings)
    while main_running:
        # Background Color
        screen.fill((0, 0, 205))
        # Title
        screen.blit(title, (73, 20))
        # Rectangle Buttons
        game_button(69, button_y, button_length, button_width)
        help_button(69, button_y + 70, button_length, button_width)
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
                if mouse_pos_x >= 7 and mouse_pos_x <= 66 and mouse_pos_y >= 275 and mouse_pos_y <= 335:
                    main_running = False
                    settings_screen()
        pygame.display.update()

main_menu()



