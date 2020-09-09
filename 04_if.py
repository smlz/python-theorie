
# Wir haben nach dem Alter gefragt
eingabe = "17"
alter = int(eingabe)

# Eine Entscheidung startet mit 'if', dann folgt eine Bedingung
if alter >= 18:
    print("Ja, Okay")   # Alles was eingerückt ist, wird ausgeführt, falls die Bedingung erfüllt wurde
    print("Du darfst")
else:  # Alternative, falls die Bedingung nicht erfüllt wurde
    print("Leider bist du noch zu jung")


eingabe = "QUit "
eingabe = eingabe.strip().lower()


if eingabe == "level 1":    # Strings kann man mit == vergleichen (Ungleich !=)
    print("Wilkommen im Festsaal")
    ...
elif eingabe == "level 2":
    print("Wilkommen im Kerker")
    ...
elif eingabe == "quit":
    print("Adieu!")
else:
    print("ERROR: Befehl wurde nicht erkannt")
