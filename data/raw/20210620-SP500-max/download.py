import logging
from pathlib import Path
from time import sleep

import pandas as pd
import yfinance as yf

logging.basicConfig(level=logging.INFO)

output_dir = Path("./20210620")

# get S&P500 ticker symbols from Wikipedia
wiki_df = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")[0]
symbols = sorted(wiki_df.loc[:, "Symbol"])
if len(symbols) != len(set(symbols)):
    raise ValueError("S&P500 contains duplicated symbols")
wiki_df.to_parquet(
    output_dir / "SP500-companies.snappy.parquet",
    engine="pyarrow",
    compression="snappy",
)

# download ticker data for max timespan from YFinance
for s in symbols:
    logging.info(f"Processing {s}")
    ticker = yf.Ticker(s)
    ticker_df = ticker.history(period="max")
    ticker_df.to_parquet(
        output_dir / f"{s}.snappy.parquet", engine="pyarrow", compression="snappy"
    )
    sleep(1)
