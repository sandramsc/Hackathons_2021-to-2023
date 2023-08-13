// Designed by Sandra Ashipala for 30-01-2022 LongHack
import Card from "@mui/material/Card";
// import Divider from "@mui/material/Divider";
import Icon from "@mui/material/Icon";

// BioCoins Dashboard React components
import SuiBox from "components/SuiBox";
import SuiTypography from "components/SuiTypography";

// Billing page components
import Transaction from "layouts/billing/components/Transaction";

function Transactions() {
  return (
    <Card className="h-100">
      <SuiBox display="flex" justifyContent="space-between" alignItems="center" pt={3} px={2}>
        <SuiTypography variant="h6" fontWeight="medium" textTransform="capitalize">
          Your BioCoins Benefits Ledger
        </SuiTypography>
        <SuiBox display="flex" alignItems="flex-start">
          <SuiBox color="text" mr={0.5} lineHeight={0}>
            <Icon color="inherit" fontSize="small">
              date_range
            </Icon>
          </SuiBox>
          <SuiTypography variant="button" textColor="text" fontWeight="regular">
            23 - 30 March 2020
          </SuiTypography>
        </SuiBox>
      </SuiBox>
      <SuiBox pt={3} pb={2} px={2}>
        <SuiBox mb={2}>
          <SuiTypography
            variant="caption"
            textColor="text"
            fontWeight="bold"
            textTransform="uppercase"
          >
            newest
          </SuiTypography>
        </SuiBox>
        <SuiBox
          component="ul"
          display="flex"
          flexDirection="column"
          p={0}
          m={0}
          customClass="no-list-style"
        >
          <Transaction
            color="success"
            icon="arrow_upward"
            name="Minor Illness Coverage at Cambrige Hospital"
            description="27 March 2020, at 12:30 PM"
            value="+ $ 300"
          />
          <Transaction
            color="success"
            icon="arrow_upward"
            name="Full Health Insurance Coverage for entire Family"
            description="27 March 2020, at 04:30 AM"
            value="+ $ 2,000"
          />
        </SuiBox>
        <SuiBox mt={1} mb={2}>
          <SuiTypography
            variant="caption"
            textColor="text"
            fontWeight="bold"
            textTransform="uppercase"
          >
            yesterday
          </SuiTypography>
        </SuiBox>
        <SuiBox
          component="ul"
          display="flex"
          flexDirection="column"
          p={0}
          m={0}
          customClass="no-list-style"
        >
          <Transaction
            color="success"
            icon="arrow_upward"
            name="Dental Care Cover for The Entire Year 2022"
            description="26 March 2020, at 12:30 PM"
            value="+ $ 1,000"
          />
          <Transaction
            color="dark"
            icon="priority_high"
            name="Premium Support at Howerrt Hospital"
            description="26 March 2020, at 05:00 AM"
            value="Pending"
          />
        </SuiBox>
      </SuiBox>
    </Card>
  );
}

export default Transactions;
