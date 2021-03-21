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
pygame.mixer.music.load(r"C:\Users\Admin\OneDrive\Desktop\All Python Projects\Tic-tac-toe\Sounds\19th Floor - Bobby Richards (1).mp3")
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
    quit_button_text = pygame.font.Font(r'C:\WINDOWS\Fonts\IMPACT.TTF', 20).render('Replay', True, lime)
    pygame.draw.rect(screen, color, quit_button)
    screen.blit(quit_button_text, (27, 303))

def theme_dropdown(x, y, length, width, color):
    theme_dropdown = (x, y, length, width) 
    theme_dropdown_text = pygame.font.SysFont('impact', 20).render('Select Theme', True, lime)
    pygame.draw.rect(screen, color, theme_dropdown, 0, 8)
    screen.blit(theme_dropdown_text, (x + 5, y + 2))

def theme_color_buttons(x, y, length, width, color, colortype):
    theme_color_buttons = (x, y, length, width) 
    theme_color_buttons_text = pygame.font.SysFont('youtube star', 20).render(colortype, True, (0, 0, 0))
    pygame.draw.rect(screen, color, theme_color_buttons, 0, 8)
    if colortype == 'Red':
        screen.blit(theme_color_buttons_text, (x + 45, y + 8))
    elif colortype == 'Purple' or colortype == 'Orange':
        screen.blit(theme_color_buttons_text, (x + 40, y + 8))
    else:
        screen.blit(theme_color_buttons_text, (x + 20, y + 8) )

screen_theme = (0, 0, 205)
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

white = (255, 255, 255) 

def tic_tac_toe_board():
    pygame.draw.rect(screen, screen_theme, (0, 0, 340, 80))
    # Vertical Lines
    tic_tac_toe_line(340 * 1/3, 80, 340 * 1/3, 340)
    tic_tac_toe_line(340 * 2/3, 80, 340 * 2/3, 340)
    # Horizontal Lines
    tic_tac_toe_line(0, (260 * 1/3) + 80 , 340, (260 * 1/3) + 80 )
    tic_tac_toe_line(0, (260 * 2/3) + 80 , 340, (260 * 2/3) + 80 )

def o_image(x, y):
    pygame.draw.circle(screen, (0, 0, 0), (x, y), 35, 10) #45, 120

def x_image(x, y):
    pygame.draw.line(screen, (0, 0, 0), (x, y), (x + 50, y + 50), 10) #(27, 95), (77, 145)
    pygame.draw.line(screen, (0, 0, 0), (x + 50, y), (x + 2, y + 50), 10) #(77, 95), (29, 145)

# State Variables
x_image_state1 = 'not ready'
x_image_state2 = 'not ready'
x_image_state3 = 'not ready'
x_image_state4 = 'not ready'
x_image_state5 = 'not ready'
x_image_state6 = 'not ready'
x_image_state7 = 'not ready'
x_image_state8 = 'not ready'
x_image_state9 = 'not ready'
o_image_state1 = 'not ready'
o_image_state2 = 'not ready'
o_image_state3 = 'not ready'
o_image_state4 = 'not ready'
o_image_state5 = 'not ready'
o_image_state6 = 'not ready'
o_image_state7 = 'not ready'
o_image_state8 = 'not ready'
o_image_state9 = 'not ready'

board_arr = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

