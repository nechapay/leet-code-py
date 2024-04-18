# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

def isValid(s):
    p = {
        '(': ')',
        '{': '}',
        '[': ']',
    }
    stk = []

    for l in s:
        if not stk and l not in p:
            return False
        if l in p:
            stk.append(l)
        else:
            if l != p[stk[-1]]:
                return False
            else:
                stk.pop()

    return not stk


if __name__ == '__main__':
    print(isValid("()[]{}"))
