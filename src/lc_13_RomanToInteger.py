# Given a roman numeral, convert it to an integer.
def romanToInt(s):
    s = s.upper()
    roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    n = len(s)
    result = roman[s[-1]]
    for i in range(n-2, -1, -1):
        current = roman[s[i]]
        next = roman[s[i+1]]

        if current < next:
            result -= current
        else:
            result += current
    return result


if __name__ == '__main__':
    print(romanToInt("MCMXCIV"))
