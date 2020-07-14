from src.server.bo.BusinessObject import BusinessObject

class Einkaufsliste(BusinessObject):
    """
    Realisierung der Einkaufsliste
    """
    def __init__(self):
        super().__init__()
        self.__name = ""
        self.__einkaufsgruppe_id = None

    def get_name(self):
        """Auslesen des Namens"""
        return self.__name

    def set_name(self, new_name):
        """Änderung des Namens"""
        self.__name = new_name

    def set_einkaufsgruppe(self,einkaufsgruppe_id):
        self.__einkaufsgruppe_id = einkaufsgruppe_id

    def get_einkaufsgruppe(self):
        return self.__einkaufsgruppe_id

    @staticmethod
    def from_dict(dict):
        new_einkaufsliste = Einkaufsliste()
        new_einkaufsliste.set_id(dict["id"])
        new_einkaufsliste.set_name(dict["name"])
        new_einkaufsliste.set_einkaufsgruppe(dict["einkaufsgruppe_id"])
        return new_einkaufsliste