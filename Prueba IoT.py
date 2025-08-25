# Test IoT con Adafruit IO
# Elaborado por: Miguel Tonatiuh Perez Castillo   

from Adafruit_IO import Client
import time
import numpy as np

ADAFRUIT_IO_USERNAME = "Tonatiuh"
ADAFRUIT_IO_KEY = "aio_ROul89fqHbd3O6lJkQFnsPkdBwDR"

ADAFRUIT_IO_USERNAME = "Sustituir por IO_USERNAME"
ADAFRUIT_IO_KEY = "Sustituir por IO_KEY"
 
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
 
def seno():
    T = 2 * np.pi
    num_puntos = 30
    t = np.linspace(0, 1, num_puntos)
    x = 2 * t
    y_sin = np.sin(T * x) / 10  
    return y_sin.tolist()
 
def coseno():
    T = 2 * np.pi  
    num_puntos = 30
    t = np.linspace(0, 1, num_puntos)  
    x = 2 * t  
    y_cos = np.cos(T * x) / 10  
    return y_cos.tolist()
 
def sendSen(y_sin):  
    for i in range(len(y_sin)):
        aio.send("sen", y_sin[i])
        time.sleep(2)  
    print("Datos de seno enviados exitosamente...")
 
def sendCos(y_cos):  
    for i in range(len(y_cos)):
        aio.send("cos", y_cos[i])
        time.sleep(2)  
    print("Datos de coseno enviados exitosamente...")
 
FnSen = seno()
sendSen(FnSen)
 
FnCos = coseno()
sendCos(FnCos)
 