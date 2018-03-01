passwords = ["asdFghjk", "asd3fGhjk", "123aSdfghjk", "asd6H"]

def is_valid_pass(pasw):
    if len(pasw) < 8:
        return False
    if not any(a.isupper() for a in pasw):
        return False
    if not any(a.isdigit() for a in pasw):
        return False
    # Ovo moze jednostavnije sa re.split()
    for ch in pasw:
        if ch.isdigit():
            str1, str2 = pasw.split(ch)
            if not str1.isalpha() and not str2.isalpha():
                return False
    return True

for pasw in passwords:
    if is_valid_pass(pasw):
        print(pasw)
