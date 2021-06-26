import numpy as np
import pandas as pd
import pytest

import finstar.evaluation.returns as returns


@pytest.mark.parametrize(
    "series_list,returns_list",
    [
        ([1, 1], [np.nan, 0]),
        ([1, np.exp(1), np.exp(2)], [np.nan, 1, 1]),
        ([np.exp(1), 1, np.exp(1)], [np.nan, -1, 1]),
    ],
)
def test_log_returns(series_list: list, returns_list: list):
    """Compute log returns for a financial series and compare to expected log returns.

    Args:
        series_list (list): financial series
        returns_list (list): expected log returns
    """
    input_series = pd.Series(series_list)
    expected_log_returns = pd.Series(returns_list)
    log_returns = returns.log_returns(input_series)
    pd.testing.assert_series_equal(log_returns, expected_log_returns)
