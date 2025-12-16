# import heapq
def largestFromListUsingHeapQ(numbers):
	if not numbers:
		return None
	
	max_heap = [ -num for num in numbers ]
	heapify(max_heap)
	return -  max_heap[0]

def heapify(arr):
	n = len(arr)

	for i in range(n//2-1,-1,-1):
		sift_down(arr,i,n)

def sift_down(arr,i,n):
	while True:
		smallest = i
		left = 2*i+1
		right = 2*i+2

		if left<n and arr[left]<arr[smallest]:
			smallest = left
		
		if right<n and arr[right]<arr[smallest]:
			smallest = right

		if smallest == i:
			break
		arr[i],arr[smallest] = arr[smallest],arr[i]

		i = smallest

print(largestFromListUsingHeapQ([1,2,3,4,5])) #output: 5

print(largestFromListUsingHeapQ([-1,-2,-3,-4,-5])) #output: -1

print(largestFromListUsingHeapQ([1,-2,-3,4,5])) #output: 5

print(largestFromListUsingHeapQ([1,2,3,3,4,4,5])) #output: 5

print(largestFromListUsingHeapQ([0,0,0,0,0])) #output: 0

print(largestFromListUsingHeapQ(None)) #output: 

print(largestFromListUsingHeapQ([1,2,3,4,5,-100])) #output: 5