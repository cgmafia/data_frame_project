import logging
from cache import InMemoryCache, DiskCache, RedisCache
from generator import DataGenerator
import time

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info("Starting the program...")

    # In-Memory Cache Example
    logger.info("\nUsing In-Memory Cache:")
    in_memory_cache = InMemoryCache()
    data_generator_memory = DataGenerator(cache=in_memory_cache)

    start_time = time.time()
    output = data_generator_memory.generate_pd_dataframe(0, 1, 1000, 100)
    logger.info(f"Time taken (first time): {time.time() - start_time:.2f} seconds")

    start_time = time.time()
    output2 = data_generator_memory.generate_pd_dataframe(0, 1, 1000, 100)
    logger.info(f"Time taken (cached): {time.time() - start_time:.2f} seconds")

    # Disk Cache Example
    logger.info("\nUsing Disk Cache:")
    disk_cache = DiskCache()
    data_generator_disk = DataGenerator(cache=disk_cache)

    start_time = time.time()
    output3 = data_generator_disk.generate_pd_dataframe(0, 2, 1000, 100)
    logger.info(f"Time taken (first time, disk cache): {time.time() - start_time:.2f} seconds")

    start_time = time.time()
    output4 = data_generator_disk.generate_pd_dataframe(0, 2, 1000, 100)
    logger.info(f"Time taken (cached on disk): {time.time() - start_time:.2f} seconds")

    # Redis Cache Example
    logger.info("\nUsing Redis Cache:")
    redis_cache = RedisCache()
    data_generator_redis = DataGenerator(cache=redis_cache)

    start_time = time.time()
    output5 = data_generator_redis.generate_pd_dataframe(0, 3, 1000, 100)
    logger.info(f"Time taken (first time, Redis cache): {time.time() - start_time:.2f} seconds")

    start_time = time.time()
    output6 = data_generator_redis.generate_pd_dataframe(0, 3, 1000, 100)
    logger.info(f"Time taken (cached in Redis): {time.time() - start_time:.2f} seconds")
