# Text wird in Anführungszeichen geschrieben, und heissen Strings (str) (Deutsch: Zeichenkette)
print("Hallo")

alter = 22

tageszeit = "Abend"
print("Guten "  + tageszeit)     # Naja
print("Guten", tageszeit)        # Gut
print(f"Guten {tageszeit}")      # Gut

print("Du bist " + str(alter) + " Jahre alt")   # Naja
print("Du bist", alter, "Jahre alt")            # Gut
print(f"Du bist {alter} Jahre alt.")            # Gut

# Grossgeschrieben
print("was?!?".upper())
print("ChrüsIMüsI".lower())

# Du bist 22 Jahre alt.
