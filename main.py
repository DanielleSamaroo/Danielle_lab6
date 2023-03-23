# Worked with Kim 3/7/23
def password_encode(password):
    # adds 3 to the original password
    encoded_password = "".join([str((int(digit) + 3) % 10) for digit in password])
    return encoded_password


def decoder(password):
    decoded_password = " "
    for x in password:
        temp_pass = int(x)
        temp_pass = int(temp_pass - 3)
        if (int(temp_pass) > 0):
            temp_pass = int(temp_pass) % 10
        else:
            temp_pass = 10 - int(temp_pass) * (-1)
        decoded_password = decoded_password + str(temp_pass)
    return decoded_password


def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    return input("\nPlease enter an option: ")

if __name__ == '__main__':
    # prints menu and asks for input in a loop
    while True:
        # function that prints menu
        print_menu()
        option = int(input("\nPlease enter an option: "))   # asks user for option input
        if option == 1:
            password = input("Please enter your password to encode: ")  # asks user for password to input
            print("Your password has been encoded and stored!\n")
        elif option == 2:
            decoded_password = decoder(password)
            print(f"The encoded password is {decoded_password}, and the original password is {password}")
        elif option == 3:
            break