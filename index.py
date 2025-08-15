def calculate_discount(price, discount_percent):
    """
    The function takes the original price (price) and the discount percentage (discount_percent) as parameters.
      If the discount is 20% or higher, then the discount is applied; otherwise, it returns the original price.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt the user for input and calculate the final price
try:
    original_price = float(input("Enter the original price of the item (KES): "))
    discount = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(original_price, discount)

    if discount >= 20:
        print(f" Discount applied! Final price: KES {final_price:,.2f}")
    else:
        print(f" No discount applied. Price remains: KES {original_price:,.2f}")

except ValueError:
    print("Please enter valid numerical values for price and discount.")
