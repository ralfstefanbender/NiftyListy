from src.server.bo.Anwender import Anwender
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
        command = "SELECT * FROM anwender"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, benutzername, email, google_id, create_time) in tuples:
            anwender = Anwender()
            anwender.set_id(id)
            anwender.set_benutzername(benutzername)
            anwender.set_email(email)
            anwender.set_google_id(google_id)
            anwender.set_erstellungszeitpunkt(create_time)
            result.append(anwender)

        self._cnx.commit()
        cursor.close()

        return result
    
    def find_by_key(self, user_id):
        """Suchen eines Anwenders mit vorgegebener user ID"""

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT * FROM anwender WHERE user_id like '{}'".format(user_id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        if len (tuples) != 0:

            for (id, benutzername, email, google_id, create_time) in tuples:
                anwender = Anwender()
                anwender.set_id(id)
                anwender.set_benutzername(benutzername)
                anwender.set_email(email)
                anwender.set_google_id(google_id)
                anwender.set_erstellungszeitpunkt(create_time)
                result.append(anwender)

        result = anwender

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_name(self, name):
        """Suchen eines Anwenders anhand des Namens des Anwenders."""

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT name FROM anwender WHERE name like '{}'".format(name)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, benutzername, email, google_id, create_time) in tuples:
            anwender = Anwender()
            anwender.set_id(id)
            anwender.set_benutzername(benutzername)
            anwender.set_email(email)
            anwender.set_google_id(google_id)
            anwender.set_erstellungszeitpunkt(create_time)
            result.append(anwender)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_google_id(self, google_id):
        """Suchen eines Anwenders anhand der Google ID des Anwenders."""

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT * FROM anwender WHERE google_id like '{}'".format(google_id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, benutzername, email, google_id, create_time) in tuples:
            anwender = Anwender()
            anwender.set_id(id)
            anwender.set_benutzername(benutzername)
            anwender.set_email(email)
            anwender.set_google_id(google_id)
            anwender.set_erstellungszeitpunkt(create_time)
            result.append(anwender)

        self._cnx.commit()
        cursor.close()

        return result        

    def insert(self, anwender):
        """Einfügen eines Anwender-Objekts in die Datenbank."""

        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) as MaxID from anwender")
        tuples = cursor.fetchall()

        for (MaxID) in tuples:
            anwender.set_id(MaxID[0]+1)

        command = "INSERT INTO anwender (id, benutzername, email, google_id, create_time) VALUES ('{}','{}','{}','{}','{}')"\
                .format(anwender.get_id(), anwender.get_benutzername(), anwender.get_email(), anwender.get_google_id(), anwender.get_erstellungszeitpunkt())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()        
    
    def update(self, anwender):
        """Wiederholtes Schreiben eines Objekts in die Datenbank."""

        cursor = self._cnx.cursor()

        command = "UPDATE anwender SET benutzername = ('{}'), email = ('{}'), google_id = ('{}'), create_time = ('{}')" "WHERE id = ('{}')"\
                .format(anwender.get_benutzername(), anwender.get_email(), anwender.get_google_id(), anwender.get_erstellungszeitpunkt(), anwender.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

    def delete(self, anwender):
        """Löschen der Daten eines Anwenders-Objekts aus der Datenbank."""

        cursor = self._cnx.cursor()

        command = "DELETE FROM anwender WHERE id={}".format(anwender.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

"""Testzwecke um uns die Daten anzeigen zu lassen"""

if __name__ == "__main__":
    with AnwenderMapper() as mapper:
        result = mapper.find_all()
        for p in result:
            print(p.get_google_id)
