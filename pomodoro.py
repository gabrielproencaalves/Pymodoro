from blibs.gui import * #|
from blibs.bin import * #|
from time import sleep  #|
from playsound import playsound
#----------------------------> IMPORTs

while True:
    
    title(texto='POMODORO', tamfai=32, faixa='-')
    menu(lista=['- 25 MIN ONLY', '- 5 MIN ONLY', '- BOTH (25 + 5)', '- BOTH (25 + 5) + REPLAY', '- SET ALARM', '- EXIT'])
    line(32, '-')
    try:
        UserInput = leiaint('Insert: ')
    except(KeyboardInterrupt):
        confirm(ui=['Are you sure? [y/n]', 'Insert: '], yes='y', no='n')
    try:
        if UserInput == 1:
            for timer in range(0, 1, 1):
                sleep(3)
                playsound('blibs/sfx/Alarm_Clock_Beep.wav')
    except(KeyboardInterrupt):
        print('\nOperation Interrupted!\n')
    
    if UserInput == 6:
        if confirm(ui=['Are you sure? [y/n]', 'Insert: '], yes='y', no='n'):
            break
        else:
            continue


exit()

