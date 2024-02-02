import cash_on_hand, overheads, profit_loss, print

def main():
    coh_result = cash_on_hand.cashonhand_calculation()
    pl_result = profit_loss.profitloss()
    overhead_return = overheads.find_overhead()
    highest_categories, highest_overhead = overhead_return

    print.determine(highest_categories, highest_overhead, coh_result, pl_result)
    
main()