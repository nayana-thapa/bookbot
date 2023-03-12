def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    print(text)
    count_text = get_count(text)
    print(count_text)



def get_text(path):
    # "with" statement in Python helps in resource management
    # that ensures you don't accidentally leave any resources
    # open. Here, we are using "with" statement to open the
    # file that takes the path of a file as an argument.
    with open(path) as f:

        # "f" is an instance, invoking read method to read
        # the content of a specified file path.
        return f.read()
    
def get_count(text):
    # "split" method splits the sentence into list 
    # Example: "I am a student" -> ["I", "am", "a", "student"]
    list_of_word = text.split() 
    return len(list_of_word)
 
main()




