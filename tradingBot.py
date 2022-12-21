import yfinance as yf
import pandas as pd

# Set the ticker symbol and time frame for the stock data
ticker = "AAPL"
time_frame = "1d"

# Get the stock data from Yahoo Finance
data = yf.Ticker(ticker).history(time_frame=time_frame)

# Calculate the 50-day simple moving average of the stock's closing price
data["SMA50"] = data["Close"].rolling(window=50).mean()

# Initialize variables to track the stock's position and the cash balance
position = 0
cash = 1000

# Iterate through the data and trade based on the SMA strategy
for index, row in data.iterrows():
    current_price = row["Close"]
    sma = row["SMA50"]
    
    # If the current price is higher than the SMA, buy the stock
    if current_price > sma:
        # Calculate the number of shares to buy based on the cash balance
        shares = int(cash / current_price)
        
        # Update the position and cash balance
        position += shares
        cash -= shares * current_price
        
        # Print a message to the console
        print(f"Bought {shares} shares of {ticker} at {current_price}")
        
    # If the current price is lower than the SMA, sell the stock
    elif current_price < sma:
        # Update the position and cash balance
        cash += position * current_price
        position = 0
        
        # Print a message to the console
        print(f"Sold {shares} shares of {ticker} at {current_price}")

# Calculate the final balance
final_balance = cash + position * current_price

# Print the final balance
print(f"Final balance: {final_balance}")
