'''
Tic-Tac-Toe game evaluator - takes the played game and decides a winning player
'''
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

def winner(game):
    '''
    Takes the game input. Consists of 3 entries - 'o' for one player,
    'x' for another player and '.' to denote an empty space on the board.
    '''
    if row_chk(game) == 'o' or col_chk(game) == 'o' or diag_chk(game) == 'o':
        winner1 = 'o'
    else:
        winner1 = None
    if row_chk(game) == 'x' or col_chk(game) == 'x' or diag_chk(game) == 'x':
        winner2 = 'x'
    else:
        winner2 = None
    if winner1 == 'o' and winner2 == 'x':
        return "invalid game"
    if winner1 == 'o' and winner2 is None:
        return 'o'
    if winner1 is None and winner2 == 'x':
        return 'x'
def main():
    '''
    Reads inputs and decides the winner
    '''
    game_inp = []
    for _ in range(3):
        game_inp.append(input().split(" "))
        if game_inp[_][0] not in 'xo.' or game_inp[_][1] not in 'xo.' or game_inp[_][2] not in 'xo.':
            print(game_inp[_])
            return "invalid input"
    print(game_inp)
    # return winner(game_inp)     

if __name__ == '__main__':
    main()
