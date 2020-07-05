import React from 'react'
import { makeStyles, Paper, Typography, Link } from '@material-ui/core';

const useStyles = makeStyles(theme => ({
  root: {
    width: '100%',
    marginTop: theme.spacing(2),
    marginBottom: theme.spacing(2),
    padding: theme.spacing(1)
  },
  content: {
    margin: theme.spacing(1),
  }
}));

/**
 * Hier wird die About Seite mit dem Impressum gezeigt.
 * 
 * @author [Lukas Ulmer](https://github.com/lukasorlando)  
 * @author [Rahel Ün](https://github.com/raheluen)
 */
function About() {

  const classes = useStyles();

  return (
    <Paper elevation={0} className={classes.root}>
      <div className={classes.content}>
        <Typography variant='h6'>
          NiftyListy
        </Typography>
        <br />
        <Typography>
          React Frontend written by <Link href='https://github.com/lukasorlando'>Lukas Ulmer</Link> and <Link href='https://github.com/raheluen'>Rahel Ün</Link>
        </Typography>
        <Typography>
          Python Backend written by <Link href='https://github.com/ralfstefanbender'>Ralf-Stefan Bender</Link> and <Link href='https://github.com/patricksinger99'> Patrick Singer</Link>
        </Typography>
        <Typography>
          Data Base written by <Link href='https://github.com/william-zhang-26'>William Zhang</Link> and <Link href='https://github.com/mariaweinberger'> Maria Weinberger</Link>
        </Typography>
        <br />
        <Typography variant='body2'>
          © Hochschule der Medien 2020, all rights reserved.
        </Typography>
      </div>
    </Paper>
  )
}

export default About;