
import app

###########################
# unit tests for the is_palindrome
# function
###########################

if app.is_palindrome( 'mom' ):
    print('Test passed')
else:
    print('Test failed')

if app.is_palindrome( 'dog' ):
    print('Test failed')
else:
    print('Test passed')

if app.is_palindrome( 'robber' ):
    print('Test failed')
else:
    print('Test passed')

if app.is_palindrome( 'i' ):
    print('Test passed')
else:
    print('Test failed')
