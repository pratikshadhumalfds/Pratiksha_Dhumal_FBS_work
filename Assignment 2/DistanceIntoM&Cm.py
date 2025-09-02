def convert_to_metric(feet, inches):
    # Convert feet and inches to total inches
    total_inches = feet * 12 + inches

    # Convert inches to cm (1 inch = 2.54 cm)
    total_cm = total_inches * 2.54

    # Convert cm to meters and remaining cm
    meters = int(total_cm // 100)
    centimeters = total_cm % 100

    return meters, centimeters

feet = float(input("Enter feet: "))
inches = float(input("Enter inches: "))

meters, centimeters = convert_to_metric(feet, inches)

print(f"{int(feet)} feet and {inches} inches is equal to {meters} meters and {centimeters:.2f} centimeters.")