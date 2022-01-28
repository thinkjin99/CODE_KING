import sys
input = sys.stdin.readline
n = int(input())
r = n // 2
combination = []
stat_map = [[int(i) for i in input().split()] for _ in  range(n)]
def make_subset(start, team_combi):
    if len(team_combi) == r:
        combination.append(team_combi)
        return
    for i in range(start, n):
        make_subset(i + 1, team_combi + [team_stat[i]])

res = 999999
#sum of row,col means stat of the team
team_stat = [sum(i) + sum(j) for i,j in zip(stat_map, zip(*stat_map))]
make_subset(0, [])
total_sum = sum(team_stat) // 2
for stat in combination:
    res = min(res, abs(total_sum - sum(stat)))
print(res)