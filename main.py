from itertools import product

from Torre import Torre

def qtd_max_discos():
    return 10

def print_torres():
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
        #print('\t '+str(torre1.get_discos()[linha]) + "\t\t\t  " + str(torre2.get_discos()[linha]) + "\t\t\t  " + str(torre3.get_discos()[linha]))
        print('        ' + built_bar_center(torre1.get_discos()[linha])+ built_bar_center(torre2.get_discos()[linha]) + built_bar_center(torre3.get_discos()[linha]))

    print(str_todos_discos)

if __name__ == '__main__':
    print("╠╠╠ Jogo Torre de Hanói ╣╣╣")
    print("Desenvolvido por Michel Galvão como Atividade Avaliativa da matéria Programação Orientada à objetos em Python da graduação de Engenharia de Software\n")
    qtd_discos = 0
    while qtd_discos <3 or qtd_discos >qtd_max_discos():
        qtd_discos = int(input("Informe a quantidade de discos desejados para o jogo (3 a "+str(qtd_max_discos())+"): "))
    torre1 = Torre(qtd_discos)
    torre2 = Torre(qtd_discos)
    torre3 = Torre(qtd_discos)

    for peso in range(qtd_discos,0,-1):
        torre1.desempilha_disco()

    for peso in range(1,qtd_discos+1):
        torre1.empilha_disco(peso)

    while True:
        print_torres()
        de_valido = True
        disco = 0
        de = int(input("Digite 1, 2 ou 3 para informar a identificação da torre de origem para mover o disco: "))
        if de == 1:
            disco = torre1.get_first()
            torre1.set_vazio_first_position_torre()
        elif de == 2:
            disco = torre2.get_first()
            torre2.set_vazio_first_position_torre()
        elif de == 3:
            disco = torre3.get_first()
            torre3.set_vazio_first_position_torre()
        else:
            de_valido = False
            print("Identificação de torre originária inválida. Tente novamente.")

        if de_valido == True:
            para = int(input("Digite 1, 2 ou 3 para informar a identificação da torre de destino para mover o disco: "))
            if para == 1:
                torre1.insert(disco)
            elif para == 2:
                torre2.insert(disco)
            elif para == 3:
                torre3.insert(disco)
            else:
                print("Identificação de torre destinatária inválida. Tente novamente.")



