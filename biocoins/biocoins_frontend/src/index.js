import React from "react";
import ReactDOM from "react-dom";
import { BrowserRouter } from "react-router-dom";
import App from "App";

// Soft UI Dashboard React Context Provider
import { SoftUIControllerProvider } from "context";

import { AuthProvider } from "auth-context/auth.context";

let user = localStorage.getItem("user");
user = JSON.parse(user);

ReactDOM.render(
  <BrowserRouter>
    <SoftUIControllerProvider>
      <AuthProvider userData={user}>
        <App />
      </AuthProvider>
    </SoftUIControllerProvider>
  </BrowserRouter>,
  document.getElementById("root")
);
