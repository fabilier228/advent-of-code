reading_file = open('input.txt', 'r')
data: list[str] = reading_file.readlines()

def check_report(report: str) -> int:
    array_of_levels: list[str] = report.split()
    first_level: int = int(array_of_levels[0])
    last_level: int = int(array_of_levels[-1])

    if last_level < first_level:
        array_of_levels.reverse()
        first_level, last_level = last_level, first_level


    prev: int = first_level
    for i in range(1, len(array_of_levels)):
        level: int = int(array_of_levels[i])
        diff: int = level - prev
        if prev >= level or diff > 3:
            return 0

        prev = level

    return 1


safe_reports: int = 0

for report in data:
    safe_reports += check_report(report)

print(safe_reports)
