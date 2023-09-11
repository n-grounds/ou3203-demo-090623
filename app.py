
def is_palindrome(string):
    for i, c in enumerate(string):
        if string[i] == string[len(string)-i-1]:
            return True
    return False
