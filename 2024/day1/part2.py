# Open the file and read lines
with open("input.txt", "r") as reading_file:
    input_data = reading_file.readlines()

# Initialize dictionaries and lists
id_count = {}
right_list = []

# Process each row
for row in input_data:
    left, right = row.strip().split()
    right = int(right)
    right_list.append(right)

    left = int(left)
    id_count[left] = 0

for elem in right_list:
    if elem in id_count:
        id_count[elem] += 1

similarity_score = sum([key * count for key, count in id_count.items()])
print(similarity_score)
