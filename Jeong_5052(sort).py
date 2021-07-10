import sys
def solution(phone_book):
    for i,PhoneNum in enumerate(phone_book):
        if i < len(phone_book) - 1: 
            if phone_book[i + 1][:len(PhoneNum)] == PhoneNum:
                print("NO")
                return
    print('YES')
    
if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(sys.stdin.readline())
        phone_book = []
        for _ in range(n):
            phone_book.append(sys.stdin.readline().strip())
        phone_book.sort()
        solution(phone_book)


