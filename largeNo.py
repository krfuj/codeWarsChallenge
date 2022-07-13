def max_no(n):
    """
    It takes a number, converts it to a string, sorts the string in reverse order, and then converts it
    back to a number
    
    :param n: The number to be sorted
    :return: The largest number that can be made from the digits of the number.
    """
    s = str(n)
    print(type(s))
    digits = sorted(s, reverse=n>0)
    return int(''.join(digits))

print(max_no(468035))