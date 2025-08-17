###WAP to calculate profit or loss...

cost_price = int(input("Enter the Cost Price: "))
selling_price = int(input("Enter the selling Price: "))

total_price = cost_price - selling_price
if(selling_price > cost_price):
    print(f'{total_price} this is your profit...')
else:
    print(f'{total_price} this is ypur loss..')    