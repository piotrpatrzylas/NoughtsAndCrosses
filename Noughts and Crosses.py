import pygame
import random
import tkinter


pygame.init()
user_width = pygame.display.Info().current_w

class Button:
    def __init__(self, type, frame, width):
        if type == "newgame":
            image = pygame.image.load("newgame.png")
            image = pygame.transform.scale(image, (width // 2, width // 10))
            frame.blit(image, (0, width))
            self.rect = pygame.Rect((0, width), (width // 2, width // 10))
            pygame.display.flip()
        if type == "quit":
            image = pygame.image.load("quit.png")
            image = pygame.transform.scale(image, (width // 3, width // 10))
            frame.blit(image, (width // 2, width))
            self.rect = pygame.Rect((width // 2, width), (width // 3, width // 10))
            pygame.display.flip()
        if type == "info":
            image = pygame.image.load("info.png")
            image = pygame.transform.scale(image, ((width // 2 - width // 3), width // 10))
            frame.blit(image, ((width // 2 + width // 3), width))
            self.rect = pygame.Rect(((width // 2 + width // 3), width), ((width // 2 - width // 3), width // 10))
            pygame.display.flip()

class Window:
    def __init__(self, uwidth):
        self.width = uwidth // 6
        height = self.width + self.width // 10
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
        self.x_standard = pygame.transform.scale(self.x_standard, ((self.width // 3) - 2, (self.width // 3) - 2))
        self.o_standard = pygame.image.load("O_standard.png")
        self.o_standard = pygame.transform.scale(self.o_standard, ((self.width // 3) - 2, (self.width // 3) - 2))
        self.Regions = {1: pygame.Rect(0, 0, self.width // 3, self.width // 3),
                        2: pygame.Rect(self.width // 3, 0, self.width // 3, self.width // 3),
                        3: pygame.Rect((self.width // 3) * 2, 0, self.width // 3, self.width // 3),
                        4: pygame.Rect(0, self.width // 3, self.width // 3, self.width // 3),
                        5: pygame.Rect(self.width // 3, self.width // 3, self.width // 3, self.width // 3),
                        6: pygame.Rect((self.width // 3) * 2, self.width // 3, self.width // 3, self.width // 3),
                        7: pygame.Rect(0, (self.width // 3) * 2, self.width // 3, self.width // 3),
                        8: pygame.Rect(self.width // 3, (self.width // 3) * 2, self.width // 3, self.width // 3),
                        9: pygame.Rect((self.width // 3) * 2, (self.width // 3) * 2, self.width // 3, self.width // 3)
                        }
        self.WinCase = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7}, {2, 5, 8}, {3, 6, 9}, {1, 5, 9}, {3, 5, 7}]

    def clear(self):
        self.frame.fill((255, 255, 255))
        self.newgameButton = Button("newgame", self.frame, self.width)
        self.quitButton = Button("quit", self.frame, self.width)
        self.infoButton = Button("info", self.frame, self.width)
        for i in range(0, 8, 2):
            pygame.draw.line(self.frame, (0, 0, 0), self.linecoord[i], self.linecoord[i + 1])

    def insertx(self, x, y):
        self.frame.blit(self.x_standard, (x, y))
        pygame.display.flip()

    def inserto(self, x, y):
        self.frame.blit(self.o_standard, (x, y))
        pygame.display.flip()

    def checkwin(self, Player, AI):
        gio = True
        for i in self.WinCase:
            if Player.issuperset(i) or \
                    AI.issuperset(i):
                gio = False
        return gio

    def winbox(self, text):
        self.text = text
        pygame.font.init()
        font = pygame.font.SysFont("Arial", 18)
        message = font.render(self.text, True, (0,0,0), (255,255,255))
        rectangle = message.get_rect()
        rectangle.center = (self.width//2), (self.width//2)
        self.frame.blit(message, rectangle)

class Game():
    CurrentWindow = Window(user_width)
    CurrentBoard = Board()
    Cross = random.choice(["Player", "AI"])
    Nought = str(list({"AI", "Player"} - {Cross})[0])
    turn = Cross
    FreeRegions = []
    GameIsOn = True
    running = True
    PlayerRegions = set()
    AIRegions = set()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if CurrentWindow.newgameButton.rect.collidepoint(mx, my):
                    CurrentBoard.clear()
                    FreeRegions = [x for x in range(1, 10)]
                    Cross = random.choice(["Player", "AI"])
                    Nought = str(list({"AI", "Player"} - {Cross})[0])
                    turn = Cross
                    GameIsOn = True
                    PlayerRegions = set()
                    AIRegions = set()
                if CurrentWindow.quitButton.rect.collidepoint(mx, my):
                    running = False
                if CurrentWindow.infoButton.rect.collidepoint(mx, my):
                    root = tkinter.Tk()
                    root.title("About...")
                    canvas = tkinter.Canvas(root, height=100, width=220)
                    canvas.pack()
                    frame = tkinter.Frame(canvas, bg = "white")
                    frame.place(relwidth = 1, relheight = 1)
                    label1 = tkinter.Label(frame, text = "Noughts and Crosses", bg = "white", fg = "black")
                    label1.pack(side = "top", fill = "both", expand = True)
                    label2 = tkinter.Label(frame, text="Copyright (C) Piotr Patrzylas 2020", bg="white", fg="black")
                    label2.pack(side="top", fill="both", expand=True)
                    label3 = tkinter.Label(frame, text="License: WTFPL", bg="white", fg="black")
                    label3.pack(side="bottom", fill="both", expand=True)
                    root.mainloop()
                if GameIsOn:
                    if turn == "Player" and GameIsOn:
                        for i in FreeRegions:
                            if CurrentBoard.Regions[i].collidepoint(mx, my):
                                if Cross == "Player":
                                    CurrentBoard.insertx(CurrentBoard.Regions[i][0] + 1,
                                                         CurrentBoard.Regions[i][1] + 1)
                                if Nought == "Player":
                                    CurrentBoard.inserto(CurrentBoard.Regions[i][0] + 1,
                                                         CurrentBoard.Regions[i][1] + 1)
                                PlayerRegions.add(i)
                                FreeRegions.remove(i)
                                GameIsOn = (CurrentBoard.checkwin(PlayerRegions, AIRegions))
                                if not GameIsOn:
                                    CurrentBoard.winbox("You have won the game!")
                                pygame.time.wait(500)
                                turn = "AI"
                    if turn == "AI" and GameIsOn:
                        if len(FreeRegions) == 0:
                            break
                        AIEasy = random.choice(FreeRegions)
                        if Cross == "AI":
                            CurrentBoard.insertx(CurrentBoard.Regions[AIEasy][0] + 1,
                                                 CurrentBoard.Regions[AIEasy][1] + 1)
                        if Nought == "AI":
                            CurrentBoard.inserto(CurrentBoard.Regions[AIEasy][0] + 1,
                                                 CurrentBoard.Regions[AIEasy][1] + 1)
                        AIRegions.add(AIEasy)
                        FreeRegions.remove(AIEasy)
                        GameIsOn = (CurrentBoard.checkwin(PlayerRegions, AIRegions))
                        if not GameIsOn:
                            CurrentBoard.winbox("You have lost the game!")
                        turn = "Player"
        pygame.display.update()
    pygame.quit()

def main():
    Game()

if __name__ == "__main__":
    main()