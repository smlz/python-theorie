import json
from datetime import datetime as time

# Einfaches Beispiel:
with open("name.json", "w") as f:
    name = "Mattia"
    json.dump(name, f)

with open("name.json") as f:
    gelesener_name = json.load(f)

print("Geschrieben haben wir:", name)
print("Und gelesen haben wir:", gelesener_name, "\n")

# Komplizierteres Beispiel:
with open("person.json", "w") as f:
    person = {
        "name": "Mattia",
        "alter": 15,
        "volljaehrig": False,
        "hobbies": ["Tennis", "Programmieren"],
        "einkommen": None,
        "zeit": time.now().isoformat(),
    }
    json.dump(person, f)

with open("person.json") as f:
    gelesene_person = json.load(f)

def print_person(person):
    print(f" - Name: {person['name']}")
    print(f" - Alter: {person['alter']}")
    print(f" - Volljährig: {person['volljaehrig']}")
    print(" - Hobbies:")
    for hobby in person["hobbies"]:
        print(f"   • {hobby}")
    print(f" - Einkommen: {person['einkommen']}")
    print(f" - Momentane Zeit: {person['zeit']}")

print("Ursprüngliche Person:")
print_person(person)
print()

print("Gespeicherte und gelesene Person:")
print_person(gelesene_person)

# Erneutes Lesen:
with open("person2.json", "w") as f:
    json.dump(person, f, indent=4)