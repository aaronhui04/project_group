from pathlib import Path
import csv

op = Path.cwd()/"Csv_Reports"/"overheads-day-90.csv"

with op.open(mode="r" , encoding="UTF-8" , newline="") as file:
    reader = csv.reader(file)
    next(reader)

    overhead_list = []
    overhead_list = [list(map(str, row))for row in reader]


def find_overhead():

    highest_categories = None
    highest_overhead = None

    for row in overhead_list:

        category = row[0]
        amount = row[1]

        if highest_overhead is None or amount > max(highest_overhead):
            highest_overhead = amount
            highest_categories = category

    overhead_return = [highest_categories, highest_overhead]

    return overhead_return

