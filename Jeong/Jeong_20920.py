
from collections import Counter
from collections import defaultdict
import random
import string


def do_sort(alphas):
    max_len = max(map(len, alphas))
    #LSD 부터 비교(least significant)
    for l in range(-1, -max_len - 1, -1):
        baskets = [[] for _ in range(27)]
        for a in alphas:
            if len(a) >= -l:
                baskets[ord(a[l]) - 97].append(a)
            else:
                baskets[-1].append(a)
        alphas = [alpha for basket in baskets for alpha in basket]
    return alphas

print(do_sort(["abc","abcd","def","ghi"]))

# def get_answer(counter):
#     count_dict = {a:c for a,c in counter.most_common()}
#     note = sorted(count_dict.items(), key=lambda x: (-x[1],-len(x[0]),x[0]))
#     return note


# def create_random_alpha(n, m):
#     letters = string.ascii_lowercase
#     alphas = []
#     for _ in range(n):
#         len_ = random.randint(1, m)
#         result_str = ''.join(random.choice(letters) for _ in range(len_))
#         alphas.append(result_str)
#     return alphas


if __name__ == "__main__":
    # n = random.randint(1, 100000)
    # m = random.randint(1, 10)
    n, m = map(int, input().split())
    alphas = [input() for _ in range(n)]
    alphas = [a for a in alphas if len(a) >= m]
    # alphas = create_random_alpha(n, m)
    counter = Counter(alphas)
    count_alphas = defaultdict(list)
    for a, cnt in counter.most_common():
        count_alphas[cnt].append(a)
    
    # ans = get_answer(counter)

    res = []
    for count, alpha_lists in count_alphas.items():
        if len(alpha_lists) > 1:
            res.extend(do_sort(alpha_lists))
        else: res.extend(alpha_lists)
        # for r in res: print(r)
    
    # matched = True
    # for a,r in zip(ans, res):
    #     if a[0] != r:
    #         print(a, r)
    #         matched = False
    # if not matched:
    #     print()
    #     print([a[0] for a in ans])
    #     print()
    #     print(res)
    #     print()
    #     print(alphas)

