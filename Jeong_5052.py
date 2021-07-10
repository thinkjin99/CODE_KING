import sys
def FindPrefix(phoneNums):
    prefix = {} #접두어를 저장하는 딕셔너리
    for index,(phone,length) in enumerate(phoneNums):
        for _,_length in phoneNums[:index]: #해당 phoneNum보다 작은 직전의 길이까지 slice해서 비교해본다.
            if _length == length: break
            if phone[:_length] in prefix:
                return "NO" #이미 존재하면 일관성 없음
        prefix[phone] = 0 #없는 경우 key에 추가해주자.
    return "YES" #일관성이 있는 경우

if __name__ == '__main__':
    t = int(input())
    ans = []
    for _ in range(t):
        phoneNums = []
        n = int(sys.stdin.readline())
        for _ in range(n):
            phoneNum = sys.stdin.readline().strip()
            phoneNums.append((phoneNum,len(phoneNum)))
        phoneNums.sort(key = lambda phoneNum : phoneNum[1]) #번호의 길이 순으로 정렬한다.
        ans.append(FindPrefix(phoneNums))
    for i in ans:
        print(i)



