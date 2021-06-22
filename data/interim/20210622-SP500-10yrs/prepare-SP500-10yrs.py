from datetime import date
from pathlib import Path

import pandas as pd
import pandas_market_calendars as mcal

input_dir = Path("data/raw/20210620-SP500-max/20210620/")

# determine NYSE market days for the last 10 years, starting 20210620
end = date(year=2021, month=6, day=20)
start = date(year=end.year - 10, month=end.month, day=end.day)
nyse = mcal.get_calendar("NYSE")
nyse_days = nyse.schedule(start_date=start, end_date=end).index

# left join with all tickers
days_df = pd.DataFrame(index=nyse_days)
days_df.index.set_names("Date", inplace=True)
for f in sorted(input_dir.glob("*.parquet")):
    if f.name == "SP500-companies.snappy.parquet":
        continue
    ticker = str(f.name).split(".")[0]
    ticker_df = pd.read_parquet(f)
    c = ticker_df.loc[:, "Close"]
    c.name = ticker
    days_df = days_df.join(c, on="Date", how="left")

days_df.to_parquet(
    "data/interim/20210622-SP500-10yrs/20210622-SP500-10yrs.snappy.parquet",
    engine="pyarrow",
    compression="snappy",
)