def win_check(array):
    if array[0] == 'X' and array[1] == 'X' and array[2] == 'X':
        return 'X Won'
    elif array[3] == 'X' and array[4] == 'X' and array[5] == 'X':
        return 'X Won'
    elif array[6] == 'X' and array[7] == 'X' and array[8] == 'X':
        return 'X Won'
    elif array[0] == 'X' and array[3] == 'X' and array[6] == 'X':
        return 'X Won'
    elif array[1] == 'X' and array[4] == 'X' and array[7] == 'X':
        return 'X Won'
    elif array[2] == 'X' and array[5] == 'X' and array[8] == 'X':
        return 'X Won'
    elif array[2] == 'X' and array[4] == 'X' and array[6] == 'X':
        return 'X Won'
    elif array[0] == 'X' and array[4] == 'X' and array[8] == 'X':
        return 'X Won'
    
    if array[0] == 'O' and array[1] == 'O' and array[2] == 'O':
        return 'O Won'
    elif array[3] == 'O' and array[4] == 'O' and array[5] == 'O':
        return 'O Won'
    elif array[6] == 'O' and array[7] == 'O' and array[8] == 'O':
        return 'O Won'
    elif array[0] == 'O' and array[3] == 'O' and array[6] == 'O':
        return 'O Won'
    elif array[1] == 'O' and array[4] == 'O' and array[7] == 'O':
        return 'O Won'
    elif array[2] == 'O' and array[5] == 'O' and array[8] == 'O':
        return 'O Won'
    elif array[2] == 'O' and array[4] == 'O' and array[6] == 'O':
        return 'O Won'
    elif array[0] == 'O' and array[4] == 'O' and array[8] == 'O':
        return 'O Won'

