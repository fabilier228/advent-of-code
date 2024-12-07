from itertools import product


def parse_input(file_path):
    with open(file_path, 'r') as reading_file:
        data = reading_file.readlines()

    map = {}
    for row in data:
        if ':' not in row:
            continue
        result, chars = row.split(':')
        numbers = [int(number) for number in chars.split()]
        map[int(result)] = numbers
    return map


def evaluate_expression(numbers, operators):
    current_sum = numbers[0]
    for i in range(len(operators)):
        operator = operators[i]
        value = numbers[i + 1]
        if operator == '+':
            current_sum += value
        elif operator == '*':
            current_sum *= value
        elif operator == "||":
            current_sum = int(str(current_sum)+str(value))
    return current_sum


def find_valid_calibration_sum(map):
    total_calibration_result = 0

    for target, numbers in map.items():
        operator_slots = len(numbers) - 1
        operator_combinations = product(["+", "*", '||'], repeat=operator_slots)

        for operators in operator_combinations:
            result = evaluate_expression(numbers, operators)
            if result == target:
                total_calibration_result += target
                break

    return total_calibration_result


file_path = 'input.txt'
map = parse_input(file_path)

total_result = find_valid_calibration_sum(map)
print(total_result)
