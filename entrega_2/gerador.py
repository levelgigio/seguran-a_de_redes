import os.path
import random
import hashlib
from datetime import datetime

SALT = "abc123"


def add_salt(string):
    return f"{string}{SALT}"


def user_exists(username):
    if os.path.isfile(f"{username}.txt"):
        return True
    else:
        return False


def generate_tokens(seed):
    tokens = []
    token = f"{seed}{datetime.now().strftime('%d%m%Y%H%M')}"
    for _ in range(5):
        token = hashlib.md5(token.encode("utf-8")).hexdigest()
        tokens.append(token[:6])

    return tokens


def get_passwords_hash(username):
    with open(f"{username}.txt", "r") as file:
        seed = file.readline()
        local_password = file.readline()

    return seed.strip(), local_password.strip()


def save_passwords_hash(username, seed, local_password):
    with open(f"{username}.txt", "w") as file:
        file.write(f"{seed}\n")
        file.write(f"{local_password}\n")


def main():
    print("Login")
    username = str(input("Username: "))
    if user_exists(username):
        print("Returning user...")
        input_password = str(input("Local password: "))
        input_password = add_salt(input_password)
        seed, local_password = get_passwords_hash(username)
        if local_password != hashlib.md5(input_password.encode("utf-8")).hexdigest():
            print("Wrong Password")
            exit(-1)
        else:
            print("Login sucessfull")
    else:
        print("New user...")
        seed = str(random.getrandbits(64))
        seed = add_salt(seed)
        local_password = input("Create local password: ")
        local_password = add_salt(local_password)
        seed = hashlib.md5(seed.encode("utf-8")).hexdigest()
        local_password = hashlib.md5(local_password.encode("utf-8")).hexdigest()

        save_passwords_hash(username, seed, local_password)

    while True:
        input("Press any key to generate tokens")
        print("Valid tokens:", *generate_tokens(seed))


if __name__ == "__main__":
    main()
