from src.server.bo import BusinessObject


class Anwender(BusinessObject):
    """
    Realisierung der Anwender
    """
    def __init__(self, benutzername,admin=False):
        super().__init__()
        self.__benutzername = benutzername
        self.__admin = admin

    def set_benutzername(self, benutzername):
        """Setzen des Benutzernamens"""
        self.__benutzername = benutzername
        return

    def get_benutzername(self):
        """Auslesen des Benutzernames"""
        return self.__benutzername

    def set_admin(self):
        """Setzen des Admin-Status"""
        self.__admin = True
        return

    @staticmethod
    def from_dict(dict):
        new_anwender = Anwender(dict["benutzername"])
        new_anwender.set_id(dict["id"])
        if dict["admin"] is True:
            new_anwender.set_admin()
        return new_anwender
