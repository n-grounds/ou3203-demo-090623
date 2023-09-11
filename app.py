
def is_palindrome(string):
    """ Return whether (True/False)
        the given string is a
        palindrome (the same forwards
        and backwards)"""
    for i, c in enumerate(string):
        if string[i] != string[len(string)-i-1]:
            return False
    return True
