import crypt
# function to test password
def test_password(algorithm_salt, hashed_password, password_guess):
# use salt to hash the guess
hashed_guess = crypt.crypt(password_guess, algorithm_salt)
# compare salted guess against hashed password
if hashed_guess == hashed_password:
return True

    return False


# load dictionary file
with open("top1000.txt", "r") as file:
    passwords = file.readlines()

# open shadow file
with open("shadow", "r") as shadow_file:
    shadow_lines = shadow_file.readlines()

# loop through each user in shadow
for line in shadow_lines:

    parts = line.strip().split(":")
    username = parts[0]
    hashed_password = parts[1]

    # get algorithm + salt
    password_parts = hashed_password.split("$")
    algorithm_salt = "$" + password_parts[1] + "$" + password_parts[2] + "$"

    # loop through passwords
    for password in passwords:

        password = password.strip()

        if test_password(algorithm_salt, hashed_password, password):
            print(username + ": " + password)
            break
