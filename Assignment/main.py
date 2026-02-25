import re

months = [
    "January.txt",
    "February.txt",
    "March.txt",
    "April.txt",
    "May.txt",
    "June.txt",
    "July.txt",
    "August.txt",
    "September.txt",
    "October.txt",
    "November.txt",
    "December.txt",
]


def check_people_value(file_path: str) -> int | None:
    try:
        search_pattern = r"\[\[Number of people: [0-9]+\]\]"
        number_pattern = r"\d+"
        with open(file_path, "r") as file_data:
            for line_num, line in enumerate(file_data, 1):
                if re.search(search_pattern, line):
                    print(
                        f"Pattern found in file {file_path} line {line_num}: {
                            line.strip()
                        }"
                    )
                    numbers = re.findall(number_pattern, line.strip())
                    return int(numbers[0])
        return 0
    except FileNotFoundError:
        print(f"{file_path} does not exist")
        return None


def find_year_with_value(target_num: int, left_year: int, right_year: int) -> int:
    first = 0
    last = len(months)-1
    while left_year <= right_year:
        mid_year = left_year + (right_year - left_year) // 2

        first_month_val = check_people_value(f"./data/{mid_year}/{months[first]}")
        last_month_val = check_people_value(f"./data/{mid_year}/{months[last]}")

        if not first_month_val:
            first += 1
            continue

        if not last_month_val:
            print("Inside the last_month_val")
            last -= 1
            continue

        if first_month_val <= target_num <= last_month_val:
            left_month = first
            right_month = last

            while left_month <= right_month:
                mid_month = left_month + (right_month - left_month) // 2
                mid_val = check_people_value(f"./data/{mid_year}/{months[mid_month]}")

                if mid_val == target_num:
                    print(
                        f"Found the value: Year -> {mid_year}, Month -> {
                            months[mid_month]
                        }"
                    )
                    return mid_year
                elif mid_val < target_num:
                    left_month = mid_month + 1
                else:
                    right_month = mid_month - 1

            return -1

        elif first_month_val > target_num:
            right_year = mid_year - 1

        else:
            left_year = mid_year + 1

    return -1


def main():
    target_num = 10959296
    left_dir = 1000
    right_dir = 9333

    result = find_year_with_value(target_num, left_dir, right_dir)

    if result != -1:
        print(f"Found in year {result}")
    else:
        print("Not found")


if __name__ == "__main__":
    main()
