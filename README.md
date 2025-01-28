# Data Generator with Modular Caching System🚀

This Python project provides a modular, scalable solution for generating data with caching mechanisms to optimize performance. The project supports **in-memory caching**, **disk-based caching**, and **Redis caching** while demonstrating a clean separation of concerns and adherence to SOLID principles.

---

## Features

- **Data Generation**: Simulates a slow process for generating random Pandas DataFrames.
- **Caching Support**: 
  - **In-Memory Cache**: Stores data in Python dictionaries for fast access.
  - **Disk Cache**: Stores data as files on the disk for persistence across program runs.
  - **Redis Cache**: Leverages Redis for distributed caching.
- **Extensibility**: Easily add new caching mechanisms by extending the base `Cache` class.
- **Logging**: Progress is logged to the console to monitor caching operations and data generation.

---

## Project Structure

```
data_generator_project/
├── cache/
│   ├── __init__.py            # Initializes the caching module
│   ├── base_cache.py          # Base Cache interface
│   ├── in_memory_cache.py     # In-Memory Cache implementation
│   ├── disk_cache.py          # Disk Cache implementation
│   ├── redis_cache.py         # Redis Cache implementation
├── generator/
│   ├── __init__.py            # Initializes the generator module
│   ├── data_generator.py      # DataGenerator class with caching
├── main.py                    # Entry point demonstrating usage
├── requirements.txt           # Project dependencies
└── README.md                  # Documentation
```

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/data-generator-caching.git
   cd data-generator-caching
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. (Optional) Start a Redis server if using Redis caching:
   - On Linux/Mac:
     ```bash
     redis-server
     ```
   - On Windows, follow [Redis for Windows installation guide](https://github.com/microsoftarchive/redis/releases).

---

## Usage

1. Run the `main.py` file:
   ```bash
   python main.py
   ```

2. The script demonstrates:
   - Using In-Memory Cache
   - Using Disk Cache
   - Using Redis Cache

3. Check the logs in the console to see the caching operations and performance improvements.

---

## Example Output

```
2025-01-27 12:34:56 - INFO - Starting the program...

2025-01-27 12:34:56 - INFO - Using In-Memory Cache:
2025-01-27 12:34:56 - INFO - Cache miss. Generating new data.
2025-01-27 12:35:01 - INFO - Data generation complete.
2025-01-27 12:35:01 - INFO - Time taken (first time): 5.01 seconds
2025-01-27 12:35:01 - INFO - Returning cached data.
2025-01-27 12:35:01 - INFO - Time taken (cached): 0.00 seconds

...

```

---

## Dependencies

- Python 3.8+
- [Pandas](https://pandas.pydata.org/)
- [NumPy](https://numpy.org/)
- [Redis](https://redis.io/) (if using Redis caching)

---

## Extending the Project

1. To add a new caching mechanism:
   - Create a new file in the `cache/` directory (e.g., `my_custom_cache.py`).
   - Extend the `Cache` class and implement `get` and `set` methods.
   - Register your custom cache in `main.py`.

2. To improve logging or error handling:
   - Update the logging configuration in `main.py`.
   - Use `try-except` blocks in cache methods to handle errors.

---

## License

This project is licensed under the MIT License. See `LICENSE` for details.

### `requirements.txt`

```plaintext
pandas==1.5.3
numpy==1.24.3
redis==5.0.0
```
