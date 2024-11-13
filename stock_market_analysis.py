# File: stock_market_analysis.py

import pandas as pd
import matplotlib.pyplot as plt

def analyze_stock_data(file_path):
    """Analyzes stock market data from a CSV file."""
    df = pd.read_csv(file_path)

    # Ensure the required columns are present
    if 'Date' not in df.columns or 'Close' not in df.columns:
        print("CSV file must contain 'Date' and 'Close' columns.")
        return

    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)

    # Plot closing prices
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['Close'], label='Closing Price', color='blue')
    plt.title('Stock Market Closing Prices')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    stock_data_file = 'data/stock_data.csv'
    analyze_stock_data(stock_data_file)
