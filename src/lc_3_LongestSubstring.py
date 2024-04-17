# Given a string s, find the length of the longest substring without repeating characters.

def lengthOfLongestSubstring(s):
    st = set()
    mx = 0
    prev = 0
    for current in range(len(s)):
        while s[current] in st:
            st.remove(s[prev])
            prev += 1
        st.add(s[current])
        mx = max(mx, current - prev + 1)

    return mx
