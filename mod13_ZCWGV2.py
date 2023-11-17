import unittest
from main import validate_inputs  # replace 'your_module' with the actual module where your function is defined

class TestStockAPIInputs(unittest.TestCase):

    def test_symbol_constraint(self):
        self.assertTrue(validate_inputs('AAPL', '1', '1', '2022-01-01', '2022-01-10'))
        self.assertTrue(validate_inputs('XYZ1234', '1', '1', '2022-01-01', '2022-01-10'))
        self.assertFalse(validate_inputs('invalid_symbol', '1', '1', '2022-01-01', '2022-01-10'))

    def test_chart_type_constraint(self):
        self.assertTrue(validate_inputs('AAPL', '1', '1', '2022-01-01', '2022-01-10'))
        self.assertTrue(validate_inputs('AAPL', '2', '1', '2022-01-01', '2022-01-10'))
        self.assertFalse(validate_inputs('AAPL', '3', '1', '2022-01-01', '2022-01-10'))

    def test_time_series_constraint(self):
        self.assertTrue(validate_inputs('AAPL', '1', '1', '2022-01-01', '2022-01-10'))
        self.assertTrue(validate_inputs('AAPL', '1', '4', '2022-01-01', '2022-01-10'))
        self.assertFalse(validate_inputs('AAPL', '1', '5', '2022-01-01', '2022-01-10'))

    def test_start_date_constraint(self):
        self.assertTrue(validate_inputs('AAPL', '1', '1', '2022-01-01', '2022-01-10'))
        self.assertFalse(validate_inputs('AAPL', '1', '1', 'invalid_date', '2022-01-10'))

    def test_end_date_constraint(self):
        self.assertTrue(validate_inputs('AAPL', '1', '1', '2022-01-01', '2022-01-10'))
        self.assertFalse(validate_inputs('AAPL', '1', '1', '2022-01-01', 'invalid_date'))

if __name__ == '__main__':
    unittest.main()
