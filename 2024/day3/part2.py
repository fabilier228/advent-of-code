import re

with open('input.txt', 'r') as reading_file:
    data: str = reading_file.read()
corrupted_memory = data

do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"
mul_pattern = r"mul\((\d+),(\d+)\)"

enabled = True
total_sum = 0

tokens = re.split(r"(\bdo\(\)|\bdon't\(\)|mul\(\d+,\d+\))", corrupted_memory)

for token in tokens:
    token = token.strip()
    if re.fullmatch(do_pattern, token):
        enabled = True
    elif re.fullmatch(dont_pattern, token):
        enabled = False
    elif enabled and (match := re.fullmatch(mul_pattern, token)):
        x, y = map(int, match.groups())
        total_sum += x * y

print(total_sum)