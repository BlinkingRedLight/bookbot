def num_words(f):
    words = (f.split())
    num_words = len((words))
    return num_words

def num_characters(f):
    lower_words = f.lower()
    freq = {}
    for word in lower_words:
        freq[word] = freq.get(word, 0) + 1
    return freq