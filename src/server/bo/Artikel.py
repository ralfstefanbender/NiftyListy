from src.server.bo.BusinessObject import BusinessObject


class Artikel(BusinessObject):
    """
    Realisierung der Artikel
    """
    def __init__(self):
        super().__init__()
        self.__name = ""
        self.__einheit = ""

    def get_name(self):
        """Auslesen des Namens"""
        return self.__name

    def set_name(self, new_name):
        """Setzen des Namens"""
        self.__name = new_name

    def get_einheit(self):
        """Auslesen der Einheit"""
        return self.__einheit

    def set_einheit(self, new_einheit):
        """Setzen der Einheit"""
        self.__einheit = new_einheit

    @staticmethod
    def from_dict(dict = dict()):
        new_artikel = Artikel()
        new_artikel.set_id(dict["id"])
        new_artikel.set_name(dict["name"])
        new_artikel.set_einheit(dict["einheit"])
        return new_artikel
        





