# este es mi script para subirlo al dispositivo
import android
import time
import csv

droide=android.Android()

# 100ms entre lecturas
dt = 100
# duracion de la muestras
fin = 5000

nombreArchivo = droide.dialogGetInput("Hola!", "Como se llamara el archivo?")
droide.ttsSpeak("Empezando recorrido")
tiempo = 0
droide.startSensingTimed(2,dt)
droide.sensorsReadAccelerometer()
lecturas = []

while tiempo <= fin:
    lecturas.append(droide.sensorsReadAccelerometer().result)
    time.sleep(dt/1000.0)
    tiempo += dt
    
droide.stopSensing();

with open(nombreArchivo.result + '.csv', 'w') as fp:
    a = csv.writer(fp,delimiter=',')
    a.writerows(lecturas)
    
droide.ttsSpeak("Termino recorrido")