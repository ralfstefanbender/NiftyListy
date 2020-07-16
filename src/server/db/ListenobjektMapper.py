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
        
        for (id, artikel_id, einzelhändler_id, Menge, Gekauft, create_time, anwender_id,einkaufsliste_id) in tuples:
            listenobjekt = Listenobjekt()
            listenobjekt.set_id(id)
            listenobjekt.set_artikel_id(artikel_id)
            listenobjekt.set_einzelhändler_id(einzelhändler_id)
            listenobjekt.set_menge(Menge)
            listenobjekt.set_ticked(Gekauft)
            listenobjekt.set_erstellungszeitpunkt(create_time)
            listenobjekt.set_user_id(anwender_id)
            listenobjekt.set_parent_list(einkaufsliste_id)
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

        if len (tuples) != 0:

            for (id, artikel_id, einzelhändler_id, Menge, Gekauft, create_time, anwender_id,einkaufsliste_id) in tuples:
                listenobjekt = Listenobjekt()
                listenobjekt.set_id(id)
                listenobjekt.set_artikel_id(artikel_id)
                listenobjekt.set_einzelhändler_id(einzelhändler_id)
                listenobjekt.set_menge(Menge)
                listenobjekt.set_ticked(Gekauft)
                listenobjekt.set_erstellungszeitpunkt(create_time)
                listenobjekt.set_user_id(anwender_id)
                listenobjekt.set_parent_list(einkaufsliste_id)
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

        command = "INSERT INTO listenobjekt (id, artikel_id, einzelhändler_id, Menge, Gekauft, create_time, anwender_id,einkaufsliste_id) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}')"\
                .format(listenobjekt.get_id(), listenobjekt.get_artikel_id(),listenobjekt.get_einzelhändler_id(), listenobjekt.get_menge(),listenobjekt.get_ticked(),listenobjekt.get_erstellungszeitpunkt(), listenobjekt.get_user_id(), listenobjekt.get_parent_list())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
    
    def update(self, listenobjekt):
        
        cursor = self._cnx.cursor()

        command = "UPDATE listenobjekt SET  artikel_id = ('{}'), einzelhändler_id = ('{}') ,Menge = ('{}'), Gekauft = ('{}'), create_time = ('{}'), anwender_id = ('{}'), einkaufsliste_id = ('{}')" "WHERE id = ('{}')"\
                .format( listenobjekt.get_artikel_id(), listenobjekt.get_einzelhändler_id(), listenobjekt.get_menge(), listenobjekt.get_ticked(), listenobjekt.get_erstellungszeitpunkt(), listenobjekt.get_user_id(), listenobjekt.get_parent_list(), listenobjekt.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

    def delete(self, listenobjekt):

        cursor = self._cnx.cursor()

        command = "DELETE FROM listenobjekt WHERE id={}".format(listenobjekt.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

#Testzwecke um uns die Daten anzeigen zu lassen

if __name__ == "__main__":
    with ListenobjektMapper() as mapper:
        result = mapper.find_all()
        hallo = mapper.find_by_key(113)
        hallo[0].set_user_id(10)
        mapper.update(hallo[0])
        for p in result:
            print(p.get_menge())




