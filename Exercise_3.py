with open('arq.txt', 'r') as arquivo:
    vowels_sum = 0
    for character in arquivo.read():
        if character.lower() in ['a', 'e', 'i', 'o', 'u']:
            vowels_sum += 1
    print(f'The read file has {vowels_sum} vowels.')
