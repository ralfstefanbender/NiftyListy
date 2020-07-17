import AnwenderBO from './AnwenderBO';
import ArtikelBO from './ArtikelBO';
import EinkaufsgruppeBO from './EinkaufsgruppeBO';
import EinkaufslisteBO from './EinkaufslisteBO';
import EinzelhändlerBO from './EinzelhändlerBO';
import ListenObjektBO from './ListenObjektBO';
import ZugehörigkeitBO from './ZugehörigkeitBO';

/**
 * Abstracts the REST interface of the Python backend with convenient access methods.
 * The class is implemented as a singleton. 
 * 
 * @author [Christoph Kunz](https://github.com/christophkunz)
 */
export default class ListAPI {

    // Singelton instance
    static #api = null;


    // Local Python backend
    #ListServerBaseURL = '/niftylisty';


    // Anwender ?
    #getAllAnwenderURL = () => `${this.#ListServerBaseURL}/anwender`;
    #addAnwenderURL = () => `${this.#ListServerBaseURL}/anwender-hinzufügen`;
    #getAnwenderURL = (id) => `${this.#ListServerBaseURL}/anwender/${id}`;
    #updateAnwenderURL = (id) => `${this.#ListServerBaseURL}/anwender/${id}`;
    #deleteAnwenderURL = (id) => `${this.#ListServerBaseURL}/anwender/${id}`;
    #searchAnwenderURL = (benutzername) => `${this.#ListServerBaseURL}/benutzername/${benutzername}`;


    // Artikel
    #getAllArtikelURL = () => `${this.#ListServerBaseURL}/artikel`;
    #getArtikelURL = (id) => `${this.#ListServerBaseURL}/artikel/${id}`;
    #addArtikelURL = () => `${this.#ListServerBaseURL}/artikel-hinzufügen`;
    #deleteArtikelURL = (id) => `${this.#ListServerBaseURL}/artikel/${id}`;

    // Einkaufsgruppe
    #getEinkaufsgruppeURL = (id) => `${this.#ListServerBaseURL}/eingaufsgruppe/${id}`;
    #getAllEinkaufsgruppeURL = () => `${this.#ListServerBaseURL}/einkaufsgruppe`;
    #addEinkaufsgruppeURL = () => `${this.#ListServerBaseURL}/einkaufsgruppe-hinzufügen`;
    #deleteEinkaufsgruppeURL = (id) => `${this.#ListServerBaseURL}/einkaufsgruppe/${id}`;

    // Einkaufsliste
    #getAllEinkaufslisteURL = () => `${this.#ListServerBaseURL}/einkaufsliste`;
    #addEinkaufslisteURL = () => `${this.#ListServerBaseURL}/einkaufsliste-hinzufügen`;
    #getEinkaufslisteURL = (id) => `${this.#ListServerBaseURL}/einkaufsliste/${id}`;
    #updateEinkaufslisteURL = (id) => `${this.#ListServerBaseURL}/einkaufsliste/${id}`;
    #deleteEinkaufslisteURL = (id) => `${this.#ListServerBaseURL}/einkaufsliste/${id}`;

    // Einzelhändler
    #getAllEinzelhändlerURL = () => `${this.#ListServerBaseURL}/einzelhändler`;
    #addEinzelhändlerURL = () => `${this.#ListServerBaseURL}/einzelhändler-hinzufügen`;
    #getEinzelhändlerURL = (id) => `${this.#ListServerBaseURL}/einzelhändler/${id}`;

    // Listenobjekt
    #getAllListenobjektURL = () => `${this.#ListServerBaseURL}/listenobjekt`;
    #addlistenobjektURL = () => `${this.#ListServerBaseURL}/listenobjekt-hinzufügen`;
    #getlistenobjektURL = (id) => `${this.#ListServerBaseURL}/listenobjekt/${id}`;
    #updateListenobjektURL = (id) => `${this.#ListServerBaseURL}/listenobjekt/${id}`;
    #deleteListenobjektURL = (id) => `${this.#ListServerBaseURL}/listenobjekt/${id}`;

