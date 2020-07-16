import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { withStyles, ListItem } from '@material-ui/core';
import { Button, List } from '@material-ui/core';
import AddIcon from '@material-ui/icons/Add';
import { ListAPI } from '../api';
import InlineError from './dialogs/InlineError';
import LoadingBar from './dialogs/LoadingBar';
import ShoppingListEntry from './ShoppingListEntry';


class ShoppingList extends Component {

  constructor(props) {
    super(props);

    this.state = {
      shoppinglists: [],
      loadingInProgress: false,
      loadingShoppingListError: null,
      addingShoppingListError: null,
    };
  }

  getShoppingLists = () => {
    ListAPI.getAPI().getShoppingListsOfGroups(this.props.group.getID()).then(shoppinglistBOs =>
      this.setState({  
        shoppinglists: shoppinglistBOs,
        loadingInProgress: false,
        loadingShoppingListError: null
      })).catch(e =>
        this.setState({ 
          shoppinglists: [],
          loadingInProgress: false,
          loadingShoppingListError: e
        })
      );

    this.setState({
      loadingInProgress: true,
      loadingShoppingListError: null
    });
  }

  /** Lifecycle Methode, die aufgerufen wird, wenn die Komponente dem Browser DOM hizugefügt wird */
  componentDidMount() {
    this.getShoppingLists();
  }

  componentDidUpdate(prevProps) {
    // reload accounts if shown state changed. Occures if the CustomerListEntrys ExpansionPanel was expanded
    // if ((this.props.show !== prevProps.show)) {
    //   this.getAccounts();
    // }
  }

  /** Fügt der Gruppe eine Einkaufsliste hinzu */
  addShoppingList = () => {
    ListAPI.getAPI().addShoppingListForGroup(this.props.group.getID()).then(shoppinglistBO => {
      this.setState({  
        shoppinglists: [...this.state.shoppinglists, shoppinglistBO],
        loadingInProgress: false,  
        addingShoppingListError: null
      })
    }).catch(e =>
      this.setState({ 
        shoppinglists: [],
        loadingInProgress: false,
        addingShoppingListError: e
      })
    );

    this.setState({
      loadingInProgress: true,
      addingShoppingListError: null
    });
  }

  deleteShoppingListHandler = (deletedShoppingList) => {
    this.setState({
      shoppinglists: this.state.shoppinglists.filter(shoppinglist => shoppinglist.getID() !== deletedShoppingList.getID())
    })
  }

  /** Rendered die Komponente */
  render() {
    const { classes, group } = this.props;
    const { shoppinglists, loadingInProgress, loadingShoppingListError, addingShoppingListError } = this.state;

    return (
      <div className={classes.root}>
        <List className={classes.shoppingList}>
          {
            shoppinglists.map(shoppinglist => <ShoppingListEntry key={shoppinglist.getID()} group={group} shoppinglists={shoppinglists} onShoppingListDeleted={this.deleteShoppingListHandler}
              show={this.props.show} />)
          }
          <ListItem>
            <LoadingBar show={loadingInProgress} />
            <InlineError error={loadingShoppingListError} InlineError={`List of Shoppinglists for groups ${group.getID()} could not be loaded.`} onReload={this.getShoppingLists} />
            <InlineError error={addingShoppingListError} InlineError={`List of Shoppinglists for groups ${group.getID()} could not be added.`} onReload={this.addShoppingList} />
          </ListItem>
        </List>
        <Button className={classes.addShoppingListButton} variant='contained' color='primary' startIcon={<AddIcon />} onClick={this.addShoppingList}>
            Neue Einkaufsliste
        </Button>
      </div>
    );
  }
}

/** Styling */
const styles = theme => ({
  root: {
    width: '100%',
  },
  shoppingList: {
    marginBottom: theme.spacing(2),
  },
  addShoppingListButton: {
    position: 'absolute',
    right: theme.spacing(3),
    bottom: theme.spacing(1),
  }
});

/** PropTypes */
shoppingList.propTypes = {
  /** @ignore */
  classes: PropTypes.object.isRequired,
  group: PropTypes.object.isRequired,
  show: PropTypes.bool.isRequired
}

export default withStyles(styles)(ShoppingList);
