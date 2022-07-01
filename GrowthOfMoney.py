#  Make a program for computing how much money 1000 euros have
#  grown to after three years with 5 percent interest rate.

p = 5     # Bank’s interest rate in percent per year.
A = 1000  # Initial amount.
n = 3     # The years.

euros_grown = float(A * (1 + (p / 100) ** n))
print("After tree years with 5 percent of interest rate, we have", round(euros_grown, 2), "euros grew.")
