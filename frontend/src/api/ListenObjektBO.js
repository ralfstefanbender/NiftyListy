import BusinessObject from './BusinessObject';

export default class ListenObjektBO extends BusinessObject {

   // Listenobjekt mit: Anwender, Artikel, Händler, Menge und Abgehakt-status
    constructor(parent_list, user_id, artikel_id, einzelhändler_id, menge, ticked) {
        super();
        this.parent_list = parent_list;
        this.user_id = user_id;
        this.artikel_id = artikel_id;
        this.einzelhändler_id = einzelhändler_id;
        this.menge = menge;
        this.ticked = ticked;
    }

    set_parent_list(parent_list) {
        this.parent_list = parent_list

    }
   
    get_parent_list() {
        return this.parent_list

    }

    set_user_id(user_id) {
        this.user_id = user_id

    }
   
    get_user_id() {
        return this.user_id

    }

    set_artikel_id(artikel_id) {
        this.artikel_id = artikel_id

    }
   
    get_artikel_id() {
        return this.artikel_id

    }

    set_einzelhändler_id(einzelhändler_id) {
        this.einzelhändler_id = einzelhändler_id

    }
   
    get_einzelhändler_id() {
        return this.einzelhändler_id

    }

    set_menge(menge) {
        this.menge = menge

    }
   
    get_menge() {
        return this.menge

    }

    set_ticked(ticked) {
        this.ticked = ticked

    }
   
    get_ticked() {
        return this.ticked

    }

    // Returns an Array of ArtikelBOs from a given JSON structure
    static fromJSON(ListenObjekt) {
        let result = [];

        if (Array.isArray(ListenObjekt)) {
            ListenObjekt.forEach((lo) => {
                Object.setPrototypeOf(lo, ListenObjektBO.prototype)
                result.push(lo)
            })
        } else {
            // Es handelt sich offenbar um ein singuläres Objekt
            let lo = ListenObjekt;
            Object.setPrototypeOf(lo, ListenObjektBO.prototype)
            result.push(lo)
        }

        return result;
    }

}