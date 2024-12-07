with open('input.txt', 'r') as reading_file:
    data = reading_file.read()


def string_to_list(string):
    result = []
    arr = string.split(',')
    for char in arr:
        result.append(int(char))
    return result

def partition_into_updates_and_ordering_data(data):
    ordering = {}
    updates = []
    for row in data.split('\n'):
        if len(row) == 5:
            [ordered_before, ordered_after] = row.split('|')
            ordered_before = int(ordered_before)
            ordered_after = int(ordered_after)

            if ordered_before not in ordering:
                ordering[ordered_before] = {'pages_before': [], 'pages_after': []}
            if ordered_after not in ordering:
                ordering[ordered_after] = {'pages_before': [], 'pages_after': []}

            ordering[ordered_before]['pages_after'].append(ordered_after)
            ordering[ordered_after]['pages_before'].append(ordered_before)

        elif len(row) > 5:
            update = string_to_list(row)
            updates.append(update)

    return updates, ordering




def is_valid_update(update, ordering):
    for i in range(len(update)):
        current_page = update[i]
        if current_page not in ordering:
            continue

        for required_before in ordering[current_page]['pages_before']:
            if required_before in update[i:]:
                return False

        for required_after in ordering[current_page]['pages_after']:
            if required_after in update[:i]:
                return False

    return True



updates, ordering = partition_into_updates_and_ordering_data(data)

correct_updates = []

for update in updates:
    if is_valid_update(update, ordering):
        correct_updates.append(update)

result = sum(update[len(update) // 2] for update in correct_updates)

# print(result)
