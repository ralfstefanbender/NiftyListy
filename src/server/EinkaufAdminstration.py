from .bo.Anwender import Anwender
from .bo.Artikel import Artikel
from .bo.Einkaufsgruppe import Einkaufsgruppe
from .bo.Einkaufsliste import Einkaufsliste
from .bo.Einzelhändler import Einzelhändler

from .DB.Mapper import Mapper
from .DB.AnwenderMapper import AnwenderMapper
from .DB.EinkaufsgruppeMapper import EinkaufsgruppeMapper
from .DB.ArtikelMapper import ArtikelMapper

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
