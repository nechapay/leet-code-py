# Given an integer x, return true if x is a palindrome, and false otherwise.

def isPalindrome(x):
    if x < 0:
        return False
    if x < 10:
        return True
    t = x
    y = 0
    while t > 0:
        digit = t % 10
        y = y * 10 + digit
        t = t // 10
    return x == y


if __name__ == '__main__':
    print(isPalindrome(121))
