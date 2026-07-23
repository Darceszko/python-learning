def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
]
    month, day, year = get_date(months)
    month = convert_month(month, months)

    print(f"{year}-{month:02d}-{int(day):02d}")


def get_date(months):
    while True:
        date = input("Date: ").strip()

        if "/" in date:
            try:
                month, day, year = date.split("/")

                if 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
                    return month, day, year
            except ValueError:
                pass

        else:
            if "," not in date:
                continue
            try:
                month, day, year = date.replace(",", "").split()

                if month in months and 1 <= int(day) <= 31:
                    return month, day, year
            except ValueError:
                pass


def convert_month(month, months):
    if month.isdigit():
        return int(month)

    return months.index(month) + 1

main()
