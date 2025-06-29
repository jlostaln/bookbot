import sys
from stats import get_num_words, get_char_count, sort_char_count

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def print_report(book_path, num_words, sorted_list):
    print(f"""
============ BOOKBOT ============
Analyzing book found at {book_path}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------""")
    for item in sorted_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    text = get_book_text(book)
    num_words = get_num_words(text)
    character_count = get_char_count(text)
    sorted_counts = sort_char_count(character_count)
    print_report(book, num_words, sorted_counts)


if __name__ == "__main__":
    main()
