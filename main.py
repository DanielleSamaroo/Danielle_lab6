# Worked with Kim 3/7/23
def password_encode(password):
    # adds 3 to the original password
    encoded_password = "".join([str((int(digit) + 3) % 10) for digit in password])
    return encoded_password


def password_decode(encoded_password):
    pass


def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    return input("\nPlease enter an option: ")

if __name__ == '__main__':
    while True:
        option = print_menu()
        if option == '1': # Encodes program
            # prompt user for password
            password = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!\n")
            # stores password and encodes
            encoded_password = password_encode(password)
        elif option == '2': # Decodes program
            pass
        elif option == '3': # Exits program
            break