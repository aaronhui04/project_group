def Scenario1(highest_categories, highest_overhead, coh_result, pl_result): 
    daykey = 'max_increment_index'
    valuekey = 'value_max_increment_index'
    plvaluekey = 'pl_value_max_increment_index'

    for entry in coh_result:
        if entry[0] == daykey:
            days_max_increment_index = entry[1]
            days_max_increment_index = int(days_max_increment_index) + 11
            break

    for entry in coh_result:
        if entry[0] == valuekey:
            value_max_increment_index = entry[1]
            break

    for entry in pl_result:
        if entry[0] == daykey:
            pl_days_max_increment_index = entry[1]
            pl_days_max_increment_index = int(pl_days_max_increment_index) + 11
            break

    for entry in pl_result:
        if entry[0] == plvaluekey:
            pl_value_max_increment_index = entry[1]    
            break

    highest_categories = highest_categories.upper()

    with open("Summary_report.txt",'w') as file:
        file.write(f"[HIGHEST OVERHEAD] {highest_categories}:{highest_overhead}%\n")
        file.write("[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN PREVIOUS DAY\n")
        file.write(f"[HIGHEST CASH SURPLUS] DAY:{days_max_increment_index}, AMOUNT: SGD{value_max_increment_index}\n")
        file.write("[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY\n")
        file.write(f"[HIGHEST NET PROFIT SURPLUS] DAY:{pl_days_max_increment_index}, AMOUNT: SGD{pl_value_max_increment_index}")

def Scenario2(highest_categories, highest_overhead, coh_result, pl_result):
    daykey = 'max_decrement_index'
    valuekey = 'value_max_decrement_index'
    plvaluekey = 'pl_value_max_decrement_index'

    for entry in coh_result:
        if entry[0] == daykey:
            days_max_decrement_index = entry[1]
            days_max_decrement_index = int(days_max_decrement_index) + 12
            break

    for entry in coh_result:
        if entry[0] == valuekey:
            value_max_decrement_index = entry[1]
            break

    for entry in pl_result:
        if entry[0] == daykey:
            pl_days_max_decrement_index = entry[1]
            pl_days_max_decrement_index = int(pl_days_max_decrement_index) + 12
            break

    for entry in pl_result:
        if entry [0] == plvaluekey:
            pl_value_max_decrement_index = entry[1]
            break

    with open("Summary_report.txt",'w') as file:
        file.write(f"[HIGHEST OVERHEAD] {highest_categories}:{highest_overhead}%\n")
        file.write("[CASH DEFICIT] CASH ON EACH DAY IS LOWER THAN PREVIOUS DAY\n")
        file.write(f"[HIGHEST CASH DEFICIT] DAY:{days_max_decrement_index}, AMOUNT: SGD{value_max_decrement_index}\n")
        file.write("[NET PROFIT DEFICIT] NET PROFIT ON EACH DAY IS LOWER THAN PREVIOUS DAY\n")
        file.write(f"[HIGHEST NET PROFIT DEFICIT] DAY:{pl_days_max_decrement_index}, AMOUNT: SGD{pl_value_max_decrement_index}")

def Scenario3(highest_categories, highest_overhead, coh_result, pl_result):
    with open("Summary_report.txt", 'w') as file:
        file.write(f"[HIGHEST OVERHEAD]{highest_categories}:{highest_overhead}%\n")

    dayskey = 'days_deficit'
    valuekey  = 'value_deficits'
    deficitkey = 'deficits'

    for entry in coh_result:
        if entry[0] == deficitkey:
            for day, value in entry[1]:
                new_value = abs(value)
                with open("Summary_report.txt", 'a') as file:
                    file.write(f"[CASH DEFICIT]DAY: {day}, AMOUNT: SGD{new_value}\n")
                    
            deficit_entry = next(entry for entry in coh_result if entry[0] == deficitkey)
            deficits = deficit_entry[1]
            sorted_deficits = sorted(deficits, key=lambda x: x[1], reverse=False)
            for i, (day, value) in enumerate(sorted_deficits[:3], start=1):
                word = "HIGHEST" if i == 1 else f"{i}nd" if i == 2 else f"{i}rd" 
                with open("Summary_report.txt", 'a') as file:
                    file.write(f"[{word} CASH DEFICIT]DAY:{day}, AMOUNT: SGD{abs(value)}\n")


    for entry in pl_result:
        if entry[0] == deficitkey:
            for day, value in entry[1]:
                pl_new_value = abs(value)
                with open("Summary_report.txt", 'a') as file:
                    file.write(f"[NET PROFIT DEFICIT]DAY: {day}, AMOUNT: SGD{pl_new_value}\n")

            pl_deficit_entry = next(entry for entry in pl_result if entry[0] == deficitkey)
            pl_deficit = pl_deficit_entry[1]
            pl_sorted_deficits = sorted(deficits, key=lambda x: x[1], reverse=False)
            for i, (day, value) in enumerate(pl_sorted_deficits[:3], start=1):
                word = "HIGHEST" if i == 1 else f"{i}nd" if i == 2 else f"{i}rd" 
                with open ("Summary_report.txt", 'a')as file:
                    file.write(f"[{word} NET PROFIT DEFICIT]DAY:{day}, AMOUNT: SGD{abs(value)}\n")








