export default class BusinessObject {

    constructor() {
        this.id = 0;
        this.erstellungszeitpunkt = Date;
    }

    setID(id) {
        this.id = id
    }

    getID(id) {
        return this.id
    }

    
    getErstellungszeitpunkt(erstellungszeitpunkt) {
        return this.erstellungszeitpunkt
    }
    
    
    toString() {
        let result = ''
        for (var prop in this) {
            result += prop + ': ' + this[prop] + ' ';
        }
        return result;
    }


}