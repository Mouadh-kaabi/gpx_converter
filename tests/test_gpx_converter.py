#!/usr/bin/env python

"""Tests for `gpx_converter` package."""

import pytest
from gpx_converter import Converter
import pandas as pd


@pytest.fixture
def converter():
    return Converter(input_file='examples/test_data/test1.gpx')


def test_gpx_to_dataframe(converter):
    result = converter.gpx_to_pandas_dataframe()
    assert result is not None
    assert isinstance(result, pd.DataFrame)


def test_gpx_to_csv(converter):
    result = converter.gpx_to_csv(output_file='examples/test_data/converted.csv')
    assert result is not None


def test_gpx_to_json(converter):
    result = converter.gpx_to_json(output_file='examples/test_data/converted.json')
    assert result is not None


def test_gpx_to_excel(converter):
    result = converter.gpx_to_excel(output_file='examples/test_data/converted.xlsx')
    assert result is not None
