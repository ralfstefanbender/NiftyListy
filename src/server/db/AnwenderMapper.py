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

        def auslesen(self):

        result = []
        cursor = self._cnx.cursor()
        cursor.execute("Wählen sie eine ID aus")
        tuples = cursor.fetchall()

       """ for (id, owner) in tuples:
            account = Account()
            account.set_id(id)
            account.set_owner(owner)
            result.append(account) """

        self._cnx.commit()
        cursor.close()

        return result
