from stats import count_words, count_characters


def get_book_text(file_path):
    with open(file_path) as file:
        book_text = file.read()
        return book_text

def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count, words_list = count_words(book_text)
    character_count = count_characters(words_list)
    print(character_count)

main()
