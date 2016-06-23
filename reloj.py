#ALEXANDER FIGUEROA
#PROGRAMA QUE IMPRIME LA HORA EN FORMATO
#HH:MM:SS
import time
import os
for x in range (1,61):
	for y in range (1,61):
		for z in range (1,61):
			print(str(x-1)+':'+str(y-1)+':'+str(z-1))
			time.sleep(1)
			os.system('cls')