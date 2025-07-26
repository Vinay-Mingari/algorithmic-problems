import re
from collections import Counter

def count_words(text):
    cleaned_text = re.sub(r'[^\w\s]', '', text.lower())
    words = cleaned_text.split()
    return dict(Counter(words))


sample_text = "Hello world!. Welcome to the world of Python."
print(count_words(sample_text))

