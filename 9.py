# 9. N-Queens

def is_safe(row, col, n, pos):
    for i in range(row):
        if pos[i] == col or abs(pos[i] - col) == row - i:
            return False
    return True


def n_queens(n, row=0, pos=[]):
    if row == n:
        return [pos]

    solutions = []
    for col in range(n):
        if is_safe(row, col, n, pos):
            new_pos = pos + [col]
            solutions += n_queens(n, row + 1, new_pos)
    return solutions


def print_solution(solution):
    print("solution:", solution)
    n = len(solution)
    for row in solution:
        print(". " * (row) + "Q " + ". " * (n - row-1))


solutions = n_queens(4)
for solution in solutions:
    print_solution(solution)
    print()
