import json

import redis
from config.app_logger import logger


MINUTE = 60
MONTHLY_TTL = 30 * 86400
WEEKLY_TTL = 7 * 86400
DAILY_TTL = 86400

host = ""
username = ""
password = ""
port = ""
db_index = 0
redis_ssl = False



class RedisCache:
    def __init__(self):
        self.log = logger
        self.redis_client = redis.Redis(
            host=host,
            port=port,
            username=username,
            password=password,
            decode_responses=True,
            db=db_index,
            ssl=redis_ssl
        )
        self.log.info(self.redis_client.ping())

    def set(self, key: str, value: any, duration: int = MONTHLY_TTL) -> bool:
        if isinstance(value, (list, dict)):
            value = json.dumps(value, default=str)
        return self.redis_client.set(key, value, ex=duration)

    def get(self, key: str) -> any:
        value = self.redis_client.get(key)
        return json.loads(value)
    def delete(self, key: str) -> int:
        return self.redis_client.delete(key)

redis_db = RedisCache()