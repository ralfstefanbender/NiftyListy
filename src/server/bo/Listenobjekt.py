from src.server.bo.BusinessObject import BusinessObject

class Listenobjekt(BusinessObject):

    def __init__(self, parent_list, artikel_name, artikel_preis, menge, ticked=False):
        super().__init__()
        self.__parent_list = parent_list
        self.__artikel_name = artikel_name
        self.__artikel_preis = artikel_preis
        self.__menge = menge
        self.__ticked = ticked

    def get_parent_list():
        return self.__parent_list

    def get_artikel_name():
        return self.__artikel_name

    def get_artikel_preis():
        return self.__artikel_preis

    def get_menge():
        return self.__menge

    def get_ticked():
        return self.__ticked

    def set_parent_list(parent):
        self.__parent_list = parent

    def set_artikel_name(name):
        self.__artikel_name = name

    def set_artikel_preis(preis):
        self.__artikel_preis = preis

    def set_menge(menge):
        self.__menge = menge

    def set_ticked(ticked):
        self.__ticked = ticked

    def tick_item():
        if self.__ticked is False:
            self.__ticked = True
        else:
            self.__ticked = False

    @staticmethod
    def from_dict(dict):
        new_listenobjekt = Listenobjekt(dict["parent_list"], dict["artikel_name"], dict["artikel_preis"], dict["menge"], dict["ticked"])
        return new_listenobjekt
