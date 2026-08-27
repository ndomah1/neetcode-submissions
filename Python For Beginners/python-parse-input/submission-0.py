from typing import List

def read_integers() -> List[int]: # input - 1,2,3,4,5
    user_input = input()
    return [int(i) for i in user_input.split(",")]


# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
