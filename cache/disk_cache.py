import os
import pickle
from typing import Any, Tuple
from .base_cache import Cache
import logging

logger = logging.getLogger(__name__)

class DiskCache(Cache):
    def __init__(self, directory: str = "cache"):
        self.directory = directory
        os.makedirs(self.directory, exist_ok=True)

    def get(self, key: Tuple) -> Any:
        filepath = os.path.join(self.directory, f"{hash(key)}.pkl")
        logger.info(f"Checking disk cache for key: {key}")
        if os.path.exists(filepath):
            with open(filepath, "rb") as f:
                logger.info("Cache hit on disk.")
                return pickle.load(f)
        logger.info("Cache miss on disk.")
        return None

    def set(self, key: Tuple, value: Any) -> None:
        filepath = os.path.join(self.directory, f"{hash(key)}.pkl")
        logger.info(f"Caching result to disk for key: {key}")
        with open(filepath, "wb") as f:
            pickle.dump(value, f)
