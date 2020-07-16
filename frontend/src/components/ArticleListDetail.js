import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { withStyles, Typography, Paper } from '@material-ui/core';
/**import { ListAPI } from '../api';*/
import InlineError from './dialogs/InlineError';
import LoadingBar from './dialogs/LoadingBar';


class ArticleListDetails extends Component {

  constructor(props) {
    super(props);

    this.state = {
      group: null,
      loadingInProgress: false,
      loadingError: null,
    };
  }

    /** Lifecycle Methode, die aufgerufen wird, wenn die Komponente dem Browser DOM hizugefügt wird */
    componentDidMount() {
    this.getGroup();
  }

  /** gets the balance for this account 
  getGroup = () => {
    ListAPI.getAPI().getGroup(this.props.groupID).then(group =>
      this.setState({
        group: group,
        loadingInProgress: false,
        loadingError: null
      })).catch(e =>
        this.setState({ // Reset state with error from catch 
          group: null,
          loadingInProgress: false,
          loadingError: e
        })
      );

    // set loading to true
    this.setState({
      loadingInProgress: true,
      loadingError: null
    });
  }
  */

  /** Rendered die Komponente */
  render() {
    const { classes, groupID, shoppinglistID } = this.props;
    const { customer, loadingInProgress, loadingError } = this.state;

    return (
      <Paper variant='outlined' className={classes.root}>

        <Typography variant='h6'>
          EInkaufsliste
        </Typography>
        <Typography className={classes.shoppinglistEntry}>
          ID: {shoppinglistID}
        </Typography>
        {
          group ?
            <Typography>
              Gruppe: {group.getLastName()}, {group.getFirstName()}
            </Typography>
            : null
        }
        <LoadingBar show={loadingInProgress} />
        <InlineError error={loadingError} InlineError={`Die Daten der Gruppen ID ${groupID} konnte nicht geladen werden.`} onReload={this.getGroup} />
      </Paper>
    );
  }
}

/** Styling */
const styles = theme => ({
  root: {
    width: '100%',
    padding: theme.spacing(1),
    marginTop: theme.spacing(1)
  },
  articlelistEntry: {
    fontSize: theme.typography.pxToRem(15),
    flexBasis: '33.33%',
    flexShrink: 0,
  }
});

/** PropTypes */
ArticleListDetails.propTypes = {
  /** @ignore */
  classes: PropTypes.object.isRequired,
  shoppinglistID: PropTypes.string.isRequired,
  articlelistID: PropTypes.string.isRequired,
}

export default withStyles(styles)(ArticleListDetails);
