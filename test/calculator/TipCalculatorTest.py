import unittest

from calculator.TipCalculator import TipCalculator

__author__ = 'joseph swager'


class TipCalculatorTest(unittest.TestCase):
    # Tests set amount method
    def test_set_bill_amount(self):
        # arrange/act
        bill_amount = TipCalculator().set_bill_amount("20.00")
        # assert
        self.assertEqual(bill_amount, 20.00)

    def test_set_bill_amount_with_dollar_sign(self):
        # arrange/act
        bill_amount = TipCalculator().set_bill_amount("$20.00")
        # assert
        self.assertEqual(bill_amount, 20.00)

    def test_set_bill_amount_as_int_value(self):
        # arrange/act
        bill_amount = TipCalculator().set_bill_amount("20")
        # assert
        self.assertEqual(bill_amount, 20.00)

    def test_set_bill_amount_raises_Value_Exception(self):
        # arrange/act/assert
        self.assertRaises(ValueError, TipCalculator().set_bill_amount, "1A23")

    # Tests set tip rate method
    def test_set_tip_rate(self):
        # arrange/act
        tip_rate = TipCalculator().set_tip_rate("15")
        # assert
        self.assertEqual(tip_rate, 0.15)

    def test_set_tip_rate_not_whole_number_raises_Type_Exception(self):
        # arrange/act/assert
        self.assertRaises(TypeError, TipCalculator().set_tip_rate, "15.5")

    def test_set_tip_rate_as_alpha_values_raises_Type_Exception(self):
        # arrange/act/assert
        self.assertRaises(TypeError, TipCalculator().set_tip_rate, "ABC")

    def test_calculate_tip(self):
        # arrange
        tipcalc = TipCalculator()
        tipcalc.set_bill_amount("10.10")
        tipcalc.set_tip_rate("20")

        # act
        tip_amount = tipcalc.calculate_tip()

        # assert
        self.assertEqual(tip_amount, 2.02)

    def test_calculate_total(self):
        # arrange
        tipcalc = TipCalculator()
        tipcalc.set_bill_amount("10.10")
        tipcalc.set_tip_rate("20")
        tipcalc.calculate_tip()

        # act
        total = tipcalc.calculate_total()

        # assert
        self.assertEqual(total, 12.12)


if __name__ == '__main__':
    unittest.main()
