# You are given a string s and an array of strings words. All the strings of words are of the same length.
# A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.
# For example, if words = ["ab", "cd", "ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab"
# are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of
# any permutation of words.
# Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.

def findSubstring(s, words):
    if not words or not s:
        return []

    result = []
    word_length = len(words[0])
    initial_hash = {}

    for word in words:
        if word in initial_hash:
            initial_hash[word] += 1
        else:
            initial_hash[word] = 1

    for i in range(word_length):
        left = i
        count = 0
        hash = {}

        for j in range(i, len(s) - word_length + 1, word_length):
            word = s[j:j + word_length]

            if word in initial_hash:
                hash[word] = hash.get(word, 0) + 1
                count += 1
                print(hash)
                while hash[word] > initial_hash[word]:
                    left_word = s[left: left + word_length]
                    hash[left_word] -= 1
                    left += word_length
                    count -= 1

                if count == len(words):
                    result.append(left)
            else:
                hash.clear()
                count = 0
                left = j + word_length

    return result


if __name__ == '__main__':
    print(findSubstring(
        "barfoothefoobarman", ["foo", "bar"]))
    print(findSubstring(
        "wordgoodgoodgoodbestword", ["word", "good", "best", "good"])
    )
