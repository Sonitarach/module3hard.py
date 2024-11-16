def calculate_structure_sum(data_structure, *args):
    total_sum = 0

    if isinstance(data_structure, (list, tuple)):
        for item in data_structure:
            total_sum += calculate_structure_sum(item) # Recursive call for list/tuple items
    elif isinstance(data_structure, dict):
        for key, value in data_structure.items():
            if isinstance(key, str):
                total_sum += len(key)
            if isinstance(key, (int, float)):
                total_sum += key
            total_sum += calculate_structure_sum(value) # Recursive call for dictionary values.
    elif isinstance(data_structure, str):
        total_sum += len(data_structure)
    elif isinstance(data_structure, (int, float)):
        total_sum += data_structure
    elif isinstance(data_structure, set): # Added handling for sets
        for item in data_structure:
            total_sum += calculate_structure_sum(item)
    return total_sum


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result) # Output: 99

#Additional test case with a set
data_structure2 = {1, 2, "test", (3,4)}
result2 = calculate_structure_sum(data_structure2)
print(result2) #Output 10