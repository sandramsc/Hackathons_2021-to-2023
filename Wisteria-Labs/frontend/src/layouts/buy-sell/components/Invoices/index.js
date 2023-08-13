// @mui material components
 import Card from "@mui/material/Card";
 import SoftButton from "components/SoftButton";
 
 // @mui material components
import Divider from "@mui/material/Divider";
import Invoice from "layouts/buy-sell/components/Invoice"
// Soft UI Dashboard React components
import SoftBox from "components/SoftBox";
import SoftTypography from "components/SoftTypography";
 
 function Invoices() {
   return (
     <Card id="delete-account" sx={{ height: "100%" }}>
 <SoftBox
        display="flex"
        justifyContent="center"
        alignItems="baseline"
        pt={3}
        pb={0.8}
        px={3}
      >
        <SoftBox textAlign="center">
          <SoftTypography variant="body2" color="text">YOU ARE SENDING</SoftTypography>
          <SoftTypography variant="h4" >
            1.002850 BTC
          </SoftTypography>
          <SoftTypography variant="h6" color="text">
            $ 701.26 per BTC
          </SoftTypography>
        </SoftBox>

      </SoftBox>

      <Divider />

      <SoftBox pt={1.25} pb={3} px={3}>

        <SoftBox lineHeight={1}>
        <SoftBox component="ul" display="flex" flexDirection="column" p={0} m={0}>
          <Invoice date="Payment Method" id="USD Wallet" />
        </SoftBox>
        </SoftBox>
    
        <Divider />

        <SoftBox lineHeight={1}>
        <SoftBox component="ul" display="flex" flexDirection="column" p={0} m={0}>
          <Invoice date="Deposit To" id="BTC Wallet" price="Change" />
        </SoftBox>
        </SoftBox>

        <Divider />

        <SoftBox lineHeight={1}>
        <SoftBox component="ul" display="flex" flexDirection="column" p={0} m={0}>
          <Invoice date="Wait Time" id="Instant"  />
        </SoftBox>
        </SoftBox>

        <Divider />

        <SoftBox lineHeight={1}>
        <SoftBox component="ul" display="flex" flexDirection="column" p={0} m={0}>
          <Invoice date="Fee"   price="$9.07"/>
          <Invoice date="Subtotal"   price="$744.56"/>
          <Invoice date="Total"   price="$753.53"/>
        </SoftBox>
        </SoftBox>
        <SoftBox px={2} mb={2} display="flex" justifyContent="center" alignItems="center">
      <SoftButton variant="gradient" color="success" width="15%" display="flex" alignItems="center">
          Confirm Purchase
        </SoftButton>
      </SoftBox>
      </SoftBox>
     </Card>
   );
 }
 
 export default Invoices;