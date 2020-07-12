import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { withStyles, Button, IconButton, Dialog, DialogTitle, DialogContent, DialogContentText, DialogActions } from '@material-ui/core';
import CloseIcon from '@material-ui/icons/Close';
import { ListAPI } from '../../api';
import ContextErrorMessage from './ContextErrorMessage';
// import LoadingProgress from './LoadingProgress';

class ArtikelEntfernen extends Component {

  constructor(props) {
    super(props);

    // Init den state
    this.state = {
      deletingInProgress: false,
      deletingError: null
    };
  }

  /** Entferne den Artikel */
  entferneArtikel = () => {
    ListAPI.getAPI().entferneArtikel(this.props.artikel.getID()).then(artikel => {
      this.setState({
        deletingInProgress: false,              
        deletingError: null                     
      });
      this.props.onClose(this.props.artikel);  
    }).catch(e =>
      this.setState({
        deletingInProgress: false,              
        deletingError: e                      
      })
    );

    // loading wird true gesetzt
    this.setState({
      deletingInProgress: true,                
      deletingError: null                     
    });
  }

  /** Hier wird der der Schließ- / Abbruchknopf per click event gesteuert */
  handleClose = () => {
    // console.log(event);
    this.props.onClose(null);
  }

  /** Rendered die Komponente */
  render() {
    const { classes, artikel, show } = this.props;
    const { deletingInProgress, deletingError } = this.state;

    return (
      show ?
        <Dialog open={show} onClose={this.handleClose}>
          <DialogTitle id='delete-dialog-title'>Entferne den Artikel
            <IconButton className={classes.closeButton} onClick={this.handleClose}>
              <CloseIcon />
            </IconButton>
          </DialogTitle>
          <DialogContent>
            <DialogContentText>
              Bist du sicher? '{artikel.getArtikel()} (ID: {artikel.getID()})?
            </DialogContentText>
            <LoadingProgress show={deletingInProgress} />
            <ContextErrorMessage error={deletingError} InlineError={`Der Artikel '${artikel.getArtikel()} (ID: ${artikel.getID()}) konnte nicht entfernt werden.`}
              onReload={this.entferneArtikel} />
          </DialogContent>
          <DialogActions>
            <Button onClick={this.handleClose} color='secondary'>
              Abbruch
            </Button>
            <Button variant='contained' onClick={this.entferneArtikel} color='primary'>
              Löschen
            </Button> 
          </DialogActions>
        </Dialog>
        : null
    );
  }
}

/** Style der Komponente */
const styles = theme => ({
  closeButton: {
    position: 'absolute',
    right: theme.spacing(1),
    top: theme.spacing(1),
    color: theme.palette.grey[500],
  }
});

/** PropTypes */
ArtikelEntfernen.propTypes = {
  /** @ignore */
  classes: PropTypes.object.isRequired,
  /** Die CustomerBO werden gelöscht*/
  artikel: PropTypes.object.isRequired,
  /** Wenn es true ist, wird der dialog gerendered */
  show: PropTypes.bool.isRequired,
  /**  
   * Handler function wird aufgerufen, wenn der dialog geschlossen ist.
   * Sendet den gelöschten ArtikelBO als Parameter oder Null, wenn "Abbruch" geklickt wird
   */
  onClose: PropTypes.func.isRequired,
}

export default withStyles(styles)(ArtikelEntfernen);
