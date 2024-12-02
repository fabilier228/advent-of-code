def is_safe(report: list[int]) -> bool:
    for i in range(1, len(report)):
        diff = report[i] - report[i - 1]
        if report[i] <= report[i - 1] or diff > 3:
            return False
    return True
def check_report(report: str) -> int:
    array_of_levels: list[int] = list(map(int, report.split()))
    first_level, last_level = array_of_levels[0], array_of_levels[-1]

    if last_level < first_level:
        array_of_levels.reverse()

    if is_safe(array_of_levels):
        return 1

    for i in range(len(array_of_levels)):
        temp_report = array_of_levels[:i] + array_of_levels[i + 1:]
        if is_safe(temp_report):
            return 1

    return 0


reading_file = open('input.txt', 'r')
data: list[str] = reading_file.readlines()

safe_reports = sum(check_report(report.strip()) for report in data)

print(safe_reports)
