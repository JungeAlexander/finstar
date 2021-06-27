import numpy as np
import pandas as pd
import pytest

import finstar.strategies.sma as sma


@pytest.mark.parametrize(
    "series_list,short,long,expected_pos",
    [
        (
            [1, 1, 5, 1],
            1,
            2,
            [
                np.nan,
                -1,
                1,
                -1,
            ],
        ),
        (
            [1, 1, 5, 1],
            1,
            1,
            [
                -1.0,
                -1.0,
                -1.0,
                -1.0,
            ],
        ),
        (
            [1, 1, 1, 1, 1, 1, 1, 3, 3, 1],
            1,
            5,
            [
                np.nan,
                np.nan,
                np.nan,
                np.nan,
                -1.0,
                -1.0,
                -1.0,
                1.0,
                1.0,
                -1.0,
            ],
        ),
    ],
)
def test_sma(series_list: list, short: int, long: int, expected_pos: list):
    """Test simple moving average (SMA) strategy.

    Args:
        series_list (list): financial series observed
        short (int): short-term average
        long (int): long-term average
        expected_pos (list): position expected by the strategy
    """
    input_series = pd.Series(series_list)
    expected = pd.Series(expected_pos)
    computed = sma.sma(input_series, short, long)
    pd.testing.assert_series_equal(computed, expected)
