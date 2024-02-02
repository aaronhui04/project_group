from pathlib import Path
import csv

zp = Path.cwd()/"Csv_Reports/cash-on-hand-sgd.csv"

with zp.open(mode="r" , encoding="UTF-8" , newline="") as file:
    reader = csv.reader(file)
    next(reader)

    cashonhand = []

    for row in reader:
        cashonhand.append([row[0],row[1]])

def cashonhand_calculation():
    days = [row[0] for row in cashonhand]
    coh = [row [1] for row in cashonhand]

    coh_difference = [int(coh[i + 1]) - int(coh[i]) for i in range(len(coh) - 1)]

    coh_result = []

    max_increment_index = coh_difference.index(max(coh_difference))
    coh_result.append(('max_increment_index', max_increment_index))
    value_max_increment_index = int(coh[max_increment_index + 1]) - int(coh[max_increment_index])
    coh_result.append(('value_max_increment_index', value_max_increment_index))
    days_max_increment_index = days[max_increment_index + 1]
    coh_result.append(('days_max_increment_index', days_max_increment_index))

    max_decrement_index = coh_difference.index(min(coh_difference))
    coh_result.append(('max_decrement_index', max_decrement_index))
    value_max_decrement_index = int(coh[max_decrement_index]) - int(coh[max_decrement_index + 1])
    coh_result.append(('value_max_decrement_index', value_max_decrement_index))
    days_max_decrement_index = days[max_decrement_index + 1]
    coh_result.append(('days_max_decrement_index', days_max_decrement_index))

    deficits = [(days[i + 1], coh_difference[i])for i in range(len(coh_difference)) if coh_difference[i] < 0]
    coh_result.append(('deficits', deficits))

    if max_decrement_index > 0:
        determine_print = 1
    elif max_decrement_index < 0 and max_increment_index > 0:
        determine_print = 3
    else:
        determine_print = 2
    coh_result.append(('determine_print', determine_print))

    return coh_result