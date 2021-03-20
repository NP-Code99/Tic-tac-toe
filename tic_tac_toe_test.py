#import pygame
#pygame.init() 
#screen = pygame.display.set_mode((340, 340))

#cool = 'yes'
#if cool == 'yes':
    #print('yes') 
    #cool = 'no'
    
#running = True
#while running:
    #for event in pygame.event.get():
        #if event.type == pygame.QUIT:
            #running = False
        #if event.type == pygame.MOUSEBUTTONDOWN:
            #pygame.draw.rect(screen, (255, 0, 0), (100, 100, 100, 100))
        #screen.fill((0, 0, 0))
    #pygame.display.update()

board_arr = ['X', 'X', 'X', 
            ' ', ' ', ' ', 
            ' ', ' ', ' ']

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
    
print(win_check(board_arr))

