from src.server.bo.Einkaufsliste import Einkaufsliste
from src.server.db.Mapper import Mapper


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

        for (id, einkaufsgruppe_id, name, create_time) in tuples:
            einkaufsliste = Einkaufsliste()
            einkaufsliste.set_id(id)
            einkaufsliste.set_name(name)
            einkaufsliste.set_einkaufsgruppe(einkaufsgruppe_id)
            einkaufsliste.set_erstellungszeitpunkt(create_time)
            result.append(einkaufsliste)
        
        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, id):
        """Sucht die Einkaufsliste nach der eingegebenen Listen ID aus"""

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT * FROM einkaufsliste WHERE id like '{}'".format(id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        if len (tuples) != 0:

            for (id, einkaufsgruppen_id, name, create_time) in tuples:
                einkaufsliste = Einkaufsliste()
                einkaufsliste.set_id(id)
                einkaufsliste.set_einkaufsgruppe(einkaufsgruppen_id)
                einkaufsliste.set_name(name)
                einkaufsliste.set_erstellungszeitpunkt(create_time)
                result.append(einkaufsliste)

        result = einkaufsliste
        
        self._cnx.commit()
        cursor.close()

        return result

    def insert(self, einkaufsliste):
        """Liste hinzufügen"""

        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) as MaxID from einkaufsliste")
        tuples = cursor.fetchall()

        for (MaxID) in tuples:
            einkaufsliste.set_id(MaxID[0]+1)

        command = "INSERT INTO einkaufsliste (id, einkaufsgruppen_id, name, create_time) VALUES ('{}','{}','{}','{}')"\
                .format(einkaufsliste.get_id(), einkaufsliste.get_einkaufsgruppe(), einkaufsliste.get_name(), einkaufsliste.get_erstellungszeitpunkt())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()  

    def update(self, einkaufsliste):
        """Wiederholtes Schreiben eines Objekts in die Datenbank."""

        cursor = self._cnx.cursor()

        command = "UPDATE einkaufsliste SET name = ('{}'), create_time = ('{}'), einkaufsgruppen_id = ('{}')" "WHERE id = ('{}')"\
                .format(einkaufsliste.get_name(), einkaufsliste.get_erstellungszeitpunkt(), einkaufsliste.get_einkaufsgruppe(), einkaufsliste.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

    def delete(self, einkaufsliste):
        """Liste löschen"""

        cursor = self._cnx.cursor()

        command = "DELETE FROM einkaufsliste WHERE id={}".format(einkaufsliste.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

"""Testzwecke um uns die Daten anzeigen zu lassen"""

if __name__ == "__main__":
    with EinkaufslisteMapper() as mapper:
        liste = mapper.find_by_key(3)
        liste.set_einkaufsgruppe(1)
        mapper.update(liste)
