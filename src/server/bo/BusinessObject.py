from abc import ABC, abstractmethod

class BusinessObject(ABC):
    """Definiert die Basisklasse des Projekts und die Mindestfunktionaöität aller Business-Objekte.
       Jedes BusinessObject besitzt eine ID welche als Primärschlüssel in der relationalen
       Datenbank genutzt wird und eine Erstellungszeitpunkt
    """
    def __init__(self):
        self._id = 0  # eindeutige Identifikationsnummer einer Instanz dieser Klasse.
        self._erstellungszeitpunkt

    def get_id(self):
        """Auslesen der ID."""
        return self._id

    def set_id(self, value):
        """Setzen der ID."""
        self._id = value

    def get_erstellungszeitpunkt(self):
        """Auslesen des Erstellungszeitpunkt"""
        return self.erstellungszeitpunkt()



