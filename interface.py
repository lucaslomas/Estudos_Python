def cores(red=False, blue=False, cyan=False, green=False, amarelo=False, reset=False, bold=False, reverse=False):
    if red:
        red = "\033[1;31m"
        return red
    if blue:
        blue = "\033[1;34m"
        return blue
    if cyan:
        cyan = "\033[1;36m"
        return cyan
    if green:
        green = "\033[0;32m"
        return green
    if amarelo:
        amarelo = "\033[1;33m"
        return amarelo
    if reset:
        reset = "\033[0;0m"
        return reset
    if bold:
        bold = "\033[;1m"
        return bold
    if reverse:
        reverse = "\033[;7m"
        return reverse


def leiaInt(msg):
    while True:
        try:
            a = (input(msg)).strip()
            a = int(a)
        except (ValueError, TypeError):
            print(f"{cores(red=True)}Erro, valor invalido{cores(reset=True)}")
        except KeyboardInterrupt:
            print(f"\n{cores(red=True)}Você quer sair? Digite 3 para isso{cores(reset=True)}")
            continue
        else:
            return a


def jogador(n, m):
    pecas_retiradas = leiaInt(f"{cores(blue=True)}Quantas peças você quer retirar?{cores(reset=True)} ")
    while pecas_retiradas == 0 or pecas_retiradas > m or pecas_retiradas > n:
        print(f"{cores(red=True)}Esse não é um valor possivel. Tente novamente{cores(reset=True)}")
        pecas_retiradas = leiaInt(f"{cores(blue=True)}Quantas peças você quer retirar?{cores(reset=True)} ")
    return pecas_retiradas


def computador(n, m):
    pecas_retiradas = 0
    while True:
        pecas_retiradas += 1
        if (n - pecas_retiradas) % (m+1) == 0:
            break
        if m == n:
            pecas_retiradas = m
            break
    print(f"{cores(green=True)}Computador retirou {pecas_retiradas}{cores(reset=True)}")
    return pecas_retiradas


def linha():
    print(25*"-")


def partida(n, m):
    from time import sleep
    if n % (m + 1) == 0:
        linha()
        print(f"{cores(blue=True)}Jogador começa a partida{cores(reset=True)}")
        n -= jogador(n, m)
    while True:
        linha()
        print(f"{cores(green=True)}computador escolhe a jogada...{cores(reset=True)}")
        sleep(1)
        n -= computador(n, m)
        print(f"{cores(cyan=True)}Restam ainda {n} peças no tabuleiro{cores(reset=True)}")
        linha()
        sleep(1)
        if n == 0:
            print(f"{cores(green=True)}Computador ganhou{cores(reset=True)}")
            break
        print(f"{cores(blue=True)}Jogador escolhe jogada{cores(reset=True)}")
        n -= jogador(n, m)
        sleep(1)
        print(f"{cores(cyan=True)}Restam ainda {n} peças no tabuleiro{cores(reset=True)}")
        if n == 0:
            print(f"{cores(blue=True)}Computador ganhou{cores(reset=True)}")
            break


def menu():
    linha()
    print(f"{cores(amarelo=True)}Escolha a opção de partida que você quer:\n1- partida unica\n2-Jogar um campeonato"
          f"{cores(reset=True)}")
    escolha = leiaInt(f"{cores(amarelo=True)}Sua opção{cores(reset=True)}")
    return escolha


def total_pecas():
    n = leiaInt("Qual a quantidade de peças no tabuleiro: ")
    while n == 0:
        print(f"{cores(red=True)}Erro. o valor não pode ser zero{cores(reset=True)}")
    return n


def pecas_para_retirar():
    m = leiaInt("Qual a quantidade maxima de peças a serem retiradas? ")
    while m == 0:
        print(f"{cores(red=True)}Erro. o valor não pode ser zero{cores(reset=True)}")
    return m
