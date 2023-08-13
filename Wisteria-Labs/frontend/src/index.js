
import React from "react";
import ReactDOM from "react-dom";
import { BrowserRouter } from "react-router-dom";
import App from "App";
import { ThemeProvider } from '@mui/material/styles';
import { SafeThemeProvider } from '@safe-global/safe-react-components';

// Soft UI Dashboard React Context Provider
import { SoftUIControllerProvider } from "context";

ReactDOM.render(
  <BrowserRouter>
    <SoftUIControllerProvider>
    <SafeThemeProvider mode="light">
    {(safeTheme: Theme) => (
      <ThemeProvider theme={safeTheme}>
      <App />
      
      </ThemeProvider>
    )}
  </SafeThemeProvider>
    </SoftUIControllerProvider>
  </BrowserRouter>,
  document.getElementById("root")
);