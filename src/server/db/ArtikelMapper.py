from server.bo.Artikel import Artikel
from server.db.Mapper import Mapper


class ArtikelMapper (Mapper):
    """Mapper-Klasse, die Artikel-Objekte auf eine relationale
    Datenbank abbildet. Hierzu wird eine Reihe von Methoden zur Verfügung
    gestellt, mit deren Hilfe z.B. Objekte gesucht, erzeugt, modifiziert und
    gelöscht werden können. Das Mapping ist bidirektional. D.h., Objekte können
    in DB-Strukturen und DB-Strukturen in Objekte umgewandelt werden.
    """

    def __init__(self):
        super().__init__()

    def find_all(self):
        """Liest alle Tupel aus und gibt sie als Objekte zurück"""

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT * FROM artikel"
        cursor.execute(command)
        tuples = cursor.fetchall()
        
        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self):
        """Sucht die Artikel nach der eingegebenen ID aus"""

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT artikel_ID FROM artikel WHERE artikel_ID like '{}'".format(artikel_ID)
        cursor.execute(command)
        tuples = cursor.fetchall()
        
        self._cnx.commit()
        cursor.close()

        return result

    def insert(self):
        """Artikel hinzufügen"""
        pass

    def update(self):
        """Wiederholtes Schreiben eines Objekts in die Datenbank."""
        pass

    def delete(self):
        """Artikel löschen"""
        pass