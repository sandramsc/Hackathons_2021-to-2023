// prop-types is a library for typechecking of props
import PropTypes from "prop-types";

// Soft UI Dashboard React components
import SoftBox from "components/SoftBox";
import SoftTypography from "components/SoftTypography";

function GetCard({ date, id, noGutter }) {
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
        <SoftTypography variant="caption" fontWeight="regular" color="white">
          {id}
        </SoftTypography>
      </SoftBox>
    </SoftBox>
  );
}

// Setting default values for the props of GetCard
GetCard.defaultProps = {
  noGutter: false,
};

// Typechecking props for the GetCard
GetCard.propTypes = {
  date: PropTypes.string.isRequired,
  id: PropTypes.string.isRequired,
  noGutter: PropTypes.bool,
};

export default GetCard;