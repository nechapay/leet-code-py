# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
# or -1 if needle is not part of haystack.

def strStr(haystack, needle):
    l = len(needle)
    for i in range(len(haystack) - l + 1):
        s = haystack[i:i+l]
        if s == needle:
            return i
    return -1


def strStrKMP(haystack, needle):
    haystack_len = len(haystack)
    needle_len = len(needle)
    res = []
    lps = [0]*needle_len

    prev = 0
    lps[0] = 0
    i = 1
    while i < needle_len:
        if needle[i] == needle[prev]:
            prev += 1
            lps[i] = prev
            i += 1
        else:
            if prev != 0:
                prev = lps[prev-1]
            else:
                lps[i] = 0
                i += 1

    i = 0
    np = 0
    while (haystack_len - i) >= (needle_len - np):
        if needle[np] == haystack[i]:
            i += 1
            np += 1

        if np == needle_len:
            res.append(i-np)
            np = lps[np-1]

        elif i < haystack_len and needle[np] != haystack[i]:
            if np != 0:
                np = lps[np-1]
            else:
                i += 1
    return -1 if not res else res[0]


if __name__ == '__main__':
    print(strStr('sadbutsad', "sad"))
    print(strStrKMP("aabaaabaaac", "aabaaac"))
