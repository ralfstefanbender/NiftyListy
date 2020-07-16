import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { withStyles, Typography, ExpansionPanel, ExpansionPanelSummary, ExpansionPanelDetails, Grid } from '@material-ui/core';
import { Button, ButtonGroup } from '@material-ui/core';
import ExpandMoreIcon from '@material-ui/icons/ExpandMore';
import GruppeForm from './dialogs/GruppeForm';
//import GruppeDeleteDialog from './dialogs/GruppeDeleteDialog';
import ShoppingList from './ShoppingList';


class GroupListEntry extends Component {

  constructor(props) {
    super(props);

    // Initialisirt einen Zustand
    this.state = {
      Gruppe: props.Gruppe,
      showGruppeForm: false,
      //showGruppeDeleteDialog: false,
    };
  }

  /** Verwaltet onChange Ereignisse des Expansion Pannels */
  expansionPanelStateChanged = () => {
    this.props.onExpandedStateChange(this.props.Gruppe);
  }

  /** Verwaltet das onListeDelete Ereignis eines EinkaufslistenListEntry  
  deleteListeHandler = (deletedListe) => {
    this.setState({
      Listen: this.state.Listen.filter(Liste => Liste.getID() !== deletedListe.getID())
    })
  }*/

  /** Verwaltet das Knopfdruck Ereignis des Gruppe bearbeiten Knopfes */
  editGruppeButtonClicked = (event) => {
    event.stopPropagation();
    this.setState({
      showGruppeForm: true
    });
  }

  /** Verwaltet das Schließen der GruppeForm */
  GruppeFormClosed = (Gruppe) => {
    // Gruppe ist nicht "null" und kann daher bearbeitet werden
    if (Gruppe) {
      this.setState({
        Gruppe: Gruppe,
        showGruppeForm: false
      });
    } else {
      this.setState({
        showGruppeForm: false
      });
    }
  }

  /** Verwaltet das onClick Ereignis des Gruppe löschen Knopfes */
  deleteGruppeButtonClicked = (event) => {
    event.stopPropagation();
    this.setState({
      showGruppeDeleteDialog: true
    });
  }

  /** Verwaltet das onClose Ereignis des GruppeDelete Dialogs */
  deleteGruppeDialogClosed = (Gruppe) => {
    // Wenn die Gruppe nicht "null" ist, so wird sie entfernt
    if (Gruppe) {
      this.props.onGruppeDeleted(Gruppe);
    };

    // Verberge den showGruppeDelete Dialog
    this.setState({
      showGruppeDeleteDialog: false
    });
  }

  /** Rendert die Komponente */
  render() {
    const { classes, expandedState } = this.props;
    const { Gruppe, showGruppeForm, showGruppeDeleteDialog } = this.state;


    return (
      <div>
        <ExpansionPanel defaultExpanded={false} expanded={expandedState} onChange={this.expansionPanelStateChanged}>
          <ExpansionPanelSummary
            expandIcon={<ExpandMoreIcon />}
            id={`Gruppe${Gruppe.getID()}Einkaufslistenpanel-header`}
          >
            <Grid container spacing={1} justify='flex-start' alignItems='center'>
              <Grid item>
                <Typography variant='body1' className={classes.heading}>{Gruppe.getGruppenname()}
                </Typography>
              </Grid>
              <Grid item>
                <ButtonGroup variant='text' size='small'>
                  <Button color='primary' onClick={this.editGruppeButtonClicked}>
                    Bearbeiten
                  </Button>
                  <Button color='secondary' onClick={this.deleteGruppeButtonClicked}>
                    Löschen
                  </Button>
                </ButtonGroup>
              </Grid>
              <Grid item xs />
              <Grid item>
                <Typography variant='body2' color={'textSecondary'}>Alle Einkaufslisten der Gruppe</Typography>
              </Grid>
            </Grid>
          </ExpansionPanelSummary>
          <ExpansionPanelDetails>
            <ShoppingList show={expandedState} Gruppe={Gruppe} />
          </ExpansionPanelDetails>
        </ExpansionPanel>
        <GruppeForm show={showGruppeForm} Gruppe={Gruppe} onClose={this.GruppeFormClosed} />
        <GruppeDeleteDialog show={showGruppeDeleteDialog} Gruppe={Gruppe} onClose={this.deleteGruppeDialogClosed} />
      </div>
    );
  }
}

/** Komponentenspezifische styles */
const styles = theme => ({
  root: {
    width: '100%',
  }
});

/** PropTypes */
GroupListEntry.propTypes = {
  /** @ignore */
  classes: PropTypes.object.isRequired,
  /** Das EinkaufsgruppenBO wird gerendert */
  Gruppe: PropTypes.object.isRequired,
  /** Der Zustand dieser GroupListEntry. Bei True werden alle Gruppen mit den zugehögigen Listen ausgegeben */
  expandedState: PropTypes.bool.isRequired,
  /**  Der Handler ist Zudtändig für das Auf und Zuklappen des Pannels (exanding/collapsing) des GroupListEntry 
   * 
   */
  onExpandedStateChange: PropTypes.func.isRequired,
  /** 
   *  Event Handler die aufgerufen wird nach erfolgreichem Löschen einer Gruppe
   * 
   */
  onGruppeDeleted: PropTypes.func.isRequired
}

export default withStyles(styles)(GroupListEntry);
