import re

def check_num(number):
    # Using a regular expression to check the phone number format
    pattern = re.compile(r'^\d{2}-\d{3}-\d{4}$')
    
    # Checking the format using the match method of the regular expression
    if pattern.match(number):
        return True
    else:
        return False

# Take user input for the phone number
num = input("Enter a phone number (in format XX-XXX-XXXX): ")

if check_num(num):
    print(f"The phone number {num} is in the correct format.")
else:
    print(f"The phone number {num} is not in the expected format (XX-XXX-XXXX).")
