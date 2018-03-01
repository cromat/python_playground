def is_isogram(string):
    string = string.lower()
    for ch in string:
        if ch.isalnum() and string.count(ch) > 1:
            return False
    return True
