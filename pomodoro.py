from blibs.gui import * #|
from blibs.bin import * #| --> IMPORTs
from time import sleep  #|
#-------------------------

try:
    while True:
        
        title(texto='POMODORO', tamfai=32, faixa='-')
        menu(lista=['- 25 MIN', '- 5 MIN', '- BOTH', '- BOTH + REPLAY', '- SET ALARM', '- EXIT'])
        line(32, '-')
        try:
            UserInput = leiaint('Insert: ')
        except(KeyboardInterrupt):
            confirm(ui=['Are you sure? [y/n]', 'Insert: '], yes='y', no='n')
        try:
            if UserInput == 1:
                sleep(1500)
        except(KeyboardInterrupt):
            print('\nOperation Interrupted!\n')
        
        if UserInput == 6:
            if confirm(ui=['Are you sure? [y/n]', 'Insert: '], yes='y', no='n'):
                break
            else:
                continue


exit()

