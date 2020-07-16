import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { withStyles, Button, IconButton, Dialog, DialogTitle, DialogContent, DialogContentText, DialogActions, TextField } from '@material-ui/core';
import CloseIcon from '@material-ui/icons/Close';
import { BankAPI, EinkaufsgruppeBO } from '../../api';
import InlineError from './InlineError';
import LoadingBar from './LoadingBar';



class GruppeForm extends Component {

  constructor(props) {
    super(props);

    let Gruppenname = '';
    if (props.Gruppe) {
      Gruppenname = props.Gruppe.getGruppenname();
    }

    // Initialisierung des Zustandes
    this.state = {
      Gruppenname: Gruppenname,
      GruppennameValidationFailed: false,
      GruppennameEdited: false,
      addingInProgress: false,
      updatingInProgress: false,
      addingError: null,
      updatingError: null
    };
    // Sicherung des Zustandes für das "Abbrechen"
    this.baseState = this.state;
  }

  /** Ergänzt eine Gruppe */
  addGruppe = () => {
    let newGruppe = new EinkaufsgruppeBO(this.state.Gruppenname);
    BankAPI.getAPI().addGruppe(newGruppe).then(Gruppe => {
      // Backend Aufru war erfolgreich
      // Initialisiert den Dialog Zustand erneut für eine leere Gruppe
      this.setState(this.baseState);
      this.props.onClose(Gruppe); // Ruft das Übergeordnete Objekt mit der Gruppe auf
    }).catch(e =>
      this.setState({
        updatingInProgress: false,    // Ladebalken wird "vervorgen"
        updatingError: e              // Error wird angegeben
      })
    );

    // set loading to true
    this.setState({
      updatingInProgress: true,       // Ladebalken wird angezeigt
      updatingError: null             // Error wird "verborgen"
    });
  }

  /** Aktualisieren der Gruppe */
  updateGruppe = () => {
    // Duplizieren der Gruppe, falls der Backendaufruf fehlschlägt
    let updatedGruppe = Object.assign(new EinkaufsgruppeBO(), this.props.Gruppe);
    // Setzt neue Attribute durch den Dialog
    updatedGruppe.setGruppenname(this.state.Gruppenname);
    BankAPI.getAPI().updateGruppe(updatedGruppe).then(Gruppe => {
      this.setState({
        updatingInProgress: false,              // Ladebalken wird "verborgen" 
        updatingError: null                     // Kein Error liegt vor
      });
      // Behalte den Neuen Zustand als BaseState
      this.baseState.Gruppenname = this.state.Gruppenname;
      this.props.onClose(updatedGruppe);      // Ruft das Übrgeordnete Objekt mit der Gruppe auf
    }).catch(e =>
      this.setState({
        updatingInProgress: false,              // Ladebalken wird "verborgen" 
        updatingError: e                        // Error wird angezeigt
      })
    );

    // Setzt den Ladezustand auf "true"
    this.setState({
      updatingInProgress: true,                 // Zeigt den Ladebalken
      updatingError: null                       // Kein error wird angegeben
    });
  }

  /** Verwaltet Texteingaben der Form und Validiert diese */
  textFieldValueChange = (event) => {
    const value = event.target.value;

    let error = false;
    if (value.trim().length === 0) {
      error = true;
    }

    this.setState({
      [event.target.id]: event.target.value,
      [event.target.id + 'PrüfungFehlgeschlagen']: error,
      [event.target.id + 'Bearbeitet']: true
    });
  }

  /** Verwaltet das Schließen durch Knopfdruck */
  handleClose = () => {
    // Reset the state
    this.setState(this.baseState);
    this.props.onClose(null);
  }

  /** Rendern der Komponente */
  render() {
    const { classes, Gruppe, show } = this.props;
    const { Gruppenname, GruppennameValidationFailed, GruppennameEdited, addingInProgress,
      addingError, updatingInProgress, updatingError } = this.state;

    let title = '';
    let header = '';

    if (Gruppe) {
      title = 'Ahtualisieren einer Gruppe';
      header = `Gruppe ID: ${Gruppe.getID()}`;
    } else {
      title = 'Erstelle eine neue Gruppe';
      header = 'Ergänzen der Gruppendaten';
    }

    return (
      show ?
        <Dialog open={show} onClose={this.handleClose} maxWidth='xs'>
          <DialogTitle id='form-dialog-title'>{title}
            <IconButton className={classes.closeButton} onClick={this.handleClose}>
              <CloseIcon />
            </IconButton>
          </DialogTitle>
          <DialogContent>
            <DialogContentText>
              {header}
            </DialogContentText>
            <form className={classes.root} noValidate autoComplete='off'>
              <TextField autoFocus type='text' required fullWidth margin='normal' id='Gruppenname' label='Gruppenname:' value={Gruppenname} 
                onChange={this.textFieldValueChange} error={GruppennameValidationFailed} 
                helperText={fGruppennameValidationFailed ? 'Der Name der Gruppe benötigt mindestens einen Buchstaben' : ' '} />
            </form>
            <LoadingBar show={addingInProgress || updatingInProgress} />
            {
              // Zeige die Fehlereldung 
              Gruppe ?
                <InlineError error={updatingError} InlineError={`Die Gruppe ${Gruppe.getID()} konnte nicht aktualisiert werden.`} onReload={this.updateGruppe} />
                :
                <InlineError error={addingError} InlineError={`Die Gruppe konnte nicht hinzugefügt werden.`} onReload={this.addGruppe} />
            }
          </DialogContent>
          <DialogActions>
            <Button onClick={this.handleClose} color='secondary'>
              Abbrechen
            </Button>
            {
              // Wenn es eine Gruppe bereits gibt so zeige den "Update" Button, ansonsten den "Hinzufügen" Button
              Gruppe ?
                <Button disabled={GruppennameValidationFailed} variant='contained' onClick={this.updateGruppe} color='primary'>
                  Update
              </Button>
                : <Button disabled={GruppennameValidationFailed || !GruppennameEdited} variant='contained' onClick={this.addGruppe} color='primary'>
                  Hinzufügen
             </Button>
            }
          </DialogActions>
        </Dialog>
        : null
    );
  }
}

/** Komponentenspezifische styles */
const styles = theme => ({
  root: {
    width: '100%',
  },
  closeButton: {
    position: 'absolute',
    right: theme.spacing(1),
    top: theme.spacing(1),
    color: theme.palette.grey[500],
  },
});

/** PropTypes */
GruppeForm.propTypes = {
  /** @ignore */
  classes: PropTypes.object.isRequired,
  /** EinkaufsgruppeBO wird bearbeitet */
  Gruppe: PropTypes.object,
  /** Wenn dies zutrifft wird die "Form" gerendert */
  show: PropTypes.bool.isRequired,
  /**  
   * Funktion die das Schließen des Dialogs verwaltet
   * Sendet das Aktualisierte oder neu erstellte EinkaufsgruppeBO als Parameter, oder als "null" im Abbruchsfall.
   *  
   * Signature: onClose(EinkaufsgruppeBO Gruppe);
   */
  onClose: PropTypes.func.isRequired,
}

export default withStyles(styles)(GruppeForm);
