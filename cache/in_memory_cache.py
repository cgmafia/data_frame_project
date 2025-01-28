from typing import Any, Dict, Tuple
from .base_cache import Cache
import logging

logger = logging.getLogger(__name__)

class InMemoryCache(Cache):
    def __init__(self):
        self.cache: Dict[Tuple, Any] = {}

    def get(self, key: Tuple) -> Any:
        logger.info(f"Checking in-memory cache for key: {key}")
        return self.cache.get(key)

    def set(self, key: Tuple, value: Any) -> None:
        logger.info(f"Caching result in memory for key: {key}")
        self.cache[key] = value
