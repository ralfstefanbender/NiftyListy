import BusinessObject from './BusinessObject';

export default class EinkaufsgruppeBO extends BusinessObject {

    constructor(einkaufsgruppe_name, teilnehmerliste, adminliste) {
        super();
        this.einkaufsgruppe_name = einkaufsgruppe_name;
        this.teilnehmerliste = teilnehmerliste;
        this.adminliste = adminliste;
    }

    /**addUser(Anwender) {

    }

    delUser(Anwender) {

    }

    promoteToAdmin(Anwender) {

    }**/

    getEinkaufsgruppeName() {
        return this.einkaufsgruppe_name
    }

    setEinkaufsgruppeName(name) {
        this.einkaufsgruppe_name = name
    }

    // Returns an Array of EinkaufsgruppeBO from a given JSON structure
    static fromJSON(einkaufsgruppe) {
        let result = [];

        if (Array.isArray(einkaufsgruppe)) {
            einkaufsgruppe.forEach((eg) => {
                Object.setPrototypeOf(eg, EinkaufsgruppeBO.prototype)
                result.push(eg)
            })
        } else {
            // Es handelt sich offenbar um ein singuläres Objekt
            let eg = einkaufsgruppe
            Object.setPrototypeOf(eg, EinkaufsgruppeBO.prototype)
            result.push(eg)
        }

        return result;
    }
}