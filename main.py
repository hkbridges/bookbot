import sys
from stats import count_words, count_characters, get_character_dict_list, sort_character_dict_list


def get_book_text(file_path):
    with open(file_path) as file:
        book_text = file.read()
        return book_text

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    book_text = get_book_text(path)
    word_count, words_list = count_words(book_text)
    character_count = count_characters(words_list)
    character_dict_list = get_character_dict_list(character_count)
    sorted_character_dict_list = sort_character_dict_list(character_dict_list)
    pathstr = str(path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for dict in sorted_character_dict_list:
        if not dict["char"].isalpha():
            continue
        else:
            print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")


main()