    // Zugehörigkeit
    #addZugehörigkeitURL = () => `${this.#ListServerBaseURL}/zugehörigkeit-hinzufügen`;
    #getZugehörigkeitURL = (id) => `${this.#ListServerBaseURL}/zugehörigkeit/${id}`;
    #deleteZugehörigkeitURL = (id) => `${this.#ListServerBaseURL}/zugehörigkeit/${id}`;

  
    //Singelton Instanz stellt sicher dass die API nur einmal vorliegt
    static getAPI() {
        if (this.#api == null) {
            this.#api = new ListAPI();
        }
        return this.#api;
    }

    /**
     *  Gibt ein Promise zurück mit dem entsprechenden JSON Objekt 
     *  Das Promise, welches durch fetch() zurückgegeben wird wird nicht bi einem HTTP Error abgelehnt, selbst bei einem, 404 oder 500 Error. 
     *  fetchAdvanced wirft den Error als auch den Serverstatus Error aus
     */
    #fetchAdvanced = (url, init) => fetch(url, init)
        .then(res => {
            // Das von fetch() zurückgegebene Promise wird bei einem Error nicht abgelehnt. 
            if (!res.ok) {
                throw Error(`${res.status} ${res.statusText}`);
            }
            return res.json();
        }
    )


    //Anwender

    // Gibt einen Promise zurück mit allen Anwendern 
    getAllAnwender() {
        return this.#fetchAdvanced(this.#getAllAnwenderURL()).then((responseJSON) => {
            let anwenderBOs = AnwenderBO.fromJSON(responseJSON);
            return new Promise(function (resolve) {
                resolve(anwenderBOs);
            })
        })
    }


    /**
     * Adds a customer and returns a Promise, which resolves to a new CustomerBO object with the 
     * firstName and lastName of the parameter customerBO object.
     * 
     * @param {CustomerBO} customerBO to be added. The ID of the new customer is set by the backend
     * @public
     */
    addAnwender(anwenderBO) {
        return this.#fetchAdvanced(this.#addAnwenderURL(), {
            method: 'POST',
            headers: {
                'Accept': 'application/json, text/plain',
                'Content-type': 'application/json',
            },
            body: JSON.stringify(anwenderBO)
        }).then((responseJSON) => {
            let responseAnwenderBO = AnwenderBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
                resolve(responseAnwenderBO);
            })
        })
    }


    //anwenderID nicht vorhanden noch zu implementieren in ShoppingListDetail.js
    getAnwender(anwenderID) {
        return this.#fetchAdvanced(this.#getAnwenderURL(anwenderID)).then((responseJSON) => {
            let responseAnwenderBO = AnwenderBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
                resolve(responseAnwenderBO);
            })
        })
    }


    updateAnwender(anwenderBO) {
        return this.#fetchAdvanced(this.#updateAnwenderURL(anwenderBO.getID()), {
            method: 'PUT',
            headers: {
                'Accept': 'application/json, text/plain',
                'Content-type': 'application/json',
            },
            body: JSON.stringify(anwenderBO)
        }).then((responseJSON) => {
            let responseAnwenderBO = AnwenderBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
                resolve(responseAnwenderBO);
            })
        })
    }


    //anwenderID nicht vorhanden noch zu implementieren in ShoppingListDetail.js
    deleteAnwender(anwenderID) {
        return this.#fetchAdvanced(this.#deleteAnwenderURL(anwenderID), {
            method: 'DELETE'
        }).then((responseJSON) => {
            let responseAnwenderBO = AnwenderBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
                resolve(responseAnwenderBO);
            })
        })
    }


    //benutzername suchen möglich?
    searchAnwender(benutzername) {
        return this.#fetchAdvanced(this.#searchAnwenderURL(benutzername)).then((responseJSON) => {
            let anwenderBOs = AnwenderBO.fromJSON(responseJSON);
            return new Promise(function (resolve) {
                resolve(anwenderBOs);
            })
        })
    }


    //Artikel

    //Einkaufsgruppe

    //Einkaufsliste

    //Einzelhändler

    //Listenobjekt
    
    //Zugehörigkeit


}
