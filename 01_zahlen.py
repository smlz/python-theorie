# Plus, Mal, Minus
print(1 + 1)
print(2 * 3)
print(3 - 5)

# Hoch
print(2**5)

print(2**0.5)   # Wurzel


# Die normale Division. Das Resultat ist immer ein float.
print(7 / 2)

# Die ganzzahlige Division. Das Resultat ist ein int.
print(7 // 3)

# Modulo: Der ganzzahlige Rest der Division
print(7 % 3)

print((7 // 3) * 3 + (7 % 3))
#     Ganzzahldiv.   Rest

# Es gibt zwei Arten von Zahlen
# Ganzzahl: int (für Integer)
print(1)

# Kommazahl: float (für Floating Point Number, Deutsch: Fliesskommazahl)
print(1.0)
print(1.1)

# Text kann in eine Ganzzahl umgewandelt werden mit der Funktion int
benutzereingabe = "19"
alter = int(benutzereingabe)
jahrgang = 2020 - alter
print(jahrgang)