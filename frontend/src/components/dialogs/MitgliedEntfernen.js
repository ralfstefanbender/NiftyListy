import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { withStyles, Button, IconButton, Dialog, DialogTitle, DialogContent, DialogContentText, DialogActions } from '@material-ui/core';
import CloseIcon from '@material-ui/icons/Close';
import { ListAPI } from '../../api';
import InlineError from './InlineError';
import LoadingBar from './LoadingBar';

class MitgliedEntfernen extends Component {

  constructor(props) {
    super(props);

    // Init den state
    this.state = {
      deletingInProgress: false,
      deletingError: null
    };
  }

  /** Entferne das Gruppenmitglied */
  entferneGruppenmitglied = () => {
    ListAPI.getAPI().entferneGruppenmitglied(this.props.gruppenmitglied.getID()).then(gruppenmitglied => {
      this.setState({
        deletingInProgress: false,              // disable loading indicator  
        deletingError: null                     // no error message
      });
      this.props.onClose(this.props.artikel);  // call the parent with the deleted customer
    }).catch(e =>
      this.setState({
        deletingInProgress: false,              // disable loading indicator 
        deletingError: e                        // show error message
      })
    );

    this.setState({
      deletingInProgress: true,                 // show loading indicator
      deletingError: null                       // disable error message
    });
  }

  /** Bahandelt die Schließ- bzw. Abbruchfunktion */
  handleClose = () => {
    this.props.onClose(null);
  }

  /** Rendered die Komponente */
  render() {
    const { classes, gruppenmitglied, show } = this.props;
    const { deletingInProgress, deletingError } = this.state;

    return (
      show ?
        <Dialog open={show} onClose={this.handleClose}>
          <DialogTitle id='delete-dialog-title'>Entferne das Gruppenmitglied
            <IconButton className={classes.closeButton} onClick={this.handleClose}>
              <CloseIcon />
            </IconButton>
          </DialogTitle>
          <DialogContent>
            <DialogContentText>
              Bist du sicher? '{gruppenmitglied.getGruppenmitglied()} (ID: {gruppenmitglied.getID()})?
            </DialogContentText>
            <LoadingBar show={deletingInProgress} />
            <InlineError error={deletingError} InlineError={`Das Gruppenmitglied '${ruppenmitglied.getGruppenmitglied()} (ID: ${gruppenmitglied.getID()}) konnte nicht entfernt werden.`}
              onReload={this.entferneGruppenmitglied} />
          </DialogContent>
          <DialogActions>
            <Button onClick={this.handleClose} color='secondary'>
              Abbruch
            </Button>
            <Button variant='contained' onClick={this.entferneGruppenmitglied} color='primary'>
              Löschen
            </Button> 
          </DialogActions>
        </Dialog>
        : null
    );
  }
}

/**Komponenten Style */
const styles = theme => ({
  closeButton: {
    position: 'absolute',
    right: theme.spacing(1),
    top: theme.spacing(1),
    color: theme.palette.grey[500],
  }
});

/** PropTypes */
MitgliedEntfernen.propTypes = {
  /** @ignore */
  classes: PropTypes.object.isRequired,
  artikel: PropTypes.object.isRequired,
  show: PropTypes.bool.isRequired,
  onClose: PropTypes.func.isRequired,
}

export default withStyles(styles)(MitgliedEntfernen);
