from server.bo.Einzelhändler import Einzelhändler
from server.db.Mapper import Mapper


class EinzelhändlerMapper (Mapper):
    """Mapper-Klasse, die Einzelhändler-Objekte auf eine relationale
    Datenbank abbildet. Hierzu wird eine Reihe von Methoden zur Verfügung
    gestellt, mit deren Hilfe z.B. Objekte gesucht, erzeugt, modifiziert und
    gelöscht werden können. Das Mapping ist bidirektional. D.h., Objekte können
    in DB-Strukturen und DB-Strukturen in Objekte umgewandelt werden.
    """

    def __init__(self):
        super().__init__()

    def find_all(self):
        """Auslesen aller EInzelhändler."""
        pass
    
    def find_by_key(self, Einzelhändler_ID):
        """Suchen eines Einzelhändlers mit vorgegebener Einzelhändler ID."""

    def find_by_name(self, name):
        """Suchen eines Einzelhändlers anhand der Einzelhändler ID."""

    def insert(self, anwender):
        """Einfügen eines Einzelhändlers-Objekts in die Datenbank."""
        pass
    
    def update(self, object):
        """Wiederholtes Schreiben eines Objekts in die Datenbank."""
        pass

    def delete(self, object):
        """Löschen der Daten eines Einzelhändler-Objekts aus der Datenbank."""
        pass