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

while True:
    date = input("Date: ").strip()

    try:
        # Format: M/D/YYYY
        if "/" in date:
            month, day, year = date.split("/")
            month = int(month)
            day = int(day)
            year = int(year)

        # Format: Month D, YYYY
        elif "," in date:
            month_name, rest = date.split(" ", 1)
            day, year = rest.replace(",", "").split()
            month = months.index(month_name) + 1
            day = int(day)
            year = int(year)

        else:
            raise ValueError

        # Validate ranges
        if not (1 <= month <= 12 and 1 <= day <= 31):
            raise ValueError

        # Output in ISO format
        print(f"{year:04}-{month:02}-{day:02}")
        break

    except ValueError:
        pass
