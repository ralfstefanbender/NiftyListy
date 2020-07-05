import BusinessObject from './BusinessObject';

export default class AnwenderBO extends BusinessObject {

    constructor(benutzername, admin) {
        super();
        this.benutzername = benutzername;
        this.admin = admin;

    }

    setBenutzername(benutzername) {
        this.benutzername = benutzername
    }

    getBenutzername() {
        return this.benutzername

    }

    setAdmin(admin) {
        this.admin = admin
    }

    // Returns an Array of AnwenderBOs from a given JSON structure
    static fromJSON(anwender) {
        let result = [];

        if (Array.isArray(anwender)) {
            anwender.forEach((an) => {
                Object.setPrototypeOf(an, AnwenderBO.prototype)
                result.push(an)
            })
        } else {
            // Es handelt sich offenbar um ein singuläres Objekt
            let an = anwender;
            Object.setPrototypeOf(an, AnwenderBO.prototype)
            result.push(an)
        }

        return result;
    }

}