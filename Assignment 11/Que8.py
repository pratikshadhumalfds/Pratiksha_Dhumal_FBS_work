###Print 1 to 100 in snakes and ladder pattern.

# Using built-in functions
def print_snakes_and_ladders_builtin():
    size = 10
    current = 1
    board = []

    for row in range(size):
        line = [current + i for i in range(size)]
        current += size
        if row % 2 == 1:
            line.reverse() 
        board.append(line)

    for row in reversed(board):  
        print(' '.join(f"{num:3}" for num in row))

print("Snakes and Ladders (with built-in functions):")
print_snakes_and_ladders_builtin()



# Without using built-in functions
def print_snakes_and_ladders_no_builtin():
    size = 10
    board = []
    current = 1
    row = 0

    while row < size:
        line = []
        col = 0
        while col < size:
            line.append(current)
            current += 1
            col += 1

        if row % 2 == 1:
            reversed_line = []
            i = len(line) - 1
            while i >= 0:
                reversed_line.append(line[i])
                i -= 1
            line = reversed_line

        board.append(line)
        row += 1

    row = len(board) - 1
    while row >= 0:
        line = board[row]
        col = 0
        while col < len(line):
            num = line[col]
            if num < 10:
                print("  " + str(num), end=' ')
            elif num < 100:
                print(" " + str(num), end=' ')
            else:
                print(str(num), end=' ')
            col += 1
        print()
        row -= 1

print("\nSnakes and Ladders (without built-in functions):")
print_snakes_and_ladders_no_builtin()

