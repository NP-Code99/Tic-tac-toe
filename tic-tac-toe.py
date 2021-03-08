import pygame
pygame.init()

# Basic Screen Stuff
screen = pygame.display.set_mode((340, 340))
pygame.display.set_caption('Tic-tac-toe')
icon = pygame.image.load(r'C:\Users\Admin\OneDrive\Desktop\All Python Projects\Tic-Tac-Toe Project\All Images\tic-tac-toe.png')
pygame.display.set_icon(icon)

# Board
board = pygame.image.load(r'C:\Users\Admin\OneDrive\Desktop\All Python Projects\Tic-Tac-Toe Project\All Images\ultimate-tic-tac-toe12-01.png')

# Marks
x_mark = pygame.image.load(r'C:\Users\Admin\OneDrive\Desktop\All Python Projects\Tic-Tac-Toe Project\All Images\close.png')
state = 'notready'
def x (pos):
    x_mark = pygame.image.load(r'C:\Users\Admin\OneDrive\Desktop\All Python Projects\Tic-Tac-Toe Project\All Images\close.png')
    global state
    state = 'ready'
    screen.blit(x_mark, (pos))

running = True
while running: 
    screen.fill((255, 255, 255))
    screen.blit(board, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            x(position)
    if state == 'ready': # Try to put the position of the mouse here
        x(position)
    pygame.display.update()


