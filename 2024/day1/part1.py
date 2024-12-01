reading_file = open("input.txt", "r")
input_data = reading_file.readlines()

left_list = []
right_list = []

for row in input_data:
    left, right = row.strip().split()
    left_list.append(int(left))
    right_list.append(int(right))

left_list.sort()
right_list.sort()


whole_distance = 0
for left, right in zip(left_list,right_list):
    whole_distance += abs(left - right)

print(whole_distance)