from src.server.bo import BusinessObject
from src.server.bo import Anwender


class Einkaufsgruppe(BusinessObject):

    def __init__(self, einkaufsgruppe_name, teilnehmerliste = [], adminliste = []):
        self.__einkaufsgruppe_name = einkaufsgruppe_name
        self.__teilnehmerliste = teilnehmerliste
        self.__adminliste = adminliste

    def add_user(self, Anwender):
        self.__teilnehmerliste.extend(Anwender)

    def del_user(self,Anwender):
        self.__teilnehmerliste.remove(Anwender)

    def promote_to_admin(self,Anwender):
        self.__adminliste.append(Anwender)
        return

    def get_einkaufsgruppe_name(self):
        return self.__einkaufsgruppe_name

    def set_einkaufsgruppe_name(self,name):
        self.__einkaufsgruppe_name = name
        return
    pass
    