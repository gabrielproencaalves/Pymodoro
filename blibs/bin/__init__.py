from ..gui import *
import os
from playsound import playsound
from datetime import datetime

def confirm(ui=['', 'Resposta: '], yes='yes', no='no'):
    title(ui[0], 32, '~')
    while True:
        try:
            valor = leiastr(ui[1]).lower()
        except KeyboardInterrupt:
            print('\033[1;31mKeyboard Interruption, fill in the data first!\033[m')
        else:
            if valor[0] in yes:
                return True
                break
            elif valor[0] in no:
                return False
                break
            else:
                print('INVALID OPTION!')
                continue


def leiafloat(texto):
    """
    Função que valida se o dado digitado é um número real.
    :param texto: É o que será mostrado ao usuário antes de digitar os dados
    """
    while True:
        try:
            Valor = float(str(input(texto)).replace(',', '.'))
        except KeyboardInterrupt:
            print('\nInserção de dados interrompida pelo usuário.')
            return 0
        except:
            print('\033[1;31mERRO: dado(s) inválido(s), tente novamente!\033[m')
        else:
            return Valor
            break


def leiaint(texto):
    """
    Função que valida se o dado digitado é um número inteiro.
    :param texto: É o que será mostrado ao usuário antes de digitar os dados
    """
    while True:
        try:
            Valor = int(input(texto))
        except KeyboardInterrupt:
            print('\nInserção de dados interrompida pelo usuário.')
            return 0
        except:
            print('\033[1;31mERRO: dado(s) inválido(s), tente novamente!\033[m')
        else:
            return Valor
            break


def leiaint__(texto):
    """
    Função que valida se o dado digitado é um número inteiro.
    :param texto: É o que será mostrado ao usuário antes de digitar os dados
    """
    while True:
        try:
            Valor = int(input(texto))
        except ValueError:
            print('\033[1;31mERRO: dado(s) inválido(s), tente novamente!\033[m')
        else:
            return Valor
            break



def leiastr(texto='Digite: '):
    """
    Função que valida se o dado digitado é uma cadeia de caracteres.
    :param texto: É o que será mostrado ao usuário antes de digitar os dados
    """
    while True:
        try:
            _texto = str(input(texto))
        except(KeyboardInterrupt):
            print('\nInserção de dados interrompida pelo usuário.')
        except:
            print('\033[1;31mERRO: dado(s) inválido(s), tente novamente!\033[m')
        else:
            if _texto in '':
                print('\033[1;31mERRO: dado(s) inválido(s), tente novamente!\033[m')
                continue
            else:
                return _texto


def notify(title='Title', message='Message', delay=5000):
    os.system(f"notify-send '{title}' '{message}' -t {delay}")


def alarm(audio, seconds=10):
    for replay in range(0, seconds, 1):
        try: 
            playsound(audio)
        except KeyboardInterrupt:
            break

def clear_scrn():
    os.system('clear')

def show_time():
     print(str(datetime.today())[0:16])
