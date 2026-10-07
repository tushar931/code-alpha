# TASK 2: STOCK PORTFOLIO TRACKER

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "AMZN": 180,
    "MSFT": 420
}

total_investment = 0

print("===== STOCK PORTFOLIO TRACKER =====")
print("Available Stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("\nEnter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available.")
        continue

    quantity = int(input("Enter quantity: "))

    investment = stock_prices[stock] * quantity
    total_investment += investment

    print(f"{stock}: {quantity} shares × ${stock_prices[stock]} = ${investment}")

print("\n===== PORTFOLIO SUMMARY =====")
print(f"Total Investment Value: ${total_investment}")

# Save result to a text file
with open("portfolio.txt", "w") as file:
    file.write("STOCK PORTFOLIO SUMMARY\n")
    file.write("=======================\n")
    file.write(f"Total Investment Value: ${total_investment}\n")

print("Portfolio summary saved to portfolio.txt")
