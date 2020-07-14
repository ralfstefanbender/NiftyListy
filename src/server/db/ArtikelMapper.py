from src.server.bo.Artikel import Artikel
from src.server.db.Mapper import Mapper


class ArtikelMapper (Mapper):
    """Mapper-Klasse, die Artikel-Objekte auf eine relationale
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
        command = "SELECT * FROM artikel"
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, name) in tuples:
            artikel = Artikel()
            artikel.set_artikel_id(id)
            artikel.set_name(name)
            result.append(artikel)
        
        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, artikel_ID):
        """Sucht die Artikel nach der eingegebenen ID aus"""

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT artikel_ID FROM artikel WHERE artikel_ID like '{}'".format(artikel_ID)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, name) in tuples:
            artikel = Artikel()
            artikel.set_artikel_id(id)
            artikel.set_name(name)
            result.append(artikel)
        
        self._cnx.commit()
        cursor.close()

        return result

    def insert(self, artikel):
        """Artikel hinzufügen"""

        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(artikel_id) as MAXID from artikel")
        tuples = cursor.fetchall()

        for (MAXID) in tuples:
            Artikel.set_id(MAXID[0]+1)

        command = "INSERT INTO artikel (artikel_id, name) VALUES ('{}','{}')"\
                .format(artikel.get_artikel_id(), artikel.get_name())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()  

    def update(self, artikel):
        """Wiederholtes Schreiben eines Objekts in die Datenbank."""
        cursor = self._cnx.cursor()

        command = "UPDATE artikel SET name = ('{}')" "WHERE artikel_id = ('{}')"\
                .format(artikel.get_name(), artikel.get_artikel_id)
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

    def delete(self, artikel):
        """Artikel löschen"""

        cursor = self._cnx.cursor()

        command = "DELETE FROM artikel WHERE id={}".format(artikel.get_artikel_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

"""Testzwecke um uns die Daten anzeigen zu lassen

if __name__ == "__main__":
    with ArtikelMapper() as mapper:
        result = mapper.find_all()
        for p in result:
            print(p)
"""