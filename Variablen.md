# **Variablen**

Hier erfährst du alles was du über eine Variable und ihre Möglichkeiten/Grenzen bei Python wissen musst. 
Du erfährst wie du sie anwenden und strukturieren kannst.

---
## Was ist eine Variable?
---

Eine Variable kann nach Belieben benannt werden und so gut wie alles beinhalten. 

Zuerst muss man einer Variable einen Namen geben:
```Python
DasisteineVariable 
```
und dann gibt man ihr noch einen Wert:

```Python
DasisteineVariable = 3 + 4

# Strings funktionieren auch als Wert:

DasisteineandereVariable = "Hello"
```
![Hi](https://www.studytonight.com/python/images/variables-in-python-2.png)

```Python
# das funktioniert nicht!

12 = x
 
# nur so rum

x = 12
```

Die Variable MUSS mindestens **einen** Buchstaben beinhalten um als Variable zu gelten. Dafür können Variablen so lang sein wie es einem beliebt.

Es gibt gewisse Zeichen die funktionieren nicht, wenn man sie in den Namen einer Variable einsetzt. Dies wären folgende Zeichen:

    Leerzeichen     !       ?       .      ,  
     _________________________________________
     ;       :       ()     []      {}      ¨
     _________________________________________
     $      £        "       '       ´       `  
     _________________________________________
     ^       ~       <>     \     /      +       
     _________________________________________
     -       *       =       ¦       @       #       
     _________________________________________
     ç       %       &       ¬       |       ¢ 
     _________________________________________
     es empfiehlt sich auch diese Buchstaben 
     nicht zu verwenden: ä, ö, ü, é, è, à

Die Variable kann auch aus einer Kombination von Buchstaben und Zahlen bestehen. 

```Python
DasisteineVariable1 = 3 + 5
DasisteineVariable2 = "Hello"
```
 
Um eine bessere Übersicht zu gewinnen kann man die Wörter mit Unterstrichen verbinden. 

```Python
Das_ist_eine_Variable_1 = 21 / 3
Das_ist_eine_Variable_2 = "Hello"
```

Die Variable speichert den Wert, den man ihr gegeben hat und man kann ihn jederzeit aufrufen oder ändern. 

### **Sinnvolle Variablen**
---
Verwendet man viele Variablen macht es Sinn, dass sie einen Sinnvollen Namen besitzen der einfach zu erkennen ist.

Beispielsweise so: 
```Python
begruessung = "Hallo mein Name ist Muster. Willkommen."
alter = "Ich habe bereits ein gewisses Alter."
rechnung = 3 + 4
```
Es hilft beim Strukturieren und organisieren des Programmes. So sind die Variablen auch leichter zu merken und wiederzufinden.

### **Wertänderung einer/mehreren Variablen**
---
Wenn man den Wert einer Variable verändern oder ergänzen möchte geht das ganz einfach so:

```Python
Variable1 = 3

# Variable1 hat den falschen Wert
# Gib einfach die gleiche Variable ein und wechsle ihren Wert.

Variable1 = 4
```
Wenn nun später die Variable "Variable1" aufgerufen wird erhält man 4. Es speichert IMMER den zuletzt eingegebenen Wert einer Variable ab. Wenn man den ändert verwendet das Programm den Wert, der als letztes vor dem verwenden der Variable gebraucht wurde. 

### **Kombination von Variablen**
---
Man kombiniert Variablen mit ihren Werten üblicherweise für folgende Gründe:
- Man möchte **1 gesamthaftes/durchschnittliches** Resultat

```Python
Variable_1 = 4 + 3
Variable_2 = 9 - 4

Variable_4 = Variable_1 + Variable_2 
Variable_5 = (Variable_1 + Variable_2) / 2

# Das funktioniert auch mit Strings

nr_1 = "Hi. "                  
nr_2 = "Wie geht es dir?"
nr_3 = nr_1 + nr_2
```
Wenn man Variablen die Strings besitzen kombiniert ist es wichtig, dass bei der ersten Variable im String am schluss ein Lehrschlag gelassen wird. Sonst sieht es so aus:

    "Hi.Wie geht es dir?"

mit Lehrschlag aber so:

    "Hi. Wie geht es dir?"

- Um **Zwischenresultate** anzuzeigen/notieren/in andere Variable umformen
```Pyhton
Variable1 = 1
Variable2 = 6

Zwischenresultat1 = Variable1 + Variable2

Notieren("Das ist das Zwischen/Resultat ", Zwischenresultat1,".")

andereVariable = Variable1
```
Man kann auch Variablen, die einen Zahlenwert besitzen mit Variablen verbinden die Strings speichern.
```Python
Zahl = 2021 - 2000

# Wenn die Zahl mittendrin sein soll:
Text = "Ich bin", Zahl, "Jahre alt."

# Ist die Zahl am Anfang oder Schluss des Strings sieht das so aus:
Text1 = "Resultat: ", Zahl
Text2 = Zahl, "Jahre ist es her."
```

---
## **Ausgabe einer Variable**
---

Nachdem eine Variable mit einem Wert erstellt wurde, wird das Ergebnis noch nicht angezeigt. Es fehlt noch der Befehl zum Ausgeben des eingegebenen. 

Das funktioniert so:
```Python
nr1 = 4 + 5
nr2 = 9 - 3

# Bei einer Rechnung kann man +, -, * oder / rechnen

nr3 = nr1 - nr2 

# um das Ergebnis nun auszugeben braucht man den Befehl print

>>> print(nr3)
3
```
Das Ganze funktioniert auch mit Strings
```Python
nr_1 = "Hello "
nr_2 = "World"

# um 2 oder mehrere Strings zu kombinieren muss man sie IMMER mit einem + kombinieren.

nr_3 = nr_1 + nr_2

>>> print(nr_3)
'Hello World'
```

## **Hier noch einmal alles zusammen gefasst**
---
```Python
# 1. Variable mit Wert erstellen
variable = 6 + 0.5
string = "Hello World"
text = "This is your result: "

# 2. Optional:Kombination von Variablen
result = text, variable

# 3. Resultat anzeigen
>>> print(string)
>>> print(result)
'Hello World
('This is your result: ', 6.5)
```
![Beispiel](https://i.ytimg.com/vi/pXK-gYE8gxg/maxresdefault.jpg)