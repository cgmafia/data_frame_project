from typing import Any, Tuple

class Cache:
    def get(self, key: Tuple) -> Any:
        """
        Retrieve the value for a given key from the cache.
        """
        raise NotImplementedError

    def set(self, key: Tuple, value: Any) -> None:
        """
        Store the value for a given key in the cache.
        """
        raise NotImplementedError
