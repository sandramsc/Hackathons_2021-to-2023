// @mui material components
import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import Icon from "@mui/material/Icon";
import Link from "@mui/material/Link";

// Soft UI Dashboard PRO Material-UI components
import SuiButton from "components/SuiButton";
import SuiBox from "components/SuiBox";
import SuiTypography from "components/SuiTypography";

// Custom styles for the SidenavCard
import styles from "examples/Sidenav/styles/sidenavCard";

// Soft UI Dashboard PRO Material-UI context
import { useSoftUIController } from "context";

function SidenavCard() {
  const [controller] = useSoftUIController();
  const { miniSidenav, sidenavColor } = controller;
  const classes = styles({ miniSidenav, sidenavColor });

  return (
    <Card className={classes.card}>
      <CardContent className={classes.card_content}>
        <SuiBox customClass={classes.card_iconBox}>
          <Icon className={classes.card_icon} fontSize="default">
            star
          </Icon>
        </SuiBox>
        <SuiBox>
          <SuiTypography variant="h6" textColor="white">
            Need help?
          </SuiTypography>
          <SuiBox mb={1.5} mt={-1}>
            <SuiTypography variant="caption" textColor="white" fontWeight="medium">
              Contact Support
            </SuiTypography>
          </SuiBox>
          <SuiButton
            component={Link}
            href="https://github.com/agelesspartners/biocoins"
            target="_blank"
            rel="noreferrer"
            size="small"
            color="default"
            fullWidth
          >
            BioCoins Dashboard
          </SuiButton>
        </SuiBox>
      </CardContent>
    </Card>
  );
}

export default SidenavCard;
