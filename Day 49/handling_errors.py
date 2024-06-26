# title = "Alice in Wonderland"
# print(title.split())

def count_words(filename):
    """Count the approximate number of words in a file"""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        # print(f"Sorry, the file {filename} does not exist.")
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")


# file = 'alice.txt'
# count_words(file)

files = ['alice.txt', 'no_file.txt']
for filename in files:
    count_words(filename)