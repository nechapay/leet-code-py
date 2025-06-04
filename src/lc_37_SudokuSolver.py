from collections import defaultdict, deque


def solveSudoku(board):
    rows, cols, block, seen = defaultdict(
        set), defaultdict(set), defaultdict(set), []

    for i in range(9):
        for j in range(9):
            el = board[i][j]
            if el != '.':
                rows[i].add(el)
                cols[j].add(el)
                block[(i // 3) * 3 + j // 3].add(el)
            else:
                seen.append((i, j))

    def dfs(index):
        if index == len(seen):
            return True

        r, c = seen[index]
        t = (r // 3) * 3 + c // 3
        for n in "123456789":
            if n not in rows[r] and n not in cols[c] and n not in block[t]:
                board[r][c] = n
                rows[r].add(n)
                cols[c].add(n)
                block[t].add(n)

                if dfs(index + 1):
                    return True

                board[r][c] = '.'
                rows[r].discard(n)
                cols[c].discard(n)
                block[t].discard(n)

        return False

    dfs(0)


if __name__ == '__main__':
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8",
                                                                                                                                                                                                          ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    solveSudoku(board)
    print(board)
