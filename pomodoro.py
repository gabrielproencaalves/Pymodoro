from blibs.gui import *         #| 25m = 1500s
from blibs.bin import *         #| 05m = 0300s
from time import sleep          #|
from playsound import playsound #|
from blibs.file import *        #|
#------------------------------------> IMPORTs
audio_list = ['Alarm_Clock_Beep', 
              'Alarm_Digital_Beep',
              'Facility_Alarm',
              'Interface_Hint_Notification',
              'Scanning_Sci_Fi_Alarm',
              'Warning_Alarm_Buzzer']



while True:
    Audio_Set = arch_read('audio.conf')





    #('blibs/sfx/' + audio_list[leiaint('Insert [1-6]: ')-1] + '.wav')
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



    if UserInput == 5:
        while True:
            title(texto='AUDIO LIST', tamfai=32, faixa='-')
            menu(lista=audio_list)
            User_Input = leiaint__('Insert [1 - 6]: ')
            if User_Input < 1 or User_Input > 6:
                print('INVALID OPTION!')
            else:
                arch_clear('audio.conf')                                                           
                arch_write('audio.conf', 'blibs/sfx/' + audio_list[User_Input - 1] + '.wav')
                break

    if UserInput == 6:
        if confirm(ui=['Are you sure? [y/n]', 'Insert: '], yes='y', no='n'):
            break
        else:
            continue
    elif UserInput > 6 or UserInput < 1:
        print('INVALID OPTION!')

exit()

