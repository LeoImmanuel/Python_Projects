# Converting Integer to Decimals

import decimal

num = int(input("Enter Integer value to be converted to Decimal: "))
print(f"Decimal value  of {num} is :{decimal.Decimal(num)}")
print(type(decimal.Decimal(num)))