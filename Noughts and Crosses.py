import pygame

#Initial Setup
pygame.init()
user_width = pygame.display.Info().current_w
width = user_width//6
height = width+width//10
frame = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic Tac Toe")
icon = pygame.image.load("tictactoe.ico")
x_standard = pygame.image.load("X_standard.png")
o_standard = pygame.image.load("O_standard.png")
vlinecoord = [[x, y] for x in [width // 3, width // 3 * 2] for y in [0, width // 3 * 3]]
hlinecoord = [[x, y] for y in [width // 3, width // 3 * 2] for x in [0, width // 3 * 3]]
linecoord = vlinecoord + hlinecoord
frame.fill((255, 255, 255))
pygame.draw.rect(frame, (192, 192, 192), (0, width, width, height - width))
for i in range(0, 8, 2):
    pygame.draw.line(frame, (0, 0, 0), linecoord[i], linecoord[i + 1])

class NoCGame:
    def __init__(self, width):
        self.width = width
        pass

class Button:
    def __init__(self, type):
        self.type = "NewGame"
    def Draw(self):
        pass

class Board:
    def ClearBoard(self):
        pass
    def InsertX(self, x,y):
        frame.blit(x_standard, (x, y))
        pygame.display.flip()
    def InsertY(self, x,y):
        frame.blit(o_standard, (x, y))
        pygame.display.flip()
    def Regions(self):
        pass

Game = NoCGame(user_width)
Board = Board()

# Main Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            print(mx, my)
            if mx < 100 and my < 100:
                x, y = mx, my
                #Board.InsertX(x, y)
    pygame.display.update()

pygame.quit()