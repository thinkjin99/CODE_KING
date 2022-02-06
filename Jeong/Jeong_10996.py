n = int(input())
if n == 1: print('*')
else:
	for i in range(2 * n):
		line = ''
		for j in range(i, n + i):
				if j % 2 != 0:
					letter = ' '
				else: letter = '*'
				line += letter
		print(line)

			