winning = ''
# Tic_tac_toe Screen
def tic_tac_toe():
    game_running = True
    tic_state = pygame.font.Font(r'C:\WINDOWS\Fonts\IMPACT.TTF', 20).render("It's X's Turn", True, lime)
    tic_num = 0
    # Globalizing all the state variables
    global x_image_state1, x_image_state2, x_image_state3, x_image_state4
    global x_image_state5, x_image_state6, x_image_state7, x_image_state8, x_image_state9
    global o_image_state1, o_image_state2, o_image_state3, o_image_state4
    global o_image_state5, o_image_state6, o_image_state7, o_image_state8, o_image_state9
    global board_arr
    global winning
    while game_running: 
        mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
        screen.fill(white)
        # Tic-Tac-Toe Board
        tic_tac_toe_board()
        screen.blit(tic_state, (124, 25))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            # Mouse Button Event for Player X
            if event.type == pygame.MOUSEBUTTONDOWN and tic_num % 2 == 0:
                # All positions for each box
                if mouse_pos_x >= 0 and mouse_pos_x <= 111 and mouse_pos_y >= 79 and mouse_pos_y <= 163 and board_arr[0] == ' ':
                    tic_state = pygame.font.Font(r'C:\WINDOWS\Fonts\IMPACT.TTF', 20).render("It's O's Turn", True, lime) 
                    tic_num += 1
                    occupied = True
                    x_image_state1 = 'ready'
                elif mouse_pos_x >= 119 and mouse_pos_x <= 223 and mouse_pos_y >= 79 and mouse_pos_y <= 163 and board_arr[1] == ' ':
                    tic_state = pygame.font.Font(r'C:\WINDOWS\Fonts\IMPACT.TTF', 20).render("It's O's Turn", True, lime)
                    tic_num += 1
                    x_image_state2 = 'ready'
                elif mouse_pos_x >= 230 and mouse_pos_x <= 339 and mouse_pos_y >= 79 and mouse_pos_y <= 163 and board_arr[2] == ' ':
                    tic_state = pygame.font.Font(r'C:\WINDOWS\Fonts\IMPACT.TTF', 20).render("It's O's Turn", True, lime)
                    tic_num += 1
                    x_image_state3 = 'ready'
                elif mouse_pos_x >= 0 and mouse_pos_x <= 111 and mouse_pos_y >= 170 and mouse_pos_y <= 248 and board_arr[3] == ' ': 
                    tic_state = pygame.font.Font(r'C:\WINDOWS\Fonts\IMPACT.TTF', 20).render("It's O's Turn", True, lime)
                    tic_num += 1
                    x_image_state4 = 'ready'
                elif mouse_pos_x >= 119 and mouse_pos_x <= 223 and mouse_pos_y >= 170 and mouse_pos_y <= 248 and board_arr[4] == ' ':
                    tic_state = pygame.font.Font(r'C:\WINDOWS\Fonts\IMPACT.TTF', 20).render("It's O's Turn", True, lime)
                    tic_num += 1
                    x_image_state5 = 'ready'
                elif mouse_pos_x >= 230 and mouse_pos_x <= 339 and mouse_pos_y >= 170 and mouse_pos_y <= 248 and board_arr[5] == ' ':
                    tic_state = pygame.font.Font(r'C:\WINDOWS\Fonts\IMPACT.TTF', 20).render("It's O's Turn", True, lime)
                    tic_num += 1
                    x_image_state6 = 'ready'
                elif mouse_pos_x >= 0 and mouse_pos_x <= 111 and mouse_pos_y >= 258 and mouse_pos_y <= 339 and board_arr[6] == ' ':
                    tic_state = pygame.font.Font(r'C:\WINDOWS\Fonts\IMPACT.TTF', 20).render("It's O's Turn", True, lime)
                    tic_num += 1
                    x_image_state7 = 'ready'
                elif mouse_pos_x >= 119 and mouse_pos_x <= 223 and mouse_pos_y >= 258 and mouse_pos_y <= 339 and board_arr[7] == ' ':
                    tic_state = pygame.font.Font(r'C:\WINDOWS\Fonts\IMPACT.TTF', 20).render("It's O's Turn", True, lime)
                    tic_num += 1
                    x_image_state8 = 'ready'
                elif mouse_pos_x >= 230 and mouse_pos_x <= 339 and mouse_pos_y >= 258 and mouse_pos_y <= 339 and board_arr[8] == ' ':
                    tic_state = pygame.font.Font(r'C:\WINDOWS\Fonts\IMPACT.TTF', 20).render("It's O's Turn", True, lime)
                    tic_num += 1
                    x_image_state9 = 'ready'
            # Mouse Button Event for Player O
            elif event.type == pygame.MOUSEBUTTONDOWN and tic_num % 2 == 1:
                # All positions for each box
                if mouse_pos_x >= 0 and mouse_pos_x <= 111 and mouse_pos_y >= 79 and mouse_pos_y <= 163 and board_arr[0] == ' ': # This will make sure you can't click on it after occupied 
                    tic_state = pygame.font.Font(r'C:\WINDOWS\Fonts\IMPACT.TTF', 20).render("It's X's Turn", True, lime)
                    tic_num += 1
                    o_image_state1 = 'ready'
                elif mouse_pos_x >= 119 and mouse_pos_x <= 223 and mouse_pos_y >= 79 and mouse_pos_y <= 163 and board_arr[1] == ' ':
                    tic_state = pygame.font.Font(r'C:\WINDOWS\Fonts\IMPACT.TTF', 20).render("It's X's Turn", True, lime)
                    tic_num += 1
                    o_image_state2 = 'ready'
                elif mouse_pos_x >= 230 and mouse_pos_x <= 339 and mouse_pos_y >= 79 and mouse_pos_y <= 163 and board_arr[2] == ' ':
                    tic_state = pygame.font.Font(r'C:\WINDOWS\Fonts\IMPACT.TTF', 20).render("It's X's Turn", True, lime)
                    tic_num += 1
                    o_image_state3 = 'ready'
                elif mouse_pos_x >= 0 and mouse_pos_x <= 111 and mouse_pos_y >= 170 and mouse_pos_y <= 248 and board_arr[3] == ' ': 
                    tic_state = pygame.font.Font(r'C:\WINDOWS\Fonts\IMPACT.TTF', 20).render("It's X's Turn", True, lime)
                    tic_num += 1
                    o_image_state4 = 'ready'
                elif mouse_pos_x >= 119 and mouse_pos_x <= 223 and mouse_pos_y >= 170 and mouse_pos_y <= 248 and board_arr[4] == ' ':
                    tic_state = pygame.font.Font(r'C:\WINDOWS\Fonts\IMPACT.TTF', 20).render("It's X's Turn", True, lime)
                    tic_num += 1
                    o_image_state5 = 'ready'
                elif mouse_pos_x >= 230 and mouse_pos_x <= 339 and mouse_pos_y >= 170 and mouse_pos_y <= 248 and board_arr[5] == ' ':
                    tic_state = pygame.font.Font(r'C:\WINDOWS\Fonts\IMPACT.TTF', 20).render("It's X's Turn", True, lime)
                    tic_num += 1
                    o_image_state6 = 'ready'
                elif mouse_pos_x >= 0 and mouse_pos_x <= 111 and mouse_pos_y >= 258 and mouse_pos_y <= 339 and board_arr[6] == ' ':
                    tic_state = pygame.font.Font(r'C:\WINDOWS\Fonts\IMPACT.TTF', 20).render("It's X's Turn", True, lime)
                    tic_num += 1
                    o_image_state7 = 'ready'
                elif mouse_pos_x >= 119 and mouse_pos_x <= 223 and mouse_pos_y >= 258 and mouse_pos_y <= 339 and board_arr[7] == ' ':
                    tic_state = pygame.font.Font(r'C:\WINDOWS\Fonts\IMPACT.TTF', 20).render("It's X's Turn", True, lime)
                    tic_num += 1
                    o_image_state8 = 'ready'
                elif mouse_pos_x >= 230 and mouse_pos_x <= 339 and mouse_pos_y >= 258 and mouse_pos_y <= 339 and board_arr[8] == ' ':
                    tic_state = pygame.font.Font(r'C:\WINDOWS\Fonts\IMPACT.TTF', 20).render("It's X's Turn", True, lime)
                    tic_num += 1
                    o_image_state9 = 'ready'

        # Placing X's or O's
        if x_image_state1 == 'ready' and board_arr[0] == ' ' or board_arr[0] == 'X': # Make sure O and X don't go on the same box
            x_image(27, 95)
            board_arr[0] = 'X'
        if x_image_state2 == 'ready' and board_arr[1] == ' ' or board_arr[1] == 'X':
            x_image(144, 95)
            board_arr[1] = 'X'
        if x_image_state3 == 'ready' and board_arr[2] == ' ' or board_arr[2] == 'X': # Use this method (Make new variable for each)
            x_image(261, 95)
            board_arr[2] = 'X'
        if x_image_state4 == 'ready' and board_arr[3] == ' ' or board_arr[3] == 'X':
            x_image(27, 185)
            board_arr[3] = 'X'
        if x_image_state5 == 'ready' and board_arr[4] == ' ' or board_arr[4] == 'X':
            x_image(144, 185)
            board_arr[4] = 'X'
        if x_image_state6 == 'ready' and board_arr[5] == ' ' or board_arr[5] == 'X':
            x_image(261, 185)
            board_arr[5] = 'X'
        if x_image_state7 == 'ready' and board_arr[6] == ' ' or board_arr[6] == 'X':
            x_image(27, 275)
            board_arr[6] = 'X'
        if x_image_state8 == 'ready' and board_arr[7] == ' ' or board_arr[7] == 'X':
            x_image(144, 275)
            board_arr[7] = 'X'
        if x_image_state9 == 'ready' and board_arr[8] == ' ' or board_arr[8] == 'X':
            x_image(261, 275)
            board_arr[8] = 'X'

        if o_image_state1 == 'ready' and board_arr[0] == ' ' or board_arr[0] == 'O':
            o_image(50, 120)
            board_arr[0] = 'O'
        if o_image_state2 == 'ready' and board_arr[1] == ' ' or board_arr[1] == 'O':
            o_image(170, 120)
            board_arr[1] = 'O'
        if o_image_state3 == 'ready' and board_arr[2] == ' ' or board_arr[2] == 'O':
            o_image(295, 120)
            board_arr[2] = 'O'
        if o_image_state4 == 'ready' and board_arr[3] == ' ' or board_arr[3] == 'O':
            o_image(50, 210)
            board_arr[3] = 'O'
        if o_image_state5 == 'ready' and board_arr[4] == ' ' or board_arr[4] == 'O':
            o_image(170, 210)
            board_arr[4] = 'O'
        if o_image_state6 == 'ready' and board_arr[5] == ' ' or board_arr[5] == 'O':
            o_image(295, 210)
            board_arr[5] = 'O'
        if o_image_state7 == 'ready' and board_arr[6] == ' ' or board_arr[6] == 'O':
            o_image(50, 300)
            board_arr[6] = 'O'
        if o_image_state8 == 'ready' and board_arr[7] == ' ' or board_arr[7] == 'O':
            o_image(170, 300)
            board_arr[7] = 'O'
        if o_image_state9 == 'ready' and board_arr[8] == ' ' or board_arr[8] == 'O':
            o_image(295, 300)
            board_arr[8] = 'O'

        # Win Check
        if win_check(board_arr) == 'X Won':
            x_image_state1 = 'not ready'
            x_image_state2 = 'not ready'
            x_image_state3 = 'not ready'
            x_image_state4 = 'not ready'
            x_image_state5 = 'not ready'
            x_image_state6 = 'not ready'
            x_image_state7 = 'not ready'
            x_image_state8 = 'not ready'
            x_image_state9 = 'not ready'

            o_image_state1 = 'not ready'
            o_image_state2 = 'not ready'
            o_image_state3 = 'not ready'
            o_image_state4 = 'not ready'
            o_image_state5 = 'not ready'
            o_image_state6 = 'not ready'
            o_image_state7 = 'not ready'
            o_image_state8 = 'not ready'
            o_image_state9 = 'not ready'
            board_arr = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            winning = 'X Won'
            winning_screen()
            game_running = False

        elif win_check(board_arr) == 'O Won':
            x_image_state1 = 'not ready'
            x_image_state2 = 'not ready'
            x_image_state3 = 'not ready'
            x_image_state4 = 'not ready'
            x_image_state5 = 'not ready'
            x_image_state6 = 'not ready'
            x_image_state7 = 'not ready'
            x_image_state8 = 'not ready'
            x_image_state9 = 'not ready'

            o_image_state1 = 'not ready'
            o_image_state2 = 'not ready'
            o_image_state3 = 'not ready'
            o_image_state4 = 'not ready'
            o_image_state5 = 'not ready'
            o_image_state6 = 'not ready'
            o_image_state7 = 'not ready'
            o_image_state8 = 'not ready'
            o_image_state9 = 'not ready'
            board_arr = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            winning = 'O Won'
            winning_screen()
            game_running = False
        # Draw Check
        else:
            if ' ' not in board_arr:
                x_image_state1 = 'not ready'
                x_image_state2 = 'not ready'
                x_image_state3 = 'not ready'
                x_image_state4 = 'not ready'
                x_image_state5 = 'not ready'
                x_image_state6 = 'not ready'
                x_image_state7 = 'not ready'
                x_image_state8 = 'not ready'
                x_image_state9 = 'not ready'

                o_image_state1 = 'not ready'
                o_image_state2 = 'not ready'
                o_image_state3 = 'not ready'
                o_image_state4 = 'not ready'
                o_image_state5 = 'not ready'
                o_image_state6 = 'not ready'
                o_image_state7 = 'not ready'
                o_image_state8 = 'not ready'
                o_image_state9 = 'not ready'
                board_arr = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
                draw_screen()
                game_running = False
        pygame.display.update()

