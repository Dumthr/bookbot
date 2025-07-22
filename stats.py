def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def get_word_count(file_contents):
    words = file_contents.split()
    count_words = 0
    for word in words:
        count_words += 1
    return count_words

def sort_on(items):
    return items["num"]

def get_char_count(file_contents):
    lower_char = file_contents.lower()
    dict_char = {}
    for char in lower_char:
        if char.isalpha():
            dict_char[char] = dict_char.get(char,0)+1
    characters_list = [{"char":char,"num":num} for char,num in dict_char.items()]
    characters_list.sort(reverse=True,key=sort_on)
    return characters_list

