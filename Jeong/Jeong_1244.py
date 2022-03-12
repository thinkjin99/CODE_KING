n = int(input())
switches = [-1] + list(map(int, input().split()))
student_num = int(input())
turn_switch = lambda x: (x + 1) % 2
for _ in range(student_num):
    sex, idx = map(int, input().split())
    if sex == 1:
        for i in range(idx, n + 1, idx):
            switches[i] = turn_switch(switches[i])
    if sex == 2:
        switches[idx] = turn_switch(switches[idx])
        for i in range(1, n // 2):
            if idx - i > 0 and idx + i <= n: 
                if switches[idx - i] == switches[idx + i]:
                    switches[idx + i] = turn_switch(switches[idx + i])
                    switches[idx - i] = turn_switch(switches[idx - i])
                else:
                    break
i = 1
while i < n:
    print(*switches[i : i + 20])
    i += 20