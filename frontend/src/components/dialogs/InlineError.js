import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { withStyles, Button } from '@material-ui/core';
import Alert from '@material-ui/lab/Alert';
import AlertTitle from '@material-ui/lab/AlertTitle';
import AutorenewIcon from '@material-ui/icons/Autorenew';

class InlineError extends Component {
  #standardText = 'Whoops - etwas ist schiefgelaufen';

  /** Rendered den InlineError wenn ein Error Objekt nicht null ist */
  render() {
    const { classes, error, InlineErrorMessage, onReload } = this.props;

    return (
      (error !== null) ?
        <Alert severity='error' className={classes.root}>
          <div>
            {this.#standardText}
          </div>
          <AlertTitle>
            {InlineErrorMessage}
          </AlertTitle>
          <div className={classes.margins}>
            Error message (for debugging only) is:
        </div>
          <div>
            {error.message}
          </div>
          {
            onReload ?
              <div className={classes.margins}>
                <Button variant='contained' color='primary' startIcon={<AutorenewIcon />} onClick={onReload}>
                  Reload
            </Button>
              </div>
              : null
          }
        </Alert>
        : null
    );
  }
}

/** Component specific styles */
const styles = theme => ({
  margins: {
    marginTop: theme.spacing(2)
  }
});

/** PropTypes */ 
InlineError.propTypes = {
  /** @ignore */
  classes: PropTypes.object.isRequired,
  /** 
   * The error object, which drives the error message 
   * If not null, the error message is shown 
   */
  error: PropTypes.object,
  /**  A contextual error message to be shown */
  InlineError: PropTypes.string,
  /** 
   * A reload handler for the onReload event, which occurs if the reload button is clicked. 
   * If given a reload button is shown 
   */
  onReload: PropTypes.func
}

export default withStyles(styles)(InlineError);
