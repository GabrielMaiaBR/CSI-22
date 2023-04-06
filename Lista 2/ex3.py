def alphanum_strings(strings):

    valid_strings = []
    for s in strings:
        has_alpha = False
        has_digit = False
        for c in s:
            if c.isalpha():
                has_alpha = True
            elif c.isdigit():
                has_digit = True
        if has_alpha and has_digit:
            valid_strings.append(s)
    return valid_strings