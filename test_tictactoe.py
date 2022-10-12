from tictactoe import TicTacToe
import pytest
def test_board_is_empty_and_player_is_1_at_start():
    game = TicTacToe()
    assert (game.board == 0).all()
    assert game.board.shape == ((3,3))
    assert game.player == 1

def test_position_is_filled():
    game = TicTacToe()
    game.make_a_move(1,(1,1))
    assert game.board[1,1] == 1

@pytest.mark.parametrize("location",[(1,1),(1,2),(2,2)])
def test_value_error_when_space_already_filled(location):
    game = TicTacToe()
    game.make_a_move(1,location)
    with pytest.raises(ValueError):
        game.make_a_move(1,location)

@pytest.mark.parametrize("player",[1, -1])
@pytest.mark.parametrize("location, expected",[((1,0), True),
                                               ((2,2),False)])
def test_check_who_won_row(location, expected, player):
    game = TicTacToe()
    game.player = player
    game.make_a_move(player,(location))
    game.make_a_move(player,(1,1))
    game.make_a_move(player,(1,2))
    x = game.check_win()
    assert x == expected
    
@pytest.mark.parametrize("player",[1, -1])
@pytest.mark.parametrize("location, expected",[((0,2), True),
                                               ((2,1),False)])
def test_check_who_won_column(location, expected, player):
    game = TicTacToe()
    game.player = player
    game.make_a_move(player, (location))
    game.make_a_move(player,(1,2))
    game.make_a_move(player,(2,2))
    x = game.check_win()
    assert x == expected

@pytest.mark.parametrize("player",[1, -1])    
@pytest.mark.parametrize("location, expected",[((0,2), True),
                                               ((2,1),False)])
def test_check_who_won_diagonal_top_right_bottom_left(location, expected, player):
    game = TicTacToe()
    game.player = player
    game.make_a_move(player, (location))
    game.make_a_move(player,(1,1))
    game.make_a_move(player,(2,0))
    x = game.check_win()
    assert x == expected
    
@pytest.mark.parametrize("player",[1, -1])
@pytest.mark.parametrize("location, expected",[((2,2), True),
                                               ((2,1),False)])
def test_check_who_won_diagonal_top_left_bottom_right(location, expected, player):
    game = TicTacToe()
    game.player = player
    game.make_a_move(player, (location))
    game.make_a_move(player,(1,1))
    game.make_a_move(player,(0,0))
    x = game.check_win()
    assert x == expected

@pytest.mark.parametrize("symbol, expected", [(-1,True),(1,False),(0, False)])
def test_check_for_draw(expected, symbol):
    game = TicTacToe()
    game.make_a_move(1,(0,1))
    game.make_a_move(1,(0,0))
    game.make_a_move(1,(2,1))
    game.make_a_move(1,(1,2))
    game.make_a_move(1,(2,0))
    game.make_a_move(-1,(1,1))
    game.make_a_move(symbol,(0,2))
    game.make_a_move(-1,(1,0))
    game.make_a_move(-1,(2,2))
    x = game.check_for_draw()
    assert x == expected

