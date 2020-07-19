from src.server.bo.BusinessObject import BusinessObject

class Einzelhändler(BusinessObject):
    """
    Realisierung der Einzelhändler
    """

    def __init__(self):
        super().__init__()
        self._name = ""

    def get_name(self):
        """Auslesen des Einzelhändlernamens"""
        return self._name

    def set_name(self, new_name):
        """Ändern des Einzelhändlernamens"""
        self._name = new_name

    @staticmethod
    def from_dict(dict=dict()):
        new_einzelhaendler = Einzelhändler()
        new_einzelhaendler.set_id(dict["id"])
        new_einzelhaendler.set_name(dict["name"])
        return new_einzelhaendler
        


