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

        size = self.width + self.height
        for k in range(size-2):
            prevChar = ""
            charAdj = 0
            for j in range(k):
                i = k - j
                if i < self.width-1 and j < self.height-1:
                     print(k,i,j, self.board[i][j], prevChar, charAdj)
                     if self.board[i][j] != "O" and self.board[i][j] == prevChar:
                         print("check")
                         charAdj += 1
                         if charAdj == 3:
                             return True
                     else:
                         charAdj = 0
                         prevChar = self.board[i][j] if self.board[i][j] != 'O' else ""
b = Board(7,6)
#b.play(4, 'j')
#b.play(4, 'j')
#b.play(4, 'j')
#b.play(4, 'r')
#b.play(3, 'j')
#b.play(3, 'j')
#b.play(3, 'r')
#b.play(2, 'j')
#b.play(2, 'r')
#b.play(1, 'r')
b.play(1, 'j')
b.play(1, 'j')
b.play(1, 'j')
b.play(1, 'r')
b.play(2, 'j')
b.play(2, 'j')
b.play(2, 'r')
b.play(3, 'j')
b.play(3, 'r')
b.play(4, 'r')
print(b)
print(b.checkWin())
#b.run()
