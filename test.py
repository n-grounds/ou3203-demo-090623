
import app

test_cases = [
    ('mom', True),
    ('dog', False),
    ('robber', False),
    ('i', True),
    ('mm', True),
    ('my', False),
    ('_+_', True),
    ('Aa', False)
 ]
for test_value, expected_result in test_cases:
    if app.is_palindrome(test_value) == expected_result:
        print('Test passed')
    else:
        print('Test failed')