from src.server.bo.Listenobjekt import Listenobjekt
from src.server.db.Mapper import Mapper


class ListenobjektMapper (Mapper):
    """Mapper-Klasse, die Listenobjekte auf eine relationale
    Datenbank abbildet. Hierzu wird eine Reihe von Methoden zur Verfügung
    gestellt, mit deren Hilfe z.B. Objekte gesucht, erzeugt, modifiziert und
    gelöscht werden können. Das Mapping ist bidirektional. D.h., Objekte können
    in DB-Strukturen und DB-Strukturen in Objekte umgewandelt werden.
    """

    def __init__(self):
        super().__init__()

    def find_all(self):

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT * FROM listenobjekt"
        cursor.execute(command)
        tuples = cursor.fetchall()
        
        for (id) in tuples:
            listenobjekt = Listenobjekt()
            listenobjekt.set_id(id)
            listenobjekt.set_id(id)
            listenobjekt.set_id(id)
            listenobjekt.set_artikel_preis(preis)
            listenobjekt.set_menge(menge)
            listenobjekt.set_ticked(ticked)
            result.append(listenobjekt)

        self._cnx.commit()
        cursor.close()

        return result 
    
    def find_by_key(self, id):
        
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT * FROM listenobjekt WHERE id like '{}'".format(id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id) in tuples:
            listenobjekt = Listenobjekt()
            listenobjekt.set_id(id)
            listenobjekt.set_id(id)
            listenobjekt.set_id(id)
            listenobjekt.set_artikel_preis(preis)
            listenobjekt.set_menge(menge)
            listenobjekt.set_ticked(ticked)
            result.append(listenobjekt)
        
        self._cnx.commit()
        cursor.close()

        return result

    def find_by_name(self, name):
    
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT name FROM listenobjekt WHERE name like '{}'".format(name)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id) in tuples:
            listenobjekt = Listenobjekt()
            listenobjekt.set_id(id)
            listenobjekt.set_id(id)
            listenobjekt.set_id(id)
            listenobjekt.set_artikel_preis(preis)
            listenobjekt.set_menge(menge)
            listenobjekt.set_ticked(ticked)
            result.append(listenobjekt)

        self._cnx.commit()
        cursor.close()

        return result    

    def insert(self, listenobjekt):
        
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) as MAXID from listenobjekt")
        tuples = cursor.fetchall()

        for (MAXID) in tuples:
            listenobjekt.set_id(MAXID[0]+1)

        command = "INSERT INTO listenobjekt (id, name) VALUES ('{}','{}')"\
                .format(listenobjekt.get_id(), listenobjekt.get_name())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
    
    def update(self, listenobjekt):
        
        cursor = self._cnx.cursor()

        command = "UPDATE listenobjekt SET name = ('{}')" "WHERE id = ('{}')"\
                .format(listenobjekt.get_name(), listenobjekt.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

    def delete(self, listenobjekt):

        cursor = self._cnx.cursor()

        command = "DELETE FROM listenobjekt WHERE id={}".format(listenobjekt.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

"""Testzwecke um uns die Daten anzeigen zu lassen

if __name__ == "__main__":
    with ListenobjektMapper() as mapper:
        result = mapper.find_all()
        for p in result:
            print(p)
"""