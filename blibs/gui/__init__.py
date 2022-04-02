def title(texto='title', tamfai=10, faixa='-'):
    print(faixa*tamfai)
    print(texto.center(tamfai))
    print(faixa * tamfai)


def line(num=10, faixa='-'):
    print(faixa * num)


def menu(lista):
    c = 0
    for i in lista:
        c += 1
        print(f'\033[1;34m{c}.\033[m \033[1;37m{i}\033[m')
