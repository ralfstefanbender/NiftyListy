import { createMuiTheme } from '@material-ui/core/styles';
import { colors } from '@material-ui/core';

const white = '#FFFFFF';

const theme = createMuiTheme({
  palette: {
    primary: {
        contrastText: white,
        dark: '#38b0a1',
        main: '#7bd4c9',
        light: '#adede5'
    },
    secondary: {
        contrastText: white,
        dark: '#2eb392',
        main: '#6fe3c6',
        light: '#a7f2d7'
    },
    error: {
        contrastText: white,
        main: colors.red[600]
    },
    background: {
        default: '#f0fffd',
        paper: white
    },
  },
});

export default theme;