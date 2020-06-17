class Einkaufsliste:
    id = 0
    item_id = 0

    def __init__(self, name):
        self.__name = name
        self.__items = {}
        self.__id = Einkaufsliste.id
        Einkaufsliste.id += 1

    def get_items(self):
        return self.__items

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def add_item(self, item_id, menge, ticked=False):
        self.__items[Einkaufsliste.item_id] = [item_id, menge,  ticked]
        Einkaufsliste.item_id += 1

    def tick_item(self, item_id):
        if self.__items[item_id][2] is False:
            self.__items[item_id][2] = True
        else:
            self.__items[item_id][2] = False

    def change_menge_item(self, item_id, new_menge):
        self.__items[item_id][1] = new_menge

    def remove_item(self, item_id):
        del self.__items[item_id]

    def remove_ticked_items(self):
        new_dict = {}
        for i in self.__items:
            if self.__items[i][2] is False:
                new_dict[i] = self.__items[i]
        self.__items = new_dict

    def clear_list(self):
        self.__items = {}


def create_einkaufsliste(name):
    new_einkaufsliste = Einkaufsliste(name)
    all_einkaufslisten[new_einkaufsliste.get_id()] = new_einkaufsliste
