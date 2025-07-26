def find_duplicates(nums):
    seen = set()
    duplicates = set()

    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return sorted(list(duplicates))

print(find_duplicates([1, 2, 3, 2, 4, 5, 1]))     
print(find_duplicates([10, 20, 30]))              
print(find_duplicates([5, 5, 5, 5, 5]))           
print(find_duplicates([]))                       
print(find_duplicates([4, 3, 2, 1, 4, 3]))         
