import BusinessObject from './BusinessObject';

/**Ist dieses BO notwenig? 
 * 
 * Alle Methoden genau dieselben wie bei der Einkaufsliste.
 * Enthalten die BO andere Methoden neben get und set?
 */

export default class EinkaufsgruppeBO extends BusinessObject {

    //this.itemID = 0
    //this.id = 0
    
    constructor(name) {
        this.name = name
        //this.items ist ein dictionary
        /**Wie geht hier die Umsetzung:
        self.__id = Einkaufsliste.id
        Einkaufsliste.id += 1 */
    }



    // Returns an Array of EinzelhändlerBO from a given JSON structure
    static fromJSON(einzelhaendler) {
        let result = [];

        if (Array.isArray(einzelhaendler)) {
            einzelhaendler.forEach((eh) => {
                Object.setPrototypeOf(eh, EinzelhändlerBO.prototype)
                result.push(eh)
            })
        } else {
            // Es handelt sich offenbar um ein singuläres Objekt
            let eh = einzelhaendler
            Object.setPrototypeOf(eh, EinzelhändlerBO.prototype)
            result.push(eh)
        }

        return result;
    }
}