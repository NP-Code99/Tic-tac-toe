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
def game_button(x, y, length, width, color): 
    purpleish = (102, 102, 255)
    game_button = (x, y, length, width) # 70, 60, 200, 50
    game_button_text = cartoony_font.render('Play Game', True, lime)
    pygame.draw.rect(screen, color, game_button, 0, 10)
    screen.blit(game_button_text, (x + 40, y + 5))

def help_button(x, y, length, width, color):
    purpleish1 = (102, 102, 255)
    help_button = (x, y, length, width) 
    help_button_text = cartoony_font.render('Help', True, lime)
    pygame.draw.rect(screen, color, help_button, 0, 10)
    screen.blit(help_button_text, (x + 69, y + 5))

def settings_button(x, y, radius, color):
    settings_button_text = settings_button_font.render('Settings', True, lime)
    pygame.draw.circle(screen, color, (x, y), radius) # 27, 305, 30
    screen.blit(settings_button_text, (x - 25, y - 10))

def back_button(x, y, length, width, color):
    back_button = (x, y, length, width) 
    back_button_text = cartoony_font.render('Back', True, lime)
    pygame.draw.rect(screen, color, back_button, 0, 10)
    screen.blit(back_button_text, (x + 18, y + 6))


def quit_button(x, y, length, width, color):
    quit_button = (x, y, length, width)
    quit_button_text = pygame.font.Font(r'C:\WINDOWS\Fonts\IMPACT.TTF', 20).render('Quit Game', True, lime)
    pygame.draw.rect(screen, color, quit_button, 0, 10)
    screen.blit(quit_button_text, (14, 303))

# Instructions Text
youtube_star_title = pygame.font.SysFont('youtube star', 40)
youtube_star_title.set_bold(True)
youtube_star_text = pygame.font.SysFont('youtube star', 18)
def instructions_text(y): # Continue to format the paragraph 
    help_screen_txt = '''1. The game is played on a grid that's 3 squares by 3 |squares. |2. You are X, your friend (or the computer in this |case) is O. Players take turns putting their marks in |empty squares. |3. The first player to get 3 of her marks in a row |(up, down, across, or diagonally) is the winner. |4. When all 9 squares are full, the game is over. |If no player has 3 marks in a row, the game ends in a tie.'''
    for item in help_screen_txt.split('|'):
        y += 20
        screen.blit(youtube_star_text.render(item, True, lime), (10, y))

def tic_tac_toe_line(start_pos_x, start_pos_y, end_pos_x, end_pos_y):
    pygame.draw.line(screen, (0, 0, 0), (start_pos_x, start_pos_y), (end_pos_x, end_pos_y), 8)

dodger_blue = (0, 0, 205)
white = (255, 255, 255) 

def tic_tac_toe_board():
    pygame.draw.rect(screen, dodger_blue, (0, 0, 340, 80))
    # Vertical Lines
    tic_tac_toe_line(340 * 1/3, 80, 340 * 1/3, 340)
    tic_tac_toe_line(340 * 2/3, 80, 340 * 2/3, 340)
    # Horizontal Lines
    tic_tac_toe_line(0, (260 * 1/3) + 80 , 340, (260 * 1/3) + 80 )
    tic_tac_toe_line(0, (260 * 2/3) + 80 , 340, (260 * 2/3) + 80 )

# Tic_tac_toe Screen
def tic_tac_toe():
    game_running = True
    quit_button_changeable_color = (102, 102, 255)
    tic_state = pygame.font.Font(r'C:\WINDOWS\Fonts\IMPACT.TTF', 20).render('Welcome to Tic-Tac-Toe', True, lime)
    mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
    x_state = 'not ready'
    while game_running: 
        screen.fill(white)
        # Tic-Tac-Toe Board
        tic_tac_toe_board()
        screen.blit(tic_state, (80, 25))
        #quit_button(10, 300, 93, 33, quit_button_changeable_color) Use quit button later if you need it 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                #print(pygame.mouse.get_pos())
                if mouse_pos_x <= 108: # Fix the position here (108 not working)
                    print(x_state)
        pygame.display.update()

