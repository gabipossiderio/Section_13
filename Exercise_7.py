vowels = ['a', 'e', 'i', 'o', 'u']

with open('arq.txt', 'r+') as arquivo:
    arquivo_old = arquivo.read()
    arquivo_new = ''
    print(f'File before changes: \n{arquivo_old}')
    for character in arquivo_old:
        if character.lower() in vowels:
            character = "*"
        arquivo_new += character
    arquivo.seek(0)
    arquivo.write(arquivo_new)
    arquivo.seek(0)
    print(f'\nFile after vowels are replaced by (*): \n{arquivo.read()}')
