### Module in python ###
# Module verwenden
# Basics für matplotlib graphiken
import matplotlib.pyplot as plt
import numpy as np

# einzelne funktion
from numpy.linalg import eig
# ganzer namespace
#from numpy.linalg import *

liste = [1, 3, 7, 15, 31, 63]

# plt.plot(range(1, len(liste)+1),liste, color="green")
# plt.xlabel("x-werte")
# plt.ylabel("y-werte")

# plt.show()

# Die basics für numpy 
liste = np.array([1, 3, 7, 15, 31, 63], dtype=np.float32)
m = np.array([[1, 0], [0, 1]], dtype=np.float32)
print(m)

evals, evecs = eig(m)
print(evals)
print(evecs)

# eigene Module erstellen
from mein_modul import *

print(mygetAbsVal(-10))


### Klassen in Python ###
# class erstellen
#c++: class Mensch{
#     public
#     Mensch(name){
#         this.name=name
#     }
#     private:
#     string name
# }

class Mensch:
    name = ""
    def __init__(self, name):
        self.name = name

    def printName(self):
        print(self.name)
    
jan = Mensch("jan")
jan.printName()
