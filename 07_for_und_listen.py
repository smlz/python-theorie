
zutaten = ["Nüsse", "Eier", "Mehl"]

# Beispiel: Liste in Mehrzal, Variabel in Einzahl
for zutat in zutaten:
    print(f"Man nehme {zutat}")
    
for letter in "Hi!":
    print(letter)
    
print("-" * 10)
    
# 1,2,3,4 Trivial:
print(1)
print(2)
print(3)
print(4)

print("-" * 10)

# Besser
for zahl in [1, 2, 3, 4]:
    print(zahl)
    
    
print("-" * 10)

# Am besten
for i in range(1, 5):
    print(i)

print("-" * 10)

# Zählen wie ein Computer: Drei mal etwas tun.
for i in range(3):
    print(f"Computer/Coder: {i}, Mensch: {i + 1}")
    
print("-" * 10)

# Etwas am Ende der Liste anhängen
zutaten.append("Zucker")

# Durchnummerierte Zutaten
for i, zutat in enumerate(zutaten, 1):
    print(f"{i}. {zutat}")
    
# Etwas vom Ende der Liste entfernen
letzte_zutat = zutaten.pop()
print(letzte_zutat)
print(zutaten)

# Ein bestimmtes Element aus der Liste entferen
zutaten.remove("Mehl")

# Fragen ob ein Element in der Liste vorkommt (mindestens ein mal)
print("Nüsse" in zutaten)
print("Koriander" in zutaten)
