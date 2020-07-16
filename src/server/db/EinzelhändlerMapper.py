from src.server.bo.Einzelhändler import Einzelhändler
from src.server.db.Mapper import Mapper

class EinzelhändlerMapper(Mapper):
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

        for (id, name, create_time) in tuples:
            einzelhändler = Einzelhändler()
            einzelhändler.set_id(id)
            einzelhändler.set_name(name)
            einzelhändler.set_erstellungszeitpunkt(create_time)
            result.append(einzelhändler)
        
        self._cnx.commit()
        cursor.close()

        return result
    
    def find_by_key(self, id):
        """Suchen eines Einzelhändlers mit vorgegebener Einzelhändler ID."""

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT * FROM einzelhändler WHERE ID like '{}'".format(id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        if len(tuples) != 0:

            for (id, name, create_time) in tuples:
                einzelhändler = Einzelhändler()
                einzelhändler.set_id(id)
                einzelhändler.set_name(name)
                einzelhändler.set_erstellungszeitpunkt(create_time)
                result.append(einzelhändler)

            result = einzelhändler

        else:

            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_name(self, name):
        """Suchen eines Einzelhändlers anhand des Namen vom Einzelhändler."""

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT * FROM einzelhändler WHERE name like '{}'".format(name)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, name, create_time) in tuples:
            einzelhändler = Einzelhändler()
            einzelhändler.set_id(id)
            einzelhändler.set_name(name)
            einzelhändler.set_erstellungszeitpunkt(create_time)
            result.append(einzelhändler)

        self._cnx.commit()
        cursor.close()

        return result

    def insert(self, einzelhändler):
        """Einfügen eines Einzelhändlers-Objekts in die Datenbank."""

        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) as MAXID from einzelhändler")
        tuples = cursor.fetchall()

        for (MaxID) in tuples:
            einzelhändler.set_id(MaxID[0]+1)

        command = "INSERT INTO einzelhändler (id, name, create_time) VALUES ('{}','{}','{}')"\
                .format(einzelhändler.get_id(), einzelhändler.get_name(), einzelhändler.get_erstellungszeitpunkt())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
    
    def update(self, einzelhändler):
        """Wiederholtes Schreiben eines Objekts in die Datenbank."""

        cursor = self._cnx.cursor()

        command = "UPDATE einzelhändler SET name = ('{}'), create_time = ('{}')" "WHERE id = ('{}')"\
                .format(einzelhändler.get_name(), einzelhändler.get_erstellungszeitpunkt(), einzelhändler.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

    def delete(self, einzelhändler):
        """Löschen der Daten eines Einzelhändler-Objekts aus der Datenbank."""

        cursor = self._cnx.cursor()

        command = "DELETE FROM einzelhändler WHERE id={}".format(einzelhändler.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

"""Testzwecke um uns die Daten anzeigen zu lassen"""

if __name__ == "__main__":
    with EinzelhändlerMapper() as mapper:
        result = mapper.find_all()
        for p in result:
            print(p.get_name())
