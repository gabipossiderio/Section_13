import string

alphabet = string.ascii_lowercase

with open('arq.txt', 'r') as arquivo:
    print(f'In the read file, it was possible to find the following quantities:')
    characters_dict = {letter: 0 for letter in alphabet}
    for character in arquivo.read():
        if character in characters_dict.keys():
            characters_dict[character] += 1
    print(characters_dict)
