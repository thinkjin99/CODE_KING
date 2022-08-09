n,m = map(int, input().split())
a = [i for i in input().split()]
b = set([i for i in input().split()])
res = [int(a_v) for a_v in a if a_v not in b]
if len(res):
	print(len(res))
	for r in sorted(res):
			print(r, end=" ")
else:
	print(0)			
