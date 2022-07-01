# Can a newborn baby in Norway expect to live for one billion (10^9) seconds? Write
# a Python program for doing arithmetics to answer the question.

oneyear_day = 365
oneday_hour = 24
onehour_min = 60
onemin_sec = 60

oneyear_sec: int = (oneyear_day * oneday_hour * onehour_min * onemin_sec)  # One year is equivalent
# to 31.536.000 seconds.
x = (10 ** 9) / oneyear_sec  # One billion of seconds divide by one year seconds give us the result.
print("Life expectancy in Norway is 80.6 years. So, the baby should expect to live, approximately", x , "years.")
