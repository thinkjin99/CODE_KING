import sys
input = sys.stdin.readline
def promising(index, profit, weight):
    if index >= N or weight >= W: return False
    else:
        bound = profit
        total_weight = weight
        k = index
        for w,p,_ in stuffs[index:]:
            if (total_weight + w) <= W:
                total_weight += w
                bound += p
                k += 1
            else: break
        if (0 <= k <= N): 
            if (k < N):
                bound += (W - total_weight) * (stuffs[k][1] / stuffs[k][0])
            return bound > max_profit

def knapsack(index, profit, weight):
    global max_profit
    if (weight <= W) and (profit > max_profit):
        max_profit = profit
    if promising(index, profit, weight):
        w,p,c = stuffs[index] #weight,profit,count
        for i in range(c+1):
            knapsack(index + 1, profit + (i * p), weight + (i * w))
            # knapsack(index + 1, profit, weight)

if __name__ == '__main__':
    N,W = map(int,input().split())
    stuffs = [tuple(map(int, input().split())) for _ in range(N)]
    max_profit = 0
    stuffs.sort(key = lambda x: x[1]/x[0], reverse = True)
    knapsack(0,0,0)
    print(max_profit)
