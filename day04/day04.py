from collections import Counter


def check_valid_password(y):
    x = str(y)
    condition_1 = len(x) == 6
    condition_2 = any([len(set(x[i:i+2])) == 1 for i in range(len(x) - 1)])
    condition_3 = all(x[i+1] >= x[i] for i in range(len(x) - 1))

    return(condition_1 and condition_2 and condition_3)


assert check_valid_password(111111) is True
assert check_valid_password(223450) is False
assert check_valid_password(122345) is True
assert check_valid_password(111111) is True

print(sum([check_valid_password(x) for x in range(153517, 630395, 1)]))


# problem 2
def check_valid_password2(y):
    x = str(y)
    condition_1 = len(x) == 6
    counts = Counter(list(x))
    condition_2 = any([v == 2 for v in counts.values()])
    condition_3 = all(x[i+1] >= x[i] for i in range(len(x) - 1))

    return(condition_1 and condition_2 and condition_3)


assert check_valid_password2(112233) is True
assert check_valid_password2(111122) is True
assert check_valid_password2(123444) is False

print(sum([check_valid_password2(x) for x in range(153517, 630395, 1)]))
