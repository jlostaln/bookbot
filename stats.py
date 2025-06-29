def get_num_words(str):
    words = str.split()
    return len(words)

def get_char_count(str):
    str = str.lower()
    char_counts = {}
    for char in str:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_char_count(char_count):
    new_list = []
    for char in char_count:
        new_list.append({"char": char, "num":char_count[char]})
    new_list.sort(reverse=True, key=lambda item: item["num"])
    return new_list
