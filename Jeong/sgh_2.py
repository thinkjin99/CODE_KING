# prices = [int(i) for i in input().split()]
# arr = []
# temp = []
# for i in range(len(prices)):
#     if (i == len(prices) - 1) or prices[i + 1] <= prices[i]:
#         temp.append(prices[i])
#         if len(temp) > 1:
#             arr.append(temp)
#         temp = []
#     else:
#         temp.append(prices[i])
#          q
# print(arr)
import time
from functools import wraps
def timer(func):
    """A decorator that prints how long a function took to run."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        t_start = time.time()
        result = func(*args, **kwargs) #func는 클로져로 저장돼 있다.
        t_total = time.time() - t_start
        print('{} took {}s'.format(func.__name__, t_total))
        return result
    return wrapper

@timer
def sleep_n_secs(n):
    """ time """
    time.sleep(n)

#sleep_n_sces 함수의 소요시간을 측정하고 싶다고 해보자.


# sleep_n_secs(3) #@를 통해 호출하는 것과 아래는 동일하다.

# wrapper = timer(sleep_n_secs)
# print(wrapper.__name__)
# print(wrapper.__doc__)
print(sleep_n_secs.__name__)
print(sleep_n_secs.__doc__)
print(sleep_n_secs(3))


# wrapper(3)

