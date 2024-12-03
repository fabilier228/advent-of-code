import re

with open('input.txt', 'r') as reading_file:
    data: str = reading_file.read()
# Example corrupted memory input
corrupted_memory = data

pattern = r"do\(\)\Wmul\((\d+),(\d+)\)"

# Find all matches of the pattern
matches = re.findall(pattern, corrupted_memory)

# Calculate the sum of products for valid matches
result_sum = sum(int(x) * int(y) for x, y in matches)

print(result_sum)