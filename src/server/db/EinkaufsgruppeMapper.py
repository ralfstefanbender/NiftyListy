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

        for (id, name, create_time) in tuples:
            einkaufsgruppe = Einkaufsgruppe()
            einkaufsgruppe.set_id(id)
            einkaufsgruppe.set_einkaufsgruppe_name(name)
            einkaufsgruppe.set_erstellungszeitpunkt(create_time)
            result.append(einkaufsgruppe)
        
        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, id):
        """Sucht die Einkaufsgruppe nach der eingegebenen ID aus"""

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT * FROM einkaufsgruppe WHERE id like '{}'".format(id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        if len (tuples) != 0:

            for (id, name, create_time) in tuples:
                einkaufsgruppe = Einkaufsgruppe()
                einkaufsgruppe.set_id(id)
                einkaufsgruppe.set_einkaufsgruppe_name(name)
                einkaufsgruppe.set_erstellungszeitpunkt(create_time)
                result.append(einkaufsgruppe)
        
            result = einkaufsgruppe
        
        else:

            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def insert(self, einkaufsgruppe):
        """Gruppe hinzufügen"""
        cursor = self._cnx.cursor()
        cursor.execute("SELECT Max(id) as MaxID from einkaufsgruppe")
        tuples = cursor.fetchall()

        for (MaxID) in tuples:
            einkaufsgruppe.set_id(MaxID[0]+1)

        command = "INSERT INTO einkaufsgruppe (id, name, create_time) VALUES ('{}','{}','{}')"\
                .format(einkaufsgruppe.get_id(), einkaufsgruppe.get_einkaufsgruppe_name(), einkaufsgruppe.get_erstellungszeitpunkt())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()  

    def update(self, einkaufsgruppe):
        """Wiederholtes Schreiben eines Objekts in die Datenbank."""

        cursor = self._cnx.cursor()

        command = "UPDATE einkaufsgruppe SET name = ('{}'), create_time = ('{}')" "WHERE id = ('{}')"\
                .format(einkaufsgruppe.get_einkaufsgruppe_name(), einkaufsgruppe.get_erstellungszeitpunkt(),einkaufsgruppe.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

    def delete(self, einkaufsgruppe):
        """Gruppe löschen"""

        cursor = self._cnx.cursor()

        command = "DELETE FROM einkaufsgruppe WHERE id = {}".format(einkaufsgruppe.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

"""Testzwecke um uns die Daten anzeigen zu lassen"""

if __name__ == "__main__":
    with EinkaufsgruppeMapper() as mapper:
        test = mapper.find_by_key(3)
        mapper.delete(test)
