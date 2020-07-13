from server.bo.Listenobjekt import Einzelhändler
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
        
        pass

    def insert(self, anwender):
        
        pass
    
    def update(self, object):
        
        pass

    def delete(self, object):

        pass