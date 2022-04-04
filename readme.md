Aplicação CLI do timer pomodoro.

--------------------------------
            POMODORO
--------------------------------
1 - 25 MIN
2 - 5 MIN
3 - BOTH
4 - BOTH + REPLAY
5 - SET ALARM
6 - EXIT
--------------------------------
Insert: 





--------------------------------
           AUDIO LIST
--------------------------------
1 - Alarm_Clock_Beep
2 - Alarm_Digital_Beep
3 - Facility_Alarm
4 - Interface_Hint_Notification
5 - Scanning_Sci_Fi_Alarm
6 - Warning_Alarm_Buzzer
--------------------------------
Insert: 




1 {
	for:
		sleep(1500)
		sinal sonoro
		sinal visual
		retornar ao menu

}

2 {
	for:
		sleep(300)
		sinal sonoro
		sinal visual
		retornar ao menu

}

3 {
	for:
		sleep(1500)
		sinal sonoro_1
		sinal visual_1
		sleep(300)
		sinal sonoro_2
		sinal visual_2
		retornar ao menu

}

4 {

	while True:
		sleep(1500)
		sinal sonoro_1
		sinal visual_1
		sleep(300)
		sinal sonoro_2
		sinal visual_2
		if ctrl+c:
		retornar ao menu

}


Alterar audios no audacity (deixar todos do mesmo tamanho)
finalizar programa
achar possíveis bugs
