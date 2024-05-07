"""
Hi, here's your problem today. This problem was recently asked by Amazon:

Given a string that may represent a number, determine if it is a number. Here's some of examples of how the number may be presented:
"123" # Integer
"12.3" # Floating point
"-123" # Negative numbers
"-.3" # Negative floating point
"1.5e5" # Scientific notation

Here's some examples of what isn't a proper number:
"12a" # No letters
"1 2" # No space between numbers
"1e1.2" # Exponent can only be an integer (positive or negative or 0)
Scientific notation requires the first number to be less than 10, however to simplify the solution assume the first number can be greater than 10. Do not parse the string with int() or any other python functions.

"""


def parse_number(s):
    # Fill this in.
    def isInteger(s):
        if not s or s == "-" or s == '+':
            return False
        if s[0] in '+-':
            s = s[1:]
        return all(c.isdigit() for c in s)

    def isDecimal(s):
        if not s or '.' not in s or s == ".":
            return False
        if s[0] in '+-':
            s = s[1:]
        s_parts = s.split(".", 1)
        if isInteger("+"+s_parts[0]) and not s_parts[1]:
            return True
        elif not s_parts[0] and isInteger("+"+s_parts[1]):
            return True
        elif isInteger("+"+s_parts[0]) and isInteger("+"+s_parts[1]):
            return True
        return False

    def isENumber(s):
        if not s or s == "E":
            return False
        s = s.replace('e', 'E')
        if 'E' not in s:
            return False
        s_parts = s.split('E', 1)
        return (isDecimal(s_parts[0]) or isInteger(s_parts[0])) and isInteger(s_parts[1])

    if not s:
        return False
    return isENumber(s) or isDecimal(s) or isInteger(s)


print(parse_number("12.3"))
# True

print(parse_number("12a"))
# False
