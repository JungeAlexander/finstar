# S&P 500 data for the last 10 years

Ran the following on 20210619 which created output files `20210619-SP500-companies.snappy.parquet` and `20210619-SP500-10yr.snappy.parquet`.

```
poetry run python download.py 1>dowload.log 2>download.err
```
