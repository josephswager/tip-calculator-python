import re

from calculator.model.Bill import Bill
from calculator.model.Tip import Tip

__author__ = 'joseph swager'


class TipCalculator(object):
    def __init__(self):
        self.bill = Bill()
        self.tip = Tip()

    def calculate_total(self):
        self.bill.total = self.bill.billAmount + self.tip.tipAmount
        return self.bill.total

    def set_tip_rate(self, rate):
        if rate.isdigit():
            self.tip.tipRate = float(rate) / 100
            return self.tip.tipRate
        else:
            raise TypeError('Must be a whole number')

    def calculate_tip(self):
        if isinstance(self.bill.billAmount, float):
            tip = self.bill.billAmount * self.tip.tipRate
            self.tip.tipAmount = round(tip, 2)
            return self.tip.tipAmount

    def set_bill_amount(self, amount):
        if re.match("(^(\$)?\d+(\.\d+)?$)", amount):
            if amount.startswith("$"):
                print("Removing Dollar Sign")
                self.bill.billAmount = round(float(amount[1:]), 2)

            if amount.isdigit():
                self.bill.billAmount = round(float(amount), 2)

            if TipCalculator.isfloat(amount):
                self.bill.billAmount = round(float(amount), 2)

            return self.bill.billAmount
        else:
            raise ValueError('This is not valid currency/decimal! Ex: $4.00, 4, 4.00')

    @classmethod
    def isfloat(cls, value):
        try:
            float(value)
            return True
        except ValueError:
            return False
