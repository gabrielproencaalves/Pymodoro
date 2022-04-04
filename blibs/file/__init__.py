from ..gui import *



def arch_test(arquivo, param='rt'):
    try:
        arch = open(arquivo, param, encoding='utf-8')
        arch.close()
    except FileNotFoundError:
        return False
    else:
        return True



def arch_create(arquivo):
    try:
        arch = open(arquivo, 'wt+')
        arch.close()
    except:
        print(f"Error: the file {arquivo} was didn't created!")
    else:
        print(f"Archive {arquivo} was created successfully!")



def arch_read(arquivo):
    try:
        arch = open(arquivo, 'rt')
    except:
        print(f'ERROR: opening the file: {arquivo}')
    else:
        for linha in arch:
            return linha
    finally:
        arch.close()



def arch_write(arquivo, dados):
    try:
        arch = open(arquivo, 'at')
    except:
        print(f"ERROR: coudn't write in: {arquivo}")
    else:
        arch.write(dados)
    finally:
        arch.close()



def arch_clear(arquivo):
    try:
        arch = open(arquivo, 'wt')
    except FileNotFoundError:
        return f'ERROR: {arquivo} not found.'
    else:
        arch = ''
