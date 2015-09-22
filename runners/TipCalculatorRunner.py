from calculator.TipCalculator import TipCalculator

__author__ = 'joseph swager'

tipCalc = TipCalculator()
tipCalc.set_bill_amount(input("What is the bill amount?"))
tipCalc.set_tip_rate(input("What is the tip rate?"))

tipCalc.calculate_tip()
print("The tip is $", end="")
print("{0:.2f}".format(tipCalc.tip.tipAmount))

tipCalc.calculate_total()
print("The Total is $", end="")
print("{0:.2f}".format(tipCalc.bill.total))
