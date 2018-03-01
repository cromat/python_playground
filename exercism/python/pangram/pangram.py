import string


def is_pangram(sentence):
    for ch in string.ascii_lowercase:
        if ch not in sentence.lower():
            return False
    return True
