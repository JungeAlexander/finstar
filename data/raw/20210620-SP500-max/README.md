# S&P 500 ticker data for max available period

Ran the following on 20210620 which created output files in `20210620`.

```
mkdir 20210620
poetry run python download.py 1>20210620/download.log 2>20210620/download.err
```
