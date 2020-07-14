from src.server.bo.Anwender import Anwender
from src.server.bo.Artikel import Artikel
from src.server.bo.Einkaufsgruppe import Einkaufsgruppe
from src.server.bo.Einkaufsliste import Einkaufsliste
from src.server.bo.Einzelhändler import Einzelhändler
from src.server.bo.Listenobjekt import Listenobjekt

from src.server.db.Mapper import Mapper
from src.server.db.AnwenderMapper import AnwenderMapper
from src.server.db.EinkaufsgruppeMapper import EinkaufsgruppeMapper
from src.server.db.ArtikelMapper import ArtikelMapper
from src.server.db.EinkaufslisteMapper import EinkaufslisteMapper
from src.server.db.EinzelhändlerMapper import EinzelhändlerMapper
from src.server.db.ListenobjektMapper import ListenobjektMapper

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

    # Anwender

    def create_anwender(self, name, email, google_user_id):

        user = Anwender()
        user.set_benutzername(name)
        user.set_email(email)
        user.set_google_id(google_user_id)
        user.set_id(1)

        with AnwenderMapper() as mapper:
            return mapper.insert(user)


    def get_anwender_by_name(self, name):
        with AnwenderMapper() as mapper:
            return mapper.find_by_name(name)


    def get_anwender_by_id(self, number):
        with AnwenderMapper() as mapper:
            return mapper.find_by_key(number)


    def get_anwender_by_email(self, email):
        with AnwenderMapper() as mapper:
            return mapper.find_by_email(email)


    def get_anwender_by_google_user_id(self, id):
        with AnwenderMapper() as mapper:
            return mapper.find_by_google_user_id(id)


    def get_all_anwender(self):
        with AnwenderMapper() as mapper:
            return mapper.find_all()


    def save_anwender(self, user):
        with AnwenderMapper() as mapper:
            mapper.update(user)


    def delete_anwender(self, user):
        with AnwenderMapper() as mapper:
            mapper.delete(user)


    def get_all_lists(self):
        with EinkaufslisteMapper() as mapper:
            return mapper.find_all()

    # Artikel

    def create_artikel(self, name, einheit):
        artikel = Artikel()
        artikel.set_name(name)
        artikel.set_einheit(einheit)
        artikel.set_id(1)

        with ArtikelMapper() as mapper:
            return mapper.insert(Artikel)

    def get_artikel_by_name(self, last_name):
        with ArtikelMapper() as mapper:
            return mapper.find_by_last_name(last_name)

    def get_artikel_by_id(self, number):
        with ArtikelMapper() as mapper:
            return mapper.find_by_key(number)

    def get_all_artikel(self):
        with ArtikelMapper() as mapper:
            return mapper.find_all()

    def save_artikel(self, artikel):
        with ArtikelMapper() as mapper:
            mapper.update(artikel)

    def delete_artikel(self, artikel):
        with ArtikelMapper() as mapper:
            mapper.delete(artikel)

    # Einzelhändler

    def create_einzelhändler(self, name):
        einzelhändler = Einzelhändler()
        einzelhändler.set_name(name)

        with EinzelhändlerMapper() as mapper:
            return mapper.insert(Einzelhändler)

    def get_einzelhändler_by_name(self, last_name):
        with EinzelhändlerMapper() as mapper:
            return mapper.find_by_last_name(last_name)

    def get_einzelhändler_by_id(self, number):
        with EinzelhändlerMapper() as mapper:
            return mapper.find_by_key(number)

    def get_all_einzelhändler(self):
        with EinzelhändlerMapper() as mapper:
            return mapper.find_all()

    def save_einzelhändler(self, artikel):
        with EinzelhändlerMapper() as mapper:
            mapper.update(artikel)

    def delete_einzelhändler(self, einzelhändler):
        with EinzelhändlerMapper() as mapper:
            mapper.delete(einzelhändler)

    # Listenobjekt

    def create_listenobjekt(self, parent_list, user_id, artikel_id, einzelhändler_id, artikel_preis, menge, ticked):
        listenobjekt = Listenobjekt()
        listenobjekt.set_parent_list(parent_list)
        listenobjekt.set_user_id(user_id)
        listenobjekt.set_artikel_id(artikel_id)
        listenobjekt.set_einzelhändler_id(einzelhändler_id)
        listenobjekt.set_artikel_preis(artikel_preis)
        listenobjekt.set_menge(menge)
        listenobjekt.set_ticked(ticked)

        with ListenobjektMapper() as mapper:
            return mapper.insert(Listenobjekt)

    def get_listenobjekt_by_name(self, last_name):
        with ListenobjektMapper() as mapper:
            return mapper.find_by_last_name(last_name)

    def get_listenobjekt_by_id(self, number):
        with ListenobjektMapper() as mapper:
            return mapper.find_by_key(number)

    def get_all_listenobjekt(self):
        with ListenobjektMapper() as mapper:
            return mapper.find_all()

    def save_listenobjekt(self, artikel):
        with ListenobjektMapper() as mapper:
            mapper.update(artikel)

    def delete_listenobjekt(self, listenobjekt):
        with ListenobjektMapper() as mapper:
            mapper.delete(listenobjekt)

