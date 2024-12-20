
def Is_Leap(year):
    if ( year % 400 == 0 ) and ( year % 100 == 0 ) :
        print(f"Given year {year} is a Leap year")
    elif ( year % 4 == 0 ) and ( year % 100 != 0 ) :
        print(f"Given year {year} is a Leap year")
    else:
        print(f"Given year {year} not a Leap year")


def is_leap_year_without_per(year):
    # Check if year is divisible by 4
    divisible_by_4 = (year // 4) * 4 == year

    # Check if year is divisible by 100
    divisible_by_100 = (year // 100) * 100 == year

    # Check if year is divisible by 400
    divisible_by_400 = (year // 400) * 400 == year

    # A year is a leap year if it's divisible by 4,
    # and not divisible by 100, or if it is divisible by 400
    return (divisible_by_4 and (not divisible_by_100 or divisible_by_400))

# Test the function
year = 2022

print(f"{year} is a leap year: {is_leap_year_without_per(year)}")
