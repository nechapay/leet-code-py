# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
# (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows)
def convert(s, numRows):
    if numRows == 1 or not s:
        return s

    result = ''
    n = len(s)
    dx = 2*numRows - 2

    for i in range(numRows):
        j = 0
        while j + i < n:
            result += s[i+j]
            if i != 0 and i != numRows - 1 and j + dx - i < n:
                result += s[j + dx - i]
            j += dx

    return result

if __name__ == '__main__':
    print(convert('PAYPALISHIRING', 3))
