#!/usr/bin/env python3

class Board:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = ["O"*width]*height

    def __repr__(self):
        println = ""
        println += ("-"*4)*self.width+"\n"
        for line in self.board:
            println += "|"
            for char in line:
                println += " {} |".format(char)
            println += "\n"
        println += ("-"*4)*self.width
        return println

    def play(self, column, color):
        if color not in ["r", "j"]:
            print("Le joueur n'est ni rouge ni jaune")
        else:
            color = "R" if color=="r" else "J"
            if column <= self.width:
                for line in range(len(self.board)):
                    if self.board[line][column-1] == "O":
                        if line == len(self.board)-1:
                            self.board[line] = self.board[line][0:column-1] + color + self.board[line][column:]
                            return
                        continue
                    else :
                        if line == 0:
                            print("cannot put more on top")
                        else:
                            self.board[line-1] = self.board[line-1][0:column-1] + color + self.board[line-1][column:]
                        return
            else:
                print("Cannot put more on right")

    def run(self):
        color_one = input("color player 1: r for 'red' and j for 'jaune'")
        if color_one not in ["r","j"]:
            print("bad color input, type r for red and j for jaune")
        else:
            color_two = "j" if color_one == "r" else "r"

        turn = 1
        while True:
            turn += 1
            if turn%2 == 0:
                self.play(int(input("Player 1 moves:")), color_one)
            else:
                self.play(int(input("Player 2 moves:")), color_two)

            print(self)

            if self.checkWin():
                break

        if turn%2 == 0 :
            print("Player 1 WON $100 000!!!")
        else:
            print("Player 2 WON $100 000!!!")

    def checkWin(self):
        for line in self.board:
            prevChar = ""
            charAdj = 0
            for char in line:
                if char == prevChar and char != 'O':
                    charAdj += 1
                    if charAdj == 3:
                        return True
                else :
                     chadAdj = 0
                     prevChar = char if char != 'O' else ""

        prevChar = ""
        for w in range(len(self.board[0])):
            prevChar = ""
            charAdj = 0
            for h in range(len(self.board)):
                if self.board[h][w] == prevChar and self.board[h][w] != 'O':
                    charAdj += 1
                    if charAdj == 3 :
                        return True
                else:
                    chadAdj = 0
                    prevChar = self.board[h][w] if self.board[h][w] != 'O' else ""

        invert = False
        shift = 0
        end = False
        while not end:
            base = shift
            prevChar = ""
            adjChar = 0
            for h in range(len(self.board)):
                if base == self.width :
                    print("invert")
                    shift = self.width
                    invert = True
                    base -= 1
                print(self.board[h][base], h, base, prevChar, adjChar)
                if self.board[h][base] == prevChar and self.board[h][base] != 'O':
                    adjChar += 1
                    if adjChar == 3:
                        return True
                else:
                    adjChar = 0
                    prevChar = self.board[h][base] if self.board[h][base] != 'O' else ""

                if invert:
                    print("sub 1", base)
                    base -= 1
                else:
                    print("add 1")
                    base += 1

            if shift == 1 and invert:
                invert = False
                end = True
            elif invert:
                shift -= 1
            else:
                shift += 1

        invert = False
        shift = 0
        while True:
            base = shift
            prevChar = ""
            adjChar = 0
            for h in range(len(self.board)-1,0):
                if base == self.width-1 :
                    print("inversion")
                    invert = True
                    base -= 1
                if self.board[h][base] == prevChar and self.board[h][base] != 'O':
                    print("check")
                    adjChar += 1
                    if adjChar == 3:
                        return True
                else:
                    adjChar = 0
                    prevChar = self.board[h][base] if self.board[h][base] != 'O' else ""

                if invert:
                    base -= 1
                else:
                    base += 1

            if shift == 1 and invert:
                break
            elif invert:
                shift -= 1
            else:
                shift += 1

        return False

b = Board(7,6)
b.play(4, 'j')
b.play(4, 'j')
b.play(4, 'j')
b.play(4, 'r')
b.play(3, 'j')
b.play(3, 'j')
b.play(3, 'r')
b.play(2, 'j')
b.play(2, 'r')
b.play(1, 'r')
print(b)
print(b.checkWin())
#b.run()
