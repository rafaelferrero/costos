# Author: Rafael E. Ferrero
"""This program receive an Excel file and extract specific data into .csv file

V1.0: The Excel have an specific structure, and the resulting .csv file too.
    The .csv file will be used to upload into Oracle Netsuite for Standard
    Cost valuation module.
    The .xls or .xlsx origin file must be located as indicated in settings.py
    The .csv resulting file will be located as indicated in settings.py, other
    way will be located in the same directory of Excel file.
"""

# https://github.com/mauricelam/hashbang
from hashbang import command


@command
def main(argument=None):
    pass


if __name__ == "__main__":
    main.execute()
