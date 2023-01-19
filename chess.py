# assignment: programming assignment 5
# author: Sona Nair
# date: 12/04/22
# file: chess.py is a programs that takes user input and draws a chess board with all possible
# movements the chosen piece can make
# input: strings
# output: drawing of board from strings

row8 = ['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8']
row7 = ['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7']
row6 = ['a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6']
row5 = ['a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5']
row4 = ['a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4']
row3 = ['a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3']
row2 = ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2']
row1 = ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1']

class Board:
    def __init__(self):
        self.board = {}
        self.empty()
    def empty(self):
        for col in 'abcdefgh':
            for row in '12345678':
                self.board[col+row] = ' '
    def set(self, pos, piece):   # pos is a square label (a1, a2, ..., h8)
        if pos in self.board.keys():
            self.board[pos] = piece
    def get_keys(self):
        return self.board
    def draw(self):
        print("   a   b   c   d   e   f   g   h")
        for row in [1,2,3,4,5,6,7,8]:
            print(" +", end = "")
            for col in 'abcdefgh':
                print("---", end = "+")
            print()
            print(9 - row, end = "|")
            for col in "abcdefgh":
                print ("   |", end = "")
            print(9 - row)
        print(" +---+---+---+---+---+---+---+---+")
        print("   a   b   c   d   e   f   g   h")
        

class Chess_Piece:
    def __init__(self, board, pos, color='white'):
        self.position = self.get_index(pos)
        self.color = color
        board.set(pos, self.get_name())
    def get_index(self, pos):
        return ('abcdefgh'.index(pos[0]), '12345678'.index(pos[1]))
    def get_name(self):
        pass
    def moves(self, board):
        pass
    def draw_new(self):
        print("   a   b   c   d   e   f   g   h")
        print(" +---+---+---+---+---+---+---+---+")
        print("8|", end = "")
        for i in range(len(row8)):
            if row8[i] in board.get_keys():
                if board.get_keys()[row8[i]] == ' ':
                    print("   |", end = "")
                elif board.get_keys()[row8[i]] == 'x':
                    print(" x |", end = "")
                else:
                    print("", board.get_keys()[row8[i]],"|", end = "")
        print("8")
        print(" +---+---+---+---+---+---+---+---+")
        print("7|", end = "")
        for i in range(len(row7)):
            if row7[i] in board.get_keys():
                if board.get_keys()[row7[i]] == ' ':
                    print("   |", end = "")
                elif board.get_keys()[row7[i]] == 'x':
                    print(" x |", end = "")
                else:
                    print("", board.get_keys()[row7[i]],"|", end = "")
        print("7")       
        print(" +---+---+---+---+---+---+---+---+")
        print("6|", end = "")
        for i in range(len(row6)):
            if row6[i] in board.get_keys():
                if board.get_keys()[row6[i]] == ' ':
                    print("   |", end = "")
                elif board.get_keys()[row6[i]] == 'x':
                    print(" x |", end = "")
                else:
                    print("", board.get_keys()[row6[i]],"|", end = "")
        print("6")
        print(" +---+---+---+---+---+---+---+---+")
        print("5|", end = "")
        for i in range(len(row5)):
            if row5[i] in board.get_keys():
                if board.get_keys()[row5[i]] == ' ':
                    print("   |", end = "")
                elif board.get_keys()[row5[i]] == 'x':
                    print(" x |", end = "")
                else:
                    print("", board.get_keys()[row5[i]],"|", end = "")
        print("5")
        print(" +---+---+---+---+---+---+---+---+")
        print("4|", end = "")
        for i in range(len(row4)):
            if row4[i] in board.get_keys():
                if board.get_keys()[row4[i]] == ' ':
                    print("   |", end = "")
                elif board.get_keys()[row4[i]] == 'x':
                    print(" x |", end = "")
                else:
                    print("", board.get_keys()[row4[i]],"|", end = "")
        print("4")
        print(" +---+---+---+---+---+---+---+---+")
        print("3|", end = "")
        for i in range(len(row3)):
            if row3[i] in board.get_keys():
                if board.get_keys()[row3[i]] == ' ':
                    print("   |", end = "")
                elif board.get_keys()[row3[i]] == 'x':
                    print(" x |", end = "")
                else:
                    print("", board.get_keys()[row3[i]],"|", end = "")
        print("3")
        print(" +---+---+---+---+---+---+---+---+")
        print("2|", end = "")
        for i in range(len(row2)):
            if row2[i] in board.get_keys():
                if board.get_keys()[row2[i]] == ' ':
                    print("   |", end = "")
                elif board.get_keys()[row2[i]] == 'x':
                    print(" x |", end = "")
                else:
                    print("", board.get_keys()[row2[i]],"|", end = "")
        print("2")
        print(" +---+---+---+---+---+---+---+---+")
        print("1|", end = "")
        for i in range(len(row1)):
            if row1[i] in board.get_keys():
                if board.get_keys()[row1[i]] == ' ':
                    print("   |", end = "")
                elif board.get_keys()[row1[i]] == 'x':
                    print(" x |", end = "")
                else:
                    print("", board.get_keys()[row1[i]],"|", end = "")
        print("1")
        print(" +---+---+---+---+---+---+---+---+")
        print("   a   b   c   d   e   f   g   h")

