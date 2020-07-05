import BusinessObject from './BusinessObject';

export default class EinkaufslisteBO extends BusinessObject {

    //this.itemID = 0
    //this.id = 0

    constructor(name) {
        this.name = name
        //this.items ist ein dictionary
        /**Wie geht hier die Umsetzung:
        self.__id = Einkaufsliste.id
        Einkaufsliste.id += 1 */
    }

    getItems() {
        return this.items
    }

    getID() {
        return this.id
    }

    getName() {
        return this.name
    }

    setName(newName) {
        this.name = newName
    }

    /**addItem {}

    tickItem {} 
    
    changeMengeItems {}

    removeItem
    
    removeTickedItems
    
    clearList*/

    
    // Returns an Array of EinkaufslisteBO from a given JSON structure
    static fromJSON(einkaufsliste) {
        let result = [];

        if (Array.isArray(einkaufsliste)) {
            einkaufsliste.forEach((el) => {
                Object.setPrototypeOf(el, EinkaufslisteBO.prototype)
                result.push(el)
            })
        } else {
            // Es handelt sich offenbar um ein singuläres Objekt
            let el = einkaufsliste
            Object.setPrototypeOf(el, EinkaufslisteBO.prototype)
            result.push(el)
        }

        return result;
    }
}