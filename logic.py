class Board:
    def __init__(self):
        self.board = [
                      [0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]
                     ]
        self.run = True
        self.chooseAgain = False

    def modify(self, row, column, player):
        
        if self.board[row-1][column-1] == 0 and row!='' and column!='':
            self.board[row-1][column-1] = player
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
                print(f"{row[0]} is the Winner")
                self.run = False
                
        
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i]!=0: 
                print(f"{self.board[0][i]} is the Winner 1")
                self.run = False
        if self.board[0][0] == self.board[1][1] == self.board[2][2]!=0 or self.board[0][2] == self.board[1][1] == self.board[2][0]!=0:
                 print(f"{self.board[1][1]} is the Winner 2")
                 self.run = False
    def checkDraw(self):
        if self.run:
            if all([0 not in r for r in self.board]):
                
                print("DRAW!") 
                self.run = False               
        

class PlayerOne:
    def __init__(self):
        pass

    def draw(self, r, c):
        board.modify(r, c, "X")

class PlayerTwo:
    def __init__(self):
        pass

    def draw(self, r, c):
        board.modify(r, c, "O")


#turn taking functions
def playerOne():
    global board
    global player1

    print("Player 1")
    r = int(input())
    c = int(input())
    
    player1.draw(r, c)
    board.show()
    
    while board.chooseAgain:
        print("P1")
        r = int(input())
        c = int(input())
        player1.draw(r, c)
        board.show()

def playerTwo():
    global board
    global player2
    print("Player 2")
    r = int(input())
    c = int(input())
    player2.draw(r, c)

    board.show()

    while board.chooseAgain:
        print("P2")
        r = int(input())
        c = int(input())
        player2.draw(r, c)
        
        board.show()

#initalizing classes
board = Board()
player1 = PlayerOne()
player2 = PlayerTwo()

#Gameloop
while board.run:
    if board.run:
        playerOne()

    board.checkDraw()
    board.checkWin()
    if board.run:
        playerTwo()
    
    board.checkWin()
    board.checkDraw()