### Datentypen in Python ###
# Variablen erstellen
val = 0

# str, int, float, bool
name = "Egon"
alter = 23
gewicht = 74.5
smart = True

# Neuzuweisungen
gewicht = 74 # cast to int

# Typen von Variablen überprüfen
print( type(gewicht))
print( id(gewicht))
gewicht = 74.4
print( type(gewicht))
print( id(gewicht))

# Boolsche Ausdrücke: Wörter statt Operatoren
print( True and True)
print( False and True)
print( False and False)
print(True and not False)


# Platzhalter
dummy = ""

### Abfragen in python ###
if name == "Egon":
    print("Name ist Egon")
elif name == "":
    print("Name ist leer")
else:
    print("Name ist nicht Egon")

### for-Schleifen in python ###
a = [ 1, 2, 3, 4, 5, 7]

for i in range(len(a)):
    print(i)
    print(a[i])

# Iteration über elemente
for val in a:
    print(val)

print("________")
# Iteration über teile von Listen Liste
for i in range(0,10,2):
    print(i)

# ZIP und enumerate
a = [1, 2, 3, 4, 5, 6]
b = [10, 20, 30, 40, 50, 60]

for val_a, val_b in zip(a,b):
    print(val_a, val_b)

for idx, val in enumerate(b):
    print(idx, val)

# while Schleife
budy=True
while budy==True:
    print("hello")
    budy=False

print(not True and False)
