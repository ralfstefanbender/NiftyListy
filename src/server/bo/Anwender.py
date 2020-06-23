from src.server.bo import BusinessObject


class Anwender(BusinessObject):

    def __init__(self, benutzername,admin=False):
        self.__benutzername = benutzername
        self.__admin = admin

    def set_benutzername(self, benutzername):
        self.__benutzername = benutzername
        return

    def get_benutzername(self):
        return self.__benutzername

    def set_admin(self):
        self.__admin = True
        return

    pass