# Dictionaries

![Dictionary](https://www.collinsdictionary.com/images/full/dictionary_168552845.jpg)

###### Quelle: Collin's Dictionary

<br>

Wir können Dictionaries brauchen um Daten mithilfe von _**Key**-**Value**-Paaren_ zu speichern. Man kürzt sie oft mit _dict_ ab.  
Der englische Name _dictionary_ bedeutet auf deutsch **Lexikon** bzw. **Nachschlagewerk**, was genau der Sinn der Dictionaries in Python ist.  
Alle Code-Beispiele dieses Markdown-Dokuments sind in der datei [examples.py](https://github.com/MaGaMe19/Markdown/blob/master/dicts/examples.py) zu finden.  
<br>

---

## Grundsyntax

```Python
dictionary = {
    key: value,
    ...
} *
```  

##### * Kein tatsächlich ausführbarer python code, nur zur Darstellung.

Wichtig: Ohne ein Komma hinter jedem Eintrag funktioniert das Ganze nicht!  
<br>

---

## Grundfuktionen

Verwendetes Dictionary für diese Erklärung:

```Python
beispiel = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
}
```  
<br>

### Zugriff auf das Dictionary
```Python
ausgabe = beispiel["key2"]

>>> print(ausgabe)
 value2
```
Das Zugreifen auf Values innerhalb von Dictionaries ist vergleichbar mit dem Zugreifen auf Listen, es werden eckige Klammern verwendet. Anders als bei Listen gibt man jedoch den **Namen des Keys** in die eckigen Klammern.  
<br>
Eine andere Methode um die Keys bzw. die Values zu erhalten, ist die Verwendung der Funktionen **.keys()**, **.values()** und **.items()**:

```Python
>>> beispiel.keys()
 dict_keys(['key1', 'key2', 'key3'])

>>> beispiel.values()
 dict_values(['value1', 'value2', 'value3'])

>>> beispiel.items()
 dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3')])
```
Die Outputs dieser Funktionen könnte man z.B. mit einem For-Loop darstellen.  
(siehe [Beispiel zu Zahlen als Key](https://github.com/MaGaMe19/Markdown/blob/master/dicts/08_dicts.md#zahlen))  
<br>

### Bearbeiten des Dictionaries

Wir können Values verändern...
```Python
beispiel["key2"] = "newValue2"

>>> print(beispiel["key2"])
 newValue2
```

...oder auch Values hinzufügen:

```Python
beispiel["key4"] = "value4" # der Key "key4" wird mit dem Value "value4" erstellt.

>>> print(beispiel)
 {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
```  
<br>

---

## Häufigste Datentypen als Key

### Strings

```Python
steckbrief = {
    "vorname": "Klaus",
    "nachname": "Müller",
    "wohnort": "Zürich",
}
```

Strings werden am häufigsten als Keys verwendet, da sie vielseitig einsetzbar sind.  
<br>

### Zahlen

```Python
zutaten = {
    1: "Mehl",
    2: "Eier",
    3: "Zucker",
}
```

Zahlen könnte man z.B. für eine nummerierte Liste verwenden: 

```Python
>>> for i, j in zutaten.items():
        print(f"{i}. {j}")

 1. Mehl
 2. Eier
 3. Zucker
```

<br>

---

## Häufigste Datentypen als Value

### Strings und Zahlen

```Python
charakter = {
    "vorname": "James",
    "nachname": "Bond",
    "alter": 35,
    "gewicht": 75,
}
```
Dies ist nützlich wenn man z.B. Einstellungen eines Nutzers speichern möchte, wie beispielsweise den zusammengestellten Spielcharakter in einem Game.  
<br>

### Booleans und "None"

```Python
spielInfo = {
    "spielGestartet": True,
    "spielGewonnen": False,
    "ausrüstung": None,
}
```
Diese Datentypen könnten wiederum in einem Game nützlich sein.  
<br>

### Dictionaries und Listen

```Python
schüler = {
    "Fritz": {
        "klasse": 7,
        "noten": [5.1, 4.5, 5.8],
    },
    "Lisa": {
        "klasse": 8,
        "noten": [4.8, 5.9, 5.6],
    },
}
```
Das ganze kann jedoch schnell kompliziert werden - um z.B. Fritz' zweite Note zu erhalten, müsste man so vorgehen:

```Python
>>> schüler["Fritz"]["noten"][1]
 4.5
```

<br>

---

## Beispiel

Hier ein etwas komplizierteres Beispiel, um ein Schulzeugnis in einem Dictionary zu speichern und anschliessend schön auszudrucken:

```Python
zeugnis = {
    "name": "Fritz Müller",
    "klasse": "8b",
    "alter": 16,
    
    "noten": {
        "deutsch": [5.3, 3.8, 4.7],
        "englisch": [5.6, 4.8, 3.1],
        "mathematik": [3.5, 4.4, 5.0],
        "chemie": [5.8, 3.7, 4.8],
        "physik": [5.9, 3.1, 5.3],
        "informatik": [5.9, 5.6, 5.7],
    }
}

def ausdrucken(z):
    # Name, Klasse und Alter drucken:
    for i,j in list(z.items())[0:3]:
        # Dem Alter "Jahre" hinzufügen:
        if i == "alter":
            j = str(j) + " Jahre"
        print(f"{i.capitalize()}: {j}")
    
    print()
    # Die Noten ausdrucken:
    for k,l in z["noten"].items():
        output = f"{k.capitalize()}:"
        for m in l:
            output += f" [{str(m)}]"
        print(output)
```

Das Ganze sieht ausgedruckt dann so aus:

```Python
>>> ausdrucken(zeugnis)
 Name: Fritz Müller
 Klasse: 8b
 Alter: 16 Jahre

 Deutsch: [5.3] [3.8] [4.7]
 Englisch: [5.6] [4.8] [3.1]
 Mathematik: [3.5] [4.4] [5.0]
 Chemie: [5.8] [3.7] [4.8]
 Physik: [5.9] [3.1] [5.3]
 Informatik: [5.9] [5.6] [5.7]
```

Wichtig ist hierbei natürlich, dass das Zeugnis in dem oben gezeigten "Format" geschrieben wird.

---

&nbsp;  

<small>Copyright &copy; 2020 MaGaMe19.</small>
