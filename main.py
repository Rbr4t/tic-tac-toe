import pygame

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((600, 600))
myFont = pygame.font.SysFont('Comic Sans MS', 30)


# Classes and methods of them
class Board:
    def __init__(self):
        self.board = [
                      [0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]
                     ]
        self.cordsBoard = [[None for i in range(3)] for i in range(3) ]
        self.run = True
        self.chooseAgain = False
        self.winner = None

    def modify(self, row, column, player, cords):
        
        if self.board[row-1][column-1] == 0 and row!='' and column!='':
            self.board[row-1][column-1] = player
            self.cordsBoard[row-1][column-1] = cords
            self.chooseAgain = False
        else:
            self.chooseAgain = True

    def show(self):
        for r in self.board:
            for c in r:
                if c==0:
                    print("-", end="")
                else:
                    print(c, end="")
            print("\n")
        
    def checkWin(self):
        for row in self.board:
            if len(set(row))==1 and 0 not in [x for x in set(row)]:
                self.winner = row[0]
                self.run = False
                
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i]!=0: 
                self.winner = self.board[0][i]
                self.run = False
        
        if self.board[0][0] == self.board[1][1] == self.board[2][2]!=0 or self.board[0][2] == self.board[1][1] == self.board[2][0]!=0:
                self.winner = self.board[1][1]
                self.run = False
    def checkDraw(self):
        if self.run:
            if all([0 not in r for r in self.board]):
                self.winner = "DRAW!" 
                self.run = False               
#class for button
class Button:
    def __init__(self, x, y) -> None:
        self.text = "Reset"
        self.bg = (255, 255, 255)
        self.x = x
        self.y = y
        self.rect = pygame.Rect(50, 30, 100, 40)

    def show(self):
        text = myFont.render(self.text, True, (0, 0, 0))
        
        pygame.draw.rect(screen, (255, 124, 45), self.rect)
        screen.blit(text, (75, 40))
        
        

    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    print("HEre")
                    board.board = [
                      [0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]
                     ]
                    board.cordsBoard = [[None for i in range(3)] for i in range(3)]
                    board.run = True

#GUI functions
def drawGrid():
    grid_area = 500 #width
    for x in range(1, 3):
        pygame.draw.line(screen, (0, 0, 0), (50+grid_area//3*x, padding_y), (50+grid_area//3*x, 500+padding_y), 2)
    for x in range(1, 3):
        pygame.draw.line(screen, (0, 0, 0), (50, padding_y+grid_area//3*x), (550, padding_y+grid_area//3*x), 2)

# we get the cell coordinates
def whichCell(mouse):
    if padding_y<mouse[1]<166+padding_y:
        
        if padding_x<mouse[0]<166+padding_x:
            return ([padding_x, padding_y], [1, 1])

        if 166+padding_x<mouse[0]<332+padding_x:
            return ([166+padding_x, padding_y], [1, 2])

        if 332+padding_x<mouse[0]<500+padding_x:
            return ([332+padding_x, padding_y], [1, 3])

    if 166+padding_y<mouse[1]<332+padding_y:
       

        if padding_x<mouse[0]<166+padding_x:
            return ([padding_x, padding_y+500//3], [2, 1])

        if 166+padding_x<mouse[0]<332+padding_x:
            return ([166+padding_x, padding_y+500//3], [2, 2])

        if 332+padding_x<mouse[0]<500+padding_x:
            return ([332+padding_x, padding_y+500//3], [2, 3])
        
    if 332+padding_y<mouse[1]<500+padding_y:
        
        if padding_x<mouse[0]<166+padding_x:
            return ([padding_x, padding_y+500//3*2], [3, 1])

        if 166+padding_x<mouse[0]<332+padding_x:
            return ([166+padding_x, padding_y+500//3*2], [3, 2])

        if 332+padding_x<mouse[0]<500+padding_x:
            return ([332+padding_x, padding_y+500//3*2], [3, 3])

#text rendering
def renderPlayer():
    global myFont, turn
    if turn == "cross":
        textsurface = myFont.render('Player 1 turn:', True, (0, 0, 0))
    else:
        textsurface = myFont.render('Player 2 turn:', True, (0, 0, 0))
    screen.blit(textsurface, (30*len('Player 1 turn:'), 40))
    

#rendering crosses and circles on screen
def renderCrossesAndCircles():
    for r in range(len(board.board)):
            for c in range(len(board.board[r])):
                if board.board[r][c] == "X":
                    screen.blit(cross, board.cordsBoard[r][c])
                elif board.board[r][c] == "O":
                    screen.blit(circle, board.cordsBoard[r][c])
#class initalizing
board = Board()
button1 = Button(50, 50)

#Game variables
mouse = None
padding_x = 50
padding_y = 80
RUN = board.run
turn = 'cross'

cross = pygame.image.load('tic-tac-toe/rsz_1x_modified.png')
circle = pygame.image.load('tic-tac-toe/rsz_o_modified.png')
screen.fill((255, 255, 255))

clock = pygame.time.Clock()

while RUN:
    clock.tick(30)

    renderCrossesAndCircles()
    board.checkDraw()
    board.checkWin()
    pygame.draw.rect(screen, (0, 0, 0), (50, padding_y, 500, 500), 2)
    drawGrid()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
        button1.click(event)
        
        if event.type == pygame.MOUSEBUTTONDOWN and board.run:
            mouse = pygame.mouse.get_pos()
            
            try:
                if turn=="cross":
                    board.modify(whichCell(mouse)[1][0], whichCell(mouse)[1][1], "X", whichCell(mouse)[0])
                    turn = "circle"
                else:
                    board.modify(whichCell(mouse)[1][0], whichCell(mouse)[1][1], "O", whichCell(mouse)[0])
                    turn = "cross"
            except:
                pass 
                
                # board.show()

    if not board.run:
        if board.winner == "DRAW":
            textsurface = myFont.render(f"Game over! It's a draw", True, (0, 0, 0))
            screen.blit(textsurface, (230, 40))
        else:  
            textsurface = myFont.render(f'Game over! {board.winner}!', True, (0, 0, 0))
            screen.blit(textsurface, (230, 40))
    else:
        renderPlayer()
    button1.show()

    pygame.display.update()
    screen.fill((255, 255, 255))
pygame.quit()