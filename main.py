def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    count_text = get_count(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_text} words found in the document")

    chars_in_dict = get_characters_dict(text)
    sorted_char_list = get_sorted_list(chars_in_dict)

    for item in sorted_char_list:
        if item["char"].isalpha():
            print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")



def get_text(path):
    # "with" statement in Python helps in resource management
    # that ensures you don't accidentally leave any resources
    # open. Here, we are using "with" statement to open the
    # file that takes the path of a file as a parameter.
    with open(path) as f:

        # "f" is an instance, invoking read method to read
        # the content of a specified file path.
        return f.read()
    
def get_count(text):
    # "split" method splits the sentence into list 
    # Example: "I am a student" -> ["I", "am", "a", "student"]
    list_of_word = text.split() 
    return len(list_of_word)

def get_characters_dict(texts):
    dict = {}
    for letter in texts:
        
        char = letter.lower()
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict

def sort_on(d):
    return d["num"]

def get_sorted_list(dict):
    list = []
    for ch in dict:
        list.append({"char": ch, "num": dict[ch]})
    list.sort(reverse=True, key=sort_on)
    return list


main()




