import redis
import pickle
from typing import Any, Tuple
from .base_cache import Cache
import logging

logger = logging.getLogger(__name__)

class RedisCache(Cache):
    def __init__(self, host: str = "localhost", port: int = 6379, db: int = 0):
        self.redis_client = redis.StrictRedis(host=host, port=port, db=db, decode_responses=False)

    def get(self, key: Tuple) -> Any:
        cache_key = str(hash(key))
        logger.info(f"Checking Redis cache for key: {cache_key}")
        result = self.redis_client.get(cache_key)
        if result:
            logger.info("Cache hit in Redis.")
            return pickle.loads(result)
        logger.info("Cache miss in Redis.")
        return None

    def set(self, key: Tuple, value: Any) -> None:
        cache_key = str(hash(key))
        logger.info(f"Caching result in Redis for key: {cache_key}")
        self.redis_client.set(cache_key, pickle.dumps(value))
