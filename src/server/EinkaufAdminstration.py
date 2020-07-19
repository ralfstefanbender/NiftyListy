from src.server.bo.Anwender import Anwender
from src.server.bo.Artikel import Artikel
from src.server.bo.Einkaufsgruppe import Einkaufsgruppe
from src.server.bo.Einkaufsliste import Einkaufsliste
from src.server.bo.Einzelhändler import Einzelhändler
from src.server.bo.Listenobjekt import Listenobjekt
from src.server.bo.Zugehörigkeit import Zugehörigkeit

from src.server.db.Mapper import Mapper
from src.server.db.AnwenderMapper import AnwenderMapper
from src.server.db.EinkaufsgruppeMapper import EinkaufsgruppeMapper
from src.server.db.ArtikelMapper import ArtikelMapper
from src.server.db.EinkaufslisteMapper import EinkaufslisteMapper
from src.server.db.EinzelhändlerMapper import EinzelhändlerMapper
from src.server.db.ListenobjektMapper import ListenobjektMapper
from src.server.db.ZugehörigkeitMapper import ZugehörigkeitMapper

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
            zugehörigkeiten = self.get_zugehörigkeit_by_anwender(user.get_id())
            if not (zugehörigkeiten is None):
                for i in zugehörigkeiten:
                    self.delete_zugehörigkeit(i)

            listenobjekte = self.get_listenobjekt_by_anwender(user.get_id())
            if not (listenobjekte is None):
                for i in listenobjekte:
                    self.delete_listenobjekt(i)


            mapper.delete(user)


    def get_all_lists(self):
        with EinkaufslisteMapper() as mapper:
            return mapper.find_all()

    # Artikel

    def create_artikel(self, name, einheit):
        artikel = Artikel()
        artikel.set_name(name)
        artikel.set_einheit(einheit)

        with ArtikelMapper() as mapper:
            return mapper.insert(Artikel)

    def get_artikel_by_name(self, name):
        with ArtikelMapper() as mapper:
            return mapper.find_by_name(name)

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
            listenobjekt = self.get_listenobjekt_by_artikel(artikel.get_id())
            if not (listenobjekt is None):
                for i in listenobjekt:
                    self.delete_listenobjekt(i)

            mapper.delete(artikel)

    # Einzelhändler

    def create_einzelhändler(self, name):
        einzelhändler = Einzelhändler()
        einzelhändler.set_name(name)
        einzelhändler.set_id(1)

        with EinzelhändlerMapper() as mapper:
            return mapper.insert(Einzelhändler)

    def get_einzelhändler_by_name(self, name):
        with EinzelhändlerMapper() as mapper:
            return mapper.find_by_name(name)

    def get_einzelhändler_by_id(self, number):
        with EinzelhändlerMapper() as mapper:
            return mapper.find_by_key(number)

    def get_all_einzelhändler(self):
        with EinzelhändlerMapper() as mapper:
            return mapper.find_all()

    def save_einzelhändler(self, einzelhändler):
        with EinzelhändlerMapper() as mapper:
            mapper.update(einzelhändler)

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
            return mapper.insert(listenobjekt)

    def get_listenobjekt_by_anwender(self, id):
        with ListenobjektMapper() as mapper:
            return mapper.find_by_anwender(id)

    def get_listenobjekt_by_einkaufsliste(self, id):
        with ListenobjektMapper() as mapper:
            return mapper.find_by_einkaufsliste(id)

    def get_listenobjekt_by_artikel(self, id):
        with ListenobjektMapper() as mapper:
            return mapper.find_by_artikel(id)

    def get_listenobjekt_by_id(self, number):
        with ListenobjektMapper() as mapper:
            return mapper.find_by_key(number)

    def get_all_listenobjekt(self):
        with ListenobjektMapper() as mapper:
            return mapper.find_all()

    def save_listenobjekt(self, listenobjekt):
        with ListenobjektMapper() as mapper:
            mapper.update(listenobjekt)

    def delete_listenobjekt(self, listenobjekt):
        with ListenobjektMapper() as mapper:
            mapper.delete(listenobjekt)

    # Einkaufsgruppe

    def create_einkaufsgruppe(self, name):
        einkaufsgruppe = Einkaufsgruppe()
        einkaufsgruppe.set_einkaufsgruppe_name(name)

        with EinkaufsgruppeMapper() as mapper:
            return mapper.insert(einkaufsgruppe)

    def get_einkaufsgruppe_by_id(self, number):
        with EinkaufsgruppeMapper() as mapper:
            return mapper.find_by_key(number)

    def get_all_einkaufsgruppe(self):
        with EinkaufsgruppeMapper() as mapper:
            return mapper.find_all()

    def save_einkaufsgruppe(self, einkaufsgruppe):
        with EinkaufsgruppeMapper() as mapper:
            mapper.update(einkaufsgruppe)

    def delete_einkaufsgruppe(self, einkaufsgruppe):
        with EinkaufsgruppeMapper() as mapper:

            zugehörigkeiten = self.get_zugehörigkeit_by_einkaufsgruppe(einkaufsgruppe.get_id())
            if not (zugehörigkeiten is None):
                for i in zugehörigkeiten:
                    self.delete_zugehörigkeit(i)

            mapper.delete(einkaufsgruppe)

    # Einkaufsliste

    def create_einkaufsliste(self, name, einkaufsgruppe_id):
        einkaufsliste = Einkaufsliste()
        einkaufsliste.set_einkaufsgruppe(einkaufsgruppe_id)
        einkaufsliste.set_name(name)
        einkaufsliste.set_id(1)

        with EinkaufslisteMapper() as mapper:
            return mapper.insert(einkaufsliste)

    def get_einkaufsliste_by_name(self, name):
        with EinkaufslisteMapper() as mapper:
            return mapper.find_by_name(name)

    def get_einkaufsliste_by_id(self, number):
        with EinkaufslisteMapper() as mapper:
            return mapper.find_by_key(number)

    def get_all_einkaufsliste(self):
        with EinkaufslisteMapper() as mapper:
            return mapper.find_all()

    def save_einkaufsliste(self, einkaufsliste):
        with EinkaufslisteMapper() as mapper:
            mapper.update(einkaufsliste)

    def delete_einkaufsliste(self, einkaufsliste):
        with EinkaufslisteMapper() as mapper:
            listenobjekt = self.get_listenobjekt_by_einkaufsliste(einkaufsliste.get_id())
            if not (listenobjekt is None):
                for i in listenobjekt:
                    self.delete_listenobjekt(i)

            mapper.delete(einkaufsliste)


        # Zugehörigkeit

    def create_zugehörigkeit(self, anwender_id, einkaufsgruppe_id):
        zugehörigkeit = Zugehörigkeit()
        zugehörigkeit.set_einkaufsgruppe_id(einkaufsgruppe_id)
        zugehörigkeit.set_anwender_id(anwender_id)
        zugehörigkeit.set_id(1)

        with ZugehörigkeitMapper() as mapper:
            return mapper.insert(zugehörigkeit)

    def get_zugehörigkeit_by_id(self, number):
        with ZugehörigkeitMapper() as mapper:
            return mapper.find_by_key(number)

    def get_zugehörigkeit_by_anwender(self, anwender_id):
        with ZugehörigkeitMapper() as mapper:
            return mapper.find_by_account(anwender_id)

    def get_zugehörigkeit_by_einkaufsgruppe(self, einkaufsgruppe_id):
        with ZugehörigkeitMapper() as mapper:
            return mapper.find_by_einkaufsgruppe(einkaufsgruppe_id)

    def get_all_zugehörigkeit(self):
        with ZugehörigkeitMapper() as mapper:
            return mapper.find_all()

    def save_zugehörigkeit(self, zugehörigkeit):
        with ZugehörigkeitMapper() as mapper:
            mapper.update(zugehörigkeit)

    def delete_zugehörigkeit(self, zugehörigkeit):
        with ZugehörigkeitMapper() as mapper:
            mapper.delete(zugehörigkeit)

    # Add

    def add_member_to_group(self, anwender_id, einkaufsgruppe_id):

        duplicate = False
        liste = self.get_all_zugehörigkeit()
        for i in liste:
            if i == [anwender_id, einkaufsgruppe_id]:
                duplicate = True

        if duplicate is False:
            self.create_zugehörigkeit(anwender_id, einkaufsgruppe_id)

    def remove_member_from_group(self, anwender_id, einkaufsgruppe_id):

        liste = self.get_all_zugehörigkeit()
        for i in liste:
            if i == [anwender_id, einkaufsgruppe_id]:
                self.delete_zugehörigkeit(i)



