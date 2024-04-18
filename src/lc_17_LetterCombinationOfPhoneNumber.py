# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that
# the number could represent. Return the answer in any order.
# A mapping of digits to letters(just like on the telephone buttons) is given below.
# Note that 1 does not map to any letters.

def letterCombinations(digits):
    if len(digits) == 0:
        return []
    phoneMap = ('abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz')

    def backtrack(combination, nextDigits, phoneMap, output):
        if len(nextDigits) == 0:
            output.append(combination)
        else:
            letters = phoneMap[int(nextDigits[0]) - 2]
            for letter in letters:
                backtrack(combination+letter, nextDigits[1:], phoneMap, output)

    result = []
    backtrack('', digits, phoneMap, result)
    return result


if __name__ == '__main__':
    print(letterCombinations("23"))
