def roman_to_int(s):
    
    roman_map = {
        'I': 1,    'V': 5,    'X': 10,
        'L': 50,   'C': 100,  'D': 500,
        'M': 1000
    }

    total = 0
    prev_value = 0

    for char in reversed(s.upper()):
        value = roman_map.get(char, 0)
        if value < prev_value:
            total -= value  
        else:
            total += value
            prev_value = value

    return total

print(roman_to_int("III"))    
print(roman_to_int("IV"))      
print(roman_to_int("IX"))      
print(roman_to_int("LVIII"))   
print(roman_to_int("MCMXCIV")) 