# Help Screen
def help_screen():
    help_running = True
    back_button_changeable_color = (102, 102, 255)
    while help_running: 
        screen.fill(dodger_blue)
        screen.blit(youtube_star_title.render('Instructions', True, lime), (74, 20))
        instructions_text(70)
        back_button(10, 278, 100, 50, back_button_changeable_color)
        mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                help_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_pos_x >= 10 and mouse_pos_x <= 109 and mouse_pos_y >= 277 and mouse_pos_y <= 328:
                    help_running = False
                    main_menu()
        # Back Button Color Changing
        if mouse_pos_x >= 10 and mouse_pos_x <= 109 and mouse_pos_y >= 277 and mouse_pos_y <= 328:
            back_button_changeable_color =  (65, 105, 225)
        else: 
            back_button_changeable_color = (102, 102, 255)
        pygame.display.update()

# Settings Screen
def settings_screen():
    settings_running = True
    back_button_changeable_color = (102, 102, 255)
    while settings_running:
        screen.fill(dodger_blue)
        screen.blit(youtube_star_title.render('Settings', True, lime), (106, 20))
        screen.blit(pygame.font.SysFont('youtube star', 22).render('Theme', True, lime), (80,100))
        back_button(10, 278, 100, 50, back_button_changeable_color)
        mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                settings_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_pos_x >= 10 and mouse_pos_x <= 109 and mouse_pos_y >= 277 and mouse_pos_y <= 328:
                    settings_running = False
                    main_menu()
        # Back Button Color Changing
        if mouse_pos_x >= 10 and mouse_pos_x <= 109 and mouse_pos_y >= 277 and mouse_pos_y <= 328:
            back_button_changeable_color = (65, 105, 225)
        else: 
            back_button_changeable_color = (102, 102, 255)
        pygame.display.update()

# Main Menu Screen
def main_menu():
    game_button_changeable_color = (102, 102, 255)
    help_button_changeable_color = (102, 102, 255)
    settings_button_changeable_color = (102, 102, 255)
    main_running = True
    button_y = 120
    cursor = pygame.cursors.compile(pygame.cursors.textmarker_strings)
    while main_running:
        # Background Color
        screen.fill((0, 0, 205))
        # Title
        screen.blit(title, (77, 20))
        # Rectangle Buttons
        game_button(69, button_y, button_length, button_width, game_button_changeable_color)
        help_button(69, button_y + 70, button_length, button_width, help_button_changeable_color)
        # Circle Button
        settings_button(37, 305, 30, settings_button_changeable_color)
        # Events / Actions
        mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                main_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_pos_x >= 69 and mouse_pos_x <= 270 and mouse_pos_y >= 119 and mouse_pos_y <= 169:
                    main_running = False
                    tic_tac_toe()
                if mouse_pos_x >= 69 and mouse_pos_x <= 270 and mouse_pos_y >= 189 and mouse_pos_y <= 239:
                    main_running = False
                    help_screen()
                if mouse_pos_x >= 7 and mouse_pos_x <= 66 and mouse_pos_y >= 275 and mouse_pos_y <= 335:
                    main_running = False
                    settings_screen()
        # Game Button Color Changing
        if mouse_pos_x >= 69 and mouse_pos_x <= 270 and mouse_pos_y >= 119 and mouse_pos_y <= 169:
            game_button_changeable_color = (65, 105, 225)
        else:
            game_button_changeable_color = (102, 102, 255)
        # Help Button Color Changing
        if mouse_pos_x >= 69 and mouse_pos_x <= 270 and mouse_pos_y >= 189 and mouse_pos_y <= 239:
            help_button_changeable_color = (65, 105, 225)
        else:
            help_button_changeable_color = (102, 102, 255)
        # Settings Button Color Changing
        if mouse_pos_x >= 7 and mouse_pos_x <= 66 and mouse_pos_y >= 275 and mouse_pos_y <= 335:
            settings_button_changeable_color = (65, 105, 225)
        else:
            settings_button_changeable_color = (102, 102, 255)
        pygame.display.update()

main_menu()



