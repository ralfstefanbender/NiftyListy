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
        cursor.execute("PLatzhalter für SQL Code")
        tuples = cursor.fetchall()

       """ for (id, owner) in tuples:
            account = Account()
            account.set_id(id)
            account.set_owner(owner)
            result.append(account) """
        
        """ Klare Definition der Rollenbetitelung fehlt  """

        self._cnx.commit()
        cursor.close()

        return result
    
    def find_by_key(self, user_ID):
        """Suchen eines Anwenders mit vorgegebener user ID

        result = []
        cursor = self._cnx.cursor()
        command = "PLatzhalter für SQL Code".format(Anwender_ID)
        cursor.execute(command)
        tuples = cursor.fetchall()

        self._cnx.commit()
        cursor.close()

        return result"""
        pass 

    def find_by_name(self, name):
        """Suchen eines Anwenders anhand des Anwendernames."""

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT name FROM anwender WHERE name like '{}'".format(name)
        cursor.execute(command)
        tuples = cursor.fetchall()

        self._cnx.commit()
        cursor.close()

        return result

    def insert(self, anwender):
        """Einfügen eines Anwender-Objekts in die Datenbank."""
        pass
    
    def update(self, object):
        """Wiederholtes Schreiben eines Objekts in die Datenbank."""
        pass

    def delete(self, object):
        """Löschen der Daten eines Anwenders-Objekts aus der Datenbank."""
        pass