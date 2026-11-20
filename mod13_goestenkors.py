import unittest
from datetime import datetime


def valid_symbol(symbol):
    return isinstance(symbol, str) and 1 <= len(symbol) <= 7 and symbol.isascii() and symbol.isalpha() and symbol.isupper()


def valid_chart_type(chart_type):
    return chart_type in ("1", "2")


def valid_time_series(time_series):
    return time_series in ("1", "2", "3", "4")


def valid_date(date):
    if not isinstance(date, str):
        return False
    try:
        parsed_date = datetime.strptime(date, "%Y-%m-%d")
        return parsed_date.strftime("%Y-%m-%d") == date
    except ValueError:
        return False


def valid_date_range(start_date, end_date):
    if not valid_date(start_date) or not valid_date(end_date):
        return False
    return end_date >= start_date


class TestStockInputs(unittest.TestCase):
    def test_symbol_valid(self):
        self.assertTrue(valid_symbol("AAPL"))
        self.assertTrue(valid_symbol("A"))
        self.assertTrue(valid_symbol("ABCDEFG"))

    def test_symbol_invalid(self):
        self.assertFalse(valid_symbol("aapl"))
        self.assertFalse(valid_symbol("AAPL1"))
        self.assertFalse(valid_symbol("ABCDEFGH"))
        self.assertFalse(valid_symbol(""))
        self.assertFalse(valid_symbol("A B"))

    def test_chart_type_valid(self):
        self.assertTrue(valid_chart_type("1"))
        self.assertTrue(valid_chart_type("2"))

    def test_chart_type_invalid(self):
        self.assertFalse(valid_chart_type("0"))
        self.assertFalse(valid_chart_type("3"))
        self.assertFalse(valid_chart_type("12"))
        self.assertFalse(valid_chart_type("a"))

    def test_time_series_valid(self):
        for choice in ("1", "2", "3", "4"):
            self.assertTrue(valid_time_series(choice))

    def test_time_series_invalid(self):
        self.assertFalse(valid_time_series("0"))
        self.assertFalse(valid_time_series("5"))
        self.assertFalse(valid_time_series("14"))
        self.assertFalse(valid_time_series("a"))

    def test_start_date_valid(self):
        self.assertTrue(valid_date("2026-01-15"))
        self.assertTrue(valid_date("2024-02-29"))

    def test_start_date_invalid(self):
        self.assertFalse(valid_date("01-15-2026"))
        self.assertFalse(valid_date("2026-1-15"))
        self.assertFalse(valid_date("2026-02-30"))
        self.assertFalse(valid_date("hello"))

    def test_end_date_valid(self):
        self.assertTrue(valid_date("2026-11-20"))
        self.assertTrue(valid_date("2025-12-31"))

    def test_end_date_invalid(self):
        self.assertFalse(valid_date("11/20/2026"))
        self.assertFalse(valid_date("2026-13-01"))
        self.assertFalse(valid_date("2026-11-2"))
        self.assertFalse(valid_date(""))

    def test_date_range_valid(self):
        self.assertTrue(valid_date_range("2026-01-01", "2026-02-01"))
        self.assertTrue(valid_date_range("2026-01-01", "2026-01-01"))

    def test_date_range_invalid(self):
        self.assertFalse(valid_date_range("2026-03-01", "2026-02-01"))
        self.assertFalse(valid_date_range("2026-02-30", "2026-03-01"))


if __name__ == "__main__":
    unittest.main()
