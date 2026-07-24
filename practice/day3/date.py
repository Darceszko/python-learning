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

    date = get_date(months)
    month, day, year = date

    # Print date in required YYYY-MM-DD format
    print(f"{year}-{month:02d}-{day:02d}")

def get_date(months):
    while True:
        # Get date from user
        date = input("Date: ").strip()
        if "/" in date:
            # Check if date contains exactly three parts
            if len(date.split("/")) != 3:
                continue

            month, day, year = date.split("/")

            # Check if all parts contain numbers
            if not month.isdigit() or not day.isdigit() or not year.isdigit():
                continue

            month = int(month)
            day = int(day)

            # Return values if the date is valid
            if 0 < month <= 12 and 0 < day <= 31:
                    return month, day, int(year)

        
        # Check for comma required by the written date format
        elif ","  in date:
            parts = date.replace(",", " ").split()

            #Check if date contains exactly three parts
            if len(parts) != 3:
                continue

            month, day, year = parts

            # Return values if the date is valid
            if month in months and day.isdigit() and 0 < int(day) <= 31 and year.isdigit():
                return  months.index(month) + 1, int(day), int(year)


main()