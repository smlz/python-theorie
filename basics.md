# __Basics__
___
**Thonny**

Thonny ist eine Entwicklungsumgebung für Python, sie  bietet alles was man braucht um in Python zu programmieren.

Hier ein Link zu der Website als Starthilfe:

https://thonny.org/ - 
[Thonny](https://thonny.org/)

![Thonny](https://www.iotxplain.com.au/wp-content/uploads/2019/06/mainidescreen.png)

Die verschiedenen Bereiche können über das "View" Menü eingeblendet werden.

**Editor:** Hier können Python- Programme geschrieben/ bearbeitet werden. 

**Shell: / Konsole**
Wenn während dem Ausführen eines Python- Programmes Fehler auftreten, werden sie hier angezeigt. In diesem Bereich findet auch die Aus- und Eingabe von Text durch ein Python- Programm statt.

**Assistant:**
Der Assistant beobachtet und analysiert die Ausführung eines Programmes und bietet im Falle eines Fehlers Hilfe.

**Object Inspector:**
Wenn im Variables- Bereich eine Variable ausgewählt wird, werden die Details des gespeicherten Werts hier angezeigt.

____

**Kommentare**

Mit dem "#" können Kommentare in ein Programm eingefügt werden. Sie sind nützlich zur Eigenorientierung und werden bei der Ausführung ignoriert. 


____

**print**

Mit print() kann auf der Shell eine Nachricht ausgegeben werden:

Nachricht in Form von Text: 

``` 
print(" Der auszugebende Text wird in runden Klammern mit Anführungszeichnen gekennzeichnet.")

print(""" Wenn der Text mehrere Zeilen beansprucht,
so werden je drei Anführungszeichen verwendet.""")
``` 

____

**Datentyp**

Mit type() kann der Datentyp des angegebenen Objektes abgerufen wrden.
```
x = 5

print(type(x))
```
____
**Eingabe** 

Der input- Befehl erlaubt dem Benutzer Etwas auf der Shell einzugeben.

```
eingabe = input("Wie heisst du?") #Hier kann der Benutzer antworten

print("Hallo," + eingabe ) 
```

-> input() liefert einen String zurück.

___

**Zusätzliches:**

Mit den folgenen Tastenkombinationen kann u.a. Zeit gespart werden:

| Kombination| Ergebnis  |    
|---------------|---------------|
|  Ctrl + Space | Code vervollständigen  [1]|   
|  alt + s | Wechseln von Editor zu Shell|  
|  alt + e |  Wechseln Shell zu Editor |  

[1] So sollte dies aussehen:
![Thonny](https://informatik.mygymer.ch/ef2019/user/pages/02.python/02.thonny/thonny-completion.png) 


Try- Except: 

Mit try kann ein Code auf Fehler getestet werden.
Mit except kann der Fehler behandelt werden.

Beispiel:
Hier tritt ein Fehler oder eine "Ausnahme" auf, da x nicht definiert ist.
```
try:
  print(x)
except:
  print("Eine Ausnahme ist aufgetreten")

```
Da der Try- Block ein Fehler auslöst, wird eine Ausnahme ausgeführt.
Es können viele Ausnahmeblöcke definiert werden, z.B. wenn ein spezieller Codeblock für eine bestimmte Art von Fehler ausgeführt werden soll:
```
x = "Hallo"

try:
  print(x)
except NameError:
  print("x ist nicht definiert")
except:
  print("Ein anderer Fehler ist aufgetreten")
else:
    print("Kein Fehler ist aufgetreten")

```

  





