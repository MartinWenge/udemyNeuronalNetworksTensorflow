### Listen in Python ###
# cmd: activate udemyNeuronNetzMitTensorflow
# Liste erstellen
liste_a = [2, 5, 11, 23, 47]

# datentypen unabhängig
liste_b = [2, 5, 'ronny', 47.2]
print(liste_b)

# Listen Operationen
print(len(liste_a))
liste_c = [[1,1,1], [2,2,2] ,3 , 47]
print(len(liste_c))
print(len(liste_c[1]))

print("_____")
# pop und append
liste_a.append(1)
print(liste_a)
liste_a.pop()
print(liste_a)
liste_a.pop(1)
print(liste_a)

print("_____")
# Listen Comprehensions
# 1D
#liste_hundert = [ wert for ... if ... ]
liste_hundert = [ i for i in range(0,101)]
#print(liste_hundert)
liste_hundert = [ i for i in range(0,101) if i % 2 == 0]
#print(liste_hundert)

# 2D
liste_2d = [[i*j for j in range(2)] for i in range(3)]
print(liste_2d)

### Dicts in Python ###
# Dict erstellen, key: values
personen_alter = {'egon': 24}
print(personen_alter)
print(personen_alter['egon'])

# erstellen mit dicts comprehensions
dict_1d = { key: 0 for key in range(3)}
print(dict_1d)
dict_1d = { key: 1 for key in ['egon', 'benny', 'ole']}
print(dict_1d)

# dicts iterieren
for key, val in dict_1d.items():
    print(key, val)

for key in dict_1d.keys():
    print(key)

for val in dict_1d.values():
    print(val)

print("___")

dict_1d = { key: val for val, key in zip([23, 57, 18], ['egon', 'benny', 'ole'])}
print(dict_1d)

### Funktionen in pyhton ###
# funktionen erstellen
def getAge(name):
    return str(dict_1d[name])

# funktionen aufrufen
alter = getAge('ole')
print(alter)

# return values von funktionen
def getAge2(name, nachricht=""):
    return str(dict_1d[name]) + nachricht

# different return values for default functions
print(getAge2('egon',' hallo'))
