from server.bo.Einkaufsgruppe import Einkaufsgruppe
from server.db.Mapper import Mapper


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
        
        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, einkaufsgruppe_ID):
        """Sucht die Einkaufsgruppe nach der eingegebenen ID aus"""

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT einkaufsgruppe_ID FROM einkaufsgruppe WHERE einkaufsgruppe_ID like '{}'".format(einkaufsgruppe_ID)
        cursor.execute(command)
        tuples = cursor.fetchall()
        
        self._cnx.commit()
        cursor.close()

        return result

    def insert(self, einkaufsgruppe):
        """Gruppe hinzufügen"""
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) as MAXID from einkaufsgruppe")
        tuples = cursor.fetchall()

        for (MAXID) in tuples:
            einkaufsgruppe.set_id(MAXID[0]+1)

        command = "INSERT INTO einkaufsgruppe (einkaufsgruppe_id, name) VALUES ('{}','{}')"\
                .format(einkaufsgruppe.get_id(), einkaufsgruppe.get_name())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()  

    def update(self, einkaufsgruppe):
        """Wiederholtes Schreiben eines Objekts in die Datenbank."""

        cursor = self._cnx.cursor()

        command = "UPDATE einkaufsgruppe SET name = ('{}')" "WHERE einkaufsgruppe_id = ('{}')"\
                .format(einkaufsgruppe.get_name(), einkaufsgruppe.get_artikel_id)
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

    def delete(self, einkaufsgruppe):
        """Gruppe löschen"""

        cursor = self._cnx.cursor()

        command = "DELETE FROM einkaufsgruppe WHERE id={}".format(einkaufsgruppe.get_artikel_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

"""Testzwecke um uns die Daten anzeigen zu lassen"""

if __name__ == "__main__":
    with EinkaufsgruppeMapper() as mapper:
        result = mapper.find_all()
        for p in result:
            print(p)