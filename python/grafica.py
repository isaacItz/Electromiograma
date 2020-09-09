import matplotlib.pyplot as plt
import numpy as np
y = []
file = open("datos", "r")
lines = file.readlines()
file.close()
x = list(range(len(lines)))
for i in lines:
    y.append(float(i[:4]))
plt.plot(x, y)
plt.ylabel("voltaje")
plt.xlabel("tiempo")
plt.title("medicion cada 500 milisegundos")
plt.show()
