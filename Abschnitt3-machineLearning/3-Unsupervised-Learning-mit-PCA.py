# Beispiel für PCA: reduktion dreidimensionale Punktwolke auf zweidimensionale punktwolke:
# Skizze PCA: https://en.wikipedia.org/wiki/Principal_component_analysis
# Daten liegen als vektoren w_i (i=1..n Anzahl Features) der Länge p vorliegen, 
# zu Matrik W mit n x p zusammenfassen
# für alle Vektoren w_i den Mittelwert u_i ausrechnen und von W abziehen:
# B=W-1u^T
# Kovarianz Matrix ausrechen: C=1/(n-1) B* o B
# Eigenvektoren der Kovarianzmatrix ausrechnen V^-1 C V=D mit D_kl=\lambda_k für k=l
# Eigenwerte der größe nach sortieren
# "kommulative Energie"(?) der Eigenwerte berechnen und anhand eines vorgegebenen Grenzwertes
#  (z.B 90% der vollständigen kommulativen Energie) die Menge der Features bestimmen, die weggelassen werden
# es werden die Features mit den geringsten Eigenwerten weggelassen
# die ursprünglichen Daten werden in den neuen Raum mit weniger dimensionen projeziert T=Z \dot W
# prozedur folgt dem Karhunen–Loève Theorem https://en.wikipedia.org/wiki/Karhunen–Loève_theorem

# originalcode von https://www.udemy.com/deep-learning-grundlagen-neuronale-netzwerke-mit-tensorflow/learn/v4/content
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import numpy as np
import random

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

nDat = 200

# Generate Data
data_x = [random.randint(1, random.randint(60, 100)) for _ in range(nDat)]
data_y = [random.randint(1, random.randint(60, 100)) for _ in range(nDat)]
data_z = [random.randint(1, random.randint(60, 100)) for _ in range(nDat)]
data = np.array([np.asarray(data_x), np.asarray(data_y), np.asarray(data_z)] )

# Helper vars
lower_dimension = 2
higher_dimension = 3
xlim = 100
ylim = 100
zlim = 100

# Plot Data in high dimension
ax.scatter(data_x, data_y, data_z, c=data_x, s=20)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.savefig('high.png')
plt.show()

# CLassifier
pca = PCA(n_components=2)
# matrix_r = pca.fit_transform(data)
# data_low = np.dot(np.transpose(matrix_r), data)
data_low = pca.fit_transform(data.T)

print(data_low)

# Plot Data in low dimension
plt.scatter([val[0] for val in data_low], [val[1] for val in data_low], c=data_x, s=20)

plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.savefig('low.png')
plt.show()
