###WAP to input electricity unit charges and calculate total electricity bill according to the given cindition:
#for first 50 units rs. 0.50/unit
#for next 100 units rs. 0.75/unit
#for next 100 units rs. 1.20/units 
#for unit above 250 rs. 1.50/unit
#an additional surcharges of 20% is added to the bill...

units = 110

total_bill = 0

if(units > 0):
    if(units > 50):
        if(units > 150):
            pass
        else:
            total_bill = 50 *0.5
            unit2 = units - 50
            total_bill = total_bill + (unit2 * 0.75)
    else:
        total_bill = units * 0.5
else:
    print("Invalid input")

print(total_bill)    