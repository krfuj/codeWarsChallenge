import re

def validate_pin(pin):
    """
    If the pin is 4 or 6 digits long, return True, otherwise return False
    
    :param pin: a string of 4 or 6 digits
    :return: True or False
    """
    if re.fullmatch("\d{4}|\d{6}", pin):
        return True
    else:
        return False