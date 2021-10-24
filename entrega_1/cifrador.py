import re
import argparse

POSSIBLE = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"


def cesar_cipher(input_filename, output_filename, key):
    with open(input_filename, "r") as file:
        phrase = file.read()

    ciphered = ""
    for char in phrase:
        if char.isalnum():
            ciphered += POSSIBLE[(POSSIBLE.find(char) + key) % len(POSSIBLE)]
        else:
            ciphered += char

    print(ciphered)
    with open(output_filename, "w") as file:
        file.write(ciphered)
    return ciphered


def cesar_decipher(input_filename, output_filename, key):
    with open(input_filename, "r") as file:
        ciphered = file.read()
    phrase = ""
    for char in ciphered:
        if char.isalnum():
            phrase += POSSIBLE[(POSSIBLE.find(char) - key) % len(POSSIBLE)]
        else:
            phrase += char

    print(phrase)
    with open(output_filename, "w") as file:
        file.write(phrase)
    return phrase


parser = argparse.ArgumentParser()
parser.add_argument("-k", type=int, default=0)
parser.add_argument(dest="input", type=str)
parser.add_argument(dest="output", type=str)
group = parser.add_mutually_exclusive_group()
group.add_argument("-c", action="store_true", default=False)
group.add_argument("-d", action="store_true", default=False)

args = parser.parse_args()

if args.c:
    cesar_cipher(args.input, args.output, args.k)
elif args.d:
    cesar_decipher(args.input, args.output, args.k)
else:
    print("Escolha cifrar ou decifrar")
