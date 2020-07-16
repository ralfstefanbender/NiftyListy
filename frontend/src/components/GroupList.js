import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { withStyles, Button, TextField, InputAdornment, IconButton, Grid, Typography } from '@material-ui/core';
import AddIcon from '@material-ui/icons/Add';
import ClearIcon from '@material-ui/icons/Clear'
import { withRouter } from 'react-router-dom';
import { ListAPI } from '../api';
import InlineError from './dialogs/InlineError';
import LoadingBar from './dialogs/LoadingBar';
import GruppeForm from './dialogs/GruppeForm';
import GroupListEntry from './GroupListEntry';


class GroupList extends Component {

  constructor(props) {
    super(props);


    let expandedID = null;

    if (this.props.location.expandGruppe) {
      expandedID = this.props.location.expandGruppe.getID();
    }

    // Initialisierung eines leeren Zustandes (state)
    this.state = {
      GruppenArray: [],
      filteredGruppe: [],
      GruppeFilterStr: '',
      error: null,
      loadingInProgress: false,
      expandedGruppeID: expandedID,
      showGruppeForm: false
    };
  }

  /** Fetch Befehl für alle EinkaufsgruppeBOs aus dem Backend */
  getGruppe = () => {
    ListAPI.getAPI().getGruppe()
      .then(EinkaufsgruppeBO =>
        this.setState({               // Erstellt einen neuen State sobald alle GruppeBOs gefetched sind
          GruppenArray: EinkaufsgruppeBO,
          filteredGruppe: [...EinkaufsgruppeBO], // speichert eine Kopie
          loadingInProgress: false,   // Der Ladebalken wird "vrborgen"
          error: null
        })).catch(e =>
          this.setState({             // Setzt den Zustand mit dem entsprechenden Error zurück 
            GruppenArray: [],
            loadingInProgress: false, // Der Ladebalken wird wieder "verborgen"
            error: e
          })
        );

    // Es wird der Ladevorgang gestartet
    this.setState({
      loadingInProgress: true,
      error: null
    });
  }

  /** Lifecycle Methode, die aufgerufen wird, wenn die Komponente dem Browser DOM hizugefügt wird */
  componentDidMount() {
    this.getGruppe();
  }

  /** 
   * Verwaltet das onExpandedStateChange Event Einer Listeneintrags Komponente. 
   * Steuert den geöffneten Zustand eines Listeneintrags des betroffenen GruppeBOs
   */
  onExpandedStateChange = Gruppe => {
    // Der Defaultwert für den geöffneten Zustand wird auf Null gesetzt
    let newID = null;

    // Wen der gleiche Eintrag angeklickt wird, so wird er geschlossen, ansonsten wird ein neuer geöffnet
    if (Gruppe.getID() !== this.state.expandedGruppeID) {
      // Öffnet den Listeneintrag des Gruppes über die GruppeID
      newID = Gruppe.getID();
    }

    this.setState({
      expandedGruppeID: newID,
    });
  }

  /** 
   * Verwaltet die "GruppeDeleted" Ereignisse der Listeneintrags Komponente
   */
  GruppeDeleted = Gruppe => {
    const newGruppenArray = this.state.GruppenArray.filter(GruppeFormState => GruppeFormState.getID() !== Gruppe.getID());
    this.setState({
      GruppenArray: newGruppenArray,
      filteredGruppe: [...newGruppenArray],
      showGruppeForm: false
    });
  }

  /** Verwalted das Gruppehinzufügen Ereignis wenn der Knopf betätigt wird */
  addGruppeButtonClicked = event => {
    // Schließe nicht den geöffneten Zustand
    event.stopPropagation();
    //Zeige den neuen Gruppeeintrag
    this.setState({
      showGruppeForm: true
    });
  }

  /** Verwaltet das "Schließen" Ereignis beim Erstellen einer neuen Gruppe */
  GruppeFormClosed = Gruppe => {
    // Die jeweilige Gruppe ist nicht null und wurde daher erstellt
    if (Gruppe) {
      const newGruppenArray = [...this.state.GruppenArray, Gruppe];
      this.setState({
        GruppenArray: newGruppenArray,
        filteredGruppe: [...newGruppenArray],
        showGruppeForm: false
      });
    } else {
      this.setState({
        showGruppeForm: false
      });
    }
  }

  /** Verwaltet das Filter Ereignis beim filtern von Gruppen */
  filterFieldValueChange = event => {
    const value = event.target.value.toLowerCase();
    this.setState({
      filteredGruppe: this.state.GruppenArray.filter(Gruppe => {
        let GruppeNameContainsValue = Gruppe.getGruppeName().toLowerCase().includes(value);
        return GruppeNameContainsValue;
      }),
      GruppeFilter: value
    });
  }

  /** Verwaltet das "Schließen" Ereignis des Filtern */
  clearFilterFieldButtonClicked = () => {
    // Der Filter wird zurückgesetzt
    this.setState({
      filteredGruppe: [...this.state.GruppenArray],
      GruppeFilter: ''
    });
  }

  /** Rendern der gesamten Komponente GroupList */
  render() {
    const { classes } = this.props;
    const { filteredGruppe, GruppeFilter, expandedGruppeID, loadingInProgress, error, showGruppeForm } = this.state;

    return (
      <div className={classes.root}>
        <Grid className={classes.GruppeFilter} container spacing={1} justify='flex-start' alignItems='center'>
          <Grid item>
            <Typography>
              Filtern der Gruppen nach Namen:
              </Typography>
          </Grid>
          <Grid item xs={4}>
            <TextField
              autoFocus
              fullWidth
              id='GruppeFilter'
              type='text'
              value={GruppeFilter}
              onChange={this.filterFieldValueChange}
              InputProps={{
                endAdornment: <InputAdornment position='end'>
                  <IconButton onClick={this.clearFilterFieldButtonClicked}>
                    <ClearIcon />
                  </IconButton>
                </InputAdornment>,
              }}
            />
          </Grid>
          <Grid item xs />
          <Grid item>
            <Button variant='contained' color='primary' startIcon={<AddIcon />} onClick={this.addGruppeButtonClicked}>
              Gruppe hinzufügen
          </Button>
          </Grid>
        </Grid>
        { 
          // Zeige die Liste der ListenEintrags Komponenten
          // Verwende keinen expliziten Abgleich da die "expandedGruppeID" auch in Str Form vorliegen könnte, wenn sie aus URL Parametern entnommen wurde
          filteredGruppe.map(Gruppe =>
            <GroupListEntry key={Gruppe.getID()} Gruppe={Gruppe} expandedState={expandedGruppeID === Gruppe.getID()}
              onExpandedStateChange={this.onExpandedStateChange}
              onGruppeDeleted={this.GruppeDeleted}
            />)
        }
        <LoadingBar show={loadingInProgress} />
        <InlineError error={error} InlineError={`Die Gruppe konnte nicht geladen werden`} onReload={this.getGruppe} />
        <GruppeForm show={showGruppeForm} onClose={this.GruppeFormClosed} />
      </div>
    );
  }
}

/** Komponenten spezifisches styling */
const styles = theme => ({
  root: {
    width: '100%',
  },
  GruppeFilter: {
    marginTop: theme.spacing(2),
    marginBottom: theme.spacing(1),
  }
});

/** PropTypes */
GroupList.propTypes = {
  /** @ignore */
  classes: PropTypes.object.isRequired,
  /** @ignore */
  location: PropTypes.object.isRequired,
}

export default withRouter(withStyles(styles)(GroupList));