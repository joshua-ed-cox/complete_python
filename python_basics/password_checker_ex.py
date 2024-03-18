# Ask a user for their username and password.
# Greet the user and tell them their password in * 

# User Inputs
username = input("What is your username: ")
password = input("What is your password: ")


# Variable calculations
len_password = len(password)
display_password = "*" * len_password


# Display
print(f"Hello, {username}! Your password is: {display_password} and has a length of {len_password}.")


# Alternate solution
# username = input("What is your username: ")
# password = input("What is your password: ")

# print(f"Hello {username}!")
# print(f"Your password is: ", end="")
# for char in password:
#     print("*", end="")