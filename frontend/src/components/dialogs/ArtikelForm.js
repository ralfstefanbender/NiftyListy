import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { withStyles, Button, IconButton, Dialog, DialogTitle, DialogContent, DialogContentText, DialogActions, TextField } from '@material-ui/core';
import CloseIcon from '@material-ui/icons/Close';
import { ListAPI, ArtikelBO } from '../../api';
import InlineError from './InlineError';
import LoadingBar from './LoadingBar';


class ArtikelForm extends Component {

  constructor(props) {
    super(props);

    let art = '';
    if (props.artikel) {
      art = props.artikel.getArtikel()
    }

    this.state = {
      artikel: art,
      artikelValidationFailed: false,
      artikelEdited: false,
      addingInProgress: false,
      updatingInProgress: false,
      addingError: null,
      updatingError: null
    };
    this.baseState = this.state;
  }

  /** Einfügeoption für Artikel */
  addArtikel = () => {
    let newArtikel = new ArtikelBO(this.state.artikel);
    ListAPI.getAPI().addArtikel(newArtikel).then(artikel => {
      // erfolgreicher Aufruf im Backend 
      this.setState(this.baseState);
      this.props.onClose(artikel); 
    }).catch(e =>
      this.setState({
        updatingInProgress: false,    
        updatingError: e             
      })
    );

    this.setState({
      updatingInProgress: true,      
      updatingError: null            
    });
  }

  /** Artikel neu laden */
  updateArtikel = () => {
    // Der originale Artikel wird dupliziert, falls das Backend nicht erfolgreich ist
    let updatedArtikel = Object.assign(new ArtikelBO(), this.props.artikel);
    updatedArtikel.setArtikel(this.state.artikel);
    ListAPI.getAPI().updateArtikel(updatedArtikel).then(artikel => {
      this.setState({
        updatingInProgress: false,              
        updatingError: null                     
      });
      // keep the new state as base state
      this.baseState.artikel = this.state.artikel;
      this.props.onClose(updatedArtikel);    
    }).catch(e =>
      this.setState({
        updatingInProgress: false,             
        updatingError: e                      
      })
    );

    // set loading to true
    this.setState({
      updatingInProgress: true,                
      updatingError: null                     
    });
  }

  textFieldValueChange = (event) => {
    const value = event.target.value;

    let error = false;
    if (value.trim().length === 0) {
      error = true;
    }

    this.setState({
      [event.target.id]: event.target.value,
      [event.target.id + 'ValidationFailed']: error,
      [event.target.id + 'Edited']: true
    });
  }

  handleClose = () => {
    this.setState(this.baseState);
    this.props.onClose(null);
  }

  /** Rendered die Komponente */
  render() {
    const { classes, artikel, show } = this.props;
    const { artikel, artikelValidationFailed, artikelEdited, addingInProgress,
      addingError, updatingInProgress, updatingError } = this.state;

    let title = '';
    let header = '';

    if (artikel) {
      title = 'Update den Artikel';
      header = `Artikel ID: ${artikel.getID()}`;
    } else {
      title = 'Erstelle einen neuen Artikel';
      header = 'Gebe die Artikel Daten ein';
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
              <TextField autoFocus type='text' required fullWidth margin='normal' id='artikel' label='Artikel:' value={artikel} 
                onChange={this.textFieldValueChange} error={artikelValidationFailed} 
                helperText={artikelValidationFailed ? 'Der Artikel muss mindestens ein Zeichen enthalten' : ' '} />
            </form>
            <LoadingBar show={addingInProgress || updatingInProgress} />
            {
              artikel ?
                <InlineError error={updatingError} InlineError={`Der Artikel ${artikel.getID()} konnte nicht geladen werden.`} onReload={this.updateArtikel} />
                :
                <InlineError error={addingError} InlineError={`Der Artikel konnte nicht hinzugefügt werdeb.`} onReload={this.addArtikel} />
            }
          </DialogContent>
          <DialogActions>
            <Button onClick={this.handleClose} color='secondary'>
              Abbruch
            </Button>
            {
              // Wenn ein Artikel vorhanden ist, zeige ein update-Button, ansonsten ein hinzufügen-Button
              artikel ?
                <Button disabled={artikelValidationFailed} variant='contained' onClick={this.updateArtikel} color='primary'>
                  Update
              </Button>
                : <Button disabled={artikelValidationFailed || !artikelEdited} variant='contained' onClick={this.addArtikel} color='primary'>
                  Hinzufügen
             </Button>
            }
          </DialogActions>
        </Dialog>
        : null
    );
  }
}

/** Komponenten Style */
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
ArtikelForm.propTypes = {
  /** @ignore */
  classes: PropTypes.object.isRequired,
  artikel: PropTypes.object,
  show: PropTypes.bool.isRequired,
  onClose: PropTypes.func.isRequired,
}

export default withStyles(styles)(ArtikelForm);
