// Nicht vollständig! Einige Funktionen fehlen noch!

import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { withStyles, Button, ListItem, ListItemSecondaryAction, Link, Typography } from '@material-ui/core';
import DeleteIcon from '@material-ui/icons/Delete';
import { ListAPI } from '../api';
import InlineError from './dialogs/InlineError';
import LoadingBar from './dialogs/LoadingBar';


class ArticleListEntry extends Component {

  constructor(props) {
    super(props);

    this.state = {
      loadingInProgress: false,
      deletingInProgress: false,
      loadingError: null,
      deletingError: null,
    };
  }

    deleteArticleList = () => {
    const { articlelist } = this.props;
    ListAPI.getAPI().deleteArticleList(articlelist.getID()).then(() => {
      this.setState({  
        deletingInProgress: false, 
        deletingError: null
      })
      this.props.onArticleListDeleted(articlelist);
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
    const { articlelist } = this.props;
    const { loadingInProgress, deletingInProgress, deletingError } = this.state;

    return (
      <div>
        <ListItem>
          <ListItemSecondaryAction>
            <Button color='secondary' size='small' startIcon={<DeleteIcon />} onClick={this.deleteArticleList}>
              Löschen
            </Button>
          </ListItemSecondaryAction>
        </ListItem>
        <ListItem>
          <LoadingBar show={loadingInProgress || deletingInProgress} />
          <InlineError error={deletingError} InlineError={`Die Einkaufsliste ${articlelist.getID()} konnte nicht gelöscht werden.`} onReload={this.deleteArticleList} />
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
  articlelistEntry: {
    fontSize: theme.typography.pxToRem(15),
    flexBasis: '33.33%',
    flexShrink: 0,
  }
});

/** PropTypes */
ArticleListEntry.propTypes = {
  /** @ignore */
  classes: PropTypes.object.isRequired,
  shoppinglist: PropTypes.object.isRequired,
  articlelist: PropTypes.object.isRequired,
  onArticleListDeleted: PropTypes.func.isRequired,
  show: PropTypes.bool.isRequired
}

export default withStyles(styles)(ArticleListEntry);
