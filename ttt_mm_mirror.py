"""
Mini-max Tic-Tac-Toe Player
"""

import poc_ttt_gui
import poc_ttt_provided as provided

# Set timeout, as mini-max can take a long time
import codeskulptor
codeskulptor.set_timeout(60)

# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}

def mm_move(board, player):
    """
    Make a move on the board.
    
    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """
    terminal_state = board.check_win()
    if terminal_state in SCORES.keys():
        return SCORES[terminal_state], (-1, -1)
    else:
        poss_moves = board.get_empty_squares()
        best_perception = -2
        best_outcome = -2
        best_move = (-1, -1)
        for test_move in poss_moves:
            clone_board = board.clone()
            clone_board.move(test_move[0], test_move[1], player)
            next_player = provided.switch_player(player)
            (outcome, dummy_move) = mm_move(clone_board, next_player)
            player_perception = outcome * SCORES[player]
            if player_perception == 1:
                return outcome, test_move
            elif player_perception > best_perception: 
                best_perception = player_perception
                best_outcome = outcome
                best_move = test_move
        return best_outcome, best_move
            

def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]

# Test game with the console or the GUI.
# Uncomment whichever you prefer.

# provided.play_game(move_wrapper, 1, False)        
poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)
