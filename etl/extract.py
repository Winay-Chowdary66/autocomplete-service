import os
import pandas as pd


sample_data = [
    {
        "time": 1661472000000000000,
        "symbol": "0A",
        "instrument_name": "Mini European 1% Fuel Oil Barges FOB Rdam (Platts) BALMO Futures",
        "asset_class": "Futures",
        "product_group": "Energy",
        "volume": 0,
        "open_interest": 0,
        "category": "1",
        "schema": "[MBO, OHLCV-1D]",
        "publisher": "CME",
        "region": "US",
        "available_from_date": "2022-01-01",
    },
    {
        "time": 1661472000000000000,
        "symbol": "1A",
        "instrument_name": "Gold Futures",
        "asset_class": "Futures",
        "product_group": "Commodities",
        "volume": 2,
        "open_interest": 0,
        "category": "3",
        "schema": "[MBO, OHLCV-1D]",
        "publisher": "CME",
        "region": "US",
        "available_from_date": "2022-01-01",
    },
    {
        "time": 1661472000000000000,
        "symbol": "2A",
        "instrument_name": "S&P 500 Index",
        "asset_class": "Equities & ETF",
        "product_group": "Indices",
        "volume": 4,
        "open_interest": 0,
        "category": "4",
        "schema": "[MBO, OHLCV-1D]",
        "publisher": "NYSE",
        "region": "US",
        "available_from_date": "2022-01-01",
    },
    {
        "time": 1661472000000000000,
        "symbol": "3A",
        "instrument_name": "EUR/USD FX Spot",
        "asset_class": "FX",
        "product_group": "Currency Pairs",
        "volume": 6,
        "open_interest": 0,
        "category": "5",
        "schema": "[MBO, OHLCV-1D]",
        "publisher": "Forex",
        "region": "EU",
        "available_from_date": "2022-01-01",
    },
    {
        "time": 1661472000000000000,
        "symbol": "4A",
        "instrument_name": "Crude Oil Futures",
        "asset_class": "Futures",
        "product_group": "Commodities",
        "volume": 8,
        "open_interest": 0,
        "category": "3",
        "schema": "[MBO, OHLCV-1D]",
        "publisher": "CME",
        "region": "US",
        "available_from_date": "2022-01-01",
    },
    {
        "time": 1661472000000000000,
        "symbol": "5A",
        "instrument_name": "AAPL",
        "asset_class": "Equities & ETF",
        "product_group": "Individual Stocks",
        "volume": 10,
        "open_interest": 0,
        "category": "4",
        "schema": "[MBO, OHLCV-1D]",
        "publisher": "NASDAQ",
        "region": "US",
        "available_from_date": "2022-01-01",
    },
    {
        "time": 1661472000000000000,
        "symbol": "ES1",
        "instrument_name": "Nearby BTIC+ Futures on E-mini S&P 500 Stock Price Index Futures",
        "asset_class": "Equities & ETF",
        "product_group": "Individual Stocks",
        "volume": 10,
        "open_interest": 0,
        "category": "4",
        "schema": "[MBO, OHLCV-1D]",
        "publisher": "NASDAQ",
        "region": "US",
        "available_from_date": "2022-01-01",
    },
        {
        "time": 1661472000000000000,
        "symbol": "ES",
        "instrument_name": "E-mini S&P 500 Futures",
        "asset_class": "Equities & ETF",
        "product_group": "Individual Stocks",
        "volume": 10,
        "open_interest": 0,
        "category": "4",
        "schema": "[MBO, OHLCV-1D]",
        "publisher": "NASDAQ",
        "region": "US",
        "available_from_date": "2022-01-01",
    },
     {
        "time": 1661472000000000000,
        "symbol": "ES",
        "instrument_name": "E-mini S&P 500 Options",
        "asset_class": "Equities & ETF",
        "product_group": "Individual Stocks",
        "volume": 10,
        "open_interest": 0,
        "category": "4",
        "schema": "[MBO, OHLCV-1D]",
        "publisher": "NASDAQ",
        "region": "US",
        "available_from_date": "2022-01-01",
    },
    {
        "time": 1661472000000000000,
        "symbol": "ES",
        "instrument_name": "Eversource Energy",
        "asset_class": "Equities & ETF",
        "product_group": "Individual Stocks",
        "volume": 10,
        "open_interest": 0,
        "category": "4",
        "schema": "[MBO, OHLCV-1D]",
        "publisher": "NASDAQ",
        "region": "US",
        "available_from_date": "2022-01-01",
    },
    {
        "time": 1661472000000000000,
        "symbol": "DHDG",
        "instrument_name": "WisdomTree International ESG Fund",
        "asset_class": "Equities & ETF",
        "product_group": "Individual Stocks",
        "volume": 10,
        "open_interest": 0,
        "category": "4",
        "schema": "[MBO, OHLCV-1D]",
        "publisher": "NASDAQ",
        "region": "US",
        "available_from_date": "2022-01-01",
    },

    # Add more sample data here
]




class Extract(object):
    def __init__(self, file_path):
        self.file_path = file_path

        self.read_file()

    def read_file(self):
        self.df = pd.read_excel(self.file_path)

    def get_dataframe(self):
        df = pd.DataFrame(sample_data)
        return df
