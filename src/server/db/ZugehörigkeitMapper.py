from src.server.bo.Zugehörigkeit import Zugehörigkeit
from src.server.db.Mapper import Mapper


class ZugehörigkeitMapper(Mapper):
    """Mapper-Klasse, die Zugehörigkeiten auf eine relationale
    Datenbank abbildet. Hierzu wird eine Reihe von Methoden zur Verfügung
    gestellt, mit deren Hilfe z.B. Objekte gesucht, erzeugt, modifiziert und
    gelöscht werden können. Das Mapping ist bidirektional. D.h., Objekte können
    in DB-Strukturen und DB-Strukturen in Objekte umgewandelt werden.
    """

    def __init__(self):
        super().__init__()

    def find_all(self):
        """Auslesen aller Zugehörigkeiten."""

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT * FROM zugehörigkeit"
        cursor.execute(command)
        tuples = cursor.fetchall()  

        for (id, anwender_id, einkaufsgruppe_id, create_time) in tuples:
            zugehörigkeit = Zugehörigkeit()
            zugehörigkeit.set_id(id)
            zugehörigkeit.set_anwender_id(anwender_id)
            zugehörigkeit.set_einkaufsgruppe_id(einkaufsgruppe_id)
            zugehörigkeit.set_erstellungszeitpunkt(create_time)
            result.append(zugehörigkeit)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, id):
        """Suchen eines Anwenders mit vorgegebener user ID"""

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT * FROM zugehörigkeit WHERE id like '{}'".format(id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        if len(tuples) != 0:

            for (id, anwender_id, einkaufsgruppe_id, create_time) in tuples:
                zugehörigkeit = Zugehörigkeit()
                zugehörigkeit.set_id(id)
                zugehörigkeit.set_anwender_id(anwender_id)
                zugehörigkeit.set_einkaufsgruppe_id(einkaufsgruppe_id)
                zugehörigkeit.set_erstellungszeitpunkt(create_time)
                result.append(zugehörigkeit)

            result = zugehörigkeit

        else:

            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_account(self, id):

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT * FROM zugehörigkeit WHERE anwender_id like '{}'".format(id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        if len(tuples) != 0:
            for (id, anwender_id, einkaufsgruppe_id, create_time) in tuples:
                zugehörigkeit = Zugehörigkeit()
                zugehörigkeit.set_id(id)
                zugehörigkeit.set_anwender_id(anwender_id)
                zugehörigkeit.set_einkaufsgruppe_id(einkaufsgruppe_id)
                zugehörigkeit.set_erstellungszeitpunkt(create_time)
                result.append(zugehörigkeit)

        else:
            result = None

        self._cnx.commit()
        cursor.close()
        return result

    def insert(self, zugehörigkeit):
        """Einfügen eines Anwender-Objekts in die Datenbank."""

        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) as MaxID from zugehörigkeit")
        tuples = cursor.fetchall()

        for (MaxID) in tuples:
            zugehörigkeit.set_id(MaxID[0]+1)

        command = "INSERT INTO zugehörigkeit (id, anwender_id, einkaufsgruppe_id, create_time) VALUES ('{}','{}','{}','{}')"\
            .format(zugehörigkeit.get_id(), zugehörigkeit.get_anwender_id(), zugehörigkeit.get_einkaufsgruppe_id(), zugehörigkeit.get_erstellungszeitpunkt())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

    def update(self, zugehörigkeit):
        """Wiederholtes Schreiben eines Objekts in die Datenbank."""

        cursor = self._cnx.cursor()

        command = "UPDATE zugehörigkeit SET anwender_id = ('{}'), einkaufsgruppe_id = ('{}'), create_time = ('{}')" "WHERE id = ('{}')"\
                .format(zugehörigkeit.get_anwender_id(), zugehörigkeit.get_einkaufsgruppe_id(), zugehörigkeit.get_erstellungszeitpunkt(), zugehörigkeit.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

    def delete(self, zugehörigkeit):

        cursor = self._cnx.cursor()

        command = "DELETE FROM zugehörigkeit WHERE id={}".format(zugehörigkeit.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
        

"""Testzwecke um uns die Daten anzeigen zu lassen"""

if __name__ == "__main__":
    with ZugehörigkeitMapper() as mapper:
        test = mapper.find_by_account(1)
        print(test)
        for i in test:
            mapper.delete(i)





