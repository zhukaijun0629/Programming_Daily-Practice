import string


def countCounterfeit(serialNumber):

    valid_amount = 0

    tests = [test1, test2, test3, test4, test5]

    for num in serialNumber:
        test_score = 0
        for test in tests:
            print(test(num))
            if not test(num):
                break
            test_score += 1
        if test_score == 5:
            valid_amount += getAmount(num)

    return valid_amount


def test1(num):
    return 10 <= len(num) <= 12


def test2(num):
    first_three = set(num[:3])

    if len(first_three) < 3:
        return False

    for char in first_three:
        if char not in string.ascii_uppercase:
            return False

    return True


def test3(num):
    year_printed = num[3:7]

    for char in year_printed:
        if not char.isdigit():
            return False

    return 1900 <= int(year_printed) <= 2019


def test4(num):
    amount = num[7:-1]
    valid = {'10', '20', '50', '100', '200', '500', '1000'}
    if amount in valid:
        return True
    return False


def test5(num):
    return num[-1] in string.ascii_uppercase


def getAmount(num):
    return int(num[7:-1])


print(countCounterfeit(['ABC19001000Z']))
