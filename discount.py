def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        dicounted_price = price - (price * discount_percent / 100)
        return dicounted_price
    else:
        return price
# prompt user for input
original_price = float(input("Enter the original price of the item: "))  
discount_percentage = float(input("Enter the discount percentage: "))

# calculate and print the final price
final_price = calculate_discount(original_price, discount_percentage)
print(f"the final price after applying the discount is : {final_price}")

