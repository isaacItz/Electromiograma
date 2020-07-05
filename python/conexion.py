#importamos las librerias necesarias
from serial import Serial
#establecemos el puerto serial del que obtendremos la informacion del sensor
ser = Serial('/dev/ttyACM0')
print(ser.name)
archivo = open("datos", "w")
linea = "";
try:
    while True:
        #leemos el valor que el sensor este devolviendo
        linea = ser.read(6)
        #damos un formato para insertar la linea en un archivo
        linea = str(linea)[:6].split("b'")[1]
        print(linea)
        #escribimos el valor formateado en el archivo
        archivo.write(linea + "\n")
except TypeError:
    print("error de formato para el archivo")
finally:
    ser.close()
    archivo.close()
