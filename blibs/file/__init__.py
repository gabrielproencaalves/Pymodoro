from ..gui import *


def arquivoexiste(arquivo='', param='rt'):
    try:
        f = open(arquivo, param, encoding='utf-8')
        f.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarquivo(arquivo):
    try:
        c = open(arquivo, 'wt+')
        c.close()
    except:
        print("Error: the file was didn't created!")
    else:
        print(f"Archive {arquivo} was created successfully!")


def lerarquivo(arquivo):
    try:
        r = open(arquivo, 'rt')
    except:
        print('ERROR: opening the file')
    else:
        print(r)
    finally:
        r.close()


def cadastrar(arquivo, dados):
    try:
        c = open(arquivo, 'at')
    except:
        print(f'Houve um erro ao escrever no arquivo: {arquivo}')
    else:
        c.write(dados[0])
        c.write(';')
        c.write(dados[1])
        c.write('\n')
    finally:
        c.close()


def limpar(arquivo):
    try:
        arch = open(arquivo, 'wt')
    except FileNotFoundError:
        return f'{arquivo} não foi encontrado.'
    else:
        arch = ''
