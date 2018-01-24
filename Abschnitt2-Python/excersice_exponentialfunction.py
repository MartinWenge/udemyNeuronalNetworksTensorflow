import numpy as np
import matplotlib.pyplot as plt

def e_function(begin, end):
    return np.exp(np.arange(begin, end+1, 1))

a=1
b=5
plt.plot(np.arange(a,b+1),e_function(a,b),'go')

plt.xlabel("Intervallwerte")
plt.ylabel("Exponentialfunktion des Intervalls")
plt.title("Aufgabe: Exponentialfunktion ganzzahliges Intervall plotten")

plt.show()
