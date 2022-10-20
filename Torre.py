class Torre:
    def __init__(self, qtd_discos):
        self._discos = []
        self._qtd_discos = qtd_discos

        for item in range(qtd_discos, 0, -1):
            self._discos.append(0)

    def empilha_disco(self, peso):
        self._discos.insert(0,peso)

    def get_tamanho(self):
        return self._qtd_discos

    def get_first(self):
        first = self._discos[self.get_tamanho() - 1]
        indice = self.get_tamanho() - 1
        while first == 0:
            first = self._discos[indice]
            if indice == 0:
                break
            else:
                indice=indice-1
        return first



    def set_vazio_first_position_torre(self):
        indice = self.get_tamanho() - 1
        while self._discos[indice] == 0:
            if indice== 0:
                break
            indice-=1
        self._discos[indice] = 0

    def insert(self,peso):
        indice = self.get_tamanho() - 1
        while True:
            if self._discos[indice-1]!= 0:
                break
            if indice== 0:
                break
            indice-=1
        self._discos.insert(indice, peso)

    def desempilha_disco(self):
        self._discos.pop()

    def get_discos(self):
        return self._discos
