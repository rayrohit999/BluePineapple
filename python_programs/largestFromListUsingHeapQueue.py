import heapq
def largestFromListUsingHeapQ(numbers):
	max_heap = [ -num for num in numbers ]
	heapq.heapify(max_heap)
	return -  max_heap[0]

print(largestFromListUsingHeapQ([2,3,4,5]))