def winning_screen():
    winning_running = True
    quit_button_changeable_color = (102, 102, 255)
    global board_arr
    while winning_running:
        screen.fill((255,215,0))
        screen.blit(pygame.font.Font('C:\WINDOWS\Fonts\IMPACT.TTF', 40).render(winning, True, (0, 0, 0)), (120, 130))
        quit_button(10, 300, 93, 33, quit_button_changeable_color)
        mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                winning_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_pos_x >= 11 and mouse_pos_x <= 103 and mouse_pos_y >= 299 and mouse_pos_y <= 330:
                    winning_running = False
                    main_menu()
        pygame.display.update()

def draw_screen():
    draw_running = True
    quit_button_changeable_color = (102, 102, 255)
    while draw_running:
        screen.fill((128,128,128))
        screen.blit(pygame.font.Font('C:\WINDOWS\Fonts\IMPACT.TTF', 40).render('Draw', True, (0, 0, 0)), (120, 130))
        quit_button(10, 300, 93, 33, quit_button_changeable_color)
        mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                winning_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_pos_x >= 11 and mouse_pos_x <= 103 and mouse_pos_y >= 299 and mouse_pos_y <= 330:
                    draw_running = False
                    main_menu()
        pygame.display.update()

# Help Screen
def help_screen():
    help_running = True
    back_button_changeable_color = (102, 102, 255)
    global screen_theme
    while help_running: 
        screen.fill(screen_theme)
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
state = 'not ready'
def settings_screen():
    settings_running = True
    theme_dropdown_changeable_color = (102, 102, 255) 
    back_button_changeable_color = (102, 102, 255)
    global state
    global screen_theme
    while settings_running:
        screen.fill(screen_theme)
        screen.blit(youtube_star_title.render('Settings', True, lime), (106, 20))
        theme_dropdown(60, 90, 120, 30, theme_dropdown_changeable_color)
        back_button(10, 278, 100, 50, back_button_changeable_color)
        mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                settings_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_pos_x >= 10 and mouse_pos_x <= 109 and mouse_pos_y >= 277 and mouse_pos_y <= 328:
                    settings_running = False
                    main_menu()
                elif mouse_pos_x >= 60 and mouse_pos_x <= 159 and mouse_pos_y >= 91 and mouse_pos_y <= 119:
                    state = 'ready'
                elif mouse_pos_x >= 60 and mouse_pos_x <= 180 and mouse_pos_y >= 120 and mouse_pos_y <= 149:
                    screen_theme = (255, 0, 0)
                elif mouse_pos_x >= 59 and mouse_pos_x <= 179 and mouse_pos_y >= 149 and mouse_pos_y <= 178:
                    screen_theme = (255,165,0)
                elif mouse_pos_x >= 61 and mouse_pos_x <= 178 and mouse_pos_y >= 179 and mouse_pos_y <= 208:
                    screen_theme = (147,112,219)
                elif mouse_pos_x >= 60 and mouse_pos_x <= 180 and mouse_pos_y >= 210 and mouse_pos_y <= 238:
                    screen_theme = (0, 0, 205)
                else: 
                    state = 'not ready'
        # Back Button Color Changing
        if mouse_pos_x >= 10 and mouse_pos_x <= 109 and mouse_pos_y >= 277 and mouse_pos_y <= 328:
            back_button_changeable_color = (65, 105, 225)
        else: 
            back_button_changeable_color = (102, 102, 255)

        # Theme Button Color Changing 
        if mouse_pos_x >= 60 and mouse_pos_x <= 159 and mouse_pos_y >= 91 and mouse_pos_y <= 119:
            theme_dropdown_changeable_color = (65, 105, 225)
        else:
            theme_dropdown_changeable_color = (102, 102, 255) 
        
        # Theme DropDown Buttons
        if state == 'ready':
            theme_color_buttons(60, 120, 120, 30, (255, 0, 0), 'Red')
            theme_color_buttons(60, 150, 120, 30, (255,165,0), 'Orange')
            theme_color_buttons(60, 180, 120, 30, (147,112,219), 'Purple')
            theme_color_buttons(60, 210, 120, 30, (0, 0, 205), 'Dodger Blue')
        pygame.display.update()

# Main Menu Screen
def main_menu():
    game_button_changeable_color = (102, 102, 255)
    help_button_changeable_color = (102, 102, 255)
    settings_button_changeable_color = (102, 102, 255)
    main_running = True
    button_y = 120
    cursor = pygame.cursors.compile(pygame.cursors.textmarker_strings)
    global screen_theme
    while main_running:
        # Background Color
        screen.fill(screen_theme)
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

if __name__ == "__main__":
    main_menu()



