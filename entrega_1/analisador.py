import re
import argparse


def analisador_de_frequencia(input_filename):
    with open(input_filename, "r") as file:
        cifrado = file.read()

    cifrado = cifrado.upper()
    cifrado = re.sub(r"[^a-zA-Z0-9]", "", cifrado)
    histograma = {}
    for char in cifrado.upper():
        if char in histograma.keys():
            histograma[char] += 1
        else:
            histograma[char] = 1

    frequency_dict = list(sorted(histograma.items(), key=lambda item: item[0]))
    most_common_letter = list(sorted(histograma.items(), key=lambda item: item[1]))[-1][0]
    
    for letter_tuple in frequency_dict:
        print(letter_tuple[0], round(letter_tuple[1]/len(cifrado) * 100, 2), "%")

    print(
        "Most common letter in ciphered text is:",
        most_common_letter,
        "\nKey should be:",
        ord(most_common_letter) - ord("A"),
    )
    return frequency_dict


parser = argparse.ArgumentParser()
parser.add_argument(dest="input", type=str)
args = parser.parse_args()
analisador_de_frequencia(args.input)
