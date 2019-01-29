from jose import jwt, JWTError
import bcrypt
import datetime as dt
import time


def generate_token(username, key):
    today = time.mktime(dt.date.today().timetuple())
    today_plus_seven = (dt.date.today() + dt.timedelta(days=7)).timetuple()
    payload = {
        "iss": "overwatch_data",
        "exp": time.mktime(today_plus_seven),
        "iat": today,
        "aud": "ow:key"
    }
    return jwt.encode(payload, key, algorithm='HS256')

def verify_token(token, key):
    try:
        token = jwt.decode(token, key, audience="ow:key", algorithms=['HS256'])
    except JWTError as e:
        token = e
    return token

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def unhash_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

def check_token(token, key):
    decoded = verify_token(token, key)
    if 'iss' in decoded:
        return True
    else:
        return False