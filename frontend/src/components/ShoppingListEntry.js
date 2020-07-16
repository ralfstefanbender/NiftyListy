import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { withStyles, Button, ListItem, ListItemSecondaryAction, Link, Typography } from '@material-ui/core';
import DeleteIcon from '@material-ui/icons/Delete';
import { ListAPI } from '../api';
import InlineError from './dialogs/InlineError';
import LoadingBar from './dialogs/LoadingBar';


class ShoppingListEntry extends Component {

  constructor(props) {
    super(props);

    this.state = {
      loadingInProgress: false,
      deletingInProgress: false,
      loadingError: null,
      deletingError: null,
    };
  }

    deleteShoppingList = () => {
    const { shoppinglist } = this.props;
    ListAPI.getAPI().deleteShoppingList(shoppinglist.getID()).then(() => {
      this.setState({ 
        deletingInProgress: false, 
        deletingError: null
      })
      this.props.onShoppingListDeleted(shoppinglist);
    }).catch(e =>
      this.setState({ 
        deletingInProgress: false,
        deletingError: e
      })
    );

    this.setState({
      deletingInProgress: true,
      deletingError: null
    });
  }

  /** Rendered die Komponente */
  render() {
    const { shoppinglist } = this.props;
    const { loadingInProgress, deletingInProgress, deletingError } = this.state;

    return (
      <div>
        <ListItem>
          <ListItemSecondaryAction>
            <Button color='secondary' size='small' startIcon={<DeleteIcon />} onClick={this.deleteShoppingList}>
              Löschen
            </Button>
          </ListItemSecondaryAction>
        </ListItem>
        <ListItem>
          <LoadingBar show={loadingInProgress || deletingInProgress} />
          <InlineError error={deletingError} InlineError={`Die Einkaufsliste ${shoppinglist.getID()} konnte nicht gelöscht werden.`} onReload={this.deleteShoppingList} />
        </ListItem>
      </div>
    );
  }
}


/** Styling */
const styles = theme => ({
  root: {
    width: '100%'
  }, 
  buttonMargin: {
    marginRight: theme.spacing(2),
  },
  shoppinglistEntry: {
    fontSize: theme.typography.pxToRem(15),
    flexBasis: '33.33%',
    flexShrink: 0,
  }
});

/** PropTypes */
ShoppingListEntry.propTypes = {
  /** @ignore */
  classes: PropTypes.object.isRequired,
  group: PropTypes.object.isRequired,
  shoppinglist: PropTypes.object.isRequired,
  onShoppingListDeleted: PropTypes.func.isRequired,
  show: PropTypes.bool.isRequired
}

export default withStyles(styles)(ShoppingListEntry);
