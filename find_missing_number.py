def find_missing(nums):
    n = len(nums) + 1  
    expected_sum = n * (n + 1) // 2  
    actual_sum = sum(nums)
    return expected_sum - actual_sum

print(find_missing([1, 2, 3, 5]))        
print(find_missing([6, 1, 2, 3, 4]))     
print(find_missing([2]))    
print(find_missing(list(range(1, 101))[:-1]))

