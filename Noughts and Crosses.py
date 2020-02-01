#Necessary modules
import pygame

#Pygame initialization
pygame.init()
user_width = pygame.display.Info().current_w
width, height = user_width//6, width+width//10
frame = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic Tac Toe")
icon = pygame.image.load("tictactoe.ico")

#Images
x_standard = pygame.image.load("X_standard.png")
o_standard = pygame.image.load("O_standard.png")
pygame.display.set_icon(icon)

#Variables and functions
running = True
vlinecoord = [[x,y] for x in [width//3, width//3*2] for y in [0, width//3*3]]
hlinecoord = [[x,y] for x in [0, width//3*3] for y in [width//3, width//3*2]]

def empty_board():
    frame.fill((255, 255, 255))
    pygame.draw.rect(frame, (192, 192, 192), (0, width, width, height - width))
    pygame.draw.line(frame, (0,0,0), vlinecoord[0], vlinecoord[1])
    pygame.draw.line(frame, (0,0,0), vlinecoord[2], vlinecoord[3])
    pygame.draw.line(frame, (0,0,0), hlinecoord[0], hlinecoord[2])
    pygame.draw.line(frame, (0,0,0), hlinecoord[1], hlinecoord[3])
empty_board()

#Main Loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            print(mx,my)
           # frame.blit(x_standard, (150,150))
           # pygame.display.flip()
    pygame.display.update()

pygame.quit()