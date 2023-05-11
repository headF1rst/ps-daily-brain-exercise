def check_win(player, board):
    for i in range(3):
        if all(cell == player for cell in board[i]):
            return True
    
    for j in range(3):
        if all(board[i][j] == player for i in range(3)):
            return True
    
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    
    return False

def solution(board):
    o_cnt, x_cnt = 0, 0
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O':
                o_cnt += 1
            elif board[i][j] == 'X':
                x_cnt += 1
    
    if x_cnt > o_cnt or abs(x_cnt - o_cnt) > 1:
        return 0
    if (check_win('O', board) and x_cnt != o_cnt - 1) or (check_win('X', board) and x_cnt != o_cnt):
        return 0
    return 1
    
    