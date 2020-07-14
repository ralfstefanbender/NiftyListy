from src.server.bo.Zugehörigkeit import Zugehörigkeit
from src.server.db.Mapper import Mapper

class AnwenderMapper (Mapper):
    """Mapper-Klasse, die Anwender-Objekte auf eine relationale
    Datenbank abbildet. Hierzu wird eine Reihe von Methoden zur Verfügung
    gestellt, mit deren Hilfe z.B. Objekte gesucht, erzeugt, modifiziert und
    gelöscht werden können. Das Mapping ist bidirektional. D.h., Objekte können
    in DB-Strukturen und DB-Strukturen in Objekte umgewandelt werden.
    """

    def __init__(self):
        super().__init__()

    def find_all(self):
        """Auslesen aller App-Anwender."""

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT * FROM zugehörigkeit"
        cursor.execute(command)
        tuples = cursor.fetchall()  

        for (id, user_id, einkaufsgruppe_id) in tuples:
            zugehörigkeit = Zugehörigkeit()
            zugehörigkeit.set_id(id)
            zugehörigkeit.set_user_id(user_id)
            zugehörigkeit.set_einkaufsgruppe_id(einkaufsgruppe_id)
            result.append(zugehörigkeit)

        self._cnx.commit()
        cursor.close()

        return result

        def find_by_key(self, zugehörigkeit_id):
        """Suchen eines Anwenders mit vorgegebener user ID"""

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT zugehörigkeit_id FROM zugehörigkeit WHERE zugehörigkeit_id like '{}'".format(zugehörigkeit_id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        if len (tuples) != 0:

            for (id, user_id, einkaufsgruppe_id) in tuples:
            zugehörigkeit = Zugehörigkeit()
            zugehörigkeit.set_id(id)
            zugehörigkeit.set_user_id(user_id)
            zugehörigkeit.set_einkaufsgruppe_id(einkaufsgruppe_id)
            result.append(zugehörigkeit)

        result = anwender

        self._cnx.commit()
        cursor.close()

        return result

        def insert(self, anwender):
        """Einfügen eines Anwender-Objekts in die Datenbank."""

        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(zugehörigkeit_id) as MaxID from zugehörigkeit")
        tuples = cursor.fetchall()

        for (MaxID) in tuples:
            anwender.set_id(MaxID[0]+1)

        command = "INSERT INTO zugehörigkeit (zugehörigkeit_id, user_id, einkaufsgruppe_id) VALUES ('{}','{}','{}')"\
            .format(zugehörigkeit.get_id(), zugehörigkeit.get_anwender_id(), zugehörigkeit.get_einkaufsgruppe_id)
            cursor.execute(command)

        self._cnx.commit()
        cursor.close() 
"""
        def update(self, anwender):
        """Wiederholtes Schreiben eines Objekts in die Datenbank."""

        cursor = self._cnx.cursor()

        command = "UPDATE anwender SET benutzername = ('{}'), user_id = ('{}'), einkaufsgruppe_id = ('{}')" "WHERE zugehörigkeit_id = ('{}')"\
                .format(anwender.get_benutzername(), anwender.get_email(), anwender.get_google_id, anwender.get_erstellungszeitpunkt, anwender.get_user_id)
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

    def delete(self, anwender):
        """Löschen der Daten eines Anwenders-Objekts aus der Datenbank."""

        cursor = self._cnx.cursor()

        command = "DELETE FROM anwender WHERE user_id={}".format(anwender.get_user_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
"""
"""Testzwecke um uns die Daten anzeigen zu lassen"""

if __name__ == "__main__":
    with ZugehörigkeitMapper() as mapper:
        result = mapper.find_all()
        for p in result:
            print(p.get_id)