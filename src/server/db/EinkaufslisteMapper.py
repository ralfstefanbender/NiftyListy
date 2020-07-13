from server.bo.Einkaufsliste import Einkaufsliste
from server.db.Mapper import Mapper


class EinkaufslisteMapper (Mapper):
    """Mapper-Klasse, die Einkaufsliste-Objekte auf eine relationale
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
        command = "SELECT * FROM einkaufsliste"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, name) in tuples:
            einkaufsliste = Einkaufsliste()
            einkaufsliste.set_id(id)
            einkaufsliste.set_einkaufsliste_name(name)
            result.append(einkaufsliste)
        
        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, einkaufsliste_ID):
        """Sucht die Einkaufsliste nach der eingegebenen Listen ID aus"""

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT einkaufsliste_ID FROM einkaufsliste WHERE einkaufsliste_ID like '{}'".format(einkaufsliste_ID)
        cursor.execute(command)
        tuples = cursor.fetchall()
        
        self._cnx.commit()
        cursor.close()

        return result

    def insert(self, einkaufsliste):
        """Liste hinzufügen"""

        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) as MAXID from einkaufsliste")
        tuples = cursor.fetchall()

        for (MAXID) in tuples:
            einkaufsliste.set_id(MAXID[0]+1)

        command = "INSERT INTO einkaufsgruppe (einkaufsliste_id, name) VALUES ('{}','{}')"\
                .format(einkaufsliste.get_id(), einkaufsliste.get_name())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()  

    def update(self, einkaufsliste):
        """Wiederholtes Schreiben eines Objekts in die Datenbank."""

        cursor = self._cnx.cursor()

        command = "UPDATE einkaufsliste SET name = ('{}')" "WHERE einkaufsliste_id = ('{}')"\
                .format(einkaufsliste.get_name(), einkaufsliste.get_einkaufsliste_id)
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

    def delete(self, einkaufsliste):
        """Liste löschen"""

        cursor = self._cnx.cursor()

        command = "DELETE FROM einkaufsliste WHERE id={}".format(einkaufsliste.get_einkaufsliste_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

"""Testzwecke um uns die Daten anzeigen zu lassen

if __name__ == "__main__":
    with EinkaufslisteMapper() as mapper:
        result = mapper.find_all()
        for p in result:
            print(p)
"""