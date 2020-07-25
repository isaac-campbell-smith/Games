from collections import defaultdict
import numpy as np
class Connect4():

    def __init__(self):
        self.col_check = defaultdict(int)
        self.player = 1
        self.board = [defaultdict(list),defaultdict(list)]
        self.fours = ['1111','2222']
        self.game_over = None
        
    def change_player(self):
        self.player = 1 if self.player == 2 else 2

    def diagonal_check(self):
        diagonals = []
        diagonals.append([self.board[0][i][i] if self.board[0][i] else '' for i in range(6)])
        diagonals.append([self.board[0][i][j] if self.board[0][i] else '' for i,j in zip(range(6), range(1,7))])
        diagonals.append([self.board[0][i][j] if self.board[0][i] else '' for i,j in zip(range(1,6), range(5))])
        diagonals.append([self.board[0][i][j] if self.board[0][i] else '' for i,j in zip(range(5), range(2,7))])
        diagonals.append([self.board[0][i][j] if self.board[0][i] else '' for i,j in zip(range(2,6), range(4))])
        diagonals.append([self.board[0][i][j] if self.board[0][i] else '' for i,j in zip(range(4), range(3,7))])
        return diagonals
    
    def score_check(self,i):
        for dic in self.board:
            for arr in dic.values():
                if self.fours[i] in ''.join(arr):
                    return f'Player {self.player} wins!'
        if max(self.col_check) < 4:
            diagonals = self.diagonal_check()
            for arr in diagonals:
                if self.fours[i] in ''.join(arr):
                    return f'Player {self.player} wins!'

        return f'Player {self.player} has a turn'
    
    def update_scores(self, col):
        i = self.player - 1
        self.col_check[col] += 1
        
        row = self.col_check[col]
        if self.board[0]:
            self.board[0][row][col] = str(i)
        else:
            self.board[0][row] = ['0' for _ in range(7)]
            self.board[0][row][col] = str(i)
        self.board[1][col].append(str(i))
        #self.board[row, col] = str(self.player)
        msg = self.score_check(i)
        return msg
    
    def play(self, col):
        if self.col_check:
            print (max(self.col_check.values()))
        if self.col_check[col] == 6:
            return 'Column full!'
        if self.game_over:
            return self.game_over
        player = self.player
        msg = self.update_scores(col)
        self.change_player()
        return msg
