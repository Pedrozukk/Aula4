import time
import winsound

cont = 40
while cont >= 0:
    print(cont)
    cont-= 1 
    time.sleep(1)
    winsound.Beep(3000, 100)
print("Booomm")
winsound.Beep(1500, 1000)