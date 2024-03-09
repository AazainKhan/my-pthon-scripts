import pandas as pd
import yfinance as yf
import os

def scrape_and_save_historical_data(tickers):
    for ticker in tickers:
        print(f"Scraping data for {ticker}...")
        try:
            stock_data = yf.download(ticker, period="max")
            if not stock_data.empty:
                filename = f"df_{ticker}.csv"
                stock_data.to_csv(filename)
                print(f"Data saved to {filename}")
            else:
                print(f"No data available for {ticker}")
        except Exception as e:
            print(f"Error scraping data for {ticker}: {e}")

def main():
    # Read the list of S&P 500 companies
    df = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")[0]
    tickers = df['Symbol'].tolist()

    # Create a directory to store the data files
    if not os.path.exists("historical_data"):
        os.makedirs("historical_data")
    os.chdir("historical_data")

    # Scrape and save historical data for each company
    scrape_and_save_historical_data(tickers)

if __name__ == "__main__":
    main()
