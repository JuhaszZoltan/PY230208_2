from module import Film

filmek:list[Film] = []

file = open(file='marvel.txt', mode='r', encoding='utf-8')
for s in file: filmek.append(Film(s))
print(f'3.1: filmek száma: {len(filmek)}')

gyko:int = 0
for f in filmek:
    gyko += f.kiadas
print(f'átlagos gyártási k: ${round(gyko / len(filmek), 2)}M')

