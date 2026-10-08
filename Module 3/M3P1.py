# Christopher Monarrez M3P1


# variables ticker_symbol, number_of_shares, and cost_per_share

ticker_symbol = input("Enter the Stock Ticker Symbol: ")
number_of_shares = int(input("Enter the Number of Shares: "))
cost_per_share = float(input("Enter the Cost per Share: "))

#calculation
amount_invested = number_of_shares * cost_per_share

#output display
print("Amount Invested: ", amount_invested)