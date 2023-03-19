def sum_of_string_digits(string):
    sum_digit = 0
    for x in string:
        if x.isnumeric() == True:
            z = int(x)
            sum_digit = sum_digit + z
    return sum_digit