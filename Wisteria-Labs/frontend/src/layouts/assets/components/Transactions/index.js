// @mui material components
import Card from "@mui/material/Card";
// import Divider from "@mui/material/Divider";
import Icon from "@mui/material/Icon";
import SoftButton from "components/SoftButton";

// Soft UI Dashboard React components
import SoftBox from "components/SoftBox";
import SoftTypography from "components/SoftTypography";

// Billing page components
import Transaction from "layouts/assets/components/Transaction";

function Transactions() {
  return (
    <Card sx={{ height: "100%" }}>
      <SoftBox display="flex" justifyContent="space-between" alignItems="center" pt={3} px={2}>
        <SoftTypography variant="h6" fontWeight="medium" textTransform="capitalize">
          Your Transaction&apos;s
        </SoftTypography>
        <SoftBox display="flex" alignItems="flex-start">
          <SoftBox color="text" mr={0.5} lineHeight={0}>
            <Icon color="inherit" fontSize="small">
              date_range
            </Icon>
          </SoftBox>
          <SoftTypography variant="button" color="text" fontWeight="regular">
            23 - 30 March 2023
          </SoftTypography>
        </SoftBox>
      </SoftBox>
      <SoftBox pt={3} pb={2} px={2}>
        <SoftBox mb={2}>
          <SoftTypography
            variant="caption"
            color="text"
            fontWeight="bold"
            textTransform="uppercase"
          >
            newest
          </SoftTypography>
        </SoftBox>
        <SoftBox
          component="ul"
          display="flex"
          flexDirection="column"
          p={0}
          m={0}
          sx={{ listStyle: "none" }}
        >
          <Transaction
            color="error"
            icon="arrow_downward"
            name="Bought BIC"
            description="27 March 2023, at 12:30 PM"
            value="- $ 2,500"
          />
          <Transaction
            color="success"
            icon="arrow_upward"
            name="Sold ETH"
            description="27 March 2023, at 04:30 AM"
            value="+ $ 2,000"
          />
        </SoftBox>
        <SoftBox mt={1} mb={2}>
          <SoftTypography
            variant="caption"
            color="text"
            fontWeight="bold"
            textTransform="uppercase"
          >
            yesterday
          </SoftTypography>
        </SoftBox>
        <SoftBox
          component="ul"
          display="flex"
          flexDirection="column"
          p={0}
          m={0}
          sx={{ listStyle: "none" }}
        >
          <Transaction
            color="success"
            icon="arrow_upward"
            name="Sold MATIC"
            description="26 March 2023, at 13:45 PM"
            value="+ $ 750"
          />
          <Transaction
            color="dark"
            icon="priority_high"
            name="Bought ETH"
            description="26 March 2023, at 05:00 AM"
            value="Pending"
          />
        </SoftBox>
        <SoftBox pt={4} px={2} mb={2} display="flex" justifyContent="center" alignItems="center">
      <SoftButton variant="gradient" color="light" width="15%" display="flex" alignItems="center">
          View Transactions
        </SoftButton>
      </SoftBox>
      </SoftBox>
    </Card>
  );
}

export default Transactions;
