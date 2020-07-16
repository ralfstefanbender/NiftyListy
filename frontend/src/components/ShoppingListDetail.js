import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { withStyles, Typography, Paper } from '@material-ui/core';
import InlineError from './dialogs/InlineError';
import LoadingBar from './dialogs/LoadingBar';


class ShoppingListDetails extends Component {

  constructor(props) {
    super(props);

    this.state = {
      group: null,
      loadingInProgress: false,
      loadingError: null,
    };
  }

  componentDidMount() {
    this.getGroup();
  }


  /** Rendered die Komponente */
  render() {
    const { classes, groupID, shoppinglistID } = this.props;
    const { group, loadingInProgress, loadingError } = this.state;

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
              Gruppe: {group.getGruppename()}
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
  shoppinglistEntry: {
    fontSize: theme.typography.pxToRem(15),
    flexBasis: '33.33%',
    flexShrink: 0,
  }
});

/** PropTypes */
ShoppingListDetails.propTypes = {
  /** @ignore */
  classes: PropTypes.object.isRequired,
  groupID: PropTypes.string.isRequired,
  shoppinglistID: PropTypes.string.isRequired,
}

export default withStyles(styles)(ShoppingListDetails);
