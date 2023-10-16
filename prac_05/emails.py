"""
Emails
Estimate: 15 minutes
Actual: 20 minutes
"""


def main():
    """Build dictionary of emails and names"""
    email_to_name = {}
    email = input("Email: ")
    while email != '':
        name = extract_name_from_email(email)
        name_check = input(f"Is your name {name}? (Y/n) ").upper()
        if name_check != 'Y' and name_check != '':
            name = input("Name: ").title()
        email_to_name[email] = name
        email = input("Email: ")
    for email, name in email_to_name.items():
        print(f"{email} {name}")


def extract_name_from_email(email):
    """Extract name from before @ symbol in email"""
    email_prefix = email.split('@')[0]
    name_parts = email_prefix.split('.')
    name = ' '.join(name_parts).title()
    return name


main()
