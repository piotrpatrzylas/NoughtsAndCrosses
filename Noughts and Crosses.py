import pygame
import tkinter
import random

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

    def __init__(self):
        super().__init__(uwidth=user_width)
        self.x_standard = pygame.image.load("X_standard.png")
        self.x_standard = pygame.transform.scale(self.x_standard, ((self.width//3)-2, (self.width//3)-2))
        self.o_standard = pygame.image.load("O_standard.png")
        self.o_standard = pygame.transform.scale(self.o_standard, ((self.width // 3) - 2, (self.width // 3) - 2))
        self.Regions = {1: [pygame.Rect(0, 0, self.width // 3, self.width // 3), 1, ""], \
                        2: [pygame.Rect(self.width // 3, 0, self.width // 3, self.width // 3), 1, ""], \
                        3: [pygame.Rect((self.width // 3)*2, 0, self.width // 3, self.width // 3), 1, ""], \
                        4: [pygame.Rect(0, self.width // 3, self.width // 3, self.width // 3), 1, ""], \
                        5: [pygame.Rect(self.width // 3, self.width // 3, self.width // 3, self.width // 3), 1, ""], \
                        6: [pygame.Rect((self.width // 3)*2, self.width // 3, self.width // 3, self.width // 3), 1, ""], \
                        7: [pygame.Rect(0, (self.width // 3)*2, self.width // 3, self.width // 3), 1, ""], \
                        8: [pygame.Rect(self.width // 3, (self.width // 3)*2, self.width // 3, self.width // 3), 1, ""], \
                        9: [pygame.Rect((self.width // 3)*2, (self.width // 3)*2, self.width // 3, self.width // 3), 1, ""]
                        }

    def ClearBoard(self):
        self.frame.fill((255, 255, 255))
        self.newgameButton = Button("newgame", self.frame, self.width)
        self.quitButton = Button("quit", self.frame, self.width)
        self.infoButton = Button("info", self.frame, self.width)
        for i in range(0, 8, 2):
            pygame.draw.line(self.frame, (0, 0, 0), self.linecoord[i], self.linecoord[i + 1])
        for i in self.Regions:
            self.Regions[i][1] = 0
    def InsertX(self, x,y):
        self.frame.blit(self.x_standard, (x, y))
        pygame.display.flip()
    def InsertO(self, x,y):
        self.frame.blit(self.o_standard, (x, y))
        pygame.display.flip()

class Game():
    CurrentWindow = Window(user_width)
    CurrentBoard = Board()
    Cross = random.choice(["Player", "AI"])
    Nought = str(list({"AI", "Player"} - {Cross})[0])
    turn = Cross

    # Main Loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                print("X: ", mx, "Y: ", my)
                print(turn)
                if CurrentWindow.newgameButton.rect.collidepoint(mx, my):
                    print("Clicked New Game")
                    CurrentBoard.ClearBoard()
                    Cross = random.choice(["Player", "AI"])
                    Nought = str(list({"AI", "Player"} - {Cross})[0])
                    turn = Cross
                if CurrentWindow.quitButton.rect.collidepoint(mx, my):
                    print("Clicked Quit Game")
                    running = False
                if CurrentWindow.infoButton.rect.collidepoint(mx, my):
                    print("Clicked Info")
                if turn == "Player" and Cross == "Player":
                    for i in range(1, 10):
                        if CurrentBoard.Regions[i][0].collidepoint(mx, my) and CurrentBoard.Regions[i][1] == 0:
                            CurrentBoard.InsertX(CurrentBoard.Regions[i][0][0]+1, CurrentBoard.Regions[i][0][0]+1)
                            CurrentBoard.Regions[i][1] == 1

                if turn == "Player" and Nought == "Player":
                    for i in range(1, 10):
                        if CurrentBoard.Regions[i][0].collidepoint(mx, my) and CurrentBoard.Regions[i][1] == 0:
                            CurrentBoard.InsertO(CurrentBoard.Regions[i][0][0] + 1, CurrentBoard.Regions[i][0][0] + 1)
                            CurrentBoard.Regions[i][1] == 1

        pygame.display.update()

    pygame.quit()
