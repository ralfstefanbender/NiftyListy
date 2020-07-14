from src.server.bo import BusinessObject
from src.server.bo import Anwender


class Einkaufsgruppe(BusinessObject):
    """
    Realisierung der Einkaufsgruppe
    """
    def __init__(self):
        super().__init__()
        self.__einkaufsgruppe_name = ""

    def get_einkaufsgruppe_name(self):
        """Auslesen des Gruppennamens"""
        return self.__einkaufsgruppe_name

    def set_einkaufsgruppe_name(self,name):
        """Gruppennamen ändern"""
        self.__einkaufsgruppe_name = name
        return

    @staticmethod
    def from_dict(dict):
        new_einkaufsgruppe = Einkaufsgruppe()
        new_einkaufsgruppe.set_id(dict["id"])
        new_einkaufsgruppe.set_einkaufsgruppe_name(dict["name"])
        return new_einkaufsgruppe
