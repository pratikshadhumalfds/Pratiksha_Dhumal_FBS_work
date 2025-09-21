###Write a Python program to find all the unique words and count the
#frequency of occurrence from a given list of strings. Use Python set data type.

string_list = [
    "Happy birthday to you",
    "May god bless you"
]

unique_words = set()

word_count = {}


for sentence in string_list:
    words = sentence.split()
    
    for word in words:
        unique_words.add(word)
        word_count[word] = word_count.get(word, 0) + 1

print("Unique words:", unique_words)

print("\nWord frequencies:")
for word in unique_words:
    print(f"{word}: {word_count[word]}")
