n = int(input())
arr = ["*","* *","*****"]
tri_size = 3 #삼각형의 크기
k = 1
for i in range(4, n + 1):
    #삼각형의 크기는 3*2^k 순으로 증가하며 이때마다 작은 삼각형을 반복한다.
    #4~6까지는 1~3까지를 2번 반복
    #7~12까지는 1~6까지를 2번 반복 이런 식으로 삼각형이 출력된다.

    #현재 줄의 위치에서 삼각형의 크기의 나머지를 구하면 반복해야할 줄의 번호가 나온다
    repeat = arr[(i - 1) % tri_size]
    blanks = ((i * 2 - 1) -2 * len(repeat)) * " "
    arr.append(repeat + blanks + repeat)
    #삼각형의 크기가 3*2^k가 되면 반복하는 삼각형의 크기가 변경된다.
    if i == 3 * (2 ** k):
        tri_size = i
        k += 1

for i, l in enumerate(arr,start=1):
    #공백과 함께 출력해준다.
    print(" " * (n - i) + l + " " * (n - i))