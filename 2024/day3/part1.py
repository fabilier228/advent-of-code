import re

with open('input.txt', 'r') as reading_file:
    data: str = reading_file.read()
corrupted_memory = data

pattern = r"do\(\)\Wmul\((\d+),(\d+)\)"

matches = re.findall(pattern, corrupted_memory)

result_sum = sum(int(x) * int(y) for x, y in matches)

print(result_sum)