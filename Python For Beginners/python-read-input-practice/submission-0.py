def add_two_numbers() -> int:
    user_input = input()
    user_lst = [int(i) for i in user_input.split(",")]
    return sum(user_lst)



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
