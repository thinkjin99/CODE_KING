import sys
def FindPrefix(phoneNums):
    prefix = {} #접두어를 저장하는 딕셔너리
    for phone_number in phoneNums:
        prefix[phone_number] = 1
    lengths = {len(i) for i in phoneNums}
    for phone in phoneNums:
        for length in lengths: #해당 phoneNum보다 작은 직전의 길이까지 slice해서 비교해본다.
            if len(phone) <= length:
                continue
            if phone[:length] in prefix:
                print("NO")
                return  #이미 존재하면 일관성 없음
    return print("YES") #일관성이 있는 경우

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        phoneNums = []
        n = int(sys.stdin.readline())
        for _ in range(n):
            phoneNum = sys.stdin.readline().strip()
            phoneNums.append(phoneNum)
        FindPrefix(phoneNums)



