from src.server.bo.BusinessObject import BusinessObject


all_Artikel = {}

class Artikel(BusinessObject):
    """
    Realisierung der Artikel
    """
    def __init__(self, name, einheit):
        super().__init__()
        self.__name = name
        self.__einheit = einheit

    def get_name(self):
        """Auslesen des Namens"""
        return self.__name

    def get_einheit(self):
        """Auslesen der Einheit"""
        return self.__einheit

    def set_name(self, new_name):
        """Setzen des Namens"""
        self.__name = new_name

    def set_einheit(self, new_einheit):
        """Setzen der Einheit"""
        self.__einheit = new_einheit

    @staticmethod
    def from_dict(dict):
        new_artikel = Artikel(dict["name"], dict["einheit"])
        return new_artikel
        





