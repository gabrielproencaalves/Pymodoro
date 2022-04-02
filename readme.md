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
