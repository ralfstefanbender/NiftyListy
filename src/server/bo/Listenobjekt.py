from src.server.bo.BusinessObject import BusinessObject

class Listenobjekt(BusinessObject):

    def __init__(self):
        super().__init__()
        self._parent_list = 0
        self._user_id = 0
        self._artikel_id = 0
        self._einzelhändler_id = 0
        self._menge = 0
        self._ticked = 0
        self._artikel_preis = 0

    def get_artikel_preis(self):
        return self._artikel_preis

    def set_artikel_preis(self, preis):
        self._artikel_preis = preis

    def get_parent_list(self):
        return self._parent_list

    def set_parent_list(self,parent):
        self._parent_list = parent

    def get_user_id(self):
        return self._user_id

    def set_user_id(self,user_id):
        self._user_id = user_id

    def get_artikel_id(self):
        return self._artikel_id

    def set_artikel_id(self,artikel_id):
        self._artikel_id = artikel_id

    def get_einzelhändler_id(self):
        return self._einzelhändler_id

    def set_einzelhändler_id(self, einzelhändler_id):
        self._einzelhändler_id = einzelhändler_id

    def get_menge(self):
        return self._menge

    def set_menge(self, menge):
        self._menge = menge

    def get_ticked(self):
        return self._ticked

    def set_ticked(self, ticked):
        self._ticked = ticked


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
