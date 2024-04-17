# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

def longestCommonPrefix(strs):
    n = len(strs)
    if not n:
        return ""

    j = 0
    pref = ''
    res = ''
    all = True

    while j < len(strs[0]):
        pref = strs[0][:j+1]
        for i in range(1, n):
            p = strs[i][:j+1]
            if p != pref:
                all = False
                break
        j += 1
        if all:
            res = pref
        else:
            break

    return res


if __name__ == '__main__':
    print(longestCommonPrefix(["flower", "flow", "flight"]))
