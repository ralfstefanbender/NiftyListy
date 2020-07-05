import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { Button, Grid, Typography, withStyles } from '@material-ui/core';

class SignIn extends Component {


	/** 
	 * Bei Betätigung des Buttons "Anmeldung mit Google", wird der prop onSignIn handler aufgerufen
	 */
	handleSignInButtonClicked = () => {
		this.props.onSignIn();
	}

	/**Render-Methode für den Fall, dass das user object null ergibt */
	render() {
		const { classes } = this.props;

		return (
			<div>
				<Typography className={classes.root} align='center' variant='h6'>Willkommen zu Nifty Listy!</Typography>
				<Typography className={classes.root} align='center'>Unsere App ermöglicht es dir Einkäufe zu planen, indem man Listen innerhalb von Familien und Gruppen aufteilt. </Typography>
				<Typography className={classes.root} align='center'>Leider bist du im Moment nicht angemeldet.</Typography>
				<Typography className={classes.root} align='center'>Um die App nutzen zu können, bitten wir dich, dich mit Google anzumelden</Typography>
				<Grid container justify='center'>
					<Grid item>
						<Button variant='contained' color='primary' onClick={this.handleSignInButtonClicked}>
							Anmeldung mit Google
      			</Button>
					</Grid>
				</Grid>
			</div>
		);
	}
}

/** Komponenten Styling */
const styles = theme => ({
	root: {
		margin: theme.spacing(2)
	}
});

/** PropTypes */
SignIn.propTypes = {
	/** @ignore */
	classes: PropTypes.object.isRequired,
	/** 
	 * Handler function, die bei einem Anmeldungsversuch aufgerufen wird.
	 */
	onSignIn: PropTypes.func.isRequired,
}

export default withStyles(styles)(SignIn)