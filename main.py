from stats import num_words, num_characters

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    text = get_book_text("books/frankenstein.txt")
    print(f"{num_words(text)} words found in the document")
    char_counts = num_characters(text)
    print(char_counts)

main()