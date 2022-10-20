from Torre import Torre

def calcular_pontuacao(min_tentativas, num_tentativas):
    pontuacao = 100 + ((min_tentativas-num_tentativas)/num_tentativas) * 100
    return pontuacao

def numero_tentativas_min(qtd_discos):
    return 2 ** qtd_discos - 1

def numero_tentativas():
    return torre1.get_numero_movimentos()+torre2.get_numero_movimentos()+torre3.get_numero_movimentos()

def qtd_max_discos():
    return 10

def print_torres():
    print("Estatísticas ➜ NÚMERO DE MOVIMENTOS: "+str(torre1.get_numero_movimentos()+torre2.get_numero_movimentos()+torre3.get_numero_movimentos()))
    print('\t\t\t   Torre 1\t\t\t\tTorre 2\t\t\t\t Torre 3')
    str_todos_discos = ''
    size_torres = torre1.get_tamanho()

    def built_bar_center(qtd):
        numbers_inverso = []
        for item in range(qtd_max_discos(),0-1,-1):
            numbers_inverso.append(item)
        bar = ' ' * numbers_inverso[qtd] + '▄' * qtd + '║' + '▄' * qtd + " "*numbers_inverso[qtd]
        return bar

    for linha in range(size_torres-1,0-1,-1):
        print('        ' + built_bar_center(torre1.get_discos()[linha])+ built_bar_center(torre2.get_discos()[linha]) + built_bar_center(torre3.get_discos()[linha]))


def inicializa_jogo():
    print("\n╠╠╠ Jogo Torre de Hanói ╣╣╣")
    print("Desenvolvido por Michel Galvão como Atividade Avaliativa da matéria Programação Orientada à objetos em Python da graduação de Engenharia de Software\n")
    qtd_discos = input("Informe a quantidade de discos desejados para o jogo (3 a " + str(qtd_max_discos()) + "): ")
    while qtd_discos == '' or int(qtd_discos) < 3 or int(qtd_discos) > qtd_max_discos():
        qtd_discos = input("Entrada inválida. Informe novamente: ")
    qtd_discos = int(qtd_discos)
    print("Você consegue vencer o jogo com " + str(numero_tentativas_min(qtd_discos)) + " tentativas.")

    torre1 = Torre(qtd_discos)
    torre2 = Torre(qtd_discos)
    torre3 = Torre(qtd_discos)

    for peso in range(qtd_discos, 0, -1):
        torre1.desempilha_disco()

    for peso in range(1, qtd_discos + 1):
        torre1.inicia_torre_com_disco(peso)
    return torre1, torre2, torre3 # Retorna uma tupla

if __name__ == '__main__':
    torre1, torre2, torre3 = inicializa_jogo() #Atribuir tupla retornada

    while True:
        print_torres()
        de_valido = True
        disco = 0

        entrada = input("Digite 1, 2 ou 3 para informar a identificação da torre de origem para mover o disco: ")
        while entrada == '' or int(entrada) >3 or int(entrada) <1:
            entrada = input("Entrada inválida. Informe novamente: ")

        de = int(entrada)
        torre_origem = -1
        if de == 1:
            disco = torre1.get_first()
            torre_origem = torre1
        elif de == 2:
            disco = torre2.get_first()
            torre_origem = torre2
        elif de == 3:
            disco = torre3.get_first()
            torre_origem = torre3
        else:
            de_valido = False
            print("Identificação de torre originária inválida. Tente novamente.")

        if de_valido == True:
            entrada = input("Digite 1, 2 ou 3 para informar a identificação da torre de destino para mover o disco: ")
            while entrada == '' or int(entrada) > 3 or int(entrada) < 1:
                entrada = input("Entrada inválida. Informe novamente: ")

            para = int(entrada)
            if para == 1:
                if torre1.insert(disco) == True:
                    torre_origem.set_vazio_first_position_torre()
            elif para == 2:
                if torre2.insert(disco) == True:
                    torre_origem.set_vazio_first_position_torre()
            elif para == 3:
                if torre3.insert(disco) == True:
                    torre_origem.set_vazio_first_position_torre()
            else:
                print("Identificação de torre destinatária inválida. Tente novamente.")


            if torre3.get_discos()[torre3.get_tamanho()-1] == 1:
                print_torres()
                print("Você venceu o jogo com "+str(numero_tentativas())+" tentativas! Sua pontuação percentual: "+str(calcular_pontuacao(numero_tentativas_min(torre1.get_tamanho()),numero_tentativas()))+"%")
                entrada = input("Deseja jogar novamente? Digite 1 para sim ou 0 para não: ")
                while entrada == '' or int(entrada) < 0 or int(entrada) > 1:
                    entrada = input("Entrada inválida. Informe novamente: ")
                entrada = int(entrada)
                if entrada == 1:
                    torre1, torre2, torre3 = inicializa_jogo()
                elif entrada == 0:
                    break



