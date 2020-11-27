# Eine Funktion ist eine Sammlung von Befehlen / Anweisungen

def sag_hallo_einfach(name=""):
    if name == "":
        print("Guten Tag.")
    else:
        print(f"Hallo {name}.")
    print("Wie geht es dir?")
    
def sag_hallo_umfassend(vorname, nachname=""):
    if nachname == "":
        print(f"Hallo {vorname}")
    else:
        print(f"Guten Tag {vorname[0]}. {nachname}")
    

sag_hallo_umfassend()  # -> Guten Tag
sag_hallo_umfassend("Hanna")  #  -> Hallo Hanna
sag_hallo_umfassend("Kurt", "Krömer", True) # -> Guten Tag Herr K. Krömer


# Eine etwas mathematischerer Variante:

def begruessung(vorname, nachname=""):
    if nachname == "":
        return f"Hallo {vorname}"
    else:
        return f"Guten Tag {vorname} {nachname}"

vorname = "Marco"

print(begruessung("Kurt"))
print(begruessung("Heidi", "Müller"))


def countdown(n):
    """Counts down from n.

    Sample usage:
    >>> countdown(3)
    3
    2
    1
    Go!
    """
    if n == 0:
        print ("Go!")
    elif n < 0:
        print("Error: Zahl ist negativ")
    else:
        print(n)
        countdown(n - 1)
    
countdown(2)