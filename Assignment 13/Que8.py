###python program to count the frequency of words appearing in a string using a dictionary...

str = 'That is a bed. That is only for sleeping'

words = str.split()        ###split string intp words for counting.
word_count = {}           ###create an empty dict for storing result.

for word in words:          ##count word frequency.
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)