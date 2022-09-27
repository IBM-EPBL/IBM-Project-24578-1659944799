import random
import time


while True:
    randomTemperature = random.randint(-128 , 100)
    if randomTemperature > 90:
        print("ALERT! high temperature : "+str(randomTemperature)+"F")
    elif randomTemperature < 10:
        print("ALERT! low temperature : "+str(randomTemperature)+"F")
    else:
        print("normal temperature: "+str(randomTemperature)+"F")
    time.sleep(2)
