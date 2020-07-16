import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { withStyles, ListItem } from '@material-ui/core';
import { Button, List } from '@material-ui/core';
import AddIcon from '@material-ui/icons/Add';
import { ListAPI } from '../api';
import InlineError from './dialogs/InlineError';
import LoadingBar from './dialogs/LoadingBar';
import ArticleListEntry from './ArticleListEntry';

class ArticleList extends Component {

    constructor(props) {
      super(props);
  
      this.state = {
        articlelists: [],
        loadingInProgress: false,
        loadingArticleListError: null,
        addingArticleListError: null,
      };
    }
  
    getArticleLists = () => {
      ListAPI.getAPI().getArticleListsOfGroups(this.props.shoppinglist.getID()).then(articlelistBOs =>
        this.setState({  
          articlelists: articlelistBOs,
          loadingInProgress: false,
          loadingArticleListError: null
        })).catch(e =>
          this.setState({ 
            articlelists: [],
            loadingInProgress: false,
            loadingArticleListError: e
          })
        );
  
      this.setState({
        loadingInProgress: true,
        loadingArticleListError: null
      });
    }
  
    /** Lifecycle Methode, die aufgerufen wird, wenn die Komponente dem Browser DOM hizugefügt wird */
    componentDidMount() {
      this.getArticleLists();
    }
  
    componentDidUpdate(prevProps) {
      // reload accounts if shown state changed. Occures if the CustomerListEntrys ExpansionPanel was expanded
      // if ((this.props.show !== prevProps.show)) {
      //   this.getAccounts();
      // }
    }
  
    /** Fügt einer EInkaufsliste Artikel hinzu */
    addArticleList = () => {
      ListAPI.getAPI().addArticleListForShoppingList(this.props.shoppingslist.getID()).then(articlelistBO => {
        this.setState({ 
          articlelists: [...this.state.articlelists, articlelistBO],
          loadingInProgress: false,
          addingArticleListError: null
        })
      }).catch(e =>
        this.setState({ 
          articlelists: [],
          loadingInProgress: false,
          addingArticleListError: e
        })
      );
  
      this.setState({
        loadingInProgress: true,
        addingArticleListError: null
      });
    }
  
    deleteArticleListHandler = (deletedArticleList) => {
      this.setState({
        articlelists: this.state.articlelists.filter(articlelist => articlelist.getID() !== deletedArticleList.getID())
      })
    }
  
    /** Rendered die Komponente */
    render() {
      const { classes, shoppinglist } = this.props;
      const { articlelists, loadingInProgress, loadingArticleListError, addingArticleListError } = this.state;
  
      return (
        <div className={classes.root}>
          <List className={classes.articleList}>
            {
              articlelists.map(articlelist => <ArticleListEntry key={articlelist.getID()} shoppinglists={shoppinglists} articlelists={articlelists} onArticleListDeleted={this.deleteArticleListHandler}
                show={this.props.show} />)
            }
            <ListItem>
              <LoadingBar show={loadingInProgress} />
              <InlineError error={loadingShoppingListError} InlineError={`Artikel der Einkaufsliste ${shoppinglist.getID()} konnten nicht geladen werden.`} onReload={this.getArticleLists} />
              <InlineError error={addingShoppingListError} InlineError={`Artikel der Einkaufsliste ${shoppinglist.getID()} konnten nicht hinzugefügt werden.`} onReload={this.addArticleList} />
            </ListItem>
          </List>
          <Button className={classes.addArticleListButton} variant='contained' color='primary' startIcon={<AddIcon />} onClick={this.addArticleList}>
              Neuer Artikel
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
    articleList: {
      marginBottom: theme.spacing(2),
    },
    addArticleListButton: {
      position: 'absolute',
      right: theme.spacing(3),
      bottom: theme.spacing(1),
    }
  });
  
  /** PropTypes */
  articleList.propTypes = {
    /** @ignore */
    classes: PropTypes.object.isRequired,
    shoppinglist: PropTypes.object.isRequired,
    show: PropTypes.bool.isRequired
  }
  
  export default withStyles(styles)(ArticleList);
  