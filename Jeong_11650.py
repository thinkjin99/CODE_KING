import copy
import sys
def merge(arr,start,mid,end):
    sortedArray = []
    left,right = (start,mid + 1)
    while left <= mid and right <= end:
        if arr[left] < arr[right]:
            sortedArray.append(arr[left])
            left += 1
        else:
            sortedArray.append(arr[right])
            right += 1

    if left > mid:
        sortedArray.extend(arr[right: end + 1])
    else:
        sortedArray.extend(arr[left: mid + 1])

    arr[start : end + 1] = sortedArray
    print(sortedArray)
    # print(arr)
    
def mergeSort(arr,start,end):
    if start < end:
        mid = (start + end) // 2
        mergeSort(arr,start,mid)
        print(arr[start:mid],arr[mid:end])
        mergeSort(arr,mid + 1,end)
        merge(arr,start,mid,end)

if __name__ == '__main__':
    # n = sys.stdin.readline()
    n= 3
    a = [1,5,2,6,8,3,4]
    # for i in range(n):
    #     a.append(tuple(input().split()))
    # b = [int(i) for i in input().split()]
    # res = ''
    # for i in merge(a,b):
    #     res += f"{i} "
    mergeSort(a,0,len(a) - 1)
    # print(a)
