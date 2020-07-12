import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { withStyles, Button, TextField, InputAdornment, IconButton, Grid, Typography } from '@material-ui/core';
import AddIcon from '@material-ui/icons/Add';
import ClearIcon from '@material-ui/icons/Clear'
import { withRouter } from 'react-router-dom';
import { ListAPI } from '../api';
/*import ContextErrorMessage from './dialogs/ContextErrorMessage';
import LoadingProgress from './dialogs/LoadingProgress';
import ArtikelForm from './dialogs/ArtikelForm';
import ListenEintrag from './ListenEintrag';*/


class GroupList extends Component {

  constructor(props) {
    super(props);


    let expandedID = null;

    if (this.props.location.expandArtikel) {
      expandedID = this.props.location.expandArtikel.getID();
    }

    // Initialisierung eines leeren Zustandes (state)
    this.state = {
      ArtikelArray: [],
      filteredArtikel: [],
      ArtikelFilterStr: '',
      error: null,
      loadingInProgress: false,
      expandedArtikelID: expandedID,
      showArtikelForm: false
    };
  }

  /** Fetch Befehl für alle ArtikelBOs aus dem Backend */
  getArtikel = () => {
    ListAPI.getAPI().getArtikel()
      .then(articleBO =>
        this.setState({               // Erstellt einen neuen State sobald alle ArtikelBOs gefetched sind
          ArtikelArray: articleBO,
          filteredArtikel: [...articleBO], // speichert eine Kopie
          loadingInProgress: false,   // Der Ladebalken wird "vrborgen"
          error: null
        })).catch(e =>
          this.setState({             // Setzt den Zustand mit dem entsprechenden Error zurück 
            ArtikelArray: [],
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
    this.getArtikel();
  }

  /** 
   * Verwaltet das onExpandedStateChange Event Einer Listeneintrags Komponente. 
   * Steuert den geöffneten Zustand eines Listeneintrags des betroffenen ArtikelBOs
   */
  onExpandedStateChange = Artikel => {
    // Der Defaultwert für den geöffneten Zustand wird auf Null gesetzt
    let newID = null;

    // Wen der gleiche Eintrag angeklickt wird, so wird er geschlossen, ansonsten wird ein neuer geöffnet
    if (Artikel.getID() !== this.state.expandedArtikelID) {
      // Öffnet den Listeneintrag des Artikels über die ArtikelID
      newID = Artikel.getID();
    }

    this.setState({
      expandedArtikelID: newID,
    });
  }

  /** 
   * Verwaltet die "ArtikelDeleted" Ereignisse der Listeneintrags Komponente
   */
  ArtikelDeleted = Artikel => {
    const newArtikelArray = this.state.ArtikelArray.filter(ArtikelFormState => ArtikelFormState.getID() !== Artikel.getID());
    this.setState({
      ArtikelArray: newArtikelArray,
      filteredArtikel: [...newArtikelArray],
      showArtikelForm: false
    });
  }

  /** Verwalted das Artikelhinzufügen Ereignis wenn der Knopf betätigt wird */
  addArtikelButtonClicked = event => {
    // Schließe nicht den geöffneten Zustand
    event.stopPropagation();
    //Zeige den neuen Artikeleintrag
    this.setState({
      showArtikelForm: true
    });
  }

  /** Verwaltet das "Schließen" Ereignis beim erstellen neuer Artikel */
  ArtikelFormClosed = Artikel => {
    // Der jeweilige Artikel ist nicht null und wurde daher erstellt
    if (Artikel) {
      const newArtikelArray = [...this.state.ArtikelArray, Artikel];
      this.setState({
        ArtikelArray: newArtikelArray,
        filteredArtikel: [...newArtikelArray],
        showArtikelForm: false
      });
    } else {
      this.setState({
        showArtikelForm: false
      });
    }
  }

  /** Verwaltet das Filter Ereignis beim filtern von Artikeln */
  filterFieldValueChange = event => {
    const value = event.target.value.toLowerCase();
    this.setState({
      filteredArtikel: this.state.ArtikelArray.filter(Artikel => {
        let ArtikelNameContainsValue = Artikel.getArtikelName().toLowerCase().includes(value);
        return ArtikelNameContainsValue;
      }),
      ArtikelFilter: value
    });
  }

  /** Verwaltet das "Schließen" Ereignis des Filtern */
  clearFilterFieldButtonClicked = () => {
    // Der Filter wird zurückgesetzt
    this.setState({
      filteredArtikel: [...this.state.ArtikelArray],
      ArtikelFilter: ''
    });
  }

  /** Rendern der gesamten Komponente GroupList */
  render() {
    const { classes } = this.props;
    const { filteredArtikel, ArtikelFilter, expandedArtikelID, loadingInProgress, error, showArtikelForm } = this.state;

    return (
      <div className={classes.root}>
        <Grid className={classes.ArtikelFilter} container spacing={1} justify='flex-start' alignItems='center'>
          <Grid item>
            <Typography>
              Filter Artikel nach Namen:
              </Typography>
          </Grid>
          <Grid item xs={4}>
            <TextField
              autoFocus
              fullWidth
              id='ArtikelFilter'
              type='text'
              value={ArtikelFilter}
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
            <Button variant='contained' color='primary' startIcon={<AddIcon />} onClick={this.addArtikelButtonClicked}>
              Artikel hinzufügen
          </Button>
          </Grid>
        </Grid>
        { 
          // Zeige die Liste der ListenEintrags Komponenten
          // Verwende keinen expliziten Abgleich da die "expandedArtikelID" auch in Str Form vorliegen könnte, wenn sie aus URL Parametern entnommen wurde
          filteredArtikel.map(Artikel =>
            <ListenEintrag key={Artikel.getID()} Artikel={Artikel} expandedState={expandedArtikelID === Artikel.getID()}
              onExpandedStateChange={this.onExpandedStateChange}
              onArtikelDeleted={this.ArtikelDeleted}
            />)
        }
        <LoadingProgress show={loadingInProgress} />
        <ContextErrorMessage error={error} contextErrorMsg={`Die Artikel konnten nicht geladen werden`} onReload={this.getArtikel} />
        <ArtikelForm show={showArtikelForm} onClose={this.ArtikelFormClosed} />
      </div>
    );
  }
}

/** Komponenten spezifisches styling */
const styles = theme => ({
  root: {
    width: '100%',
  },
  ArtikelFilter: {
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