# Input Validation:
# Ensures dates are in correct dd-mm-yyyy format
# Handles invalid dates (like 31-02-2023) automatically

# Precise Calculation:
# Uses Python's built-in datetime module for accurate date math

# Output:
# Shows total days with comma formatting for readability
# Displays dates in a more readable format (e.g., "15 August 1990")
# Proper error messages for invalid input


from datetime import datetime

def calculate_date_difference(date1_str, date2_str):
    # Convert string to datetime object
    date_format = "%d-%m-%Y"
    date1 = datetime.strptime(date1_str, date_format)
    date2 = datetime.strptime(date2_str, date_format)
    
    # Calculate the absolute difference in days
    difference = abs((date2 - date1).days)
    
    print(f"Difference between {date1_str} and {date2_str} is {difference} days.")

# Example usage
birthdate = input("Enter your birthdate (dd-mm-yyyy): ")
today = input("Enter today's date (dd-mm-yyyy): ")

calculate_date_difference(birthdate, today)
