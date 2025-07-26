from collections import OrderedDict

def first_unique_char(s):
    s = s.lower()  
    freq = OrderedDict()

    for char in s:
        if char.isalpha(): 
            freq[char] = freq.get(char, 0) + 1

    for char, count in freq.items():
        if count == 1:
            return char

    return None


print(first_unique_char("aabbcdd"))             
print(first_unique_char("aabbcc"))              
print(first_unique_char("Vinay is coding!"))    
print(first_unique_char(""))                    
print(first_unique_char("abcabcde"))            
