
from django.core.cache import cache
from redis import ConnectionError

from authapp.Utils.key_generators import make_key


def cache_it(key_prefix=None, timeout=None):
    def cache_it_decorator(func):
        cache_key_prefix = key_prefix or func.__name__

        def cache_it_wrapper(*args, **kwargs):
            delete_this = kwargs.pop('deleteThis', False)
            dummy_args = list(args)
            dummy_args.extend(kwargs.values())
            cache_key = "{}:{}".format(cache_key_prefix, make_key(*dummy_args))
            try:
                if delete_this:
                    cache.delete(cache_key)
                    return None
                result = cache.get(cache_key)
                if not result:
                    result = func(*args, **kwargs)
                    cache.set(cache_key, result, timeout)
            except ConnectionError as err:
                if delete_this:
                    return None
                return func(*args, **kwargs)
            return result

        return cache_it_wrapper

    return cache_it_decorator
