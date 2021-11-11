import sys
def merge(arr,start,mid,end,order):
    sortedArray = []
    left,right = (start,mid + 1)
    while left <= mid and right <= end:
        if arr[left][order] <= arr[right][order]:
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
    
def mergeSort(arr,start,end,order):
    if start < end:
        mid = (start + end) // 2
        mergeSort(arr,start,mid,order)
        mergeSort(arr,mid + 1,end,order)
        merge(arr,start,mid,end,order)

if __name__ == '__main__':
    n = sys.stdin.readline()
    arr = []
    for i in range(int(n)):
        arr.append(tuple(map(int,sys.stdin.readline().split())))
    mergeSort(arr,0,len(arr) - 1,1)
    mergeSort(arr,0,len(arr) - 1,0)
    res = ''
    for i,j in arr:
        res += f"{i} {j}\n"
    print(res)
