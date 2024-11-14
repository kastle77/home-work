from gc import get_referents


def get_multiplied_digits(number):
    str_number = str(number)
    if len(str_number) > 1:
        first = int(str_number[0])
        if int(str_number[-1]) == 0:
            return get_multiplied_digits(str_number[0:-1])
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return int(str_number)
result = get_multiplied_digits(40203)

print(result)
