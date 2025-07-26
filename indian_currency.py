def indian_currency(num):
    num_str = str("{:.2f}".format(num))
    if '.' in num_str:
        whole, decimal = num_str.split('.')
    else:
        whole, decimal = num_str, ''

    if len(whole) > 3:
        main = whole[-3:]
        prefix = whole[:-3]
        prefix_groups = []
        while len(prefix) > 2:
            prefix_groups.insert(0, prefix[-2:])
            prefix = prefix[:-2]
        if prefix:
            prefix_groups.insert(0, prefix)
        formatted = ','.join(prefix_groups + [main])
    else:
        formatted = whole

    return formatted + ('.' + decimal if decimal else '')
print(indian_currency(1234567.89))  
print(indian_currency(100))         
print(indian_currency(100000.7))    
