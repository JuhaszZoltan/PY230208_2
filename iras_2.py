file = open(file='nevek.csv', mode='a', encoding='utf-8')

print('az adatbekérés befejezéséhez hagyja a "név" mezőt üresen!')

while True:
    nev:str = input('kérem a diák nevét: ')
    if nev == '': break
    atlag:float = float(input(f'kérem {nev} tanulmányi átlagát: '))
    file.write(f'{nev};{atlag}\n')