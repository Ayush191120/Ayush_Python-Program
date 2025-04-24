# List Comprehensions:
# sorted(c for c in s if c.isalpha()) extracts and sorts letters
# sorted(c for c in s if c.isdigit()) extracts and sorts digits

# Concatenation:
# Combines the sorted letters and digits with letters + digits
# Joins them into a single string with ''.join()


def sort_letters_digits(s):
    letters = sorted([ch for ch in s if ch.isalpha()])
    digits = sorted([ch for ch in s if ch.isdigit()])
    return ''.join(letters + digits)

# Example usage
input_str = input("Enter a string with letters and digits: ")
result = sort_letters_digits(input_str)
print("Output:", result)
