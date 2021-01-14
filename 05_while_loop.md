# While-Loops

**While-Loops** sind sogenannte Schleifen. Sie wiederholen eine Folge von Aktionen so lange, bis eine bestimmte Bedingung nicht mehr erfüllt wird.<br>
<br>
<img src=https://www.tutorialspoint.com/scala/images/scala_while_loop.jpg width="400"><br>
*Quelle: Tutorialspoint* <br>

---

## Grundlagen
Als erstes wird eine Bedingung benötigt, die wir erfüllt haben wollen. 

Wir brauchen eine Variable, die speichert, ob wir fertig sind. Dafür benutzt man am besten `done`.

Zuerst ist die Bedingung nicht erfüllt, das heisst `done = False`.

Die Aktionen werden wiederholt, bis die Bedingung `done = False` nicht mehr erfüllt wird. In diesem Fall wird `done = False` auf `done = True` gesetzt. Dadurch wird die Wiederholung gestoppt und der Loop ist abgeschlossen.

```Python
done = False
while not done:
    ...
    done = True
```
Dieses Programm würde nichts ausgeben, es zeigt nur welcher Teil der Schleife immer gebraucht wird. Bei den drei Punkten könnten irgendwelche Anweisungen stehen.

---

## Break
Die `break`-Anweisung beendet einen While-Loop sofort vollständig. Die Ausführung geht bei der ersten Anweisung nach dem Schleifenende weiter.

```Python
n = 5
while n > 0:
    n = n - 1
    if n == 2:
        break
    print(n)

print("Loop ended.")
```
Hier wird `n > 5` gebraucht, dadurch braucht es die Variable `done` nicht. Man kann also in diesem Fall auch direkt einen Loop verwenden, ohne eine Variable abzuspeichern.

## Continue
Mit der `continue`-Anweisung wird die Schleifeniteration sofort beendet und die Ausführung springt wieder an den Anfang der Schleife. Je nach Aktion wird der While-Loop dann fortgeführt oder vollständig beendet.

```Python
n = 5
while n > 0:
    n = n - 1
    if n == 2:
        continue
    print(n)

print("Loop ended.")
```
So funktionieren die beiden Ausdrücke `break` und `continue`:<br>
<img src=https://files.realpython.com/media/t.899f357dd948.png width="350"> <br>
*Quelle: Realpython*

---
## Else
In Python ist es möglich, am Ende eines While-Loops noch ein `else` anzufügen. Die Anweisung unter `else` wird nur ausgeführt, wenn die Bedingung als falsch gewertet wird und so die Schleife endet. Die Anweisung wird nicht ausgeführt, wenn die Schleife durch eine `break`-Anweisung beendet wird.

```Python
n = 5
while n > 0:
    n = n - 1
    print(n)
else:
    print('Loop done.')
```

---

## Beispiele:

```Python
done = False
anzahl_hallos = 0

while not done: 

    print("Hallo")
    anzahl_hallos = anzahl_hallos + 1

    if anzahl_hallos == 5:
        done = True
```
In dieser Schleife ist auch noch ein __if__ eingebaut, dies ändert an der Ausführung des While-Loops aber nichts. 
Die Aufgabe `print("Hallo)` wird solange wiederholt, bis fünfmal "Hallo" ausgegeben wurde.

```Python
done = False

while not done:

    eingabe = input("Wähle zwischen A, B und C: ").strip().lower()

    if eingabe == "a":
        print("Du hast A gewählt")
        done = True
    elif eingabe == "b":
        print("Du hast B gewählt")
        done = True
    elif eingabe == "c":
        print("Du hast C gewählt")
        done = True
    else:
        print("Error: Du hast einen Käse eingegeben!")
        print("Versuche es noch einmal")
```

Wenn die Antwort des Users nicht A, B oder C ist, wiederholt das Programm noch einmal den While-Loop. Wenn die Antwort A, B oder C ist, ist `done` "erledigt" und das Programm ist beendet.