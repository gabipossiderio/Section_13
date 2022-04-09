with open('arq.txt', 'r') as arquivo:
    lines = arquivo.readlines()
    print(f'The typed file has {len(lines)} lines.')
