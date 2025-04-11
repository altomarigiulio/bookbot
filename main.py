from stats import word_count
from stats import stat
from stats import sort_characters_by_count
import sys


def get_book_text(file_path):
    file_content = open(file_path)
    print(file_content.read())


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = sys.argv[1]
    # get_book_text(path)
    print("============ BOOKBOT ============" \
    "Analyzing book found at books/frankenstein.txt..."\
    "----------- Word Count ----------")
    word_count(path)
    print("--------- Character Count -------")
    stat(path)
    print("============= END ===============")    



main()
