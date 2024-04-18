# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

def generateParenthesis(n):
    def backtrack(res, t, l, r):
        if l == 0 and r == 0:
            res.append(t)
            return

        if l > 0:
            t += '('
            backtrack(res, t, l-1, r)
            t = t[:-1]

        if r > 0 and l < r:
            t += ')'
            backtrack(res, t, l, r-1)
            t = t[:-1]

    res = []
    t = ''
    backtrack(res, t, n, n)
    return res


if __name__ == '__main__':
    print(generateParenthesis(3))
