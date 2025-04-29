from dreieck import triangle
import jsonpickle


def save():
    dreieck = triangle(3, 4)
    with open("dreieck.json", "w") as f:
        # Use jsonpickle to encode the object and save it to the file
        f.write(jsonpickle.encode(dreieck))


def load():
    with open("dreieck.json", "r") as f:
        # Use jsonpickle to decode the object from the file
        dreieck = jsonpickle.decode(f.read())
    dreieck.angles()
    print(dreieck)


save()
load()

