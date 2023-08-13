import { useState, useEffect } from "react";

// react-github-btn
import GitHubButton from "react-github-btn";

// clsx is a utility for constructing className strings conditionally
import clsx from "clsx";

// @mui material components
import Drawer from "@mui/material/Drawer";
import Divider from "@mui/material/Divider";
import Switch from "@mui/material/Switch";
import IconButton from "@mui/material/IconButton";
import Link from "@mui/material/Link";
import Icon from "@mui/material/Icon";

// @mui icons
import TwitterIcon from "@mui/icons-material/Twitter";
import FacebookIcon from "@mui/icons-material/Facebook";

// BioCoins Dashboard React components
import SuiBox from "components/SuiBox";
import SuiTypography from "components/SuiTypography";
import SuiButton from "components/SuiButton";

// Custom styles for the Configurator
import styles from "examples/Configurator/styles";

// BioCoins Dashboard React context
import { useSoftUIController } from "context";

function Configurator() {
  const [controller, dispatch] = useSoftUIController();
  const { openConfigurator, transparentSidenav, fixedNavbar, sidenavColor } = controller;
  const [disabled, setDisabled] = useState(false);
  const classes = styles({ sidenavColor });
  const sidenavColors = ["primary", "dark", "info", "success", "warning", "error"];

  // Use the useEffect hook to change the button state for the sidenav type based on window size.
  useEffect(() => {
    // A function that sets the disabled state of the buttons for the sidenav type.
    function handleDisabled() {
      return window.innerWidth > 1200 ? setDisabled(false) : setDisabled(true);
    }

    // The event listener that's calling the handleDisabled function when resizing the window.
    window.addEventListener("resize", handleDisabled);

    // Call the handleDisabled function to set the state with the initial value.
    handleDisabled();

    // Remove event listener on cleanup
    return () => window.removeEventListener("resize", handleDisabled);
  }, []);

  const handleCloseConfigurator = () => {
    dispatch({ type: "OPEN_CONFIGURATOR", value: false });
  };

  const handleTransparentSidenav = () => {
    dispatch({ type: "TRANSPARENT_SIDENAV", value: true });
  };

  const handleWhiteSidenav = () => {
    dispatch({ type: "TRANSPARENT_SIDENAV", value: false });
  };

  const handleFixedNavbar = () => {
    dispatch({ type: "FIXED_NAVBAR", value: !fixedNavbar });
  };

  return (
    <Drawer
      variant="permanent"
      classes={{
        paper: clsx(classes.configurator, {
          [classes.configurator_open]: openConfigurator,
          [classes.configurator_close]: !openConfigurator,
        }),
      }}
    >
      <SuiBox
        display="flex"
        justifyContent="space-between"
        alignItems="baseline"
        pt={3}
        pb={0.8}
        px={3}
      >
        <SuiBox>
          <SuiTypography variant="h5">BioCoins Customizer</SuiTypography>
          <SuiTypography variant="body2" textColor="text">
            Customize your BioCoins Dashboard
          </SuiTypography>
        </SuiBox>

        <Icon
          className={`font-bold ${classes.configurator_close_icon}`}
          onClick={handleCloseConfigurator}
        >
          close
        </Icon>
      </SuiBox>

      <Divider />

      <SuiBox pt={1.25} pb={3} px={3}>
        <SuiBox>
          <SuiTypography variant="h6">Side panel Colors</SuiTypography>

          <SuiBox my={0.5}>
            {sidenavColors.map((color) => (
              <IconButton
                key={color}
                className={clsx(classes.configurator_sidenav_color, classes[color], {
                  [classes.active_color]: sidenavColor === color,
                })}
                onClick={() => dispatch({ type: "SIDENAV_COLOR", value: color })}
              />
            ))}
          </SuiBox>
        </SuiBox>

        <SuiBox mt={3}>
          <SuiTypography variant="h6">Side panel Type</SuiTypography>
          <SuiBox customClass={classes.configurator_sidenav_types}>
            <SuiButton
              buttonColor="info"
              variant={transparentSidenav ? "gradient" : "outlined"}
              onClick={handleTransparentSidenav}
              disabled={disabled}
              fullWidth
            >
              Transparent
            </SuiButton>
            <SuiButton
              buttonColor="info"
              variant={transparentSidenav ? "outlined" : "gradient"}
              onClick={handleWhiteSidenav}
              disabled={disabled}
              fullWidth
            >
              White
            </SuiButton>
          </SuiBox>
        </SuiBox>
        <SuiBox mt={3} mb={2}>
          <SuiTypography variant="h6">Navbar Fixed</SuiTypography>

          <Switch checked={fixedNavbar} onChange={handleFixedNavbar} />
        </SuiBox>

        <Divider />
        <SuiBox display="flex" justifyContent="center">
          <GitHubButton
            href="https://github.com/agelesspartners/biocoins"
            data-icon="octicon-star"
            data-size="large"
            data-show-count="true"
            aria-label="BioCoins Project on GitHub"
          >
            Star
          </GitHubButton>
        </SuiBox>
        <SuiBox mt={3} textAlign="center">
          <SuiBox mb={0.5}>
            <SuiTypography variant="h6">Thank you for sharing!</SuiTypography>
          </SuiBox>

          <SuiBox display="flex" justifyContent="center">
            <SuiBox mr={1.5}>
              <SuiButton
                component={Link}
                href="https://github.com/agelesspartners/biocoins"
                target="_blank"
                rel="noreferrer"
                buttonColor="dark"
              >
                <TwitterIcon />
                &nbsp; Tweet
              </SuiButton>
            </SuiBox>
            <SuiButton
              component={Link}
              href="https://github.com/agelesspartners/biocoins"
              target="_blank"
              rel="noreferrer"
              buttonColor="dark"
            >
              <FacebookIcon />
              &nbsp; Share
            </SuiButton>
          </SuiBox>
        </SuiBox>
      </SuiBox>
    </Drawer>
  );
}

export default Configurator;
