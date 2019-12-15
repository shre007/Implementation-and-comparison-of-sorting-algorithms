#Heapsort
#Reference: https://www.programiz.com/dsa/heap-sort
#Reference2: https://www.geeksforgeeks.org/heap-sort/
#Name: Shreyas Arvind Vaze
#Student ID: 1001649822

def heapify(arr, n, i):
    max = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    if left_child < n and arr[i] < arr[left_child]:
        max = left_child

    if right_child < n and arr[max] < arr[right_child]:
        max = right_child

    if max != i:
        arr[i], arr[max] = arr[max], arr[i]
        heapify(arr, n, max)

def heapSort(arr):
    n = len(arr)
    for i in range(0,n,1):
        heapify(arr, n, i)
    for i in range(n-1,0,-1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


arr = [15, 14, 16, 8, 9, 10]
heapSort(arr)
n = len(arr)
print("Sorted array is")
for i in range(n):
    print("%d" % arr[i])
