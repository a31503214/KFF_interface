
import redis


re = redis.Redis(host="localhost",port=6379,db=0)
re.set("key_name01","value_tom01")
print(re.get("key_name01"))