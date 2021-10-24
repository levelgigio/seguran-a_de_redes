import os.path
import hashlib
from datetime import datetime


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


def remove_used_tokens(tokens, used_token):
    used = 0
    valid_tokens = tokens.copy()
    for token in reversed(tokens):
        if token == used_token or used == 1:
            valid_tokens.remove(token)
            used = 1

    return valid_tokens


def main():
    last_used_token = None

    while True:
        print("=============\nLogin")
        username = str(input("Username: "))
        if user_exists(username):
            print("Returning user...")
            input_token = str(input("Enter your token: "))
            seed, _ = get_passwords_hash(username)
            valid_tokens = remove_used_tokens(generate_tokens(seed), last_used_token)
            if input_token in valid_tokens:
                print("Login sucessfull")
                last_used_token = input_token
            else:
                print("Login failed")


if __name__ == "__main__":
    main()
