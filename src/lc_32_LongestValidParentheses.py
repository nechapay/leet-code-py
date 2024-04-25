# Given a string containing just the characters '(' and ')', return the length of the longest
# valid(well-formed) parentheses substring.

def longestValidParentheses(s: str) -> int:
    arr = [0]*len(s)
    stk = []
    for i in range(len(s)):
        if s[i] == '(':
            stk.append(i)
        else:
            if stk:
                arr[i] = 1
                arr[stk.pop()] = 1

    mx = 0
    count = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            count += 1
        else:
            count = 0
        mx = count if mx < count else mx

    return mx


if __name__ == '__main__':
    print(longestValidParentheses("(()"))
    print(longestValidParentheses("()((((((()()"))
