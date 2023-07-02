import jwt
import datetime

def create_token(user_id,secret_key,expires_in_minutes = 60):
    payload = {
        'user_id': user_id,
        'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=expires_in_minutes)
    }

    token = jwt.encode(payload,secret_key,algorithm='HS256')
    return token

user_id = 123
# secret_key = 'your_secret_key'
secret_key = 'a'

token = create_token(user_id, secret_key)
print(token)