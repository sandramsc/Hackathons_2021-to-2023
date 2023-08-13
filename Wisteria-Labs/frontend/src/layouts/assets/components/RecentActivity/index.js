// @mui material components
import Card from "@mui/material/Card";

// Soft UI Dashboard React components
import SoftBox from "components/SoftBox";
import SoftTypography from "components/SoftTypography";

// Soft UI Dashboard React examples
import TimelineItem from "examples/Timeline/TimelineItem";

function RecentActivity() {
  return (
    <Card className="h-100">
      <SoftBox pt={3} px={3}>
        <SoftTypography variant="h6" fontWeight="medium">
          RECENT ACTIVITY
        </SoftTypography>
      </SoftBox>
      <SoftBox p={2}>
        <TimelineItem
          color="success"
          icon="notifications"
          title="Bought Ethereum"
          dateTime="22 DEC 7:20 PM"
        />
        <TimelineItem
          color="error"
          icon="inventory_2"
          title="Bought Bitcoin"
          dateTime="21 DEC 11 PM"
        />
        <TimelineItem
          color="info"
          icon="shopping_cart"
          title="Recieved USDC"
          dateTime="21 DEC 9:34 PM"
        />
        <TimelineItem
          color="warning"
          icon="payment"
          title="Bought Shiba Inu"
          dateTime="20 DEC 2:20 AM"
        />
      </SoftBox>
    </Card>
  );
}

export default RecentActivity;
