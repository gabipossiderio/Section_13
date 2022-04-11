vowels = ['a', 'e', 'i', 'o', 'u']

with open('file1.txt', 'r+') as old_file:
    file_content = old_file.read()
    modified_content = ''
    print(f'File before changes: \n{file_content}')
    for character in file_content:
        if character.lower() in vowels:
            character = "*"
        modified_content += character
with open('file2.txt', 'r+') as new_file:
    new_file.write(modified_content)
    new_file.seek(0)
    print(f'\nFile after vowels are replaced by (*): \n{new_file.read()}')