class Rook(Chess_Piece):
    def get_name(self):
        return "R"
    def moves(self, board):
        for key in board.get_keys():
            key_index = self.get_index(key)
            if key_index == self.position:
                continue
            elif key_index[0] == self.position[0]:
                board.set(key, "x")
            elif key_index[1] == self.position[1]:
                board.set(key, "x")    
        
                
class King(Chess_Piece):
    def get_name(self):
        return "K"
    def moves(self, board):
        for key in board.get_keys():
            key_index = self.get_index(key)
            if key_index == self.position:
                continue
            elif key_index[0] == self.position[0]:
                if key_index[1] == (self.position[1] - 1):
                    board.set(key, "x")
                if key_index[1] == (self.position[1] + 1):
                    board.set(key, "x")
            elif key_index[1] == self.position[1]:
                if key_index[0] == (self.position[0] - 1):
                    board.set(key, "x")
                if key_index[0] == (self.position[0] + 1):
                        board.set(key, "x")
            elif key_index[0] == (self.position[0] + 1):
                    if key_index[1] == (self.position[1] - 1):
                        board.set(key, "x")
                    if key_index[1] == (self.position[1] + 1):
                        board.set(key, "x")
            elif key_index[0] == (self.position[0] - 1):
                    if key_index[1] == (self.position[1] + 1):
                        board.set(key, "x")
                    if key_index[1] == (self.position[1] - 1):
                        board.set(key, "x")

class Queen(Chess_Piece):
    def get_name(self):
        return "Q"
    def moves(self, board):
        for key in board.get_keys():
            key_index = self.get_index(key)
            if key_index == self.position:
                continue
            elif key_index[0] == self.position[0]:
                board.set(key, "x")
            elif key_index[1] == self.position[1]:
                board.set(key, "x")
            for i in range(8):
                if key_index[0] == (self.position[0] + i):
                    if key_index[1] == (self.position[1] + i):
                        board.set(key, "x")
            for i in range(8):
                if key_index[0] == (self.position[0] - i):
                    if key_index[1] == (self.position[1] - i):
                        board.set(key, "x")
            for i in range(8):
                if key_index[0] == (self.position[0] + i):
                    if key_index[1] == (self.position[1] - i):
                        board.set(key, "x")
            for i in range(8):
                if key_index[0] == (self.position[0] - i):
                    if key_index[1] == (self.position[1] + i):
                        board.set(key, "x")

class Knight(Chess_Piece):
    def get_name(self):
        return "N"
    def moves(self, board):
        for key in board.get_keys():
            key_index = self.get_index(key)
            if key_index == self.position:
                continue
            elif key_index[0] == (self.position[0] + 2):
                if key_index[1] == (self.position[1] + 1):
                    board.set(key, "x")
                elif key_index[1] == (self.position[1] - 1):
                    board.set(key, "x")
            elif key_index[0] == (self.position[0] - 2):
                if key_index[1] == (self.position[1] + 1):
                    board.set(key, "x")
                elif key_index[1] == (self.position[1] - 1):
                    board.set(key, "x")
            elif key_index[1] == (self.position[1] + 2):
                if key_index[0] == (self.position[0] + 1):
                    board.set(key, "x")
                elif key_index[0] == (self.position[0] - 1):
                    board.set(key, "x")
            elif key_index[1] == (self.position[1] - 2):
                if key_index[0] == (self.position[0] + 1):
                    board.set(key, "x")
                elif key_index[0] == (self.position[0] - 1):
                    board.set(key, "x")
                
