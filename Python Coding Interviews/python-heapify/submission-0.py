import heapq
from typing import List


def heapify_strings(strings: List[str]) -> List[str]:
    heap = strings
    heapq.heapify(strings)
    return heap


def heapify_integers(integers: List[int]) -> List[int]:
    heap = integers
    heapq.heapify(integers)
    return heap


def heap_sort(nums: List[int]) -> List[int]:
    heap = nums
    heapq.heapify(nums)
    return [heapq.heappop(heap) for _ in range(len(heap))]


# do not modify below this line
print(heapify_strings(["b", "a", "e", "c", "d"]))
print(heapify_integers([3, 4, 5, 1, 2, 6]))
print(heap_sort([3, 4, 5, 1, 2, 6]))