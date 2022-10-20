class Torre:
    def __init__(self, qtd_discos):
        self._discos = []
        self._qtd_discos = qtd_discos
        self._numero_movimentos = 0

        for item in range(qtd_discos, 0, -1):
            self._discos.append(0)

    def inicia_torre_com_disco(self, peso):
        self._discos.insert(0,peso)

    def desempilha_disco(self):
        self._discos.pop()

    def get_tamanho(self):
        return self._qtd_discos

    def get_numero_movimentos(self):
        return self._numero_movimentos

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

        if indice != 0 and self._discos[indice-1] <peso:
            print("Movimentação inválida: Um disco maior nunca deve ficar por cima de um disco menor")
            return False
        else:
            self._discos.insert(indice, peso)
            self._numero_movimentos += 1
            return True

    def get_discos(self):
        return self._discos
