class Film:
    def __init__(self, sor:str):
        v:list[str] = sor.strip().split(';')
        self.cim:str = v[0]
        self.fazis:int = int(v[1])
        self.bemutato:str = v[2]
        self.kiadas:int = int(v[3])
        self.bevetel:int = int(v[4])
