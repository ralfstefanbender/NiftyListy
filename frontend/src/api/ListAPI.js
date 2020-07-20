import AnwenderBO from './AnwenderBO';
import ArtikelBO from './ArtikelBO';
import EinkaufsgruppeBO from './EinkaufsgruppeBO';
import EinkaufslisteBO from './EinkaufslisteBO';
import EinzelhändlerBO from './EinzelhändlerBO';
import ListenObjektBO from './ListenObjektBO';
import ZugehörigkeitBO from './ZugehörigkeitBO';


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
    #addListenobjektURL = () => `${this.#ListServerBaseURL}/listenobjekt-hinzufügen`;
    #getListenobjektURL = (id) => `${this.#ListServerBaseURL}/listenobjekt/${id}`;
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

    getAllArtikel() {
        return this.#fetchAdvanced(this.#getAllArtikelURL()).then((responseJSON) => {
            let artikelBOs = ArtikelBO.fromJSON(responseJSON);
            return new Promise(function (resolve) {
                resolve(artikelBOs);
            })
        })
    }


    //artikelID vorhanden???
    getArtikel(artikelID) {
        return this.#fetchAdvanced(this.#getArtikelURL(artikelID)).then((responseJSON) => {
            let responseArtikelBO = ArtikelBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
                resolve(responseArtikelBO);
            })
        })
    }


    addArtikel(artikelBO) {
        return this.#fetchAdvanced(this.#addArtikelURL(), {
            method: 'POST',
            headers: {
                'Accept': 'application/json, text/plain',
                'Content-type': 'application/json',
            },
            body: JSON.stringify(artikelBO)
        }).then((responseJSON) => {
            let responseArtikelBO = ArtikelBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
                resolve(responseArtikelBO);
            })
        })
    }


    //artikelID vorhanden???
    deleteAnwender(artikelID) {
        return this.#fetchAdvanced(this.#deleteArtikelURL(artikelID), {
            method: 'DELETE'
        }).then((responseJSON) => {
            let responseArtikelBO = ArtikelBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
                resolve(responseArtikelBO);
            })
        })
    }


    //Einkaufsgruppe

    getAllEinkaufsgruppen() {
        return this.#fetchAdvanced(this.#getAllEinkaufsgruppeURL()).then((responseJSON) => {
            let einkaufsgruppeBOs = EinkaufsgruppeBO.fromJSON(responseJSON);
            return new Promise(function (resolve) {
                resolve(einkaufsgruppeBOs);
            })
        })
    }


    //einkaufsgruppeID vorhanden???
    getEinkaufsgruppen(einkaufsgruppeID) {
        return this.#fetchAdvanced(this.#getEinkaufsgruppeURL(einkaufsgruppeID)).then((responseJSON) => {
            let responseEinkaufsgruppeBO = EinkaufsgruppeBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
                resolve(responseEinkaufsgruppeBO);
            })
        })
    }


    addEinkaufsgruppe(einkaufsgruppeBO) {
        return this.#fetchAdvanced(this.#addEinkaufsgruppeURL(), {
            method: 'POST',
            headers: {
                'Accept': 'application/json, text/plain',
                'Content-type': 'application/json',
            },
            body: JSON.stringify(einkaufsgruppeBO)
        }).then((responseJSON) => {
            let responseEinkaufsgruppeBO = EinkaufsgruppeBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
                resolve(responseEinkaufsgruppeBO);
            })
        })
    }


    //einkaufsgruppeID vorhanden???
    deleteEinkaufsgruppe(einkaufsgruppeID) {
        return this.#fetchAdvanced(this.#deleteEinkaufsgruppeURL(einkaufsgruppeID), {
            method: 'DELETE'
        }).then((responseJSON) => {
            let responseEinkaufsgruppeBO = EinkaufsgruppeBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
                resolve(responseEinkaufsgruppeBO);
            })
        })
    }

    //Einkaufsliste

    getAllEinkaufslisten() {
        return this.#fetchAdvanced(this.#getAllEinkaufslisteURL()).then((responseJSON) => {
            let einkaufslisteBOs = EinkaufslisteBO.fromJSON(responseJSON);
            return new Promise(function (resolve) {
                resolve(einkaufslisteBOs);
            })
        })
    }


    //einkaufslisteID vorhanden???
    getEinkaufslisten(einkaufslisteID) {
        return this.#fetchAdvanced(this.#getEinkaufslisteURL(einkaufslisteID)).then((responseJSON) => {
            let responseEinkaufslisteBO = EinkaufslisteBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
                resolve(responseEinkaufslisteBO);
            })
        })
    }


    addEinkaufsliste(einkaufslisteBO) {
        return this.#fetchAdvanced(this.#addEinkaufslisteURL(), {
            method: 'POST',
            headers: {
                'Accept': 'application/json, text/plain',
                'Content-type': 'application/json',
            },
            body: JSON.stringify(einkaufslisteBO)
        }).then((responseJSON) => {
            let responseEinkaufslisteBO = EinkaufslisteBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
                resolve(responseEinkaufslisteBO);
            })
        })
    }


    updateEinkaufsliste(einkaufslisteBO) {
        return this.#fetchAdvanced(this.#updateEinkaufslisteURL(einkaufslisteBO.getID()), {
            method: 'PUT',
            headers: {
                'Accept': 'application/json, text/plain',
                'Content-type': 'application/json',
            },
            body: JSON.stringify(einkaufslisteBO)
        }).then((responseJSON) => {
            let responseEinkaufslisteBO = EinkaufslisteBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
                resolve(responseEinkaufslisteBO);
            })
        })
    }


    //einkaufslisteID vorhanden???
    deleteEinkaufsliste(einkaufslisteID) {
        return this.#fetchAdvanced(this.#deleteEinkaufslisteURL(einkaufslisteID), {
            method: 'DELETE'
        }).then((responseJSON) => {
            let responseEinkaufslisteBO = EinkaufslisteBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
                resolve(responseEinkaufslisteBO);
            })
        })
    }


    //Einzelhändler

    // Gibt einen Promise zurück mit allen Einzelhändlern
    getAllEinzelhändler() {
        return this.#fetchAdvanced(this.#getAllEinzelhändlerURL()).then((responseJSON) => {
            let einzelhändlerBOs = EinzelhändlerBO.fromJSON(responseJSON);
            return new Promise(function (resolve) {
                resolve(einzelhändlerBOs);
            })
        })
    }


    addEinzelhändler(einzelhändlerBO) {
        return this.#fetchAdvanced(this.#addEinzelhändlerURL(), {
            method: 'POST',
            headers: {
                'Accept': 'application/json, text/plain',
                'Content-type': 'application/json',
            },
            body: JSON.stringify(einzelhändlerBO)
        }).then((responseJSON) => {
            let responseEinzelhändlerBO = EinzelhändlerBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
                resolve(responseEinzelhändlerBO);
            })
        })
    }



    getEinzelhändler(einzelhändlerID) {
        return this.#fetchAdvanced(this.#getEinzelhändlerURL(einzelhändlerID)).then((responseJSON) => {
            let responseEinzelhändlerBO = EinzelhändlerBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
                resolve(responseEinzelhändlerBO);
            })
        })
    }


    //Listenobjekt

    // Gibt einen Promise zurück mit allen Listenobjekten
    getAllListenobjekt() {
        return this.#fetchAdvanced(this.#getAllListenobjektURL()).then((responseJSON) => {
            let listenobjektBOs = ListenObjektBO.fromJSON(responseJSON);
            return new Promise(function (resolve) {
                resolve(listenobjektBOs);
            })
        })
    }
    
    
    addListenobjekt(listenobjektBO) {
        return this.#fetchAdvanced(this.#addListenobjektURL(), {
            method: 'POST',
            headers: {
                'Accept': 'application/json, text/plain',
                'Content-type': 'application/json',
            },
            body: JSON.stringify(listenobjektBO)
        }).then((responseJSON) => {
            let responseListenobjektBO = ListenObjektBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
                resolve(responseListenobjektBO);
            })
        })
    }


    getListenobjekt(listenobjektID) {
        return this.#fetchAdvanced(this.#getListenobjektURL(listenobjektID)).then((responseJSON) => {
            let responseListenobjektBO = ListenObjektBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
                resolve(responseListenobjektBO);
            })
        })
    }


    updateListenobjekt(listenobjektBO) {
        return this.#fetchAdvanced(this.#updateListenobjektURL(listenobjektBO.getID()), {
            method: 'PUT',
            headers: {
                'Accept': 'application/json, text/plain',
                'Content-type': 'application/json',
            },
            body: JSON.stringify(listenobjektBO)
        }).then((responseJSON) => {
            let responseListenobjektBO = ListenObjektBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
                resolve(responseListenobjektBO);
            })
        })
    }



    deleteListenobjekt(listenobjektID) {
        return this.#fetchAdvanced(this.#deleteListenobjektURL(listenobjektID), {
            method: 'DELETE'
        }).then((responseJSON) => {
            let responseListenobjektBO = ListenObjektBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
                resolve(responseListenobjektBO);
            })
        })
    }
    
    //Zugehörigkeit
    

    addZugehörigkeit(zugehörigkeitBO) {
        return this.#fetchAdvanced(this.#addZugehörigkeitURL(), {
            method: 'POST',
            headers: {
                'Accept': 'application/json, text/plain',
                'Content-type': 'application/json',
            },
            body: JSON.stringify(zugehörigkeitBO)
        }).then((responseJSON) => {
            let responseZugehörigkeitBO = ZugehörigkeitBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
                resolve(responseZugehörigkeitBO);
            })
        })
    }



    getZugehörigkeit(zugehörigkeitID) {
        return this.#fetchAdvanced(this.#getZugehörigkeitURL(zugehörigkeitID)).then((responseJSON) => {
            let responseZugehörigkeitBO = ZugehörigkeitBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
                resolve(responseZugehörigkeitBO);
            })
        })
    }


    deleteZugehörigkeit(zugehörigkeitID) {
        return this.#fetchAdvanced(this.#deleteZugehörigkeitURL(zugehörigkeitID), {
            method: 'DELETE'
        }).then((responseJSON) => {
            let responseZugehörigkeitBO = ZugehörigkeitBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
                resolve(responseZugehörigkeitBO);
            })
        })
    }


}