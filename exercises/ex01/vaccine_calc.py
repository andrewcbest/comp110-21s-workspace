"""A vaccination calculator."""

__author__ = "730390102"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...
population_input = input("Enter population.")
population = float(population_input)

doses_admined_input = input("Enter the number of vaccine doses already given.")
doses_admined = float(doses_admined_input)

doses_per_day_input = input("Enter the number of vaccine doses given per day moving forward.")
doses_per_day = float(doses_per_day_input)

target_percent_input = input("Enter the target percent of the population to be vaccinated.")
target_percent = int(target_percent_input)

target_population: float = population * (target_percent / 100)
target_doses: float = target_population * 2
doses_left: float = target_doses - doses_admined
days_left: float = (doses_left / doses_per_day)
today: datetime = datetime.today()
days_left_time: timedelta = timedelta(days_left)
date_complete: datetime = today + days_left_time

target_percent_output = str(int(target_percent))
days_left_output = str(int(round(float(days_left))))

print("We will reach " + target_percent_output + "% vaccination in " + days_left_output + " days, ")
print("which falls on " + date_complete.strftime("%B %d, %Y"))