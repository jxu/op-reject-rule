from number import memoize

@memoize
def make_string(pos, has_leading, has_0, has_1, has_A):
    if pos == 0:
        return has_leading and has_0 and has_1 and has_A


    next_has_0 = True if has_leading else has_0  # 0 must be after a leading digit
    strings = make_string(pos-1, has_leading, next_has_0, has_1, has_A)  # Append 0

    strings += make_string (pos-1, True, has_0, True, has_A)  # Append 1
    strings += make_string(pos-1, True, has_0, has_1, True)  # Append A
    strings += 13*make_string(pos-1, True, has_0, has_1, has_A)  # Append other digits

    return strings


strings = make_string(16, False, False, False, False)
print(hex(strings)[2:].upper())