![Bild](https://thumbs.dreamstime.com/b/d-rendering-abstract-blocks-mathematical-formulas-located-virtual-space-d-rendering-abstract-blocks-mathematical-122389859.jpg)
Zahlen
==

Eine der nützlichsten Eigenschaften von Python ist die Fähigkeit zu rechnen. Python kann :


Addition  ($2+2 = 4$)
``` python
Syntax
2 + 2 = 4
```
Subtraktion ($4-2 = 2$)
``` python
Syntax
4 - 2 = 2
```
Multiplikation ($2*2 = 4$)
``` python
Syntax
2 * 2 = 4
```
Division ($4:2 = 2$)
``` python
Syntax
4 / 2 = 2
```
Exponentialrechnen ($2^2 = 4$)
``` python
Syntax
2 ** 2 = 4
```
Wurzel ( $\sqrt{2} =  1.4142135623731$ )
>* Man kann entweder einfach die gewünschte Wurzel in einen Exponenten umwandeln. 
Bsp. $\sqrt{2^1} = 2^{1:2} = 2^{0.5}$ 
>* Oder man kann es importieren. Hierbei kann jedoch nur die Quadratwurzel gezogen werden.
``` python
Syntax
1) 2 ** 0.5 = 1.4142135623731

2) from math import sqrt
   sqrt(2) = 1.4142135623731
```
Ganzzahlige Division ($10:3 = 3$)
``` python
Syntax
10 // 3 = 3
```
Ganzzahliger Rest ($10:3 = 1$)
``` python
Syntax
10 % 3 = 1
```

####Importieren

>Man kann allerlei Math Funktionen importieren. Ich hab noch den Logarithmus hinzugefügt weil er noch oft verwendet wird.
log(x, Basis) = Exponent
``` python
from math import log

log(9, 3) = 2
```

######In Python wird zwischen 2 Arten von Zahlen unterschieden:

```
Interger
Eine Ganze Zahl (-2, -1, 0, 1, 2,...)
```
```
Float
Eine Kommazahl (-3.14, 2.48349, 5.0)
```
>Wenn ein Benutzer in Python eine Eingabe macht ist es immer zuerst ein String. Um es zu einem Interger umzuwandeln kann man (int) verwenden. Das ist notwendig wenn man damit rechnen will. Zuunterst im vorhandenen Code findet ihr ein Beispiel.

Beispiel Code
=
``` python
#Mal, Plus, Minus
print(1+1)
print(2*3)
print(3-5)

# Hoch
print(2**5)

#Wurzel
print(2**0.5)  

#Die normale divison. Resultat ist immer float.
print(7/2)

#Ganzzahlige Division. Das Resuktat ist ein int.
print(7//3)

#Modulo: Der ganzzahlge Rest der Division
print(7%3)

#Es gibt 2 Arten von Zahlen
#Ganzzahl: int (Interger)
print(1)
#Kommazahl: float (Floating point Number, Fliesskommazahl)
print(1.0)

# Text kann in eine Ganzzahl umgewandelt werden mit der Funktion int
Benutzereingabe = "145"
alter = int(Benutzereingabe)
Jahrgang = 2020 - alter
print(Jahrgang)
```