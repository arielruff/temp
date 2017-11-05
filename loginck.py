from functools import wraps
from flask import redirect
from flask import session as login_session

def login_check(l):
    '''Checks to see whether a user is logged in'''
    @wraps(l)
    def x(*args, **kwargs):
        if 'username' not in login_session:
            return redirect('/login')
        return l(*args, **kwargs)
    return x