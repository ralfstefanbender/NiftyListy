from server.bo.Einkaufsgruppe import Einkaufsgruppe
from server.db.Mapper import Mapper


class EinkaufsgruppeMapper (Mapper):
    """Mapper-Klasse, die Einkaufsgruppe-Objekte auf eine relationale
    Datenbank abbildet. Hierzu wird eine Reihe von Methoden zur Verfügung
    gestellt, mit deren Hilfe z.B. Objekte gesucht, erzeugt, modifiziert und
    gelöscht werden können. Das Mapping ist bidirektional. D.h., Objekte können
    in DB-Strukturen und DB-Strukturen in Objekte umgewandelt werden.
    """

    def __init__(self):
        super().__init__()