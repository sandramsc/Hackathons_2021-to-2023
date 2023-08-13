// @mui material components
import Card from "@mui/material/Card";
import Icon from "@mui/material/Icon";

// Soft UI Dashboard PRO Material-UI components
import SuiBox from "components/SuiBox";
import SuiTypography from "components/SuiTypography";

// Soft UI Dashboard PRO Material-UI example components
import TimelineItem from "examples/Timeline/TimelineItem";

function OrdersOverview() {
  return (
    <Card className="h-100">
      <SuiBox pt={3} px={3}>
        <SuiTypography variant="h6" fontWeight="medium">
          BioCoins Trials overview
        </SuiTypography>
        <SuiBox mt={1} mb={2}>
          <SuiTypography variant="button" textColor="text" fontWeight="regular">
            <SuiTypography display="inline" variant="body2" verticalAlign="middle">
              <Icon className="font-bold text-success">arrow_upward</Icon>
            </SuiTypography>
            &nbsp;
            <SuiTypography variant="button" textColor="text" fontWeight="medium">
              44%
            </SuiTypography>{" "}
            this month
          </SuiTypography>
        </SuiBox>
      </SuiBox>
      <SuiBox p={2}>
        <TimelineItem
          color="success"
          icon="notifications"
          title="3 clinical trial projects await funding"
          dateTime="22 DEC 7:20 PM"
        />
        <TimelineItem
          color="error"
          icon="inventory_2"
          title="1 project in review"
          dateTime="21 DEC 11 PM"
        />
        <TimelineItem
          color="info"
          icon="shopping_cart"
          title="7 new projects aquired for April 2022"
          dateTime="21 DEC 9:34 PM"
        />
        <TimelineItem
          color="warning"
          icon="payment"
          title="New payment method added for order #4395133"
          dateTime="20 DEC 2:20 AM"
        />
        <TimelineItem
          color="primary"
          icon="vpn_key"
          title="New card added for order #4395133"
          dateTime="18 DEC 4:54 AM"
        />
        <TimelineItem color="dark" icon="paid" title="New order #9583120" dateTime="17 DEC" />
      </SuiBox>
    </Card>
  );
}

export default OrdersOverview;
