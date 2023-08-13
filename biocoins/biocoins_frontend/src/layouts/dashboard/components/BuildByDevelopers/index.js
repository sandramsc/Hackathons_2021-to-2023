// @mui material components
import Card from "@mui/material/Card";
import Grid from "@mui/material/Grid";
import Icon from "@mui/material/Icon";

// BioCoins Dashboard React components
import SuiBox from "components/SuiBox";
import SuiTypography from "components/SuiTypography";

// Custom styles for the BuildByDevelopers
import styles from "layouts/dashboard/components/BuildByDevelopers/styles";

// Images
import wavesWhite from "assets/images/shapes/waves-white.svg";
import rocketWhite from "assets/images/illustrations/rocket-white.png";

function BuildByDevelopers() {
  const classes = styles();

  return (
    <Card>
      <SuiBox p={2}>
        <Grid container spacing={3}>
          <Grid item xs={12} lg={6}>
            <SuiBox display="flex" flexDirection="column" height="100%">
              <SuiBox pt={1} mb={0.5}>
                <SuiTypography variant="body2" textColor="text" fontWeight="medium">
                  Welcome To Your Dashboard
                </SuiTypography>
              </SuiBox>
              <SuiTypography variant="h5" fontWeight="bold" gutterBottom>
                BioCoins
              </SuiTypography>
              <SuiBox mb={6}>
                <SuiTypography variant="body2" textColor="text">
                  Biocoins is a platform for researchers, patients, and investors to collectively
                  fund clinical trials. By allowing researchers to tokenize incentives (early
                  treatment access, IP royalties ,data access, and more) for their planned clinical
                  trial, we help researchers fund clinical trials faster than ever before.
                </SuiTypography>
              </SuiBox>
              <SuiTypography
                component="a"
                href="#"
                variant="button"
                textColor="text"
                fontWeight="medium"
                customClass={classes.buildByDevelopers_button}
              >
                Read More
                <Icon className="font-bold">arrow_forward</Icon>
              </SuiTypography>
            </SuiBox>
          </Grid>
          <Grid item xs={12} lg={5} className="ml-auto relative">
            <SuiBox
              height="100%"
              display="grid"
              justifyContent="center"
              alignItems="center"
              backgroundColor="info"
              borderRadius="lg"
              backgroundGradient
            >
              <SuiBox
                component="img"
                src={wavesWhite}
                alt="waves"
                display="block"
                position="absolute"
                left={0}
                width="100%"
                height="100%"
              />
              <SuiBox component="img" src={rocketWhite} alt="rocket" width="100%" pt={3} />
            </SuiBox>
          </Grid>
        </Grid>
      </SuiBox>
    </Card>
  );
}

export default BuildByDevelopers;
