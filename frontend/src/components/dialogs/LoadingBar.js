import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { withStyles, LinearProgress } from '@material-ui/core';

class LoadingBar extends Component {

  /** Rendered die Komponente */
  render() {
    const { classes, show } = this.props;

    return (
      show ?
        <div className={classes.root}>
          <LinearProgress color='secondary' />
        </div>
        : null
    );
  }
}

/** Komponenten Style */
const styles = theme => ({
  root: {
    width: '100%',
    marginTop: theme.spacing(2),
  }
});

/** PropTypes */
LoadingBar.propTypes = {
  /** @ignore */
  classes: PropTypes.object.isRequired,
  /** Wenn true, wird der Ladebalken gerendered */
  show: PropTypes.bool.isRequired,
}

export default withStyles(styles)(LoadingBar);
