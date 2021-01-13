<center>_Funktionen_<center>
==

<center><img src="https://asciich.ch/wordpress/wp-content/uploads/2013/09/python_featured_image.png" alt="python" width="100"/><center> 
<span style="color:skyblue">_in Python_</span> by Neringa
<br/>
==


<h2>Was ist eine Funktion?</h2>
<br/>

>Eine Funktion ist eine Sammlung von Befehlen / Anweisungen

>数学の機能は完全に異なります
>><span style="color:yellow">sɹǝpuɐ zuɐƃ ʞᴉʇɐɯǝɥʇɐW ɹǝp uᴉ puᴉs uǝuoᴉʇʞunℲ ǝᴉp</span>


<br/>

---

<h2>die einfachste Funktion:</h2>

```python
def name_der_funktion():
  pass
```
- mit `def` wird die Funktion eingeleitet
- nach dem Namen der Funktion müssen Klammern `()` folgen
- in der Klammer stehen die Argumente, die die Funktion verwenden darf
- <span style="color:black; background: #ffff99">Die Funktion wird hier noch nicht ausgeführt</span>, sondern nur abgespeichert.

```python
name_der_funktion()
```

> In diesem Fall ist die Funktion ziemlich unnötig, denn sie tut absolut nichts.


---
<br/>
<h2>Ein einfaches Beispiel :</h2>


```python
def sag_hallo(name=""):
    if name == "":
        print("Guten Tag.")
    else:
        print(f"Hallo {name}.")
    print("Wie geht es dir?")
```
- Wenn beim Abrufen der Funktion der Name in den Klammern nicht gegeben ist (`sag_hallo()`), wird die Variable `name` als ein leerer String `""` abgespeichert.

<details>
    <summary><span style="color:skyblue">----&rarr;  <i>Output:</i></span></summary>
    <code>
    >>> Guten Tag.
    <br>
    >>> Wie geht es dir?
    </code>
</details>
<br>

- Wenn der Name jedoch vorgegeben ist (`sag_hallo("Jason")`), kann der `else`-Block in Gang gesetzt werden.

<details>
    <summary><span style="color:skyblue">----&rarr;  <i>Output:</i></span></summary>
    <code>
    >>> Hallo Jason.
    <br>
    >>> Wie geht es dir?
    </code>
    <br>
</details>

---
<br>
<h2>ein schwierigeres Beispiel :</h2>

```python
def sag_hallo_umfassend(vorname, nachname=""):
    if nachname == "":
        print(f"Hallo {vorname}")
    else:
        print(f"Guten Tag {vorname[0]}. {nachname}")
```
 - <span style="color:black; background: #ccffff">Hier muss `vorname` angegeben sein</span>, denn es wird innerhalb der Funktion gebraucht und wird im Gegensatz zu `nachname` nicht einfach als leerer String `""` gespeichert.


 ```python
#Fall 1:
sag_hallo_umfassend()

#>>> TypeError: sag_hallo_umfassend() missing 1 required positional argument: 'vorname'

#Fall 2:
sag_hallo_umfassend("Pennywise")

>>> Hallo Pennywise

#Fall 3:
sag_hallo_umfassend("Michael", "Myers")

>>> Guten Tag M. Myers
```
---
<br/>

Eine andere Variante:
-


```python
def begruessung(vorname, nachname=""):
    if nachname == "":
        return f"Hallo {vorname}"
    else:
        return f"Guten Tag {vorname} {nachname}"
```
- Hier wird das `return`-Statement verwendet.
- `return` beendet die Funktion und gibt dabei das Resultat, das direkt nach `return` angegeben werden muss, zurück

```python
#Fall 1:
print(begruessung("Kurt"))

>>> Hallo Kurt

#Fall 2:
print(begruessung("Heidi", "Müller"))

>>> Guten Tag Heidi Müller
```
---
<br/>

Eine etwas mathematischere Variante:
-

```python
def countdown(n):
    if n == 0:
        print ("Go!")
    elif n < 0:
        print("Error: Zahl ist negativ")
    else:
        print(n)
        countdown(n - 1)
```
- Hier wird <u> die Rekursion</u> verwendet
- das bedeutet, dass die Funktion sich selbst aufruft
- In diesem Fall ruft die Funktion sich so lange auf, bis das Argument `0` beträgt.
```python
#Fall 1:
countdown(3)

>>>
3
2
1
Go!

#Fall 2:
countdown(-2)

>>> Error: Zahl ist negativ
```
---
<br/>

Ein kleiner Zusatz:
-
>Wie kann man eine Funktion als Argument verwenden?

ein sehr simples Beispiel:

```python
def mach_etwas(func):
    print(func())

def sag_hallo():
    return "hallo"

def sag_ciao():
    return "ciao"

#Fall 1:
mach_etwas(sag_hallo)

>>> hallo

#Fall 2:
mach_etwas(sag_ciao)

>>> ciao
```
- ohne die Klammer `()` wird die Funktion nicht in Gang gebracht, deshalb kann man sie gut als Argument einsetzen


<details>
  <summary><strong><span style="color:black; background: #cc6699">Click here to see the end</span></strong></summary>
  <p><center><font face="courier" size="7" color="#fff">
    THE END
    </font><center></p>
</details>
