"""Utility functions for wrangling data."""

__author__ = "730390102"


from csv import DictReader


def read_csv_rows(csv_file: str) -> list[dict[str, str]]:
    """Read a CSV file's contents into a list of rows."""
    rows: list[dict[str, str]] = []
    
    # TODO 0.1) Complete the implementation of this function here.
    file_handle = open(csv_file, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    rows: list[dict[str, str]] = []
    for row in csv_reader:
        rows.append(row)
    return rows
    file_handle.close()
# TODO: Define the other functions here.
