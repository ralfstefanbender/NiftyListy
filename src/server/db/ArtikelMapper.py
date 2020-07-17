from src.server.bo.Artikel import Artikel
from src.server.db.Mapper import Mapper


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

        for (id, name, einheit, create_time) in tuples:
            artikel = Artikel()
            artikel.set_id(id)
            artikel.set_name(name)
            artikel.set_einheit(einheit)
            artikel.set_erstellungszeitpunkt(create_time)
            result.append(artikel)
        
        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, id):
        """Sucht die Artikel nach der eingegebenen ID aus"""

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT * FROM artikel WHERE id like '{}'".format(id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        if len(tuples) != 0:

            for (id, name, einheit, create_time) in tuples:

                artikel = Artikel()
                artikel.set_id(id)
                artikel.set_name(name)
                artikel.set_einheit(einheit)
                artikel.set_erstellungszeitpunkt(create_time)
                result = artikel
        else:

            result = None
        
        self._cnx.commit()
        cursor.close()

        return result

    def find_by_name(self, name):
        """Suchen eines Artikel anhand des Namens des Artikels."""

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT * FROM artikel WHERE name like '{}'".format(name)
        cursor.execute(command)
        tuples = cursor.fetchall()

        if len(tuples) != 0:

            for (id, name, einheit, create_time) in tuples:
                artikel = Artikel()
                artikel.set_id(id)
                artikel.set_name(name)
                artikel.set_einheit(einheit)
                artikel.set_erstellungszeitpunkt(create_time)
                result = artikel

        else:

            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def insert(self, artikel):
        """Artikel hinzufügen"""

        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) as MaxID from artikel")
        tuples = cursor.fetchall()

        for (MaxID) in tuples:
            artikel.set_id(MaxID[0]+1)

        command = "INSERT INTO artikel (id, name, einheit, create_time) VALUES ('{}','{}','{}','{}')"\
                .format(artikel.get_id(), artikel.get_name(), artikel.get_einheit(), artikel.get_erstellungszeitpunkt())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()  

    def update(self, artikel):
        """Wiederholtes Schreiben eines Objekts in die Datenbank."""
        cursor = self._cnx.cursor()

        command = "UPDATE artikel SET name = ('{}'), einheit = ('{}'), create_time = ('{}')" "WHERE id = ('{}')"\
                .format(artikel.get_name(), artikel.get_einheit(), artikel.get_erstellungszeitpunkt(), artikel.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

    def delete(self, artikel):
        """Artikel löschen"""

        cursor = self._cnx.cursor()

        command = "DELETE FROM artikel WHERE id = {}".format(artikel.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

"""Testzwecke um uns die Daten anzeigen zu lassen"""

if __name__ == "__main__":
    with ArtikelMapper() as mapper:
        artikel = mapper.find_by_name("Wasser").get_id()
        print(artikel)
