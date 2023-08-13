// prop-types is a library for typechecking of props
import PropTypes from "prop-types";

// Soft UI Dashboard React components
import SoftBox from "components/SoftBox";
import SoftTypography from "components/SoftTypography";

function Invoice({ date, id, price, noGutter }) {
  return (
    <SoftBox
      component="li"
      display="flex"
      justifyContent="space-between"
      alignItems="center"
      py={1}
      pr={1}
      mb={noGutter ? 0 : 1}
    >
      <SoftBox lineHeight={1}>
        <SoftTypography display="block" variant="button" fontWeight="medium">
          {date}
        </SoftTypography>
        <SoftTypography variant="caption" fontWeight="regular" color="text">
          {id}
        </SoftTypography>
      </SoftBox>
      <SoftBox display="flex" alignItems="center">
        <SoftTypography variant="button" fontWeight="regular" color="text">
          {price}
        </SoftTypography>
      </SoftBox>
    </SoftBox>
  );
}

// Setting default values for the props of Invoice
Invoice.defaultProps = {
  noGutter: false,
};

// Typechecking props for the Invoice
Invoice.propTypes = {
  date: PropTypes.string.isRequired,
  id: PropTypes.string.isRequired,
  price: PropTypes.string.isRequired,
  noGutter: PropTypes.bool,
};

export default Invoice;