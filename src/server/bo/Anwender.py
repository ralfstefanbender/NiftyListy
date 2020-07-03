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

