from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    if len(word) > 0:
        word_list = list(word)
        final_dict = {word_list[0]: word_list.count(word_list[0])}

        for char in word_list[1:]:
            if char in final_dict.keys():
                continue
            final_dict[char] = word_list.count(char)
    else:
        return "Word must not be empty"

    return final_dict




# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
