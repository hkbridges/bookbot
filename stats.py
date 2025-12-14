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