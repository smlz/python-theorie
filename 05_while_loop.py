
# Variable die speichert ob wir fertig sind
done = False

anzahl_hallos = 0

while not done:  # Machen solange wir noch nicht fertig sind
    print('Hallo')
    anzahl_hallos = anzahl_hallos + 1
    # Kurzversion:
    #anzahl_hallos += 1
    if anzahl_hallos == 5:
        done = True

done = False
while not done:
    eingabe = input("Wähle zwischen A, B und C: ")
    eingabe = eingabe.strip().lower()   # Clean user input

    if eingabe == 'a':
        print('Du hast A gewählt')
        done = True
    elif eingabe == 'b':
        print('Du hast B gewählt')
        done = True
    elif eingabe == 'c':
        print('Du hast C gewählt')
        done = True
    else:
        print('Error: Du hast einen Käse eingegeben!')
        print('Versuche es noch einmal')



# antworten = 'a b c'.split()
# eingabe = ''
# while eingabe.strip().lower() not in antworten:
#     eingabe = input("Wähle zwischen A, B und C: ")
