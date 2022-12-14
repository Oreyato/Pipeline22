from datetime import datetime


decorator_cache = {}


def cache(func):
    def cache_wrapped(*args, **kwargs):
        print('v CACHE INFOS ======================================')
        if decorator_cache.get(func.__name__) is None:
            result = func(*args, **kwargs)

            decorator_cache[func.__name__] = {args: result}

            print(f'Add new cache object: {decorator_cache}')

            print('^ CACHE INFOS ======================================')
            return result
        else:
            if decorator_cache.get(func.__name__).get(args) is None:
                result = func(*args, **kwargs)

                decorator_cache[func.__name__] = {args: result}

                print(f'Add new cache object: {decorator_cache.get(func.__name__)}'
                      f'\nunder "{func.__name__}"')

                print('^ CACHE INFOS ======================================')
                return result
            else:
                print("Cache object found, directly return result")
                print('^ CACHE INFOS ======================================')
                return decorator_cache.get(func.__name__).get(args)

    return cache_wrapped


def cache_light(func):
    def cache_wrapped(*args, **kwargs):
        if decorator_cache.get(func.__name__) is None:
            result = func(*args, **kwargs)
            decorator_cache[func.__name__] = {args: result}
            return result
        else:
            if decorator_cache.get(func.__name__).get(args) is None:
                result = func(*args, **kwargs)
                decorator_cache[func.__name__] = {args: result}
                return result
            else:
                return decorator_cache.get(func.__name__).get(args)
    return cache_wrapped


def execution_time(func):
    def exec_time_wrapped(*args, **kwargs):
        start_time = datetime.now()

        result = func(*args, **kwargs)

        end_time = datetime.now()
        delta = end_time - start_time
        delta_sec = delta.total_seconds()

        if delta_sec == 0.0:
            print(f'\n================================================='
                  f'\n'
                  f'"{func.__name__}" process was too quick to calculate its speed'
                  f'\n================================================='
                  f'\n')
        else:
            print(f'\n================================================='
                  f'\n'
                  f'"{func.__name__}" process took {delta_sec} seconds'
                  f'\n================================================='
                  f'\n')
        return result
    return exec_time_wrapped


def execution_time_light(func):
    def exec_time_l_wrapped(*args, **kwargs):
        start_time = datetime.now()

        result = func(*args, **kwargs)

        end_time = datetime.now()
        delta = end_time - start_time
        delta_sec = delta.total_seconds()

        if delta_sec == 0.0:
            print(f'"{func.__name__}" process was too quick to calculate its speed')
        else:
            print(f'"{func.__name__}" process took {delta_sec} seconds')
        return result
    return exec_time_l_wrapped


if __name__ == '__main__':
    #@execution_time_light
    @cache
    #@execution_time
    def test(integer):
        iiis = []

        for i in range(1000000):
            iiis.append(i)

        # print(iiis)
        return integer+10

    print(f'First pass: {test(0)}')
    print(f'Second pass: {test(1)}')
    print(f'Third pass: {test(1)}')
