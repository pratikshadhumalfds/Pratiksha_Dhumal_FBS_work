cost_price = float(input("Enter the cost price of the book: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate discount amount
discount_amount = (discount_percent / 100) * cost_price

# Calculate selling price
selling_price = cost_price - discount_amount

print("Selling price of the book:", selling_price)