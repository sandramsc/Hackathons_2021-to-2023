// prop-types is a library for typechecking of props
import PropTypes from "prop-types";

// @mui material components
import Card from "@mui/material/Card";
import Icon from "@mui/material/Icon";

// Soft UI Dashboard React components
import SuiBox from "components/SuiBox";
import SuiTypography from "components/SuiTypography";

// Custom styles for the MasterCard
import styles from "examples/Cards/MasterCard/styles";

// Images
import ipRoyaltyLogo from "assets/images/logos/iproyalty.png";

function MasterCard({ color, number, holder, expires }) {
  const classes = styles({ color });
  const numbers = [...`${number}`];

  if (numbers.length < 16 || numbers.length > 16) {
    throw new Error(
      "Invalid value for the prop number, the value for the number prop shouldn't be greater than or less than 16 digits"
    );
  }

  const num1 = numbers.slice(0, 4).join("");
  const num2 = numbers.slice(4, 8).join("");
  const num3 = numbers.slice(8, 12).join("");
  const num4 = numbers.slice(12, 16).join("");

  return (
    <Card className={classes.masterCard}>
      <SuiBox p={2}>
        <SuiBox color="white" p={1} lineHeight={0} display="inline-block">
          <Icon className={classes.masterCard_icon} fontSize="medium">
            wifi
          </Icon>
        </SuiBox>
        <SuiTypography
          variant="h5"
          textColor="white"
          fontWeight="medium"
          customClass={classes.masterCard_number}
        >
          {num1}&nbsp;&nbsp;&nbsp;{num2}&nbsp;&nbsp;&nbsp;{num3}&nbsp;&nbsp;&nbsp;{num4}
        </SuiTypography>
        <SuiBox display="flex" justifyContent="space-between" alignItems="center">
          <SuiBox display="flex" alignItems="center">
            <SuiBox mr={3}>
              <SuiTypography variant="button" textColor="white" fontWeight="regular" opacity={0.8}>
                Token Holder
              </SuiTypography>
              <SuiTypography
                variant="h6"
                textColor="white"
                fontWeight="medium"
                textTransform="capitalize"
              >
                {holder}
              </SuiTypography>
            </SuiBox>
            <SuiBox>
              <SuiTypography variant="button" textColor="white" fontWeight="regular" opacity={0.8}>
                Expires
              </SuiTypography>
              <SuiTypography variant="h6" textColor="white" fontWeight="medium">
                {expires}
              </SuiTypography>
            </SuiBox>
          </SuiBox>
          <SuiBox display="flex" justifyContent="flex-end" width="20%">
            <SuiBox component="img" src={ipRoyaltyLogo} alt="master card" width="60%" mt={1} />
          </SuiBox>
        </SuiBox>
      </SuiBox>
    </Card>
  );
}

// Setting default values for the props of MasterCard
MasterCard.defaultProps = {
  color: "dark",
};

// Typechecking props for the MasterCard
MasterCard.propTypes = {
  color: PropTypes.oneOf(["primary", "secondary", "info", "success", "warning", "error", "dark"]),
  number: PropTypes.number.isRequired,
  holder: PropTypes.string.isRequired,
  expires: PropTypes.string.isRequired,
};

export default MasterCard;
