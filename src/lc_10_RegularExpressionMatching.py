# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string(not partial).

def isMatch(s: str, p: str) -> bool:
    if not p or p[0] == '*':
        return False

    m = len(s)
    n = len(p)
    dp = [[False for x in range(n+1)] for y in range(m+1)]
    dp[0][0] = True

    for j in range(1, n+1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if s[i-1] == p[j-1] or p[j-1] == '.':
                dp[i][j] = dp[i-1][j-1]
            elif p[j-1] == '*':
                dp[i][j] = dp[i][j-2]
                if s[i-1] == p[j-2] or p[j-2] == '.':
                    dp[i][j] = dp[i][j] or dp[i-1][j]

    return dp[m][n]


def print_matrix(mtx, s=''):
    print(s)
    for i in range(len(mtx)):
        print('|', end=" ")
        for j in range(len(mtx[i])):
            elem = 1 if mtx[i][j] else 0
            print(elem, end=" ")
        print("|")
    return ''


if __name__ == '__main__':
    print(isMatch("ab", ".*"))
