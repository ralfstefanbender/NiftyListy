from src.server.bo.Einkaufsgruppe import Einkaufsgruppe
from src.server.db.Mapper import Mapper


class EinkaufsgruppeMapper (Mapper):
    """Mapper-Klasse, die Einkaufsgruppe-Objekte auf eine relationale
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
        command = "SELECT * FROM einkaufsgruppe"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, name, create_time, teilnehmerliste, artikelliste) in tuples:
            einkaufsgruppe = Einkaufsgruppe()
            einkaufsgruppe.set_id(id)
            einkaufsgruppe.set_einkaufsgruppe_name(name)
            einkaufsgruppe.set_erstellungszeitpunkt(create_time)
            einkaufsgruppe.set_teilnehmerliste(teilnehmerliste)
            einkaufsgruppe.set_artikelliste(artikelliste)
            result.append(einkaufsgruppe)
        
        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, einkaufsgruppe_id):
        """Sucht die Einkaufsgruppe nach der eingegebenen ID aus"""

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT einkaufsgruppe_id FROM einkaufsgruppe WHERE einkaufsgruppe_id like '{}'".format(einkaufsgruppe_id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        if len (tuples) != 0:

            for (id, name, create_time, teilnehmerliste, artikelliste) in tuples:
                einkaufsgruppe = Einkaufsgruppe()
                einkaufsgruppe.set_id(id)
                einkaufsgruppe.set_einkaufsgruppe_name(name)
                einkaufsgruppe.set_erstellungszeitpunkt(create_time)
                einkaufsgruppe.set_teilnehmerliste(teilnehmerliste)
                einkaufsgruppe.set_artikelliste(artikelliste)
                result.append(einkaufsgruppe)
        
        result = einkaufsgruppe
        
        self._cnx.commit()
        cursor.close()

        return result

    def insert(self, einkaufsgruppe):
        """Gruppe hinzufügen"""
        cursor = self._cnx.cursor()
        cursor.execute("SELECT Max(einkaufsgruppe_id) as MaxID from einkaufsgruppe")
        tuples = cursor.fetchall()

        for (MaxID) in tuples:
            einkaufsgruppe.set_id(MaxID[0]+1)

        command = "INSERT INTO einkaufsgruppe (einkaufsgruppe_id, einkaufsgruppe_name, create_time, teilnehmerliste, artikelliste) VALUES ('{}','{}','{}','{}','{}')"\
                .format(einkaufsgruppe.get_id(), einkaufsgruppe.get_name(), einkaufsgruppe.get_erstellungszeitpunkt, einkaufsgruppe.get_teilnehmerliste, einkaufsgruppe.get_artikelliste)
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()  

    def update(self, einkaufsgruppe):
        """Wiederholtes Schreiben eines Objekts in die Datenbank."""

        cursor = self._cnx.cursor()

        command = "UPDATE einkaufsgruppe SET einkaufsgruppe_name = ('{}'), einkaufsgruppe_create_time = ('{}'), einkaufsgruppe_teilnehmerliste = ('{}'), einkaufsgruppe_artikelliste = ('{}')" "WHERE einkaufsgruppe_id = ('{}')"\
                .format(einkaufsgruppe.get_name(), einkaufsgruppe.get_id, einkaufsgruppe.get_create_time, einkaufsgruppe.get_teilnehmerliste, einkaufsgruppe.get_artikelliste)
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

    def delete(self, einkaufsgruppe):
        """Gruppe löschen"""

        cursor = self._cnx.cursor()

        command = "DELETE FROM einkaufsgruppe WHERE einkaufsgruppe_id = {}".format(einkaufsgruppe.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

"""Testzwecke um uns die Daten anzeigen zu lassen"""

if __name__ == "__main__":
    with EinkaufsgruppeMapper() as mapper:
        result = mapper.find_all()
        for p in result:
            print(p.get_einkaufsgruppe_name)