import sys
input = sys.stdin.readline
N, m = map(int,input().split())
sums = []
cards = [int(i) for i in input().split()]
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            card_sum = cards[i] + cards[j] + cards[k]
            if card_sum <= m:
                sums.append(card_sum)
print(m - min(map(lambda x: m - x, sums)))
