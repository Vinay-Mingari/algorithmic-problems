import re
from collections import Counter

def are_anagrams(str1, str2):
    """
    Checks if two strings are anagrams.
    Ignores case, spaces, and punctuation.

    Args:
        str1 (str): First string
        str2 (str): Second string

    Returns:
        bool: True if anagrams, False otherwise
    """
    # Clean the strings: remove non-alphanumeric characters, lowercase
    clean1 = re.sub(r'[^a-zA-Z0-9]', '', str1).lower()
    clean2 = re.sub(r'[^a-zA-Z0-9]', '', str2).lower()

    # Compare character counts
    return Counter(clean1) == Counter(clean2)


# 🧪 Test Cases
print(are_anagrams("Listen", "Silent"))               # True
print(are_anagrams("Debit card", "Bad credit"))       # True
print(are_anagrams("Astronomer", "Moon starer"))      # True
print(are_anagrams("Hello", "Olelh!!"))              # True
print(are_anagrams("Vinay", "Navi"))   