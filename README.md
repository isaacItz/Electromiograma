Proceso de captacion de la señal producida por un sensor electromiografico.

lo primero es conectar el sensor a una interfaz que pueda interpretar los datos generados por el sensor

la interfaz utilizada sera un arduino
como punto importante cabe recalcar que la informacion que este sensor genera es analogica y esta comprendida por valores enteros 
desde el 0 hasta el 1023 con un total de 1024 valores posibles representables

el sensor esta diseñado para trabajar directamente con microcontroladores como arduino o rasphberry pi
lo primero es configurar el arduino para enviar informacion por el puerto serial 
esto lo hacemos con la instruccion Serial.begin() pasando como argumento la cantidad maxima de bits que se transmitiran por segundo
entonces solo conectamos nuestro sensor al arduino y procedemos a hacer la lectura del pin analogico al que el sensor esta conectado
una ves configurado el sketch ahora solo resta subirlo al arduino
una ves realizada la configuracion ahora solo resta leer la informacion del puerto serial
para esto utilizaremos python y la libreria serial
establecemos el puerto del que vamos a leer la informacion generada por el arduino y ya esta ahora solo resta guardar la informaicon 
