
import redis
from dotenv import load_dotenv
import os 



load_dotenv(dotenv_path='../.flaskenv')
r = redis.Redis(
    host=os.getenv('REDIS_HOST'), port=os.getenv('REDIS_PORT'),
    username=os.getenv('REDIS_USERNAME'), # use your Redis user. More info https://redis.io/docs/latest/operate/oss_and_stack/management/security/acl/
    password=os.getenv('REFIS_PASSWORD'), # use your Redis password
    # ssl=True,
    # ssl_certfile="./redis_user.crt",
    # ssl_keyfile="./redis_user_private.key",
    # ssl_ca_certs="./redis_ca.pem",
)
# r.lpush('try','aaa')
# r.rpush('try','bbb')
session_id ="seesionId"
# r.rpush(session_id,'你好嗎')
# r.rpush(session_id,'我很好')
r.rpop(session_id)
# True
elements = r.lrange(session_id, 0, -1)
elements = [elem.decode('utf-8') for elem in elements]
print(elements)
# elements = [elem.decode('utf-8') for elem in elements]
# print(elements)