import numpy as np
#see game
class SnakesLadders():

    def __init__(self):
        self.player = 0 #players will be 0 & 1 to make indexing scores easier
        self.scores = [0, 0] 
        self.status = False #changes if game has been won
        self.board = {        # 'ladders' & 'snakes' locations
                        2:38, 
                        7:14,
                        8:31,
                        15:26,
                        16:6,
                        28:84,
                        21:42,
                        36:44,
                        46:25,
                        49:11,
                        51:67,
                        62:19,
                        64:60,
                        71:91,
                        74:53,
                        78:98,
                        87:94,
                        89:68,
                        92:88,
                        95:75,
                        99:80,
                        100: 'Game over!'
                        }
        
    def update_player(self, doubles=False):
        """Changes our current player if """
        if self.player == 0:
            self.player = 1 if not doubles else 0
        else:
            self.player = 0 if not doubles else 1
        
    def play_msg(self):
        if type(self.scores[self.player]) == int:
            return f'Player {self.player+1} is on square {self.scores[self.player]}'
        else:
            self.status = 'Game over!'
            return f'Player {self.player+1} Wins!'
            
    def update_position(self, roll):
        position = self.scores[self.player] + roll
        if position > 100:
            position = 100 + (100 - self.scores[self.player] - roll)
        if position in self.board:
            position = self.board[position]
            
        self.scores[self.player] = position

    def roll(self):
        die1, die2 = np.random.randint(1, 7, size=2)
        doubles = die1 == die2
        if doubles:
            print (f'Player {self.player+1} has rolled {die1}s!')
        else:
            print (f'Player {self.player+1} has rolled {die1} and {die2}')
        return int(die1+die2), doubles

    def play(self):
        if self.status:
            return self.status
    
        roll, doubles = self.roll()
        self.update_position(roll)
        play_msg = self.play_msg()

        self.update_player(doubles)
        return play_msg

if __name__ == '__main__':
    game = SnakesLadders()
    while not game.status:
        print (game.play(), '\n')
    