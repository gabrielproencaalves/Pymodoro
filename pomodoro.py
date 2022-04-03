from blibs.gui import *         #| 25m = 1500s
from blibs.bin import *         #| 05m = 0300s
from time import sleep          #|
from playsound import playsound #|
#------------------------------------> IMPORTs
audio_list = ['Alarm_Clock_Beep', 
              'Alarm_Digital_Beep',
              'Facility_Alarm',
              'Interface_Hint_Notification',
              'Scanning_Sci_Fi_Alarm',
              'Warning_Alarm_Buzzer']



while True:
    try:
        title(texto='AUDIO LIST', tamfai=32, faixa='-')
        menu(lista=audio_list)
        Audio_Set = ('blibs/sfx/' + audio_list[leiaint('Insert [1-6]: ')-1] + '.wav')
    except:
        print('INVALID OPTION!')
    else:
        break


while True:
    title(texto='POMODORO', tamfai=32, faixa='-')
    menu(lista=['- 25 MIN ONLY',
                '- 5 MIN ONLY',
                '- BOTH (25 + 5)',
                '- BOTH (25 + 5) + REPLAY',
                '- SET ALARM',
                '- EXIT'])
    
    line(32, '-')
    


    try:
        UserInput = leiaint('Insert: ')
    except(KeyboardInterrupt):
        confirm(ui=['Are you sure? [y/n]', 'Insert: '], yes='y', no='n')



    try:
        if UserInput == 1:
            for timer in range(0, 1, 1):
                sleep(1)
                playsound(Audio_Set)
        elif UserInput == 2:
            for timer in range(0, 1, 1):
                sleep(3)
                playsound(Audio_Set)
    except(KeyboardInterrupt):
        print('\nOperation Interrupted!\n')



    if UserInput == 6:
        if confirm(ui=['Are you sure? [y/n]', 'Insert: '], yes='y', no='n'):
            break
        else:
            continue
    elif UserInput > 6 or UserInput < 1:
        print('INVALID OPTION!')

exit()

