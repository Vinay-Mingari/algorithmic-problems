def combine_elements(list1, list2):

    import math

    def overlap_ratio(a, b):
        a_left, a_right = a
        b_left, b_right = b
        overlap_left = max(a_left, b_left)
        overlap_right = min(a_right, b_right)
        overlap_length = max(0, overlap_right - overlap_left)
        a_length = a_right - a_left
        return overlap_length / a_length if a_length else 0

    combined = list1 + list2
    combined.sort(key=lambda x: x['positions'][0])  

    result = []
    skip_indices = set()

    for i in range(len(combined)):
        if i in skip_indices:
            continue
        current = combined[i]
        curr_pos = current['positions']
        curr_values = current['values']

        for j in range(i + 1, len(combined)):
            other = combined[j]
            other_pos = other['positions']
            other_values = other['values']

            if overlap_ratio(curr_pos, other_pos) > 0.5 or overlap_ratio(other_pos, curr_pos) > 0.5:
                
                curr_values += other_values
                skip_indices.add(j)

        result.append({'positions': curr_pos, 'values': curr_values})

    return result



list1 = [
    {"positions": [0, 10], "values": [1, 2]},
    {"positions": [15, 25], "values": [3]},
]

list2 = [
    {"positions": [5, 12], "values": [4]},     
    {"positions": [20, 30], "values": [5, 6]}, 
]

merged = combine_elements(list1, list2)
print(merged)
