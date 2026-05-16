def get_book_text(filepath: str) -> str:
    with open(filepath) as file:
        book_text = file.read()
    return book_text

frankenstein_filepath = "books/frankenstein.txt"

def main():
    print(get_book_text(frankenstein_filepath))

main()