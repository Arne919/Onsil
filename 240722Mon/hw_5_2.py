def count_character(input_string, find_string):
    count = 0
    for char in input_string:
        if char == find_string:
            count += 1
    return count

    
result = count_character("Hello, World!", "o")
print(result)  # 2
