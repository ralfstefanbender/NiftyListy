import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { Paper, Typography, Tabs, Tab } from '@material-ui/core';
import { Link as RouterLink } from 'react-router-dom';
import DropDownMenu from '../dialogs/DropDownMenu';

class Header extends Component {

    constructor(props) {
      super(props);
      this.state = {
        tabindex: 0
      };
    }
  
    /**onChange events der Tabs Komponente*/
    handleTabChange = (e, newIndex) => {
      // console.log(newValue)
      this.setState({
        tabindex: newIndex
      })
    };
  
    /** Rendered die Komponente */
    render() {
      const { user } = this.props;
  
      return (
        <Paper variant='outlined' >
          <DropDownMenu user={user} />
          <Typography variant='h3' component='h1' align='center'>
            NiftyListy
          </Typography>
          <Typography variant='h4' component='h2' align='center'>
            Client Advisor Home
          </Typography>
          {
            user ?
              <Tabs indicatorColor='primary' textColor='primary' centered value={this.state.tabindex} onChange={this.handleTabChange} >
                <Tab label='Listen' component={RouterLink} to={`/listen`} />
                <Tab label='Gruppen' component={RouterLink} to={`/gruppen`} />
                <Tab label='Report' component={RouterLink} to={`/report`} />
                <Tab label='About' component={RouterLink} to={`/about`} />
              </Tabs>
              : null
          }
        </Paper>
      )
    }
  }
  
  /** PropTypes */
  Header.propTypes = {
    /** Der eingeloggte Firesbase User */
    user: PropTypes.object,
  }
  
  export default Header;