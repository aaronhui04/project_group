from pathlib import Path
import csv

fp = Path.cwd()/"Csv_Reports"/"profit-and-loss-sgd.csv"

with fp.open(mode="r", encoding="UTF-8", newline="") as file: 
    reader = csv.reader(file) 
    next(reader)

    profitandloss = []

    for row in reader:
        profitandloss.append([row[0],row[1],row[2],row[3],row[4]])

def profitloss():
    days = [row[0] for row in profitandloss]
    netprofit = [row[4] for row in profitandloss]

    PandL_difference = [int(netprofit[i + 1]) - int(netprofit[i]) for i in range(len(netprofit) - 1)]

    pl_result = []

    pl_max_increment_index = PandL_difference.index(max(PandL_difference))
    pl_result.append(('max_increment_index', pl_max_increment_index))
    pl_value_max_increment_index = int(netprofit[pl_max_increment_index + 1]) - int(netprofit[pl_max_increment_index])
    pl_result.append(('pl_value_max_increment_index', pl_value_max_increment_index))
    pl_days_max_increment_index = days[pl_max_increment_index + 1]
    pl_result.append(('pl_days_max_increment_index', pl_days_max_increment_index))

    pl_max_decrement_index = PandL_difference.index(min(PandL_difference))
    pl_result.append(('max_decrement_index', pl_max_decrement_index))
    pl_value_max_decrement_index = int(netprofit[pl_max_decrement_index]) - int(netprofit[pl_max_decrement_index + 1])
    pl_result.append(('pl_value_max_decrement_index', pl_value_max_decrement_index))
    pl_days_max_decrement_index = days[pl_max_decrement_index + 1]
    pl_result.append(('pl_days_max_decrement_index', pl_days_max_decrement_index))

    deficits = [(days[i + 1], PandL_difference[i]) for i in range(len(PandL_difference))if PandL_difference[i] < 0]
    pl_result.append(('deficits', deficits))

    return pl_result
