import re

# Name: Handles single names, multi-part names, apostrophes, and hyphens
name = r"^[A-Z][a-z]*?(?:['-][A-Z][a-z]+)*(?: [A-Z][a-z]*?(?:['-][A-Z][a-z]+)*)*$"
name_regex = re.compile(name)

# Phone Number: Accepts 123-456-7890, (123) 456-7890, 123.456.7890, 123 456 7890
phone_number = r"^(\(\d{3}\)|\d{3})[-.\s]?\d{3}[-.\s]?\d{4}$"
phone_regex = re.compile(phone_number)

# Email Address: Must start with a letter; allows letters, numbers, dots, hyphens before @
# Example valid: john.cena@wwe.com, example.name@domain.co.ke
# Example invalid: 123john.cena@wwe.com
email_address = r"^[A-Za-z][\w\.-]*@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
email_regex = re.compile(email_address)
email_strict_regex = re.compile(r"^(?!.*\.\.)[A-Za-z][\w\.-]*@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")