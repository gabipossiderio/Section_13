import string

with open('arq.txt', 'r') as arquivo:
    vowels_sum = 0
    consonants_sum = 0
    ignored_chars = string.whitespace + string.punctuation + string.digits
    for character in arquivo.read():
        if character.lower() in ['a', 'e', 'i', 'o', 'u']:
            vowels_sum += 1
        elif character in ignored_chars:
            pass
        else:
            consonants_sum += 1
    print(f'The read file has {vowels_sum} vowels and {consonants_sum} consonants.')
