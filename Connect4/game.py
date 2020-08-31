from collections import defaultdict
import numpy as np
class Connect4():
    """
    Playable & Fully functioning skeleton for terminal-based Connect 4
    TODO: 
         1. Add starting message
         2. Simulation option
         3. Refactor diagonal checker for efficiency
         4. Modularize checker 
    """

    def __init__(self):
        self.col_check = defaultdict(int)
        self.player = 1
        self.board = np.full((6,7),'0')
        self.fours = ['1111','2222']
        self.game_over = None
        
    def change_player(self):
        self.player = 1 if self.player == 2 else 2

    def diagonal_check(self):
        #CREATE ALL POSSIBLE WINNING DIAGONALS AS A COMPACTED ARR
        #NEED TO REFACTOR TO NOT HAVE TO RECREATE EVERYTIME
        diagonals = []
        diagonals.append([self.board[i][i] for i in range(6)])
        diagonals.append([self.board[i][j] for i,j in zip(range(6), range(1,7))])
        diagonals.append([self.board[i][j] for i,j in zip(range(1,6), range(5))])
        diagonals.append([self.board[i][j] for i,j in zip(range(5), range(2,7))])
        diagonals.append([self.board[i][j] for i,j in zip(range(2,6), range(4))])
        diagonals.append([self.board[i][j] for i,j in zip(range(4), range(3,7))])
        
        diagonals.append([self.board[-1-i][i] for i in range(6)])
        diagonals.append([self.board[-1-i][j] for i,j in zip(range(6), range(1,7))])
        diagonals.append([self.board[-1-i][j] for i,j in zip(range(1,6), range(5))])
        diagonals.append([self.board[-1-i][j] for i,j in zip(range(5), range(2,7))])
        diagonals.append([self.board[-1-i][j] for i,j in zip(range(2,6), range(4))])
        diagonals.append([self.board[-1-i][j] for i,j in zip(range(4), range(3,7))])
        return diagonals
    
    def score_check(self,i):
        for row in self.board:
            
            if self.fours[i] in ''.join(row):
                self.game_over='Game has finished!'
                return f'Player {self.player} wins!'
            
        if max(self.col_check.values()) >= 4:
            for col in self.board.T:
                if self.fours[i] in ''.join(col):
                    self.game_over='Game has finished!'
                    return f'Player {self.player} wins!'
                
            if len(self.col_check) >= 4:
                diagonals = self.diagonal_check()
                for arr in diagonals:
                    if self.fours[i] in ''.join(arr):
                        self.game_over='Game has finished!'
                        return f'Player {self.player} wins!'

        return f'Player {self.player} has a turn'
    
    def update_scores(self, col):
        i = self.player - 1
        self.col_check[col] += 1
        
        row = 6 - self.col_check[col]
        
        self.board[row, col] = str(self.player)

        msg = self.score_check(i)
        return msg
    
    def play(self, col):
        if self.game_over:
            return self.game_over
        
        if self.col_check[col] == 6:
            return 'Column full!'

        player = self.player
        msg = self.update_scores(col)
        self.change_player()
        return msg