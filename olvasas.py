file = open(file='diakok.txt', mode='r', encoding='utf-8')

lnm:int = -1
lmdn:str = ''

for s in file:
    v:list[str] = s.strip().split(' ')
    magassag:int = int(v[2])
    if magassag > lnm:
        lnm = magassag
        lmdn = f'{v[0]} {v[1]}'

print(f'a legmagasabb diák {lmdn} ({lnm} cm)')