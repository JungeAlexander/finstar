import pandas as pd
import yfinance as yf

# get S&P500 ticker symbols from Wikipedia
wiki_df = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")[0]
symbols = list(wiki_df.loc[:, "Symbol"])
assert len(symbols) == len(set(symbols))

# download ticker data for last 10 years from YFinance
tickers = yf.Tickers(symbols)
ticker_df = tickers.history(period="10y")

# save both Wikipedia and YFinance data
wiki_df.to_parquet(
    "20210619-SP500-companies.snappy.parquet", engine="pyarrow", compression="snappy"
)
ticker_df.to_parquet(
    "20210619-SP500-10yr.snappy.parquet", engine="pyarrow", compression="snappy"
)
