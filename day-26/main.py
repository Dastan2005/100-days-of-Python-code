numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)

range(1, 5)
new_nums = [n * 2 for n in range(1, 5)]
print(new_nums)

list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = list(map(int, list_of_strings))
result = [int(n) for n in list_of_strings if int(n) % 2 == 0]
print(result)

file1 = [3, 6, 5, 8, 33, 12, 7, 4, 72, 2, 42, 13]
file2 = [3, 6, 13, 5, 7, 89, 12, 3, 33, 34, 1, 344, 42]
result = list(set(file1) & set(file2))
print(result)