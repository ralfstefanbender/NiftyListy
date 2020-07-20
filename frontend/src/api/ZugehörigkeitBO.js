import BusinessObject from './BusinessObject';

export default class ZugehörigkeitBO extends BusinessObject {

   // Zughörigkeit zwischen Gruppen und Anwendern
    constructor(anwender_id, einkaufsgruppe_id) {
        super();
        this.anwender_id = anwender_id;
        this.einkaufsgruppe_id = einkaufsgruppe_id;
    }

    set_anwender_id(anwender_id) {
        this.anwender_id = anwender_id

    }
   
    get_anwender_id() {
        return this.anwender_id

    }

    set_einkaufsgruppe_id(einkaufsgruppe_id) {
        this.einkaufsgruppe_id = einkaufsgruppe_id

    }
   
    get_einkaufsgruppe_id() {
        return this.einkaufsgruppe_id

    }

    // Returns an Array of ArtikelBOs from a given JSON structure
    static fromJSON(Zughörigkeit) {
        let result = [];

        if (Array.isArray(Zughörigkeit)) {
            Zughörigkeit.forEach((zu) => {
                Object.setPrototypeOf(zu, ZugehörigkeitBO.prototype)
                result.push(zu)
            })
        } else {
            // Es handelt sich offenbar um ein singuläres Objekt
            let zu = Zughörigkeit;
            Object.setPrototypeOf(zu, ZugehörigkeitBO.prototype)
            result.push(zu)
        }

        return result;
    }

}