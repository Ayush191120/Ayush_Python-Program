# Slab-based Calculation:
# Clearly defines each consumption slab with its rate
# Automatically calculates how many units fall into each slab

# Input Validation:
# Handles negative values
# Validates numeric input

# Output:
# Well-formatted bill presentation
# Clear labeling of each component


def calculate_electricity_bill(units):
    total = 0

    print("Electricity Bill:")
    
    if units > 500:
        slab = units - 500
        cost = slab * 15
        print(f"501-{units} units @ 15/unit = {cost} ₹")
        total += cost
        units = 500

    if units > 300:
        slab = units - 300
        cost = slab * 10
        print(f"301-{units} units @ 10/unit = {cost} ₹")
        total += cost
        units = 300

    if units > 100:
        slab = units - 100
        cost = slab * 7
        print(f"101-{units} units @ 7/unit = {cost} ₹")
        total += cost
        units = 100

    if units > 0:
        cost = units * 5
        print(f"0-{units} units @ 5/unit = {cost} ₹")
        total += cost

    print(f"Total Amount Payable = {total} ₹")


# Example usage
try:
    usage = int(input("Enter electricity usage in kWh: "))
    if usage < 0:
        print("Usage cannot be negative.")
    else:
        calculate_electricity_bill(usage)
except ValueError:
    print("Please enter a valid integer.")
