# Welcome to MkDocs

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.

## Simple Trading Strategies

### Simple moving average (SMA)

Let $p_1,\ldots,p_n$ be stock prices. The $\textit{SMA}_{k}$ is the mean of the last $k$ prices at time point $n$ and defined as:

$$
\begin{align}
    \textit{SMA}_{k} &= \frac{p_{n-k+1} + p_{n-k+2} \cdots + p_{n}}{k} \\
    &= \frac{1}{k} \sum_{i=n-k+1}^{n} p_{i}
\end{align}
$$

This is an old strategy defined by Brock *et al.*, 2002. [https://doi.org/10.1111/j.1540-6261.1992.tb04681.x](https://doi.org/10.1111/j.1540-6261.1992.tb04681.x)
> In its simplest form this strategy is expressed as buying (or selling) when the short-period moving average risesabove (or falls below) the long-period moving average. The idea behind computing moving averages it to smooth out an otherwise volatile series. When the short-period moving average penetrates the long-period moving average, a trend is considered to be initiated. The most popular moving average rule is 1-200, where the short period is one day and the long period is 200 days. While numerous variations of this rule are used in practice, we attempted to select several of the most popular ones: 1-50, 1-150, 5-150, 1-200, and 2-200.

TODO: add visual explanation

## Statistics

### Gross performance

### Cumulative returns

### Average, annualized risk-return statistics

### Maximum drawdown and the longest drawdown period
