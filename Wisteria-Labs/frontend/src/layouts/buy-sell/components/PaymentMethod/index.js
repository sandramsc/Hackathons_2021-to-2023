// @mui material components
import Card from "@mui/material/Card";
import Grid from "@mui/material/Grid";

// Soft UI Dashboard React components
import SoftBox from "components/SoftBox";
import SoftTypography from "components/SoftTypography";
import SoftButton from "components/SoftButton";
import Exchange from "assets/images/exchange.png";
// Soft UI Dashboard React base styles
import borders from "assets/theme/base/borders";

function PaymentMethod() {
  const { borderWidth, borderColor } = borders;

  return (
    <Card id="delete-account">
      <SoftBox pt={2} px={2} display="flex" justifyContent="space-between" alignItems="center">
        <SoftTypography variant="h6" fontWeight="medium">
          Amount
        </SoftTypography>
      </SoftBox>
      <SoftBox p={2}>
        <Grid container spacing={3}>
          <Grid item xs={12} md={5.5}>
            <SoftBox
              border={`${borderWidth[1]} solid ${borderColor}`}
              borderRadius="lg"
              display="flex"
              justifyContent="space-between"
              alignItems="center"
              p={3}
            >
              
              <SoftTypography variant="h6" fontWeight="medium">
              744.56
              </SoftTypography>
              <SoftBox ml="auto" lineHeight={0}>
              <SoftTypography variant="h6" fontWeight="medium">
              USD
              </SoftTypography>
              </SoftBox>
            </SoftBox>
          </Grid>
          <Grid item xs={6} md={1}>
            <SoftBox
  
              borderRadius="lg"
              display="flex"
              justifyContent="center"
              alignItems="center"
              p={3}
            >
              
              <SoftTypography variant="h6" fontWeight="medium">
              <img width="25rem" src={Exchange} alt="" />
              </SoftTypography>
            </SoftBox>
          </Grid>
          <Grid item xs={12} md={5.5}>
            <SoftBox
              border={`${borderWidth[1]} solid ${borderColor}`}
              borderRadius="lg"
              display="flex"
              justifyContent="space-between"
              alignItems="center"
              p={3}
            >
              
              <SoftTypography variant="h6" fontWeight="medium">
                1.002850
              </SoftTypography>
              <SoftBox ml="auto" lineHeight={0}>
              <SoftTypography variant="h6" fontWeight="medium">
              BTC
              </SoftTypography>
              </SoftBox>
            </SoftBox>
          </Grid>
          
        </Grid>
      </SoftBox>
      <SoftBox pt={2} px={2} mb={2} display="flex" justifyContent="center" alignItems="center">
      <SoftButton variant="gradient" color="dark" width="15%" display="flex" alignItems="center">
          Buy Cryptocurrency
        </SoftButton>
      </SoftBox>
    </Card>
  );
}

export default PaymentMethod;
