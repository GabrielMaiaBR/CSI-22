def check_character(string1, string2):
    for char in string1:
        if char not in string2:
            return False
    return True