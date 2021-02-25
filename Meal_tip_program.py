'''
Write a program to prompt the user for the price of the meal and
the percent tip they want to leave and then print both the tip amount and
the total bill with the tip included.
'''
# def total(*args):
#     tip_percent=tip_percent//100*100
#     tip = tip_percent//100*meal_price
#     result = meal_price + tip
#     print(f"Price pf the meal:{meal_price}")
#     print(f"Tip percent they want to leave: {tip_percent} and tip amount they want to leave is: {tip}")
#     print(f" Total bill with tip included: {result}")
# meal_price=int(input("Enter meal price:"))
# tip_percent=int(input("Enter percent of tip:"))
# total(meal_price,tip_percent)
# ------------------------------------------------------------------------------------------------
# class Total:
#     def __init__(self,tip_percent,tip,meal_price):
#         self.tip_percent=tip_percent
#         self.tip=tip
#         self.meal_price=meal_price
#         tip_percent = tip_percent // 100 * 100
#         tip = tip_percent//100*meal_price
#         result = meal_price + tip
#
#
#     def statement(self,*args):
#         print(f"Price pf the meal:{self.meal_price}")
#         print(f"Tip percent they want to leave: {self.tip_percent} and tip amount they want to leave is: {self.tip}")
#         print(f" Total bill with tip included: {self.result}")
#
# meal_price=int(input("Enter meal price:"))
# tip_percent=int(input("Enter percent of tip:"))
# Total.statement(meal_price,tip_percent)
# ------------------------------------------------------------------------------------------------------
meal_price=int(input("Enter meal price:"))
tip_percent=int(input("Enter tip percent:"))//100*100
tip=int(tip_percent)//100*int(meal_price)
result=int(meal_price)+int(tip)
print(f"Price of the meal:{meal_price}")
print(f"Tip percent they want to leave: {tip_percent} and tip amount they want to leave is: {tip}")
print(f"Total bill with tip included: {result}")