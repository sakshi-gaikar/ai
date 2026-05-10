def safe(r, c):
    for i in range(r):
        if board[i] == c or abs(board[i]-c) == abs(i-r):
            return False
    return True


def solve(r):
    global n, board

    if r == n:
        print(board)
        return

    for c in range(n):

        if safe(r, c):   # bound (pruning unsafe choices)

            board[r] = c  # place queen

            solve(r + 1)  # next row

            board[r] = -1  # backtrack


n = 4
board = [-1] * n

solve(0)