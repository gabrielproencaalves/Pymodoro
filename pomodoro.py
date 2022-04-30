#---------------------------------
from blibs.gui import *         #| 25m = 1500s
from blibs.bin import *         #| 05m = 0300s
from time import sleep          #|
from blibs.file import *        #|
#------------------------------------> IMPORTs
clear_scrn()
audio_list = ['Alarm_Clock_Beep', 
              'Alarm_Digital_Beep',
              'Facility_Alarm',
              'Interface_Hint_Notification',
              'Scanning_Sci_Fi_Alarm',
              'Warning_Alarm_Buzzer',
              'Test Alarm']


while True:
#--------------------------------------------------------------
    Audio_Set = arch_read('audio.conf')
    title(texto='POMODORO', tamfai=32, faixa='-')
    menu(lista=['- 25 MIN ONLY',
                '- 5 MIN ONLY',
                '- BOTH (25 + 5)',
                '- BOTH (25 + 5) + REPLAY',
                '- SET ALARM',
                '- EXIT'])
    line(32, '-')
#--------------------------------------------------------------


#--------------------------------------------------------------
    try:
        UserInput = leiaint__('Insert: ')


    except(KeyboardInterrupt):
        clear_scrn()
        print('INVALID OPTION!')
    else:
#--------------------------------------------------------------


#--------------------------------------------------------------
        try:


            if UserInput == 1: # 25 minutes
                for timer in range(0, 1, 1):
                    sleep(1500)
                    notify('TIME OUT!', '25 MINUTES HAVE PASSED!\n', 10000)
                    alarm(audio=Audio_Set)
                    clear_scrn()
                show_time()


            elif UserInput == 2: # 5 minutes
                for timer in range(0, 1, 1):
                    sleep(300)
                    notify('TIME OUT!', '5 MINUTES HAVE PASSED!\n', 10000)
                    alarm(audio=Audio_Set)
                    clear_scrn()
                show_time()


            elif UserInput == 3: # BOTH
                for timer in range(0, 1, 1):
                    sleep(1500)
                    notify('TIME OUT!', '25 MINUTES HAVE PASSED!\n', 10000)
                    alarm(audio=Audio_Set)
                    sleep(300)
                    notify('TIME OUT!', '5 MINUTES HAVE PASSED!\n', 10000)
                    alarm(audio=Audio_Set)
                clear_scrn()
                show_time()

            
            elif UserInput == 4: # BOTH  + REPLAY
                while True:
                    sleep(1500)
                    notify('TIME OUT!', '25 MINUTES HAVE PASSED!\n', 10000)
                    alarm(audio=Audio_Set)
                    sleep(300)
                    notify('TIME OUT!', '5 MINUTES HAVE PASSED!\n', 10000)
                    alarm(audio=Audio_Set)
                clear_scrn()
                show_time()


        except(KeyboardInterrupt):
            clear_scrn()
            print('\nOperation Interrupted!\n')
#--------------------------------------------------------------


#--------------------------------------------------------------
        if UserInput == 5: # Set Alarm
                                                                              

                while True:
                    clear_scrn()
                    title(texto='AUDIO LIST', tamfai=32, faixa='-')
                    menu(lista=(audio_list))


                    try:
                        User_Input = leiaint__('Insert [1 - 7]: ')
                    except KeyboardInterrupt:
                        clear_scrn()
                        break
                    except:
                        clear_scrn()
                        break
                    else:

                        if User_Input < 1 or User_Input > 7:
                            print('INVALID OPTION!')
                        

                        elif User_Input == 7:
                            alarm(audio=Audio_Set)


                        else:
                            arch_clear('audio.conf')
                            arch_write('audio.conf', 'blibs/sfx/' + audio_list[User_Input - 1] + '.mp3')
                            clear_scrn()
                            break						
#--------------------------------------------------------------


#--------------------------------------------------------------
        elif UserInput == 6: # Exit

            if confirm(ui=['Are you sure? [y/n]', 'Insert: '], yes='y', no='n'):
                clear_scrn()
                exit()
            
            else:
                continue
        
        elif UserInput > 6 or UserInput < 1:
            print('INVALID OPTION!')
#--------------------------------------------------------------

