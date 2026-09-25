item = float(input("enter the price of the item: "))
price = item 
rate = 0.06875
def calculate_tax():
    tax = price * rate
    print(f"{item} costs ${price} dollars before tax and ${price + tax} after tax")
calculate_tax()