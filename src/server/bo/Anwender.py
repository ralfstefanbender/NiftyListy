from src.server.bo import BusinessObject as bo


class Anwender(bo.BusinessObject):
    """
    Realisierung der Anwender
    """
    def __init__(self):
        super().__init__()
        self._benutzername = ""
        self._email = ""
        self._google_id = ""

    def set_benutzername(self, benutzername):
        """Setzen des Benutzernamens"""
        self._benutzername = benutzername

    def get_benutzername(self):
        """Auslesen des Benutzernames"""
        return self._benutzername

    def set_email(self, email):
        """Setzen der E-Mail"""
        self._email = email

    def get_email(self):
        """Auslesen der E-Mail"""
        return self._email

    def set_google_id(self, id):
        """Setzen der User ID"""
        self._google_id = id

    def get_google_id(self):
        """Auslesen der User ID"""
        return self._google_id


    @staticmethod
    def from_dict(dict = dict()):
        """Umwandeln eines Python dict() in einen listentry()"""
        new_anwender = Anwender()
        new_anwender.set_id(dict["id"])
        new_anwender.set_google_id(dict["google_id"])
        new_anwender.set_benutzername(dict["benutzername"])
        new_anwender.set_email(dict["email"])
        return new_anwender

