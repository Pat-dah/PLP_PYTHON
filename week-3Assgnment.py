def calculate_discount(price, discount_percent):
    if discount_percent >=20:
        discount_amount =price * (discount_percent/100)
        final_price = price-discount_amount
        return  final_price
    else:
        return price

# 2Using the calculate_discount function, prompt the user to enter the original price of an item and
# the discount percentage. Print the final price after applying the discount, or
# if no discount was applied, print the original price.
original_price =float(input("enter the original price for this item: "))
discount =float(input(" what is the percentage discount for this?  "))

final_price = calculate_discount(original_price, discount)
print(f"This is the final price",{final_price})