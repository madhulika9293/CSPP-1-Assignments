'''
Tic-Tac-Toe game evaluator - takes the played game and decides a winning player
'''
def is_validgame(game):
    x_count, o_count = 0, 0
    for each_row in game:
        for each_box in each_row:
            if each_box == 'x':
                x_count += 1
            elif each_box == 'o':
                o_count += 1
            elif each_box == '.':
                pass
            else:
                return "invalid input"
    if abs(o_count - x_count) != 1:
        return "invalid game"
    return None

def row_chk(game):
    '''
    checks for winners in rows
    '''
    res = ''
    if set(game[0]) == {'o'} or set(game[1]) == {'o'} or set(game[2]) == {'o'}:
        res = 'o'
    if set(game[0]) == {'x'} or set(game[1]) == {'x'} or set(game[2]) == {'x'}:
        res = 'x'
    return res

def col_chk(game):
    '''
    checks for winners in columns
    '''
    res = ''
    col1 = [game[_][0] for _ in range(3)]
    col2 = [game[_][1] for _ in range(3)]
    col3 = [game[_][2] for _ in range(3)]
    if set(col1) == {'o'} or set(col2) == {'o'} or set(col3) == {'o'}:
        res = 'o'
    if set(col1) == {'x'} or set(col2) == {'x'} or set(col3) == {'x'}:
        res = 'x'
    return res

def diag_chk(game):
    '''
    checks for winners diagonally
    '''
    res = ''
    diag1 = [game[_][_] for _ in range(3)]
    diag2 = [game[i][2-i] for i in range(3)]
    if set(diag1) == {'o'} or set(diag2) == {'o'}:
        res = 'o'
    if set(diag1) == {'x'} or set(diag2) == {'x'}:
        res = 'x'
    return res

def winner(game):
    '''
    Takes the game input. Consists of 3 entries - 'o' for one player,
    'x' for another player and '.' to denote an empty space on the board.
    '''
    return is_validgame(game) or row_chk(game) or col_chk(game) or\
     diag_chk(game) or 'draw'

def main():
    '''
    Reads inputs and decides the winner
    '''
    game_inp = []
    for _ in range(3):
        game_inp.append(input().split(" "))
    print(winner(game_inp))

if __name__ == '__main__':
    main()
