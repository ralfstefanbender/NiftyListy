from server.bo.Listenobjekt import Listenobjekt
from server.db.Mapper import Mapper


class ListenobjektMapper (Mapper):


    def __init__(self):
        super().__init__()

    def find_all(self):

        result = []
        cursor = self._cnx.cursor()
        command = "SELECT * FROM listenobjekt"
        cursor.execute(command)
        tuples = cursor.fetchall()
        
        self._cnx.commit()
        cursor.close()

        return result 
    
    def find_by_key(self, listenobjekt_ID):
        
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT listenobjekt_ID FROM listenobjekt WHERE listenobjekt_ID like '{}'".format(listenobjekt_ID)
        cursor.execute(command)
        tuples = cursor.fetchall()
        
        self._cnx.commit()
        cursor.close()

        return result

    def find_by_name(self, name):
    
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT name FROM listenobjekt WHERE name like '{}'".format(name)
        cursor.execute(command)
        tuples = cursor.fetchall()

        self._cnx.commit()
        cursor.close()

        return result    

    def insert(self, listenobjekt):
        
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) as MAXID from listenobjekt")
        tuples = cursor.fetchall()

        for (MAXID) in tuples:
            listenobjekt.set_id(MAXID[0]+1)

        command = "INSERT INTO listenobjekt (listenobjekt_id, name) VALUES ('{}','{}')"\
                .format(listenobjekt.get_id(), listenobjekt.get_name())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
    
    def update(self, listenobjekt):
        
        cursor = self._cnx.cursor()

        command = "UPDATE listenobjekt SET name = ('{}')" "WHERE listenobjekt_id = ('{}')"\
                .format(listenobjekt.get_name(), listenobjekt.get_listenobjekt_id)
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

    def delete(self, listenobjekt):

        cursor = self._cnx.cursor()

        command = "DELETE FROM listenobjekt WHERE id={}".format(listenobjekt.get_händler_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

"""Testzwecke um uns die Daten anzeigen zu lassen"""

if __name__ == "__main__":
    with ListenobjektMapper() as mapper:
        result = mapper.find_all()
        for p in result:
            print(p)