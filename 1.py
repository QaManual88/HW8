def find_unique_value(some_list):
    unique_value = 0
    for num in some_list:
        unique_value ^= num
    return unique_value

# Приклади використання
print(find_unique_value([1, 2, 2, 1, 2]))



