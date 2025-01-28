import pandas as pd
import numpy as np
from time import sleep
from typing import Tuple
from cache.base_cache import Cache
import logging

logger = logging.getLogger(__name__)

class DataGenerator:
    def __init__(self, cache: Cache):
        self.cache = cache

    def generate_pd_dataframe(self, mean: float, std: float, rows: int, columns: int) -> pd.DataFrame:
        key: Tuple = (mean, std, rows, columns)

        # Check cache
        cached_result = self.cache.get(key)
        if cached_result is not None:
            logger.info("Returning cached data.")
            return cached_result

        # Simulate a slow process
        logger.info("Cache miss. Generating new data.")
        sleep(5)  # Simulate delay
        data = pd.DataFrame(np.random.normal(mean, std, size=(rows, columns)))
        logger.info("Data generation complete.")

        # Cache the result
        self.cache.set(key, data)
        return data
