# Implement the calculator for the date of Easter.
# The following algorithm computes the date for Easter Sunday for any year between 1900 to 2099.
# Ask the user to enter a year. Compute the following:
# a = year % 19
# b = year % 4
# c = year % 7
# d = (19 * a + 24) % 30
# e = (2 * b + 4 * c + 6 * d + 5) % 7
# dateofeaster = 22 + d + e
# Special note: The algorithm can give a date in April. Also, if the year is one of four special years
# (1954, 1981, 2049, or 2076) then subtract 7 from the date.
# Your program should print an error message if the user provides a date that is out of range.

def easter_calc(year):
    if 1900 <= year <= 2099:
        a = year % 19
        b = year % 4
        c = year % 7
        d = (19 * a + 24) % 30
        e = (2 * b + 4 * c + 6 * d + 5) % 7
        dateofeaster_int = 22 + d + e

        if year == 1954 or year == 1981 or year == 2049 or year == 2076:
            dateofeaster_int -= 7

        month = "March"
        if dateofeaster_int > 31:
            april_date = dateofeaster_int % 31
            return april_date, "of April", year
        else:
            return dateofeaster_int, "of", month, year

print(easter_calc(1954))


# def IanTaylorEasterJscr(year):
#  a = year % 19
#  b = year >> 2
#  c = b // 25 + 1
#  d = (c * 3) >> 2
#  e = ((a * 19) - ((c * 8 + 5) // 25) + d + 15) % 30
#  e += (29578 - a - e * 32) >> 10
#  e -= ((year % 7) + b - d + e + 2) % 7
#  d = e >> 5
#  day = e - d * 31
#  month = d + 3
#  return year, month, day
#
# print(IanTaylorEasterJscr(2018))
