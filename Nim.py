import interface
from time import sleep
if interface.menu() == 2:
    interface.linha()
    print("O CAMPEONATO VAI COMEÇAR!!!")
    interface.linha()
    sleep(1)
    for partidas in range(1, 4):
        n = interface.total_pecas()
        m = interface.pecas_para_retirar()
        while m > n:
            print("Configuração invalida. Tente novamente")
            n = interface.total_pecas()
            m = interface.pecas_para_retirar()
        print(f"Vai começar a {partidas}º")
        interface.partida(n, m)
        print(f"o jogo está Computador {partidas} x 0 Jogador")
        interface.linha()
else:
    interface.linha()
    print("Uma partida unica vai começar")
    n = interface.total_pecas()
    m = interface.pecas_para_retirar()
    while m > n:
        print("Configuração invalida. Tente novamente")
        n = interface.total_pecas()
        m = interface.pecas_para_retirar()
    interface.partida(n, m)
