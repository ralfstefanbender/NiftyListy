from src.server.bo.BusinessObject import BusinessObject


class Zugehörigkeit(BusinessObject):
    """
    Realisierung der Zugehörigkeit zwischen Einkaufsgruppe und Anwender
    """
    def __init__(self):
        super().__init__()
        self.__anwender_id = None
        self.__einkaufsgruppe_id = None

    def get_anwender_id(self):
        return self.__anwender_id

    def set_anwender_id(self, anwender_id):
        self.__anwender_id = anwender_id

    def get_einkaufsgruppe_id(self):
        return self.__einkaufsgruppe_id

    def set_einkaufsgruppe_id(self, einkaufsgruppe_id):
        self.__einkaufsgruppe_id = einkaufsgruppe_id

    @staticmethod
    def from_dict(dict = dict()):
        new_zugehörigkeit = Zugehörigkeit()
        new_zugehörigkeit.set_id(dict["id"])
        new_zugehörigkeit.set_anwender_id(dict["anwender_id"])
        new_zugehörigkeit.set_einkaufsgruppe_id(dict["einkaufsgruppe_id"])
        return new_zugehörigkeit