from abc import ABC, abstractmethod
from datetime import datetime

class BusinessObject(ABC):
    """
    Definiert die Basisklasse des Projekts und die Mindestfunktionalität aller Business-Objekte.
    Jedes BusinessObject besitzt eine ID welche als Primärschlüssel in der relationalen
    Datenbank genutzt wird und einen Erstellungszeitpunkt
    """
    def __init__(self):
        self._id = 0  # eindeutige Identifikationsnummer einer Instanz dieser Klasse.
        self._erstellungszeitpunkt = datetime.now()

    def get_id(self):
        """Auslesen der ID."""
        return self._id

    def set_id(self, value):
        """Setzen der ID."""
        self._id = value

    def get_erstellungszeitpunkt(self):
        """Auslesen des Erstellungszeitpunkts"""
        return self._erstellungszeitpunkt

    def set_erstellungszeitpunkt(self, date):
        """Auslesen des Erstellungszeitpunkt"""
        self._erstellungszeitpunkt = date



