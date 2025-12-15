def count_words(book_text):
    words_list = book_text.split()
    word_count = len(words_list)
    return word_count, words_list

def count_characters(words_list):
    character_dict = {}
    for words in words_list:
        for characters in words:
            characters = characters.lower()
            if characters not in character_dict:
                character_dict[characters] = 1
            else:
                character_dict[characters] += 1
    return character_dict

def get_character_dict_list(character_dict):
    character_dict_list = []
    for character, count in character_dict.items():
        character_dict_individual = {"char": character, "num": count}
        character_dict_list.append(character_dict_individual)
    return character_dict_list

def sort_by_num(items):
    return items["num"]

def sort_character_dict_list(character_dict_list):
    character_dict_list.sort(reverse=True,key=sort_by_num)
    return character_dict_list
def print_report (path, word_count, sorted_character_dict_list):
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