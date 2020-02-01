#Necessary modules
import pygame

#Pygame initialization
pygame.init()
user_width, user_height = pygame.display.Info().current_w, pygame.display.Info().current_h
width, height = 300, 350
frame = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic Tac Toe")
icon = pygame.image.load("tictactoe.ico")
frame.fill((0, 0, 5))
pygame.draw.rect(frame, (192, 192, 192), (0,300, 300, 50))

#Images
x_standard = pygame.image.load("X_standard.png")
o_standard = pygame.image.load("O_standard.png")
pygame.display.set_icon(icon)

#Variables and functions
running = True
coord = [[i,j] for i in [0, 101, 201] for j in [0, 101, 201]]

def empty_board():
    for c in coord:
        pygame.draw.rect(frame, (255, 255, 255), (c[0], c[1], 99, 99))
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