from src.server.bo.BusinessObject import BusinessObject

class Listenobjekt(BusinessObject):

    def __init__(self):
        super().__init__()
        self.__parent_list = 0
        self.__user_id = 0
        self.__artikel_id = 0
        self.einzelhändler_id = 0
        self.__artikel_preis = 0
        self.__menge = 0
        self.__ticked = 0

    def get_parent_list(self):
        return self.__parent_list

    def set_parent_list(parent):
        self.__parent_list = parent

    def get_user_id(self):
        return self.__user_id

    def set_user_id(self,user_id):
        self.__user_id = user_id

    def get_artikel_id(self):
        return self.__artikel_id

    def set_artikel_id(self,artikel_id):
        self.__artikel_id = artikel_id

    def get_einzelhändler_id(self):
        return self.einzelhändler_id

    def set_einzelhändler_id(self,einzelhändler_id):
        self.einzelhändler_id = einzelhändler_id

    def get_artikel_preis():
        return self.__artikel_preis

    def set_artikel_preis(preis):
        self.__artikel_preis = preis

    def get_menge(self):
        return self.__menge

    def set_menge(self, menge):
        self.__menge = menge

    def get_ticked(self):
        return self.__ticked

    def set_ticked(self, ticked):
        self.__ticked = ticked


    @staticmethod
    def from_dict(dict):
        new_listenobjekt = Listenobjekt()
        new_listenobjekt.set_id(dict["id"])
        new_listenobjekt.set_parent_list(dict["parent_list"])
        new_listenobjekt.set_user_id(dict["user_id"])
        new_listenobjekt.set_artikel_id(dict["artikel"])
        new_listenobjekt.set_einzelhändler_id(dict["einzelhändler"])
        new_listenobjekt.set_artikel_preis(dict["artikel_preis"])
        new_listenobjekt.set_menge(dict["menge"])
        new_listenobjekt.set_ticked(dict["ticked"])
        return new_listenobjekt
