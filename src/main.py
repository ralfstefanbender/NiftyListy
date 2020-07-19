from flask import Flask,jsonify
from flask_restx import Api, Resource, fields
from flask_cors import CORS

from src.server.bo.Artikel import Artikel
from src.server.bo.Zugehörigkeit import Zugehörigkeit
from src.server.bo.Einkaufsliste import Einkaufsliste
from src.server.bo.Listenobjekt import Listenobjekt
from src.server.bo.Einkaufsliste import Einkaufsliste
from src.server.bo.Einkaufsgruppe import Einkaufsgruppe
from src.server.bo.Zugehörigkeit import Zugehörigkeit

from src.server.EinkaufAdminstration import EinkaufAdministration


app = Flask(__name__)
CORS(app, resources=r'/niftylisty/*')
api = Api(app, version='0.1 pre-alpha', title='NiftyListy API',
    description='Demo-API für NiftyListy')
shopping = api.namespace('shopping', description='Funktionen des SSLS')

bo = api.model('BusinessObject', {
    'id': fields.Integer(attribute='_id', description='Der Unique Identifier eines Business Object'),
    'creation_date': fields.Date(attribute='_erstellungszeitpunkt', description='Das Erstellungsdatum '
                                                                            'eines Business Object'),
})

anwender = api.inherit('Anwender', bo, {
    'benutzername': fields.String(attribute='_benutzername', description='Der Benutzername eines Anwenders'),
    'email': fields.String(attribute='_email', description='Der E-Mail eines Anwenders'),
    'google_id': fields.String(attribute='_google_id', description='Die Google-ID eines Anwenders'),
})

artikel = api.inherit('Artikel', bo, {
    'name': fields.String(attribute='_name', description='Der Name eines Artikels'),
    'einheit': fields.String(attribute='_einheit', description='Die Einheit eines Artikels'),
})

einkaufsgruppe = api.inherit('Einkaufsgruppe', bo, {
    'einkaufsgruppe_name': fields.String(attribute='_einkaufsgruppe_name', description='Der Name der Einkaufsgruppe'),
})

einkaufsliste = api.inherit('Einkaufsliste', bo, {
    'name': fields.String(attribute='_name', description='Der Name der Einkaufsliste'),
    'einkaufsgruppe_id': fields.Integer(attribute='_einkaufsgruppe_id', description='Die ID der Einkaufsgruppe'),
})

einzelhändler = api.inherit('Einzelhändler', bo, {
    'name': fields.String(attribute='_name', description='Der Name des Einzelhändlers'),
})

listenobjekt = api.inherit('Listenobjekt', bo, {
    'parent_list': fields.Integer(attribute='_parent_list', description='Die ID der Gruppe'),
    'user_id': fields.Integer(attribute='_user_id', description='Die ID des Anwenders'),
    'artikel_id': fields.Integer(attribute='_artikel_id', description='Die ID des Artikels'),
    'einzelhändler_id': fields.Integer(attribute='_einzelhändler_id', description='Die ID des Einzelhändlers'),
    'menge': fields.String(attribute='_menge', description='Die Menge'),
    'ticked': fields.String(attribute='_ticked', description='Gekauft'),
})

zugehörigkeit = api.inherit('Zugehörigkeit', bo, {
    'anwender_id': fields.Integer(attribute='_anwender_id', description='Die ID des Anwenders'),
    'einkaufsgruppe_id': fields.Integer(attribute='_einkaufsgruppe_id', description='Die ID der Gruppe'),
})

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return jsonify({'hello': 'world'})

"""Anwender"""
@shopping.route("/anwender/<int:id>")
@shopping.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@shopping.param('id', 'Die ID des Account-Objekts')
class AnwenderOperationen(Resource):
    @shopping.marshal_with(anwender)
    def get(self,id):
        """Auslesen eines Anwenders aus der DB"""
        adm = EinkaufAdministration()
        user = adm.get_anwender_by_id(id)
        return user

    def delete(self,id):
        """Löschen eines Anwender aus der DB"""
        adm = EinkaufAdministration()
        user = adm.get_anwender_by_id(id)
        if user is None:
            return 'Anwender konnte nicht aus der DB gelöscht werden', 500
        else:
            adm.delete_anwender(user)
            return 'Anwender wurde erfolgreich aus der DB gelöscht', 200

"""Artikel"""

@shopping.route("/artikel/<int:id>")
@shopping.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@shopping.param('id', 'Die ID des Account-Objekts')
class ArtikelOperationen(Resource):
    @shopping.marshal_with(artikel)
    def get(self,id):
        """Auslesen eines Artikels aus der DB """
        adm = EinkaufAdministration()
        item = adm.get_artikel_by_id(id)
        return item

    def delete(self,id):
        """Löschen eines Artikels aus der DB"""
        adm = EinkaufAdministration()
        item = adm.get_artikel_by_id(id)
        if item is None:
            return 'Artikel konnte nicht aus der DB gelöscht werden', 500
        else:
            adm.delete_artikel(item)
            return 'Artikel wurde erfolgreich aus der DB gelöscht', 200

    @shopping.expect(artikel)
    def put(self, id):
        """Artikel werden aktualisiert"""
        adm = EinkaufAdministration()
        item = Artikel.from_dict(api.payload)

        if item is not None:
            item.set_id(id)
            adm.save_artikel(item)
            return "Artikel wurde erfolgreich geändert", 200
        else:
            return "Artikel konnte nicht geändert werden", 500

    @shopping.marshal_with(artikel, code=200)
    @shopping.expect(artikel)
    def post(self):
        adm = EinkaufAdministration()
        proposal = Artikel.from_dict(api.payload)
        if proposal is not None:
            c = adm.create_artikel(proposal.get_name(), proposal.get_einheit())
            return c, 200
        else:
            return '', 500

