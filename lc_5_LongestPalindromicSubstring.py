# Given a string s, return the longest palindromic substring in s.
def longestPalindrome(s):
    st = list(s)
    st2 = ['#']*(len(s)*2 + 1)

    for i in range(len(st)):
        st2[2*i+1] = st[i]
    p = [0]*len(st2)
    c = r = idx = mx = i_mir = 0
    for i in range(len(st2)):
        i_mir = 2*c - i

        p[i] = min(p[i_mir], r-i) if r > i else 0

        while i > p[i] and i + 1 + p[i] < len(st2) and st2[i-1-p[i]] == st2[i+1 + p[i]]:
            p[i] += 1
        if p[i] + i > r:
            r = p[i]+i
            c = i

        if mx < p[i]:
            idx = i
            mx = p[i]

    return ''.join(list(''.join(st2)[idx-mx:idx+mx].split('#')))


def longestPalindrome2(s):
    n = len(s)
    res = ''

    def backtrack(left, right):
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]
    for i in range(n):
        res = max(res, backtrack(i, i), backtrack(i, i+1), key=len)
    return res


if __name__ == '__main__':
    print(longestPalindrome('aabba'))
    print(longestPalindrome2('aabba'))
