"""Vaccine calculator exercise as a structured program."""

from datetime import datetime, timedelta

__author__ = "730390102"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    population: int = int(input("Population: "))
    doses: int = int(input("Doses administered: "))
    doses_per_day: int = int(input("Doses per day: "))
    target: int = int(input("Target percent vaccinated: "))
    # TODO 2: Call days_to_target and store result in a variable.
    days_left: int = days_to_target(population, doses, doses_per_day, target)
    # TODO 4: Call future_date and store result in a variable.
    date_complete = future_date(days_left)
    # TODO 5: Print the expected output using the variables above.
    print("We will reach " + str(target) + " in ")
    print(days_left)
    print(" days, which falls on ")
    print(date_complete)

    
# TODO 1: Define days_to_target function
def days_to_target(population: int, doses: int, doses_per_day: int, target: int) -> int:
    """Determines the number of days to meet vaccination target."""
    total_doses: float = population * (target / 100) * 2
    doses_left: float = total_doses - doses
    days_left: float = doses_left / doses_per_day
    return(int(round(days_left)))


# TODO 3: Define future_date function
def future_date(days_left: int) -> str:
    """Produces the date the vaccinatino target will be met."""
    today: datetime = datetime.today()
    days_left_time: timedelta = timedelta(days_left)
    date_complete: datetime = today + days_left_time
    return(date_complete.strftime("%B %d, %Y"))


if __name__ == "__main__":
    main()