"""Einkaufsgruppe"""

@shopping.route("/einkaufsgruppe/<int:id>")
@shopping.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@shopping.param('id', 'Die ID des Account-Objekts')
class EinkaufsgruppeOperationen(Resource):
    @shopping.marshal_with(einkaufsgruppe)
    def get(self,id):
        """Auslesen einer Einkaufsgruppe aus der DB """
        adm = EinkaufAdministration()
        item = adm.get_einkaufsgruppe_by_id(id)
        return item

    def delete(self,id):
        """Löschen einer Einkaufsgruppe aus der DB"""
        adm = EinkaufAdministration()
        item = adm.get_einkaufsgruppe_by_id(id)
        if item is None:
            return 'Einkaufsgruppe konnte nicht aus der DB gelöscht werden', 500
        else:
            adm.delete_einkaufsgruppe(item)
            return 'Einkaufsgruppe wurde erfolgreich aus der DB gelöscht', 200

"""Einkaufsliste"""

@shopping.route("/einkaufsliste/<int:id>")
@shopping.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@shopping.param('id', 'Die ID des Account-Objekts')
class EinkaufslisteOperationen(Resource):
    @shopping.marshal_with(einkaufsliste)

    def get(self,id):
        """Auslesen einer Einkaufsliste aus der DB """
        adm = EinkaufAdministration()
        item = adm.get_einkaufsliste_by_id(id)
        return item

    def delete(self,id):
        """Löschen einer Einkaufsliste aus der DB"""
        adm = EinkaufAdministration()
        item = adm.get_einkaufsliste_by_id(id)
        if item is None:
            return 'Einkaufsliste konnte nicht aus der DB gelöscht werden', 500
        else:
            adm.delete_einkaufsliste(item)
            return 'Einkaufsliste wurde erfolgreich aus der DB gelöscht', 200

"""Einzelhändler"""

@shopping.route("/einzelhändler/<int:id>")
@shopping.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@shopping.param('id', 'Die ID des Account-Objekts')
class EinzelhändlerOperationen(Resource):
    @shopping.marshal_with(einzelhändler)

    def get(self,id):
        """Auslesen einer Einzelhändler aus der DB """
        adm = EinkaufAdministration()
        item = adm.get_einzelhändler_by_id(id)
        return item

    def delete(self,id):
        """Löschen eines Einzelhändlers aus der DB"""
        adm = EinkaufAdministration()
        item = adm.get_einzelhändler_by_id(id)
        if item is None:
            return 'Einzelhändler konnte nicht aus der DB gelöscht werden', 500
        else:
            adm.delete_einzelhändler(item)
            return 'Einzelhändler wurde erfolgreich aus der DB gelöscht', 200

"""Listenobjekt"""

@shopping.route("/listenobjekt/<int:id>")
@shopping.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@shopping.param('id', 'Die ID des Account-Objekts')
class ListenobjektOperationen(Resource):
    @shopping.marshal_with(listenobjekt)

    def get(self,id):
        """Auslesen einer Listenobjektes aus der DB """
        adm = EinkaufAdministration()
        item = adm.get_listenobjekt_by_id(id)
        return item

    def delete(self,id):
        """Löschen eines Listenobjektes aus der DB"""
        adm = EinkaufAdministration()
        item = adm.get_listenobjekt_by_id(id)
        if item is None:
            return 'Listenobjekt konnte nicht aus der DB gelöscht werden', 500
        else:
            adm.delete_listenobjekt(item)
            return 'Listenobjekt wurde erfolgreich aus der DB gelöscht', 200

"""Zugehörigkeit"""  

@shopping.route("/zugehörigkeit/<int:id>")
@shopping.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@shopping.param('id', 'Die ID des Account-Objekts')
class ZugehörigkeitOperationen(Resource):
    @shopping.marshal_with(zugehörigkeit)

    def get(self,id):
        """Auslesen einer Listenobjektes aus der DB """
        adm = EinkaufAdministration()
        item = adm.get_zugehörigkeit_by_id(id)
        return item

    def delete(self,id):
        """Löschen eines Listenobjektes aus der DB"""
        adm = EinkaufAdministration()
        item = adm.get_zugehörigkeit_by_id(id)
        if item is None:
            return 'Zugehörigkeit konnte nicht aus der DB gelöscht werden', 500
        else:
            adm.delete_zugehörigkeit(item)
            return 'Zugehörogkeit wurde erfolgreich aus der DB gelöscht', 200

if __name__ =='__main__':
    app.run(debug=True)