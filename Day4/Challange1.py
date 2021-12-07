with open('data.txt') as f:
    data = f.read().strip().split()

numbers = data[0]
data.pop(0)

tmpboards = [data[x:x + 25] for x in range(0, len(data), 25)]
boards = []

for board in tmpboards:
    boards.append({}.fromkeys(board, False))

for n in numbers:
    for board in boards:
        if n in board:
            board[n] = True


# WIP