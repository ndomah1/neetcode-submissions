from typing import List # this is used to add type hints for List type

def get_sum(nums: List[int]) -> int:
    final_sum = 0

    for num in nums:
        final_sum += num
    
    return final_sum


def get_min(nums: List[int]) -> int:
    final_min = nums[0]

    for num in nums[1:]:
        if num < final_min:
            final_min = num

    return final_min


def get_max(nums: List[int]) -> int:
    final_max = nums[0]

    for num in nums[1:]:
        if num > final_max:
            final_max = num

    return final_max


# do not modify below this line
print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))
