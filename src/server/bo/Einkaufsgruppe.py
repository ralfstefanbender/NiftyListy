from src.server.bo import BusinessObject
from src.server.bo import Anwender


class Einkaufsgruppe(BusinessObject):
    """
    Realisierung der Einkaufsgruppe
    """
    def __init__(self, einkaufsgruppe_name, teilnehmerliste = [], artikelliste =[]):
        super().__init__()
        self.__einkaufsgruppe_name = einkaufsgruppe_name
        self.__teilnehmerliste = teilnehmerliste
        self.artikelliste = artikelliste

    def add_user(self, Anwender):
        """Hinzufügen eines Users"""
        self.__teilnehmerliste.extend(Anwender)

    def del_user(self,Anwender):
        """Löschen eines Users"""
        self.__teilnehmerliste.remove(Anwender)

    def get_einkaufsgruppe_name(self):
        """Auslesen des Gruppennamens"""
        return self.__einkaufsgruppe_name

    def set_einkaufsgruppe_name(self,name):
        """Gruppennamen ändern"""
        self.__einkaufsgruppe_name = name
        return

    