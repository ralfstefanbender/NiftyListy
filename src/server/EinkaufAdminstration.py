from src.server.bo.Anwender import Anwender
from src.server.bo.Artikel import Artikel
from src.server.bo.Einkaufsgruppe import Einkaufsgruppe
from src.server.bo.Einkaufsliste import Einkaufsliste
from src.server.bo.Einzelhändler import Einzelhändler

from src.server.db.Mapper import Mapper
from src.server.db.AnwenderMapper import AnwenderMapper
from src.server.db.EinkaufsgruppeMapper import EinkaufsgruppeMapper
from src.server.db.ArtikelMapper import ArtikelMapper
from src.server.db.EinkaufslisteMapper import EinkaufslisteMapper


class EinkaufAdministration (object):
    """Diese Klasse aggregiert nahezu sämtliche Applikationslogik (engl. Business Logic).

    Sie ist wie eine Spinne, die sämtliche Zusammenhänge in ihrem Netz (in unserem
    Fall die Daten der Applikation) überblickt und für einen geordneten Ablauf und
    dauerhafte Konsistenz der Daten und Abläufe sorgt.

    Die Applikationslogik findet sich in den Methoden dieser Klasse. Jede dieser
    Methoden kann als *Transaction Script* bezeichnet werden. Dieser Name
    lässt schon vermuten, dass hier analog zu Datenbanktransaktion pro
    Transaktion gleiche mehrere Teilaktionen durchgeführt werden, die das System
    von einem konsistenten Zustand in einen anderen, auch wieder konsistenten
    Zustand überführen. Wenn dies zwischenzeitig scheitern sollte, dann ist das
    jeweilige Transaction Script dafür verwantwortlich, eine Fehlerbehandlung
    durchzuführen.

    Diese Klasse steht mit einer Reihe weiterer Datentypen in Verbindung. Dies
    sind:
    - die Klassen BusinessObject und deren Subklassen,
    - die Mapper-Klassen für den DB-Zugriff."""

def __init__(self):
    pass

def get_all_lists(slef):
    """Hier sollen alle unsere Listen ausgelesen werden"""
    with EinkaufslisteMapper() as mapper:
        return mapper.find_all()

"""Administration muss auf den neusten Stand gebracht werden"""