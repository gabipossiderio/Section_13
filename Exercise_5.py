with open('arq.txt', 'r') as arquivo:
    typed_character = input('Please, type a character: ')
    chars_sum = 0
    for character in arquivo.read():
        if character == typed_character:
            chars_sum += 1
    if chars_sum == 0:
        print('Could not find the character typed in the read file.')
    else:
        print(f'We found the character typed {chars_sum} times in the read file.')