class Bishop(Chess_Piece):
    def get_name(self):
        return "B"
    def moves(self, board):
        for key in board.get_keys():
            key_index = self.get_index(key)
            if key_index == self.position:
                continue
            for i in range(8):
                if key_index[0] == (self.position[0] + i):
                    if key_index[1] == (self.position[1] + i):
                        board.set(key, "x")
            for i in range(8):
                if key_index[0] == (self.position[0] - i):
                    if key_index[1] == (self.position[1] - i):
                        board.set(key, "x")
            for i in range(8):
                if key_index[0] == (self.position[0] + i):
                    if key_index[1] == (self.position[1] - i):
                        board.set(key, "x")
            for i in range(8):
                if key_index[0] == (self.position[0] - i):
                    if key_index[1] == (self.position[1] + i):
                        board.set(key, "x")
    
        
if __name__ == '__main__':
    print("Welcome to the Chess Game!")
    try:
        board = Board()
        board.draw()
    except TypeError:
        print()
    while True:
        choice = input("Enter a chess piece and its position or type X to exit:\n").lower()
        if choice == "x":
            print("Goodbye!")
            break
        elif choice[0] == "r":
            if choice[1] == "a" or choice[1] == "b" or choice[1] == "c" or choice[1] == "d" or choice[1] == "e" or choice[1] == "f" or choice[1] == "g" or choice[1] == "h":
                if choice[2] == "1" or choice[2] == "2" or choice[2] == "3" or choice[2] == "4" or choice[2] == "5" or choice[2] == "6" or choice[2] == "7" or choice[2] == "8":
                    rook = Rook(board, choice[1:])
                    rook.moves(board)
                    rook.draw_new()
        elif choice[0] == "k":
            if choice[1] == "a" or choice[1] == "b" or choice[1] == "c" or choice[1] == "d" or choice[1] == "e" or choice[1] == "f" or choice[1] == "g" or choice[1] == "h":
                if choice[2] == "1" or choice[2] == "2" or choice[2] == "3" or choice[2] == "4" or choice[2] == "5" or choice[2] == "6" or choice[2] == "7" or choice[2] == "8":
                    king = King(board, choice[1:])
                    king.moves(board)
                    king.draw_new()
        elif choice[0] == "b":
            if choice[1] == "a" or choice[1] == "b" or choice[1] == "c" or choice[1] == "d" or choice[1] == "e" or choice[1] == "f" or choice[1] == "g" or choice[1] == "h":
                if choice[2] == "1" or choice[2] == "2" or choice[2] == "3" or choice[2] == "4" or choice[2] == "5" or choice[2] == "6" or choice[2] == "7" or choice[2] == "8":
                    bishop = Bishop(board, choice[1:])
                    bishop.moves(board)
                    bishop.draw_new()
        elif choice[0] == "n":
            if choice[1] == "a" or choice[1] == "b" or choice[1] == "c" or choice[1] == "d" or choice[1] == "e" or choice[1] == "f" or choice[1] == "g" or choice[1] == "h":
                if choice[2] == "1" or choice[2] == "2" or choice[2] == "3" or choice[2] == "4" or choice[2] == "5" or choice[2] == "6" or choice[2] == "7" or choice[2] == "8":
                    knight = Knight(board, choice[1:])
                    knight.moves(board)
                    knight.draw_new()
        elif choice[0] == "q":
            if choice[1] == "a" or choice[1] == "b" or choice[1] == "c" or choice[1] == "d" or choice[1] == "e" or choice[1] == "f" or choice[1] == "g" or choice[1] == "h":
                if choice[2] == "1" or choice[2] == "2" or choice[2] == "3" or choice[2] == "4" or choice[2] == "5" or choice[2] == "6" or choice[2] == "7" or choice[2] == "8":
                    queen = Queen(board, choice[1:])
                    queen.moves(board)
                    queen.draw_new()

        board.__init__()
            

