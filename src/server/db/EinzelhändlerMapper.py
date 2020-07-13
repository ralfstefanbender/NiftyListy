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
        """Auslesen aller Einzelhändler."""

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT * FROM einzelhändler"
        cursor.execute(command)
        tuples = cursor.fetchall()
        
        self._cnx.commit()
        cursor.close()

        return result
    
    def find_by_key(self, Einzelhändler_ID):
        """Suchen eines Einzelhändlers mit vorgegebener Einzelhändler ID."""

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT händler_ID FROM einzelhändler WHERE händler_ID like '{}'".format(Einzelhändler_ID)
        cursor.execute(command)
        tuples = cursor.fetchall()
        
        self._cnx.commit()
        cursor.close()

        return result

    def find_by_name(self, name):
        """Suchen eines Einzelhändlers anhand der Einzelhändler ID."""

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT name FROM einzelhändler WHERE name like '{}'".format(name)
        cursor.execute(command)
        tuples = cursor.fetchall()
        
        self._cnx.commit()
        cursor.close()

        return result

    def insert(self, einzelhändler):
        """Einfügen eines Einzelhändlers-Objekts in die Datenbank."""

        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) as MAXID from einzelhändler")
        tuples = cursor.fetchall()

        for (MAXID) in tuples:
            einzelhändler.set_id(MAXID[0]+1)

        command = "INSERT INTO einzelhändler (händler_id, name) VALUES ('{}','{}')"\
                .format(einzelhändler.get_id(), einzelhändler.get_name())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
    
    def update(self, einzelhändler):
        """Wiederholtes Schreiben eines Objekts in die Datenbank."""

        cursor = self._cnx.cursor()

        command = "UPDATE einzelhändler SET name = ('{}')" "WHERE händler_id = ('{}')"\
                .format(einzelhändler.get_name(), einzelhändler.get_händler_id)
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

    def delete(self, einzelhändler):
        """Löschen der Daten eines Einzelhändler-Objekts aus der Datenbank."""

        cursor = self._cnx.cursor()

        command = "DELETE FROM einzelhändler WHERE id={}".format(einzelhändler.get_händler_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

"""Testzwecke um uns die Daten anzeigen zu lassen"""

if __name__ == "__main__":
    with EinzelhändlerMapper() as mapper:
        result = mapper.find_all()
        for p in result:
            print(p)