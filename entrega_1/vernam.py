import argparse
import random

POSSIBLE = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"


def generate_vernam_key(key_len):
    key = ""
    for i in range(key_len):
        position = random.randint(0, len(POSSIBLE)-1)
        key += POSSIBLE[position]
    return key


def vernam_cipher(input_filename, output_filename, key_filename):
    with open(input_filename, "r") as file:
        phrase = file.read()
    with open(key_filename, "w") as file:
        key = generate_vernam_key(len(phrase))
        file.write(key)

    ciphered = ""
    for i in range(len(phrase)):
        char = phrase[i]
        individual_key = key[i]
        if char.isalnum():
            ciphered += POSSIBLE[(POSSIBLE.find(char) + POSSIBLE.find(individual_key)) % len(POSSIBLE)]
        else:
            ciphered += char

    print(ciphered)
    with open(output_filename, "w") as file:
        file.write(ciphered)
    return ciphered


def vernam_decipher(input_filename, output_filename, key_filename):
    with open(input_filename, "r") as file:
        ciphered = file.read()
    with open(key_filename, "r") as file:
        key = file.read()
    phrase = ""
    for i in range(len(ciphered)):
        char = ciphered[i]
        individual_key = key[i]
        if char.isalnum():
            phrase += POSSIBLE[(POSSIBLE.find(char) - POSSIBLE.find(individual_key)) % len(POSSIBLE)]
        else:
            phrase += char

    print(phrase)
    with open(output_filename, "w") as file:
        file.write(phrase)
    return phrase


parser = argparse.ArgumentParser()
parser.add_argument(dest="key", type=str)
parser.add_argument(dest="input", type=str)
parser.add_argument(dest="output", type=str)
group = parser.add_mutually_exclusive_group()
group.add_argument("-c", action="store_true", default=False)
group.add_argument("-d", action="store_true", default=False)

args = parser.parse_args()

if args.c:
    vernam_cipher(args.input, args.output, args.key)
elif args.d:
    vernam_decipher(args.input, args.output, args.key)
else:
    print("Escolha cifrar ou decifrar")
