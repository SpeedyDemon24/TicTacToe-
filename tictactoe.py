import numpy as np

class TicTacToe:
    def __init__(self):
        self.board = np.zeros((3,3))
        self.player = 1
        
    def play_game(self):
        has_won = False
        has_drawn = False
        while not has_won and not has_drawn:
            print(self.board)
            position_str = input(f"player {self.player} make a move: ")
            position = (int(position_str[0]),int(position_str[-1]))
            try:
                self.make_a_move(self.player, position)
            except ValueError as e:
                print(e)
                continue
                
            has_won = self.check_win()
            has_drawn = self.check_for_draw()
            self.player = self.player*-1
        if has_won:
            print("Player ",self.player*-1, " has won the game")
        else:
            print("Tie Game")
        
        
    def make_a_move(self, symbol, position):
        if self.board[position]==0: 
            self.board[position] = symbol
        else:
            raise ValueError("There is a number in this place")
 
    def check_win_row(self):
        return (self.board.sum(axis= 1) == self.player*3).any()

    def check_win_column(self):
        return (self.board.sum(axis= 0) == self.player*3).any()
    
    def check_win_diagonal_top_right_bottom_left(self):
        return (np.diag(np.fliplr(self.board)).sum() == self.player*3)
    
    def check_win_diagonal_top_left_bottom_right(self):
        return(np.diag(self.board).sum() == self.player*3) 

    def check_win(self):
        return any([self.check_win_row(),
                    self.check_win_column(),
                    self.check_win_diagonal_top_left_bottom_right(),
                    self.check_win_diagonal_top_right_bottom_left()])
    
            
    def check_for_draw(self):
        if (self.board == 0).any():
            return False 
        else:
            if self.check_win():
                return False
            else:
                return True
            
    
     
        
  
    
game = TicTacToe()
game.play_game()