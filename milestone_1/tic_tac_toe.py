from itertools import chain


class TicTacToe:

    def __init__(self):
        self.board = []

    def create_board(self):
        print("Here is the playboard: ")
        print()
        for i in range(3):
            row = []
            for j in range(3):
                row.append("-")
            self.board.append(row)
        self.print_board()

    def print_board(self):
        print()
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def player_move(self, icon):
        if icon == "X":
            number = 1
        elif icon == "O":
            number = 2

        print("Your turn player {}".format(number))

        row = int(input("Pick a row: "))
        column = int(input("Pick a column: "))
        if self.board[row - 1][column - 1] == "-":
            self.board[row - 1][column - 1] = icon
        else:
            print()
            print("That space is taken!")

    def is_victory(self, icon):
        if self.board[0][0] == icon and self.board[0][1] == icon and self.board[0][2] == icon or \
                self.board[1][0] == icon and self.board[1][1] == icon and self.board[1][2] == icon or \
                self.board[2][0] == icon and self.board[2][1] == icon and self.board[2][2] == icon or \
                self.board[0][0] == icon and self.board[1][0] == icon and self.board[2][0] == icon or \
                self.board[0][1] == icon and self.board[1][1] == icon and self.board[2][1] == icon or \
                self.board[0][2] == icon and self.board[1][2] == icon and self.board[2][2] == icon or \
                self.board[0][0] == icon and self.board[1][1] == icon and self.board[2][2] == icon or \
                self.board[0][2] == icon and self.board[1][1] == icon and self.board[2][0] == icon:
            return True
        else:
            return False

    def is_tie(self):
        if "-" not in chain(*self.board):
            return True
        else:
            return False

    def start(self):
        while True:
            self.create_board()
            while True:
                self.player_move("X")
                self.print_board()
                if self.is_victory("X"):
                    print("X wins! Congratulations!")
                    break
                elif self.is_tie():
                    print("There is a tie.")
                    break
                self.player_move("O")
                self.print_board()
                if self.is_victory("O"):
                    print("O wins! Congratulations!")
                    break
                elif self.is_tie():
                    print("There is a tie.")
                    break
            restart = input("Do want to play Again? (y/n):  ")
            if restart == "y" or restart == "Y":
                self.board.clear()
            else:
                break


tic_tac_toe = TicTacToe()
tic_tac_toe.start()
