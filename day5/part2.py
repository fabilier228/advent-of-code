from part1 import is_valid_update, partition_into_updates_and_ordering_data

with open('input.txt', 'r') as reading_file:
    data = reading_file.read()


updates, ordering = partition_into_updates_and_ordering_data(data)
corrected_updates = []


def insert_in_order(page, corrected_update, ordering):
    if not corrected_update:
        corrected_update.append(page)
        return

    inserted = False
    for i in range(len(corrected_update)):
        current_page = corrected_update[i]

        if current_page in ordering[page]['pages_after']:
            corrected_update.insert(i, page)
            return

    if not inserted:
        corrected_update.append(page)


def correct_update(update, ordering):
    corrected_update = []
    for page in update:
        insert_in_order(page, corrected_update, ordering)
    return corrected_update




result = 0
for update in updates:
    if not is_valid_update(update, ordering):
        new_update = correct_update(update, ordering)

        result += new_update[len(update) // 2]


print(result)




