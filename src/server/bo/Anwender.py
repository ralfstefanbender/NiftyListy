from src.server.bo import BusinessObject


class Anwender(BusinessObject):
    """
    Realisierung der Anwender
    """
    def __init__(self):
        super().__init__()
        self.__benutzername = ""
        self.__email = ""
        self.__google_id = ""

    def set_benutzername(self, benutzername):
        """Setzen des Benutzernamens"""
        self.__benutzername = benutzername

    def get_benutzername(self):
        """Auslesen des Benutzernames"""
        return self.__benutzername

    def set_email(self, email):
        """Setzen der E-Mail"""
        self.__email = email

    def get_email(self):
        """Auslesen der E-Mail"""
        return self.__email

    def set_google_id(self, id):
        """Setzen der User ID"""
        self.__google_id = id

    def get_google_id(self):
        """Auslesen der User ID"""
        return self.__google_id


    @staticmethod
    def from_dict(dict = dict()):
        """Umwandeln eines Python dict() in einen listentry()"""
        new_anwender = Anwender()
        new_anwender.set_id(dict["id"])
        new_anwender.set_google_id()_id(dict["google_id"])
        new_anwender.set_benutzername(dict["benutzername"])
        new_anwender.set_email(dict["email"])
        return new_anwender

