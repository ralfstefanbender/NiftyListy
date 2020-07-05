import BusinessObject from './BusinessObject';

export default class ArtikelBO extends BusinessObject {

   // Dictionary für "all_Artikel" noch ergänzen
    constructor(name, einheit) {
        super();
        this.name = name;
        this.einheit = einheit;
    }

    setName(name) {
        this.name = name

    }
   
    getName() {
        return this.name

    }

    setEinheit(einheit) {
        this.einheit = einheit

    }
   
    getEinheit() {
        return this.einheit

    }

    // Returns an Array of ArtikelBOs from a given JSON structure
    static fromJSON(artikel) {
        let result = [];

        if (Array.isArray(artikel)) {
            artikel.forEach((ar) => {
                Object.setPrototypeOf(ar, ArtikelBO.prototype)
                result.push(ar)
            })
        } else {
            // Es handelt sich offenbar um ein singuläres Objekt
            let ar = artikel;
            Object.setPrototypeOf(ar, ArtikelBO.prototype)
            result.push(ar)
        }

        return result;
    }

}