from math import pi

file = open(file='elso.txt', mode='w', encoding='UTF-8')

file.write('hello, this is my first txt file! :3 uwu\n')

nev:str = 'Juhász Zoltán'
file.write(f'My name is {nev}\n')

file.write(f'Pi = {pi}')

print('done!')