from server.bo.Einkaufliste import Einkaufsliste
from server.db.Mapper import Mapper


class EinkaufslisteMapper (Mapper):
    """Mapper-Klasse, die Einkaufsliste-Objekte auf eine relationale
    Datenbank abbildet. Hierzu wird eine Reihe von Methoden zur Verfügung
    gestellt, mit deren Hilfe z.B. Objekte gesucht, erzeugt, modifiziert und
    gelöscht werden können. Das Mapping ist bidirektional. D.h., Objekte können
    in DB-Strukturen und DB-Strukturen in Objekte umgewandelt werden.
    """

    def __init__(self):
        super().__init__()