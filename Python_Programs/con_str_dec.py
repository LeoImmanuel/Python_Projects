# Converting String to Decimals

import decimal

str_nums = str(input("Enter String of numbers to be converted to Decimal: "))
print(f"Converting string to decimal :{decimal.Decimal(str_nums)}")
print(type(decimal.Decimal(str_nums)))