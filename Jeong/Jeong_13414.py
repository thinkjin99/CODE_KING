import sys
input = sys.stdin.readline
k, l = map(int, input().split())
student_dict = {}
for i in range(l):
    num = input().rstrip()
    student_dict[num] = i
res = sorted(student_dict.keys(), key = lambda x: student_dict[x])
print("\n".join(res[:k]))