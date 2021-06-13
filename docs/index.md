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

## Simple moving average (SMA)

Let $p_1,\ldots,p_n$ be stock prices. The $\textit{SMA}_{k}$ is the mean of the last $k$ prices at time point $n$ and defined as:

$$
\begin{align}
    \textit{SMA}_{k} &= \frac{p_{n-k+1} + p_{n-k+2} \cdots + p_{n}}{k} \\
    &= \frac{1}{k} \sum_{i=n-k+1}^{n} p_{i}
\end{align}
$$

Reference: Brock *et al.*, 2002. [https://doi.org/10.1111/j.1540-6261.1992.tb04681.x](https://doi.org/10.1111/j.1540-6261.1992.tb04681.x)
