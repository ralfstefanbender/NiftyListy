from src.server.bo.BusinessObject import BusinessObject

class Einkaufsliste(BusinessObject):
    """
    Realisierung der Einkaufsliste
    """
    item_id = 0

    def __init__(self, name):
        super().__init__()
        self.__name = name
        self.__items = {}

    def get_items(self):
        """Auslesen der Items"""
        return self.__items

    def get_id(self):
        """Auslesen der ID"""
        return self.__id

    def get_name(self):
        """Auslesen des Namens"""
        return self.__name

    def set_name(self, new_name):
        """Änderung des Namens"""
        self.__name = new_name

    def add_item(self, item_id, menge, ticked=False):
        """Hinzufügen eines Items"""
        self.__items[Einkaufsliste.item_id] = [item_id, menge,  ticked]
        Einkaufsliste.item_id += 1

    def tick_item(self, item_id):
        """Abhaken eines Items"""
        if self.__items[item_id][2] is False:
            self.__items[item_id][2] = True
        else:
            self.__items[item_id][2] = False

    def change_menge_item(self, item_id, new_menge):
        """Änderung der Menge eines Items"""
        self.__items[item_id][1] = new_menge

    def remove_item(self, item_id):
        """Entfernen eines Items"""
        del self.__items[item_id]

    def remove_ticked_items(self):
        """Entfernen der abgehakten Items"""
        new_dict = {}
        for i in self.__items:
            if self.__items[i][2] is False:
                new_dict[i] = self.__items[i]
        self.__items = new_dict

    def clear_list(self):
        """Entfernen aller Items"""
        self.__items = {}

    @staticmethod
    def from_dict(dict):
        new_einkaufsliste = Einkaufsliste(dict["name"])
        return new_einkaufsliste