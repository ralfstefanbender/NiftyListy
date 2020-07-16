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
    'creation_date': fields.DateTime(attribute='_erstellungszeitpunkt', description='Das Erstellungsdatum '
                                                                            'eines Business Object'),
})

anwender = api.inherit('Anwender', bo, {
    'benutzername': fields.String(attribute='__benutzername', description='Der Benutzername eines Anwenders'),
    'email': fields.String(attribute='__email', description='Der E-Mail eines Anwenders'),
    'google_id': fields.String(attribute='__google_id', description='Die Google-ID eines Anwenders'),
})

artikel = api.inherit('Artikel', bo, {
    'name': fields.DateTime(attribute='__name', description='Der Name eines Artikels'),
    'einheit': fields.DateTime(attribute='__einheit', description='Die Einheit eines Artikels'),
})

einkaufsgruppe = api.inherit('Einkaufsgruppe', bo, {
    'einkaufsgruppe_name': fields.Integer(attribute='__einkaufsgruppe_name', description='Der Name der Einkaufsgruppe'),
})

einkaufsliste = api.inherit('Einkaufsliste', bo, {
    'name': fields.Integer(attribute='__name', description='Der Name der Einkaufsliste'),
    'einkaufsgruppe_id': fields.Integer(attribute='__einkaufsgruppe_id', description='Die ID der Einkaufsgruppe'),
})

einzelhändler = api.inherit('Einzelhändler', bo, {
    'name': fields.Integer(attribute='__name', description='Der Name des Einzelhändlers'),
})

listenobjekt = api.inherit('Listenobjekt', bo, {
    'parent_list': fields.Integer(attribute='__parent_list', description='Die ID der Gruppe'),
    'user_id': fields.Integer(attribute='__user_id', description='Die ID des Anwenders'),
    'artikel_id': fields.Integer(attribute='__artikel_id', description='Die ID des Artikels'),
    'einzelhändler_id': fields.Integer(attribute='__einzelhändler_id', description='Die ID des Einzelhändlers'),
    'menge': fields.Integer(attribute='__menge', description='Die Menge'),
    'ticked': fields.Integer(attribute='__ticked', description='Gekauft'),
})

Zugehörigkeit = api.inherit('Zugehörigkeit', bo, {
    'anwender_id': fields.Integer(attribute='__anwender_id', description='Die ID des Anwenders'),
    'einkaufsgruppe_id': fields.Integer(attribute='__einkaufsgruppe_id', description='Die ID der Gruppe'),
})


@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return jsonify({'hello': 'world'})


if __name__ =='__main__':
    app.run(debug=True)