from src.server.bo.BusinessObject import BusinessObject


class Artikel(BusinessObject):

    def __init__(self, name, einheit):
        self.__name = name
        self.__einheit = einheit

    def get_name(self):
        return self.__name

    def get_einheit(self):
        return self.__einheit

    def set_name(self, new_name):
        self.__name = new_name

    def set_einheit(self, new_einheit):
        self.__einheit = new_einheit


    def create_artikel(name, einheit="Stk"):
        new_artikel = Artikel(name, einheit)
        all_Artikel[new_artikel.get_id()] = new_artikel





