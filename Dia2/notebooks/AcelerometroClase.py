import android

droide.ttsSpeak("Empezando recorrido")
droide=android.Android()
# 100ms entre lecturas
dt = 100
# duracion de la muestras
fin = 5000

nombreArchivo = droide.dialogGetInput("Hola!", "Como se llamará el archivo?")

tiempo = 0
droide.startSensingTimed(2,dt)
droide.sensorsReadAccelerometer()
lecturas = []

import time
while tiempo <= fin:
    lecturas.append(droide.sensorsReadAccelerometer().result)
    time.sleep(dt/1000.0)
    tiempo += dt
    
droide.stopSensing();

import csv
with open(nombreArchivo.result + '.csv', 'w') as fp:
    a = csv.writer(fp,delimiter=',')
    a.writerows(lecturas)