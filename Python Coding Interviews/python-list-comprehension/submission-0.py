from typing import List


def create_list_of_odds(n: int) -> List[int]:
    odd_nums = [1]

    for i in range(2, n + 1):
        if i % 2 != 0:
            odd_nums.append(i)

    return odd_nums



# do not modify below this line
print(create_list_of_odds(1))
print(create_list_of_odds(5))
print(create_list_of_odds(6))
print(create_list_of_odds(10))
