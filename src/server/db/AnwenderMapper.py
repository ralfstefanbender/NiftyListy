from server.bo.Anwender import Anwender
from server.db.Mapper import Mapper


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

        for (id, name, benutzername, email) in tuples:
            anwender = Anwender()
            anwender.set_user_id(id)
            anwender.set_name(name)
            anwender.set_benutzername(benutzername)
            anwender.set_email(email)
            result.append(anwender)

        self._cnx.commit()
        cursor.close()

        return result
    
    def find_by_key(self, user_ID):
        """Suchen eines Anwenders mit vorgegebener user ID"""

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT user_ID FROM anwender WHERE user_ID like '{}'".format(user_ID)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, name, benutzername, email) in tuples:
            anwender = Anwender()
            anwender.set_user_id(id)
            anwender.set_name(name)
            anwender.set_benutzername(benutzername)
            anwender.set_email(email)
            result.append(anwender)

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

        for (id, name, benutzername, email) in tuples:
            anwender = Anwender()
            anwender.set_user_id(id)
            anwender.set_name(name)
            anwender.set_benutzername(benutzername)
            anwender.set_email(email)
            result.append(anwender)

        self._cnx.commit()
        cursor.close()

        return result

    def insert(self, anwender):
        """Einfügen eines Anwender-Objekts in die Datenbank."""

        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(user_id) as MAXID from anwender")
        tuples = cursor.fetchall()

        for (MAXID) in tuples:
            anwender.set_id(MAXID[0]+1)

        command = "INSERT INTO anwender (user_id, name, benutzername, email) VALUES ('{}','{}','{}','{}')"\
                .format(anwender.get_user_id(), anwender.get_name(), anwender.get_benutzername(), anwender.get_email())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()        
    
    def update(self, anwender):
        """Wiederholtes Schreiben eines Objekts in die Datenbank."""

        cursor = self._cnx.cursor()

        command = "UPDATE anwender SET name = ('{}'), benutzername = ('{}'), email = ('{}')" "WHERE user_id = ('{}')"\
                .format(anwender.get_name(), anwender.get_benutzername(), anwender.get_email(), anwender.get_user_id)
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

    def delete(self, anwender):
        """Löschen der Daten eines Anwenders-Objekts aus der Datenbank."""

        cursor = self._cnx.cursor()

        command = "DELETE FROM anwender WHERE id={}".format(anwender.get_user_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

"""
Testzwecke um uns die Daten anzeigen zu lassen

if __name__ == "__main__":
    with AnwenderMapper() as mapper:

        result = mapper.find_by_key(1)
        print(result.get_user_id())

"""