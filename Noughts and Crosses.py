import pygame
import tkinter

#Initial Setup
pygame.init()
user_width = pygame.display.Info().current_w

class Button:
    def __init__(self, type, frame, width):
        if type == "newgame":
            image = pygame.image.load("newgame.png")
            image = pygame.transform.scale(image, (width//2, width//10))
            frame.blit(image, (0, width))
            self.rect = pygame.Rect((0, width), (width//2, width//10))
            pygame.display.flip()
        if type == "quit":
            image = pygame.image.load("quit.png")
            image = pygame.transform.scale(image, (width//3, width//10))
            frame.blit(image, (width//2, width))
            self.rect = pygame.Rect((width//2, width), (width//3, width//10))
            pygame.display.flip()
        if type == "info":
            image = pygame.image.load("info.png")
            image = pygame.transform.scale(image, ((width//2-width//3), width // 10))
            frame.blit(image, ((width//2+width//3), width))
            self.rect = pygame.Rect(((width//2+width//3), width), ((width//2-width//3), width // 10))
            pygame.display.flip()

class Window:
    def __init__(self, uwidth):
        self.width = uwidth//6
        height = self.width+self.width//10
        self.frame = pygame.display.set_mode((self.width, height))
        vlinecoord = [[x, y] for x in [self.width // 3, self.width // 3 * 2] for y in [0, self.width // 3 * 3]]
        hlinecoord = [[x, y] for y in [self.width // 3, self.width // 3 * 2] for x in [0, self.width // 3 * 3]]
        self.linecoord = vlinecoord + hlinecoord
        self.frame.fill((255, 255, 255))
        self.newgameButton = Button("newgame", self.frame, self.width)
        self.quitButton = Button("quit", self.frame, self.width)
        self.infoButton = Button("info", self.frame, self.width)
        for i in range(0, 8, 2):
            pygame.draw.line(self.frame, (0, 0, 0), self.linecoord[i], self.linecoord[i + 1])

class Board(Window):
    pygame.display.set_caption("Noughts and Crosses")
    icon = pygame.image.load("tictactoe.ico")
    pygame.display.set_icon(icon)
    x_standard = pygame.image.load("X_standard.png")
    o_standard = pygame.image.load("O_standard.png")
    def __init__(self):
        super().__init__(uwidth=user_width)
    def ClearBoard(self):
        self.frame.fill((255, 255, 255))
        self.newgameButton = Button("newgame", self.frame, self.width)
        self.quitButton = Button("quit", self.frame, self.width)
        self.infoButton = Button("info", self.frame, self.width)
        for i in range(0, 8, 2):
            pygame.draw.line(self.frame, (0, 0, 0), self.linecoord[i], self.linecoord[i + 1])
    def InsertX(self, x,y):
        self.frame.blit(self.x_standard, (x, y))
        pygame.display.flip()
    def InsertY(self, x,y):
        self.frame.blit(self.o_standard, (x, y))
        pygame.display.flip()
    def Regions(self):
        pass

CurrentWindow = Window(user_width)
CurrentBoard = Board()

# Main Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            print(mx, my)
            if CurrentWindow.newgameButton.rect.collidepoint(mx,my):
                print("Clicked New Game")
                CurrentBoard.ClearBoard()
            if CurrentWindow.quitButton.rect.collidepoint(mx,my):
                print("Clicked Quit Game")
                running = False
            if CurrentWindow.infoButton.rect.collidepoint(mx, my):
                print("Clicked Info")
            if mx < 100 and my < 100:
                x, y = mx, my
                CurrentBoard.InsertX(x, y)
    pygame.display.update()

pygame.quit()