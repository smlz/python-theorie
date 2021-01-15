# _IF, ELSE und ELIF_  

 ### Dieses Dokument dient dazu, das Konzept für die If/Else Statments besser zu verstehen.       

In einem ersten Schritt wird erklärt für was die If/Else Statments gebräuchlich sind und in einem zweiten Schritt wird aufgezeigt wie sie im Code integriert werden.  

## Wieso und wo braucht man IF/Else Statements?  

If/Else/Elif Statments werden dazu genutzt um eine Hypothese zu überprüfen. Zum Beispiel ob die Summe zweier Zahlen gleich X ist.

### Beispiel

```python
    a=1
    b=2
    c=3
    if a+b == c:
        print("a+b=c") 
    else:
        print("a+b=x")
```

## Wie funktionieren IF/Else Statements?

![Bild IF/ELIF/ELSE](https://i.imgur.com/fqJOBUS.png)  

### Wichtig für das Verständnis von If/Else Statements ist die Reihenfolge in welcher sie stehen. 

  
  
__If__ steht am Anfang eines solchen "If/Else Blocks". Es gibt die erste Bedingung an.
>if a+b == c  

Wenn diese Kondition erfüllt ist, folgt ein Befehl:
>print ("a+b=c")

In Python würde dies wie Folgt aussehen:

```python
if a+b == c:
    print ("a+b=c")
```

__Else__ beendet den Loup der Anforderungen. Else wird gebraucht, wenn keine Bedingungen erfüllt sind.

Beispiel:

```python
    a=1
    b=1
    c=3
    
    If a+b = c:         # 1+1 ≠ 3 deshalb ist dieses Statment nicht erfüllt      
        print("True")
    else:               # else wird ausgeführt
        print("False")

```
Else hat keine eigenen Anforderungen, sondern gibt nur einen Befehl.


__Elif__ steht für "Else,If".   
 Elif wird meistens in der Mitte eines "If/Else-Block" verwendet:

>If...  
>elif...  
>else...

Elif überprüft eine weitere Hypothese, wenn das If Statement nicht zugetroffen hat. Im Gegensatz zu Else können weitere, konkrete Bedingungen überprüft werden. Es können unendlich viele Elifs an die "Kette" angeheftet werden.
### __*Achtung*__:  
Diese "If/Else-Blöcke" werden von Oben nach Unten gelesen und sobald eine Bedingung erfüllt wurde, bricht diese Kette ab und der entsprechende Befehl wird ausgeführt.

```python
    a=1
    b=2
    c=3
    if a+b >= c:        #Diese Statement wurde nicht erfüllt 
        print("a+b>c")  
    elif a+b <= c:      #Diese Statement wurde nicht erfüllt 
        print("a+b<c")
    elif a+b == c:      #Diese Statement wurde erfüllt! -->  print("a+b=c") --> Stop 
        print("a+b=c")
    else:               #Dieses Statement wird nicht mehr beachtet, da die Kette vorher endet
        print("?")
```



### Kleines Hilfe Video:
[![Video](https://techvidvan.com/tutorials/wp-content/uploads/sites/2/2019/12/Python-if-elif-ladder.jpg)](https://www.youtube.com/watch?v=42MBMSOZgD4)   
   
   
## Quellen
___
### Bild
>1. https://techvidvan.com/tutorials/wp-content/uploads/sites/2/2019/12/Python-if-elif-ladder.jpg
>2. https://i.imgur.com/fqJOBUS.png

### Video
>1. https://www.youtube.com/watch?v=42MBMSOZgD4



## Zussatz:

Mit If können True und False bestummen werden. Mann nennt diese Boolische Ausdrücke. Die Boolischen Ausdrücke Vergleichen zwei Dinge, wie zum Beispiel die länge eines Wortes oder die Grösse einer Zahl.
Mit booleschen Operatoren können verschiedene boolesche Ausdrücke verkettet oder verneint werden. So können komplizierte Bedingungen wie „Ist A gleich B oder B gleich D“ formuliert werden. Es gibt die folgenden Operatoren:

not:  
Kehrt den Wahrheitswert eines Ausdrucks um. Der Operator macht dasselbe wie das deutsche Wort nicht.  
and:  
Ist wahr, wenn die Ausdrücke links und rechts des Operators wahr sind. Es handelt sich um eine und Verknüpfung.  
or:  
Ist wahr, wenn der Ausdruck links oder der Ausdruck rechts des Operators wahr ist. Es ist auch wahr, wenn beide wahr sind. Es handelt sich um eine oder Verknüpfung.   
(https://pythonbuch.com/bool.html)



