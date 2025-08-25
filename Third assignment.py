# Function to calculate the final price after applying a discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent /10000) * price
        final_price = price - discount_amount
        return final_price
    else:
        # If discount is less than 20%, no discount applied
        return price

# Prompt the user for inputs
original_price = float(input("Enter the original price of the item: ")) 
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(original_price, discount_percent)

# Display the result
if discount_percent >= 20:
    print(f"Final price after {discount_percent}% discount: ${final_price:.2f}")
else:
    print(f"No discount applied. The price remains: ${final_price:.2f}")
