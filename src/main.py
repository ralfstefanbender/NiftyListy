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
    'einkaufsgruppe_name': fields.Integer(attribute='__einkaufsgruppe_name', description='Der Name der Einkaufsgruppe'),
})

einkaufsliste = api.inherit('Einkaufsliste', bo, {
    'name': fields.Integer(attribute='_name', description='Der Name der Einkaufsliste'),
    'einkaufsgruppe_id': fields.Integer(attribute='_einkaufsgruppe_id', description='Die ID der Einkaufsgruppe'),
})

einzelhändler = api.inherit('Einzelhändler', bo, {
    'name': fields.Integer(attribute='_name', description='Der Name des Einzelhändlers'),
})

listenobjekt = api.inherit('Listenobjekt', bo, {
    'parent_list': fields.Integer(attribute='_parent_list', description='Die ID der Gruppe'),
    'user_id': fields.Integer(attribute='_user_id', description='Die ID des Anwenders'),
    'artikel_id': fields.Integer(attribute='_artikel_id', description='Die ID des Artikels'),
    'einzelhändler_id': fields.Integer(attribute='_einzelhändler_id', description='Die ID des Einzelhändlers'),
    'menge': fields.Integer(attribute='_menge', description='Die Menge'),
    'ticked': fields.Integer(attribute='_ticked', description='Gekauft'),
})

Zugehörigkeit = api.inherit('Zugehörigkeit', bo, {
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
        item = adm.get_anwender_by_id(id)
        if item is None:
            return '', 500
        else:
            adm.delete_artikel(item)
            return '', 200

"""Artikel"""

@shopping.route("/item/<int:id>")
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
            return '', 500
        else:
            adm.delete_artikel(item)
            return '', 200

"""Einkaufsgruppe"""

@shopping.route("/einkaufsgruppe/<int:id>")
@shopping.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@shopping.param('id', 'Die ID des Account-Objekts')
class EinkaufsgruppeOperationen(Resource):
    @shopping.marshal_with(einkaufsgruppe)


    def delete(self,id):
        """Löschen einer Einkaufsgruppe aus der DB"""
        adm = EinkaufAdministration()
        item = adm.get_einkaufsgruppe_by_id(id)
        if item is None:
            return '', 500
        else:
            adm.delete_artikel(item)
            return '', 200

"""Einkaufsliste"""

@shopping.route("/einkaufsliste/<int:id>")
@shopping.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@shopping.param('id', 'Die ID des Account-Objekts')
class EinkaufslisteOperationen(Resource):
    @shopping.marshal_with(einkaufsliste)


    def delete(self,id):
        """Löschen einer Einkaufsliste aus der DB"""
        adm = EinkaufAdministration()
        item = adm.get_einkaufsliste_by_id(id)
        if item is None:
            return '', 500
        else:
            adm.delete_artikel(item)
            return '', 200

"""Einzelhändler"""

@shopping.route("/einzelhändler/<int:id>")
@shopping.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@shopping.param('id', 'Die ID des Account-Objekts')
class EinzelhändlerOperationen(Resource):
    @shopping.marshal_with(einzelhändler)


    def delete(self,id):
        """Löschen eines Einzelhändlers aus der DB"""
        adm = EinkaufAdministration()
        item = adm.get_einzelhändler_by_id(id)
        if item is None:
            return '', 500
        else:
            adm.delete_artikel(item)
            return '', 200

"""Listenobjekt"""

@shopping.route("/listenobjekt/<int:id>")
@shopping.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@shopping.param('id', 'Die ID des Account-Objekts')
class ListenobjektOperationen(Resource):
    @shopping.marshal_with(listenobjekt)


    def delete(self,id):
        """Löschen eines Listenobjektes aus der DB"""
        adm = EinkaufAdministration()
        item = adm.get_listenobjekt_by_id(id)
        if item is None:
            return '', 500
        else:
            adm.delete_artikel(item)
            return '', 200

if __name__ =='__main__':
    app.run(debug=True)