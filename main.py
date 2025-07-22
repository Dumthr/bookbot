from stats import get_book_text,get_word_count,get_char_count
import sys
def main():
    if len(sys.argv) <2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        
        text = get_book_text(sys.argv[1])
        word_count = get_word_count(text)
        char_count = get_char_count(text)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")

        for item in char_count:
            print(f"{item['char']}: {item['num']}")
        print("============= END ===============")
    
if __name__ == "__main__":
    main()

