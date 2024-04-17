# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer
# (similar to C/C++'s atoi function).

# The algorithm for myAtoi(string s) is as follows:

# 1. Read in and ignore any leading whitespace.
# 2. Check if the next character(if not already at the end of the string) is '-' or '+'.
# Read this character in if it is either. This determines if the final result is negative or positive respectively.
# Assume the result is positive if neither is present.
# 3. Read in next the characters until the next non-digit character or the end of the input is reached.
# The rest of the string is ignored.
# 4. Convert these digits into an integer(i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0.
# Change the sign as necessary(from step 2).
# 5. If the integer is out of the 32-bit signed integer range[-231, 231 - 1], then clamp the integer so that
# it remains in the range. Specifically, integers less than - 231 should be clamped to - 231,
# and integers greater than 231 - 1 should be clamped to 231 - 1.
# 6. Return the integer as the final result.
# Note:

# Only the space character ' ' is considered a whitespace character.
# Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.

def myAtoi(s: str) -> int:
    if not s:
        return 0
    st = ''
    sign = 1
    signed = False

    for i in range(len(s)):
        if s[i] == ' ' and not st:
            if signed:
                return 0
            continue
        if (s[i] == '-' or s[i] == '+') and not st:
            if signed:
                return 0
            sign = -1 if s[i] == '-' else 1
            signed = True
            continue
        if s[i].isdigit():
            st += s[i]
        else:
            break
        if signed and not st:
            return 0
    if not st:
        return 0
    result = sign * int(st)
    result = 2**31 - 1 if result > 2**31 - 1 else result
    result = -2**31 if result < -2**31 else result
    return result


if __name__ == '__main__':
    print(myAtoi("  -42"))
