"""
Get password of desired length and print asterisks of password length
"""


def main():
    minimum_length = int(input("Minimum length for password: "))
    password = get_password(minimum_length)
    print_password(password)


def print_password(password):
    print(len(password) * '*')


def get_password(minimum_length):
    password = input("Password: ")
    while len(password) < minimum_length:
        print("Password is not long enough")
        password = input("Password: ")
    return password


main()
